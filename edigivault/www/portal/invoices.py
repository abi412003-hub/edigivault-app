import frappe
no_cache = 1
def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw("Please log in", frappe.AuthenticationError)
    context.invoices = frappe.get_all("DigiVault Invoice",
        fields=["name", "client", "invoice_date", "total_amount", "workflow_state"],
        order_by="creation desc", limit=50)
    context.title = "Invoices"
