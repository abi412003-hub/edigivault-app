import frappe
no_cache = 1
def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw("Please log in", frappe.AuthenticationError)
    context.projects = frappe.get_all("DigiVault Project",
        fields=["name", "project_name", "project_status", "client", "start_date", "creation"],
        order_by="creation desc", limit=50)
    context.title = "My Projects"
