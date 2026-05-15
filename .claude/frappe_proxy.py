import os
import sys
import http.client
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

TARGET_HOST = "127.0.0.1"
TARGET_PORT = 8000
SITE_HOST = "helpdesk.localhost"
HOP_BY_HOP = {
    "connection", "keep-alive", "proxy-authenticate", "proxy-authorization",
    "te", "trailers", "transfer-encoding", "upgrade",
}


def login_admin():
    conn = http.client.HTTPConnection(TARGET_HOST, TARGET_PORT, timeout=30)
    body = "usr=Administrator&pwd=admin"
    headers = {
        "Host": SITE_HOST,
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": str(len(body)),
    }
    conn.request("POST", "/api/method/login", body=body, headers=headers)
    resp = conn.getresponse()
    set_cookies = []
    for k, v in resp.getheaders():
        if k.lower() == "set-cookie":
            set_cookies.append(v)
    resp.read()
    conn.close()
    return resp.status, set_cookies


class Proxy(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_login_bridge(self):
        try:
            status, cookies = login_admin()
            if status != 200:
                self.send_error(502, f"Upstream login returned {status}")
                return
            target = "/helpdesk/home"
            self.send_response(302)
            for c in cookies:
                self.send_header("Set-Cookie", c)
            self.send_header("Location", target)
            self.send_header("Content-Length", "0")
            self.end_headers()
        except Exception as e:
            try:
                self.send_error(502, f"Login bridge error: {e}")
            except Exception:
                pass

    def proxy(self):
        if self.path.startswith("/__login_admin"):
            self.do_login_bridge()
            return
        try:
            length = int(self.headers.get("Content-Length", "0") or "0")
            body = self.rfile.read(length) if length else None

            headers = {}
            for k, v in self.headers.items():
                if k.lower() in HOP_BY_HOP:
                    continue
                headers[k] = v
            headers["Host"] = SITE_HOST
            headers["X-Forwarded-Host"] = SITE_HOST

            conn = http.client.HTTPConnection(TARGET_HOST, TARGET_PORT, timeout=60)
            conn.request(self.command, self.path, body=body, headers=headers)
            resp = conn.getresponse()
            data = resp.read()

            self.send_response(resp.status, resp.reason)
            for k, v in resp.getheaders():
                if k.lower() in HOP_BY_HOP or k.lower() == "content-length":
                    continue
                self.send_header(k, v)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(data)
            conn.close()
        except Exception as e:
            try:
                self.send_error(502, f"Proxy error: {e}")
            except Exception:
                pass

    do_GET = proxy
    do_POST = proxy
    do_PUT = proxy
    do_DELETE = proxy
    do_PATCH = proxy
    do_OPTIONS = proxy
    do_HEAD = proxy

    def log_message(self, fmt, *args):
        sys.stderr.write("[proxy] " + (fmt % args) + "\n")


def main():
    port = int(os.environ.get("PORT", "3000"))
    print(f"Frappe proxy on :{port} -> http://{TARGET_HOST}:{TARGET_PORT} (Host: {SITE_HOST})", flush=True)
    ThreadingHTTPServer(("127.0.0.1", port), Proxy).serve_forever()


if __name__ == "__main__":
    main()
