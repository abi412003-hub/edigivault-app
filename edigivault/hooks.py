app_name = "edigivault"
app_title = "e-DigiVault"
app_publisher = "Chilume Legal & Liaisoning Pvt. Ltd."
app_description = "Digital Property Documentation & Liaisoning Platform"
app_email = "abi412003@gmail.com"
app_license = "MIT"
app_version = "1.0.0"

website_route_rules = [
    {"from_route": "/portal", "to_route": "portal"},
    {"from_route": "/portal/projects", "to_route": "portal/projects"},
    {"from_route": "/portal/projects/<n>", "to_route": "portal/project_detail"},
    {"from_route": "/portal/properties", "to_route": "portal/properties"},
    {"from_route": "/portal/estimates", "to_route": "portal/estimates"},
    {"from_route": "/portal/estimates/<n>", "to_route": "portal/estimate_detail"},
    {"from_route": "/portal/services", "to_route": "portal/services"},
    {"from_route": "/portal/invoices", "to_route": "portal/invoices"},
    {"from_route": "/portal/payments", "to_route": "portal/payments"},
    {"from_route": "/portal/documents", "to_route": "portal/documents"},
    {"from_route": "/portal/leads", "to_route": "portal/leads"},
]

portal_menu_items = [
    {"title": "Dashboard", "route": "/portal", "role": "DigiVault Client"},
    {"title": "My Projects", "route": "/portal/projects", "role": "DigiVault Client"},
    {"title": "My Properties", "route": "/portal/properties", "role": "DigiVault Client"},
    {"title": "Estimates", "route": "/portal/estimates", "role": "DigiVault Client"},
    {"title": "Services", "route": "/portal/services", "role": "DigiVault Client"},
    {"title": "Invoices", "route": "/portal/invoices", "role": "DigiVault Client"},
    {"title": "Leads", "route": "/portal/leads", "role": "DigiVault BD"},
]

app_include_css = "/assets/edigivault/css/edigivault.css"
app_include_js = "/assets/edigivault/js/edigivault.js"
web_include_css = "/assets/edigivault/css/portal.css"

role_home_page = {
    "DigiVault Client": "/portal",
    "DigiVault MRA": "/app/e-digivault",
    "DigiVault BD": "/app/e-digivault",
    "DigiVault Delivery Partner": "/app/e-digivault",
    "DigiVault Channel Partner": "/portal",
    "DigiVault Incharge": "/app/e-digivault",
    "DigiVault Regional Head": "/app/e-digivault",
    "DigiVault Statehead": "/app/e-digivault",
    "DigiVault Accountant": "/app/e-digivault",
    "DigiVault Legal": "/app/e-digivault",
    "DigiVault Admin": "/app/e-digivault",
    "DigiVault Super Admin": "/app/e-digivault",
}
