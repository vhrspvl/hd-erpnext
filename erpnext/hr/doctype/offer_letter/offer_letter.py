# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import today

class OfferLetter(Document):
	pass

@frappe.whitelist()
def make_employee(source_name, target_doc=None):
	def set_missing_values(source, target):
		ja = frappe.get_doc("Job Applicant", source.job_applicant)
		target.personal_email = ja.email_id
		target.date_of_birth = ja.date_of_birth
		target.gender = ja.sex
		if ja.sex == "Male":
			target.salutation = "Mr"
		elif ja.sex == "Female":
			target.salutation = "Ms"
		target.scheduled_confirmation_date = today()
		target.final_confirmation_date = today()
	doc = get_mapped_doc("Offer Letter", source_name, {
			"Offer Letter": {
				"doctype": "Employee",
				"field_map": {
					"applicant_name": "employee_name",
					"offer_date": "scheduled_confirmation_date" 
				}}
		}, target_doc, set_missing_values)
	return doc



@frappe.whitelist()
def send_mail_to_candidate(job_applicant):
	ja = frappe.get_doc("Job Applicant",job_applicant)
	candidate_mail_id = ja.email_id
	frappe.sendmail(
        recipients=[candidate_mail_id],
        subject='Offer Letter Details - ',
		message="hi"
    )
	return "OK"