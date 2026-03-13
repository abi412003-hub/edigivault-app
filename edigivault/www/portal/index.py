import frappe

no_cache = 1

def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw("Please log in to access the portal", frappe.AuthenticationError)
    
    user = frappe.session.user
    context.user_name = frappe.db.get_value("User", user, "full_name") or user
    context.project_count = frappe.db.count("DigiVault Project") or 0
    context.property_count = frappe.db.count("DigiVault Property") or 0
    context.estimate_count = frappe.db.count("DigiVault Estimate") or 0
    context.lead_count = frappe.db.count("DigiVault Lead") or 0
    context.service_count = frappe.db.count("DigiVault Service") or 0
    context.projects = frappe.get_all("DigiVault Project",
        fields=["name", "project_name", "project_status", "client", "creation"],
        order_by="creation desc", limit=5)
    context.estimates = frappe.get_all("DigiVault Estimate",
        fields=["name", "client", "service", "estimate_status", "total_price", "estimate_date"],
        order_by="creation desc", limit=5)
    context.no_cache = 1
    context.title = "e-DigiVault Portal"
