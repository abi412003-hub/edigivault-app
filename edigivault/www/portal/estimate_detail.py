import frappe
no_cache = 1
def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw("Please log in", frappe.AuthenticationError)
    n = frappe.form_dict.get("n")
    if not n:
        frappe.throw("Estimate not specified")
    doc = frappe.get_doc("DigiVault Estimate", n)
    context.doc = doc
    context.steps = doc.estimate_steps or []
    context.title = f"Estimate {n}"
