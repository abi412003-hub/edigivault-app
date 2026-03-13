import frappe
no_cache = 1
def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw("Please log in", frappe.AuthenticationError)
    context.documents = frappe.get_all("DigiVault Client Document",
        fields=["name", "client", "document_name", "document_type", "status", "creation"],
        order_by="creation desc", limit=50)
    context.title = "Documents"
