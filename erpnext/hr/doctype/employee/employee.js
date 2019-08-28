// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.provide("erpnext.hr");
// frm.add_custom_button(__("announcement"), function() {
	
// })
erpnext.hr.EmployeeController = frappe.ui.form.Controller.extend({
	setup: function() {
		this.frm.fields_dict.user_id.get_query = function(doc, cdt, cdn) {
			return {
				query: "frappe.core.doctype.user.user.user_query",
				filters: {ignore_user_type: 1}
			}
		}
		this.frm.fields_dict.reports_to.get_query = function(doc, cdt, cdn) {
			return { query: "erpnext.controllers.queries.employee_query"} }
	},

	onload: function() {
		this.frm.set_query("leave_approver", "leave_approvers", function(doc) {
			return {
				query:"erpnext.hr.doctype.employee_leave_approver.employee_leave_approver.get_approvers",
				filters:{
					user: doc.user_id
				}
			}
		});
	},

	refresh: function() {
		var me = this;
		erpnext.toggle_naming_series();
		
	},

	date_of_birth: function() {
		return cur_frm.call({
			method: "get_retirement_date",
			args: {date_of_birth: this.frm.doc.date_of_birth}
		});
	},

	salutation: function() {
		if(this.frm.doc.salutation) {
			this.frm.set_value("gender", {
				"Mr": "Male",
				"Ms": "Female"
			}[this.frm.doc.salutation]);
		}
	},

});
frappe.ui.form.on('Employee',{
	prefered_contact_email:function(frm){		
		frm.events.update_contact(frm)		
	},
	personal_email:function(frm){
		frm.events.update_contact(frm)
	},
	company_email:function(frm){
		frm.events.update_contact(frm)
	},
	user_id:function(frm){
		frm.events.update_contact(frm)
	},
	update_contact:function(frm){
		var prefered_email_fieldname = frappe.model.scrub(frm.doc.prefered_contact_email) || 'user_id';
		frm.set_value("prefered_email",
			frm.fields_dict[prefered_email_fieldname].value)
	},
	status: function(frm) {
		return frm.call({
			method: "deactivate_sales_person",
			args: {
				employee: frm.doc.employee,
				status: frm.doc.status
			}
		});
	},
	create_user: function(frm) {
		if (!frm.doc.prefered_email)
		{
			frappe.throw(__("Please enter Preferred Contact Email"))
		}
		frappe.call({
			method: "erpnext.hr.doctype.employee.employee.create_user",
			args: { employee: frm.doc.name, email: frm.doc.prefered_email },
			callback: function(r)
			{
				frm.set_value("user_id", r.message)
			}
		});
	},
	refresh: function(frm){
		if(!frm.doc.__islocal){
			frm.add_custom_button(__('Send Announcement'), function () {
				frappe.call({
					"method": "hunter_douglas.custom.send_announcement",
					args : {
						"name": frm.doc.name					 
					},
					callback:function(r){


					}
				})
			});
		}
	},
	onload: function(frm){
		frm.add_custom_button(__('Update MIS'), function () {
			var d = new frappe.ui.Dialog({
				'fields': [
					{ label: "Date of Joining", 'fieldname': 'date_of_joining', 'fieldtype': 'Date' },
					{fieldtype: "Link", fieldname: "gender", label: __("Gender"), options: "Gender"},
					{ label: "Date of Birth", 'fieldname': 'date_of_birth', 'fieldtype': 'Date' },
					{fieldtype: "Link", fieldname: "department", label: __("Department"), options:"Department"},
					{fieldtype: "Select", fieldname: "salary_mode", label: __("Salary Mode"), options: ["Bank","Cash","Cheque"]},
					{fieldtype: "Data", fieldname: "bank_name", label: __("Bank Name"), depends_on: 'eval:doc.salary_mode == "Bank"'},
					{fieldtype: "Data", fieldname: "bank_ac_no", label: __("Bank A/C No"), depends_on: 'eval:doc.salary_mode == "Bank"'},
					{fieldtype: "Data", fieldname: "ifsc_code", label: __("IFSC Code"), depends_on: 'eval:doc.salary_mode == "Bank"'},
					{fieldtype: "Column Break", fieldname: "cb6", label: __(""), reqd: 1},
					{fieldtype: "Link", fieldname: "working_shift", label: __("Working Shift"), options: "Working Shift"},
					{fieldtype: "Data", fieldname: "pan_number", label: __("PAN Number")},
					{fieldtype: "Data", fieldname: "uan_number", label: __("UAN Number")},
					{fieldtype: "Data", fieldname: "cell_number", label: __("Cell Number")},
					{fieldtype: "Data", fieldname: "father_name", label: __("Father Name")},
					{fieldtype: "Data", fieldname: "husband_wife_name", label: __("Husband /Wife Name")},
					{fieldtype: "Section Break", fieldname: "sb1", label: __("Address details"), reqd: 1},
					{fieldtype: "Select", fieldname: "permanent_address_is", label: __("Permanent Address Is"), options: ["Rented","Owned"]},
					{fieldtype: "Small Text", fieldname: "permanent_address", label: __("Permanent Address")},
					{fieldtype: "Column Break", fieldname: "cb1", label: __(""), reqd: 1},
					{fieldtype: "Select", fieldname: "current_address_is", label: __("Current Address Is"), options: ["Rented","Owned"]},
					{fieldtype: "Small Text", fieldname: "current_address", label: __("Current Address")}

				],
				primary_action: function () {
					var args = d.get_values()
					frappe.call({
						method: "hunter_douglas.custom.update_mis",
						args: {
							"employee": frm.doc.employee_number,
							"date_of_joining":args.date_of_joining,
							"gender":args.gender,
							"date_of_birth":args.date_of_birth,
							"department":args.department,
							"salary_mode":args.salary_mode,
							"bank_name":args.bank_name,
							"bank_ac_no":args.bank_ac_no,
							"ifsc_code":args.ifsc_code,
							"working_shift":args.working_shift,
							"pan_number":args.pan_number,
							"uan_number":args.uan_number,
							"cell_number":args.cell_number,
							"father_name":args.father_name,
							"husband_wife_name":args.husband_wife_name,
							"permanent_address_is":args.permanent_address_is,
							"permanent_address":args.permanent_address,
							"current_address_is":args.current_address_is,
							"current_address":args.current_address					
						},
						callback: function (r) {
							frappe.msgprint(__("Request Updated"))
							d.hide()
						}
					})
				}
			});
			d.show();
		});
	}
});
cur_frm.cscript = new erpnext.hr.EmployeeController({frm: cur_frm});

