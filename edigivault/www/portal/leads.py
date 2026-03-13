import frappe
no_cache = 1
def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw("Please log in", frappe.AuthenticationError)
    context.leads = frappe.get_all("DigiVault Lead",
        fields=["name", "lead_name", "lead_status", "phone_no", "email", "lead_type", "created_date"],
        order_by="creation desc", limit=50)
    context.title = "Leads"
