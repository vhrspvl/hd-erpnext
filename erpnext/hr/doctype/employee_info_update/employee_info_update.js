// Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Info Update', {
	refresh: function(frm) {

	},
	before_submit: function(frm){
		if(frappe.session.user != "hr.hdi@hunterdouglas.asia"){
			validated = false;
			frappe.msgprint("System Admin Only can Submit this File")
		}
	},
	on_submit: function(frm){
		frappe.call({
			"method": "hunter_douglas.custom.update_main_mis",
			args:{
				"name": frm.doc.name,
				"employee": frm.doc.employee_code,
				"status": frm.doc.status
			},
			callback: function(r){
				frappe.msgprint("MIS Updated")
			}
		})
	}
});
