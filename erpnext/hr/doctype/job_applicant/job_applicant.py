# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document
import frappe
from frappe import _
from frappe.utils import comma_and, validate_email_add

sender_field = "email_id"

class DuplicationError(frappe.ValidationError): pass

class JobApplicant(Document):
	def onload(self):
		offer_letter = frappe.get_all("Offer Letter", filters={"job_applicant": self.name})
		if offer_letter:
			self.get("__onload").offer_letter = offer_letter[0].name

	def autoname(self):
		keys = filter(None, (self.applicant_name, self.email_id, self.job_title))
		if not keys:
			frappe.throw(_("Name or Email is mandatory"), frappe.NameError)
		self.name = " - ".join(keys)

	def validate(self):
		self.check_email_id_is_unique()
		if self.email_id:
			validate_email_add(self.email_id, True)

		if not self.applicant_name and self.email_id:
			guess = self.email_id.split('@')[0]
			self.applicant_name = ' '.join([p.capitalize() for p in guess.split('.')])

	def check_email_id_is_unique(self):
		if self.email_id:
			names = frappe.db.sql_list("""select name from `tabJob Applicant`
				where email_id=%s and name!=%s and job_title=%s""", (self.email_id, self.name, self.job_title))

			if names:
				frappe.throw(_("Email Address must be unique, already exists for {0}").format(comma_and(names)), frappe.DuplicateEntryError)






@frappe.whitelist()
def send_next_level_details(emp_id,name):
	if emp_id and name:
		frappe.sendmail(
			recipients= emp_id,
			subject='Job Applicant',
			message="""
			<p> Dear Sir,<p><br>
			<p>You are the Next Level of Interviewer for the below applicant.You can see it by clicking <a href= "%s">Job Applicant</a></p><br><br>
			<p>Thank You</p>""" %(frappe.utils.get_url_to_form("Job Applicant",name))
        )
	return "Ok"

@frappe.whitelist()
def send_mail_for_salary_approval(name):
	if name:
		frappe.sendmail(
			recipients= ['subash.p@voltechgroup.com'],
			subject='Salary Approval',
			message="""
			<p> Dear Sir,<p><br>
			<p>Kindly Approve the Salary for the new Employee. You can see it by clicking <a href= "%s">Approve Salary</a></p><br><br>
			<p>Thank You</p>""" %(frappe.utils.get_url_to_form("Job Applicant",name))
        )
	return "Ok"