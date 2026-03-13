import frappe

@frappe.whitelist()
def get_portal_dashboard():
    """Get dashboard data for the client portal"""
    user = frappe.session.user
    if user == "Guest":
        frappe.throw("Not authenticated")
    
    return {
        "projects": frappe.db.count("DigiVault Project"),
        "properties": frappe.db.count("DigiVault Property"),
        "estimates": frappe.db.count("DigiVault Estimate"),
        "leads": frappe.db.count("DigiVault Lead"),
        "services": frappe.db.count("DigiVault Service"),
        "recent_projects": frappe.get_all("DigiVault Project",
            fields=["name", "project_name", "project_status", "client"],
            order_by="creation desc", limit=5),
        "recent_estimates": frappe.get_all("DigiVault Estimate",
            fields=["name", "service", "estimate_status", "total_price"],
            order_by="creation desc", limit=5),
    }

@frappe.whitelist()
def convert_lead_to_client(lead_name):
    """Convert an approved lead to a client"""
    lead = frappe.get_doc("DigiVault Lead", lead_name)
    if lead.lead_status != "Approved":
        frappe.throw("Only approved leads can be converted")
    
    client = frappe.new_doc("DigiVault Client")
    client.client_name = lead.lead_name
    client.phone_no = lead.phone_no
    client.email = lead.email
    client.client_type = "Organisation" if lead.lead_type == "Organization" else "Personal"
    client.client_status = "Active"
    client.insert()
    
    # Update lead
    lead.lead_status = "Approved"
    lead.save()
    
    return {"client": client.name, "message": f"Client {client.name} created from lead {lead_name}"}

@frappe.whitelist()
def get_service_catalog():
    """Get all services grouped by category"""
    services = frappe.get_all("DigiVault Service",
        fields=["name", "service_name", "service_category", "is_active"],
        order_by="service_category asc, service_name asc",
        limit=200)
    
    grouped = {}
    for s in services:
        cat = s.service_category or "Other"
        grouped.setdefault(cat, []).append(s)
    
    return grouped
