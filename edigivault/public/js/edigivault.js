// e-DigiVault Client Scripts for Desk
// Auto-calculate estimate totals
frappe.ui.form.on('DigiVault Estimate', {
    refresh(frm) {
        calculate_estimate_totals(frm);
    },
    estimate_steps_add(frm) { calculate_estimate_totals(frm); },
    estimate_steps_remove(frm) { calculate_estimate_totals(frm); },
});

frappe.ui.form.on('Estimate Step', {
    duration_days(frm) { calculate_estimate_totals(frm); },
    date_from(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.date_from && row.date_to) {
            let diff = frappe.datetime.get_diff(row.date_to, row.date_from);
            frappe.model.set_value(cdt, cdn, 'duration_days', diff + 1);
        }
    },
    date_to(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.date_from && row.date_to) {
            let diff = frappe.datetime.get_diff(row.date_to, row.date_from);
            frappe.model.set_value(cdt, cdn, 'duration_days', diff + 1);
        }
    },
});

function calculate_estimate_totals(frm) {
    let total_days = 0;
    (frm.doc.estimate_steps || []).forEach(step => {
        total_days += (step.duration_days || 0);
    });
    frm.set_value('total_time_days', total_days);
}

// Auto-populate client name on Lead conversion
frappe.ui.form.on('DigiVault Lead', {
    refresh(frm) {
        if (frm.doc.lead_status === 'Approved' && !frm.doc.__islocal) {
            frm.add_custom_button('Convert to Client', () => {
                frappe.new_doc('DigiVault Client', {
                    client_name: frm.doc.lead_name,
                    phone_no: frm.doc.phone_no,
                    email: frm.doc.email,
                    client_type: frm.doc.lead_type === 'Organization' ? 'Organisation' : 'Personal',
                });
            }, 'Actions');
        }
    }
});

// Task - auto update progress
frappe.ui.form.on('DigiVault Task', {
    refresh(frm) {
        if (frm.doc.workflow_state === 'Assigned' || frm.doc.workflow_state === 'In Progress') {
            frm.add_custom_button('Upload Document', () => {
                let d = new frappe.ui.Dialog({
                    title: 'Upload Document',
                    fields: [
                        { fieldname: 'file', fieldtype: 'Attach', label: 'Document File' },
                        { fieldname: 'description', fieldtype: 'Small Text', label: 'Description' },
                    ],
                    primary_action_label: 'Upload',
                    primary_action(values) {
                        frappe.call({
                            method: 'frappe.client.attach_file',
                            args: {
                                filename: values.file,
                                doctype: frm.doctype,
                                docname: frm.docname,
                            },
                            callback(r) {
                                d.hide();
                                frm.reload_doc();
                                frappe.show_alert({ message: 'Document uploaded', indicator: 'green' });
                            }
                        });
                    }
                });
                d.show();
            });
        }
    }
});
