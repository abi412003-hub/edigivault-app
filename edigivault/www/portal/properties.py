import frappe
no_cache = 1
def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw("Please log in", frappe.AuthenticationError)
    context.properties = frappe.get_all("DigiVault Property",
        fields=["name", "property_name", "property_type", "property_address", "total_area", "area_unit", "survey_number", "district", "client"],
        order_by="creation desc", limit=50)
    context.title = "My Properties"
