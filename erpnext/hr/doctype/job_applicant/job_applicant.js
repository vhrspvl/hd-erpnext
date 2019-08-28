// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

// For license information, please see license.txt

// for communication
cur_frm.email_field = "email_id";

frappe.ui.form.on("Job Applicant", {
	refresh: function(frm) {
		if (!frm.doc.__islocal) {
			if(frm.doc.status != "Open"){
			if (frm.doc.__onload && frm.doc.__onload.offer_letter) {
				frm.add_custom_button(__("Offer Letter"), function() {
					frappe.set_route("Form", "Offer Letter", frm.doc.__onload.offer_letter);
				}, __("View"));
			} else {
				frm.add_custom_button(__("Offer Letter"), function() {
					frappe.route_options = {
						"job_applicant": frm.doc.name,
						"applicant_name": frm.doc.applicant_name,
						"designation": frm.doc.job_opening,
						"basic": frm.doc.hdi_basic,
						"job_opening": frm.doc.job_title,						
						"hra": frm.doc.hdi_hra,
						"gross": frm.doc.annual_gross,
						"food_allowance": frm.doc.hdi_food_allowance,
						"ea": frm.doc.hdi_education_allowance,
						"lta": frm.doc.ctc_hdi
					};
					frappe.new_doc("Offer Letter");
				}, __("Make"));
					cur_frm.page.set_inner_btn_group_as_primary(__("Make"));
				}
			}
		}
		if(frm.doc.interview_evaluation_keys.length == 0){
			for(var i =0;i<11;i++){
				var row = frappe.model.add_child(frm.doc,  "Interview Evaluation Keys", "interview_evaluation_keys");
				if(i == 0){
					row.label = "Personality- Appearance, Grooming, Body language & Eye Contact "
					row.weightage_w = '5%';
				}
				if(i == 1){
					row.label = "Characterstics -Assertive , Achivement Oriented, Responsible , Out going,Open, Dedicated,Mature,Professional"
					row.weightage_w = '5%';
				}
				if(i == 2){
					row.label = "Goal/Preception of self-Realistic appraisal of self,Field interested Realistic in career goals"
					row.weightage_w = '5%';
				}
				if(i == 3){
					row.label = "Skills-Creativity, Logic, Presentation Skills , knowledge in computer"
					row.weightage_w = '10%';
				}
				if(i == 4){
					row.label = "Job expectations – Realistic, Match with HD needs, Relevant"
					row.weightage_w = '10%';
				}
				if(i == 5){
					row.label = "Education-Matching with HD requirement "
					row.weightage_w = '10%';
				}
				if(i == 6){
					row.label = "Job Knowledge"
					row.weightage_w = '20%';
				}
				if(i == 7){
					row.label = "Knowledge- of HD operations in India and world wide"
					row.weightage_w = '5%';
				}
				if(i == 8){
					row.label = "HDI Culture Adoptability Seriousness,Sincerity,Simple,Skillful "
					row.weightage_w = '10%';
				}
				if(i == 9){
					row.label = "Past Experience in the relvent field"
					row.weightage_w = '15%';
				}
				if(i == 10){
					row.label = "Other Remarks / recommendations"
					row.weightage_w = '5%';
				}
				refresh_field("interview_evaluation_keys");
			}
		}
		// frappe.call({
		// 	"method": "frappe.client.get_list",
		// 	args: {
		// 		doctype: "Evaluation Keys"
		// 	},
		// 	callback: function (r) {
		// 		if (r.message) {
		// 			$.each(r.message, function (i, d) {
		// 				frappe.call({
		// 					"method": "frappe.client.get",
		// 					args: {
		// 						doctype: "Evaluation Keys",
		// 						name: d.name,
		// 					},
		// 					callback: function (r) {
		// 						if (r.message) {
		// 								var row = frappe.model.add_child(frm.doc,  "Interview Evaluation Keys", "interview_evaluation_keys");
		// 								row.label = d.name
		// 								row.weightage_w = r.message.weightage;
									
		// 						}
								
								
		// 						refresh_field("interview_evaluation_keys");
								
								
		// 					}
		// 				})
		
		// 			})
		// 		}
		// 	}
		// })
	if(frm.doc.salary_approved=="1"){
		frm.add_custom_button(__("Salary Approved")).addClass('btn btn-success');
	}
	},
	is_there_2nd_level: function(frm){
		if(!frm.doc.interviewer_code_1  && frm.doc.is_there_2nd_level == 1){
		validated=false
		frappe.msgprint("Kindly Select the Next Level Interviewer Code")
		}
	},
	is_there_3rd_level: function(frm){
		if(!frm.doc.interviewer_code_2 && frm.doc.is_there_3rd_level == 1){
		validated=false
		frappe.msgprint("Kindly Select the Next Level Interviewer Code")
		}
	},
	validate: function(frm){
		frm.trigger("is_there_2nd_level")
		frm.trigger("is_there_3rd_level")
	},
	after_save: function(frm){
		if(frm.doc.interviewer_code_1 && frm.doc.is_there_2nd_level == 1 && frm.doc.sms_sent_to_interviewer1 == ""){
			frappe.call({
				"method": "erpnext.hr.doctype.job_applicant.job_applicant.send_next_level_details",
				args:{
					"emp_id": frm.doc.interviewer_code_1,
					"name": frm.doc.name					
				},
				callback: function(r){
					if(r.message){
						frm.set_value("sms_sent_to_interviewer1","Sent")
					}
				}			
			})
		}
		if(frm.doc.interviewer_code_2 && frm.doc.is_there_3rd_level == 1 && frm.doc.sms_sent_to_interviewer2 == ""){
			frappe.call({
				"method": "erpnext.hr.doctype.job_applicant.job_applicant.send_next_level_details",
				args:{
					"emp_id": frm.doc.interviewer_code_2,
					"name": frm.doc.name					
				},
				callback: function(r){
					if(r.message){
						frm.set_value("sms_sent_to_interviewer2","Sent")
					}
				}			
			})
		}
	},
	send_for_salary_approval:function(frm){
		frm.set_value("salary_approval_sent","1")
		frappe.call({
			"method":"erpnext.hr.doctype.job_applicant.job_applicant.send_mail_for_salary_approval",
			args:{
				"name": frm.doc.name
			},
			callback:function(r){
				frappe.msgprint("Sent for Salary Approval")
				frm.save();
			}
		})
	},

approve_salary:function(frm){
	frm.set_value("salary_approved","1")
	frm.save();
	},
	

});