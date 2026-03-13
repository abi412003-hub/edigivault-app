# Copy HTML files and remaining assets
$src = "C:\Users\abi41\Downloads\edigivault-app\edigivault\edigivault"
$dst = "C:\Users\abi41\Downloads\edigivault-frappe\edigivault"

# HTML portal pages
$htmlFiles = @("index.html","projects.html","project_detail.html","properties.html","estimates.html","estimate_detail.html","services.html","invoices.html","payments.html","documents.html","leads.html")
foreach ($f in $htmlFiles) {
    Copy-Item "$src\www\portal\$f" "$dst\www\portal\$f" -Force -ErrorAction SilentlyContinue
    if ($?) { Write-Host "OK $f" } else { Write-Host "SKIP $f" }
}

# CSS
Copy-Item "$src\public\css\portal.css" "$dst\public\css\portal.css" -Force
Copy-Item "$src\public\css\edigivault.css" "$dst\public\css\edigivault.css" -Force

# JS
New-Item -ItemType Directory -Path "$dst\public\js" -Force | Out-Null
Copy-Item "$src\public\js\edigivault.js" "$dst\public\js\edigivault.js" -Force

# API
New-Item -ItemType Directory -Path "$dst\api" -Force | Out-Null
Copy-Item "$src\api\__init__.py" "$dst\api\__init__.py" -Force
Copy-Item "$src\api\portal.py" "$dst\api\portal.py" -Force

# Templates dir
New-Item -ItemType Directory -Path "$dst\templates" -Force | Out-Null

Write-Host ""
Write-Host "=== Done! Now push to GitHub ==="
Write-Host "cd C:\Users\abi41\Downloads\edigivault-frappe"
Write-Host "git init"
Write-Host "git add -A"
Write-Host 'git commit -m "e-DigiVault Frappe app v1"'
Write-Host "git branch -M main"
Write-Host "git remote add origin https://github.com/abi412003-hub/edigivault-app.git"
Write-Host "git push -u origin main --force"
