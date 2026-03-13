import frappe
no_cache = 1
def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw("Please log in", frappe.AuthenticationError)
    context.payments = frappe.get_all("DigiVault Payment",
        fields=["name", "client", "amount", "payment_date", "payment_mode", "payment_status"],
        order_by="creation desc", limit=50)
    context.title = "Payments"
