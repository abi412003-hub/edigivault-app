import frappe
no_cache = 1
def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw("Please log in", frappe.AuthenticationError)
    n = frappe.form_dict.get("n")
    if not n:
        frappe.throw("Project not specified")
    doc = frappe.get_doc("DigiVault Project", n)
    context.doc = doc
    context.properties = frappe.get_all("DigiVault Property",
        filters={"client": doc.client} if doc.client else {},
        fields=["name", "property_name", "property_type", "property_address"], limit=20)
    context.estimates = frappe.get_all("DigiVault Estimate",
        filters={"client": doc.client} if doc.client else {},
        fields=["name", "service", "estimate_status", "total_price"], limit=10)
    context.title = f"Project {n}"
