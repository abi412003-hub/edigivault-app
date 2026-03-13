import frappe
no_cache = 1
def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw("Please log in", frappe.AuthenticationError)
    context.estimates = frappe.get_all("DigiVault Estimate",
        fields=["name", "client", "service", "estimate_status", "total_price", "total_time_days", "estimate_date"],
        order_by="creation desc", limit=50)
    context.title = "Estimates"
