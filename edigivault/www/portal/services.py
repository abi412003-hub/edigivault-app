import frappe
no_cache = 1
def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw("Please log in", frappe.AuthenticationError)
    all_services = frappe.get_all("DigiVault Service",
        fields=["name", "service_name", "service_category", "is_active"],
        order_by="service_category asc, service_name asc", limit=200)
    grouped = {}
    for s in all_services:
        cat = s.service_category or "Other"
        grouped.setdefault(cat, []).append(s)
    context.service_groups = grouped
    context.total_services = len(all_services)
    context.title = "Services Catalog"
