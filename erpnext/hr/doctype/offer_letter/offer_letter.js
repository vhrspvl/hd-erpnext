// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.provide("erpnext.offer_letter");

frappe.ui.form.on("Offer Letter", {
	select_terms: function (frm) {
		erpnext.utils.get_terms(frm.doc.select_terms, frm.doc, function (r) {
			if (!r.exc) {
				frm.set_value("terms", r.message);
			}
		});
	},

	refresh: function (frm) {
		if ((!frm.doc.__islocal) && (frm.doc.status == 'Accepted') && (frm.doc.docstatus === 1)) {
			frm.add_custom_button(__('Make Employee'),
				function () {
					erpnext.offer_letter.make_employee(frm)
				}
			);
		}
	},
	send_mail_to_candidate: function(frm){
		frappe.call({
			"method": 'erpnext.hr.doctype.offer_letter.offer_letter.send_mail_to_candidate',
			args:{
				"job_applicant": frm.doc.job_applicant
			},
			callback: function(r){
				if(r.message == "OK"){
					frm.set_value("mail_sent","Yes")
				}
			}
		})
	}

});

erpnext.offer_letter.make_employee = function (frm) {
	frappe.model.open_mapped_doc({
		method: "erpnext.hr.doctype.offer_letter.offer_letter.make_employee",
		frm: frm
	});
};
