from __future__ import unicode_literals
from frappe import _
import frappe

def get_data():
    system_manager = frappe.get_doc("User", frappe.session.user).get("roles",{"role": "System Manager"})
    if system_manager:
        return [
            {
                "label": _("Employee and Attendance"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Employee",
                        "description": _("Employee records."),
                    },
                    {
                        "type": "doctype",
                        "name": "Employee Attendance Tool",
                        "label": _("Employee Attendance Tool"),
                        "description":_("Mark Attendance for multiple employees"),
                        "hide_count": True
                    },
                    {
                        "type": "doctype",
                        "name": "Attendance",
                        "description": _("Attendance record."),
                    },
                    {
                        "type": "doctype",
                        "name": "Fetch Attendance",
                        "description": _("Attendance record."),
                    },
                    {
                        "type": "doctype",
                        "name": "Shift Assignment",
                        "description": _("Attendance record."),
                    },
                    {
                        "type": "doctype",
                        "name": "Shift Assignment Tool",
                        "description": _("Attendance record."),
                    },
                    {
                        "type": "doctype",
                        "name": "Upload Attendance",
                        "description":_("Upload attendance from a .csv file"),
                        "hide_count": True
                    },
                ]
            },
            {
            	"label": _("Recruitment"),
            	"items": [
            		{
            			"type": "doctype",
            			"name": "Job Opening",
            			"description": _("Opening for a Job."),
            		},
            		{
            			"type": "doctype",
            			"name": "Job Applicant",
            			"description": _("Applicant for a Job."),
            		},
            		{
            			"type": "doctype",
            			"name": "Offer Letter",
            			"description": _("Offer candidate a Job."),
            		},
                    
            	]
            },
            {
                "label": _("Leaves and Holiday"),
                "items": [
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Employee Leave Balance",
                        "doctype": "Leave Application"
                    },
                    {
                        "type": "doctype",
                        "name": "Leave Application",
                        "description": _("Applications for leave."),
                    },
                    {
                        "type": "doctype",
                        "label": _("On Duty Application"),
                        "name": "On Duty Application",
                        "description": _("Applications for OnDuty.")
                    },
                    {
                        "type": "doctype",
                        "label": _("Tour Application"),
                        "name": "Tour Application",
                        "description": _("Applications for OnDuty.")
                    },
                    {
                        "type": "doctype",
                        "name": "Movement Register",
                        "description": _("Applications for Permission.")
                    },
                    {
                        "type": "doctype",
                        "name": "Compensatory Off Application",
                        "description": _("Applications for Permission.")
                    },
                    {
                        "type": "doctype",
                        "name": "Leave Approval",
                        "description": _("Bulk Leave Approval")
                    },
                    {
                        "type": "doctype",
                        "name": "On Duty Approval",
                        "label": _("On Duty Approval"),
                        "description": _("Bulk On Duty Approval")
                    },
                    {
                        "type": "doctype",
                        "name": "Tour Application Approval",
                        "label": _("Tour Approval"),
                        "description": _("Bulk On Duty Approval")
                    },
                    {
                        "type": "doctype",
                        "name": "Movement Register Approval",
                        "description": _("Bulk Movement Register Approval")
                    },
                    {
                        "type": "doctype",
                        "name": "Compensatory Off Approval",
                        "description": _("Bulk Compensatory Off Approval")
                    },
                    {
                        "type": "doctype",
                        "name":"Leave Type",
                        "description": _("Type of leaves like casual, sick etc."),
                    },
                    {
                        "type": "doctype",
                        "name": "Holiday List",
                        "description": _("Holiday master.")
                    },
                    {
                        "type": "doctype",
                        "name": "Leave Allocation",
                        "description": _("Allocate leaves for a period.")
                    },
                    {
                        "type": "doctype",
                        "name": "Leave Control Panel",
                        "label": _("Leave Allocation Tool"),
                        "description":_("Allocate leaves for the year."),
                        "hide_count": True
                    },
                    {
                        "type": "doctype",
                        "name": "Leave Block List",
                        "description": _("Block leave applications by department.")
                    },
                    

                ]
            },
            {
                "label": _("Travel Management"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Travel Management",
                        "label": _("Travel Management Application"),
                        "description": _("Bulk Movement Register Approval."),
                    },
                    {
                        "type": "doctype",
                        "name": "Travel Management Approval",
                        "description": _("Bulk Movement Register Approval."),
                    },
                    {
                        "type": "doctype",
                        "name": "Expense Claim",
                        "label": _("Expense Claim Application"),
                        "description": _("Claims for company expense."),
                    },
                    {
                        "type": "doctype",
                        "name": "Expense Claim Approval",
                        "label": _("Expense Claim Approval"),
                        "description": _("Bulk Expense Claim Approval")
                    },
                    

                ]
            },
            {

                "label": _("Performance Management"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Performance Management",
                        "description": _("Performance Management."),
                    },
                    {
                        "type": "doctype",
                        "name": "Performance Management Self",
                        "label":_("Performance Management - Self"),
                        "description": _("Performance Management."),
                    }
                ]
            },
            {
            	"label": _("Payroll"),
            	"items": [
            		{
            			"type": "doctype",
            			"name": "Salary Slip",
            			"description": _("Monthly salary statement."),
            		},
            		{
            			"type": "doctype",
            			"name": "Payroll Entry",
            			"label": _("Payroll Entry"),
            			"description":_("Generate Salary Slips"),
            			"hide_count": True
            		},
            		{
            			"type": "doctype",
            			"name": "Salary Structure",
            			"description": _("Salary template master.")
            		},
            		{
            			"type": "doctype",
            			"name": "Salary Component",
            			"label": _("Salary Components"),
            			"description": _("Earnings, Deductions and other Salary components")
            		},

            	]
            },
            {
            	"label": _("Expense Claims"),
            	"items": [
            		{
            			"type": "doctype",
            			"name": "Employee Advance",
            			"description": _("Manage advance amount given to the Employee"),
            		},
            		{
            			"type": "doctype",
            			"name": "Expense Claim",
            			"description": _("Claims for company expense."),
            		},
            		{
            			"type": "doctype",
            			"name": "Expense Claim Type",
            			"description": _("Types of Expense Claim.")
            		},
            	]
            },
            {
            	"label": _("Appraisals"),
            	"items": [
            		{
            			"type": "doctype",
            			"name": "Appraisal",
            			"description": _("Performance appraisal."),
            		},
            		{
            			"type": "doctype",
            			"name": "Appraisal Template",
            			"description": _("Template for performance appraisals.")
            		},
            		{
            			"type": "page",
            			"name": "team-updates",
            			"label": _("Team Updates")
            		},
            	]
            },
            {
            	"label": _("Employee Loan Management"),
            	"icon": "icon-list",
            	"items": [
            		{
            			"type": "doctype",
            			"name": "Loan Type",
            			"description": _("Define various loan types")
            		},
            		{
            			"type": "doctype",
            			"name": "Employee Loan Application",
            			"description": _("Employee Loan Application")
            		},
            		{
            			"type": "doctype",
            			"name": "Employee Loan"
            		},
            	]
            },
            {
            	"label": _("Training"),
            	"items": [
            		{
            			"type": "doctype",
            			"name": "Training Program"
            		},
            		{
            			"type": "doctype",
            			"name": "Training Event"
            		},
            		{
            			"type": "doctype",
            			"name": "Training Result"
            		},
            		{
            			"type": "doctype",
            			"name": "Training Feedback"
            		},
            	]
            },

            {
                "label": _("Fleet Management"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Vehicle"
                    },
                    {
                        "type": "doctype",
                        "name": "Vehicle Log"
                    },
                ]
            },
            {
            	"label": _("Setup"),
            	"icon": "fa fa-cog",
            	"items": [
            		{
            			"type": "doctype",
            			"name": "HR Settings",
            			"description": _("Settings for HR Module")
            		},
            		{
            			"type": "doctype",
            			"name": "Employment Type",
            			"description": _("Types of employment (permanent, contract, intern etc.).")
            		},
            		{
            			"type": "doctype",
            			"name": "Branch",
            			"description": _("Organization branch master.")
            		},
            		{
            			"type": "doctype",
            			"name": "Department",
            			"description": _("Organization unit (department) master.")
            		},
            		{
            			"type": "doctype",
            			"name": "Designation",
            			"description": _("Employee designation (e.g. CEO, Director etc.).")
            		},
            		{
            			"type": "doctype",
            			"name": "Daily Work Summary Settings"
            		},
            	]
            },
            {
                "label": _("Reports"),
                "icon": "fa fa-list",
                "items": [
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Employee Leave Balance",
                        "doctype": "Leave Application"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Employee Birthday",
                        "doctype": "Employee"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Employees working on a holiday",
                        "doctype": "Employee"
                    },
                    {
                        "type": "report",
                        "name": "Employee Information",
                        "doctype": "Employee"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Salary Register",
                        "doctype": "Salary Slip"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Monthly Attendance Sheet",
                        "doctype": "Attendance"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Vehicle Expenses",
                        "doctype": "Vehicle"
                    },

                ]
            },
            # {
            # 	"label": _("Help"),
            # 	"icon": "fa fa-facetime-video",
            # 	"items": [
            # 		{
            # 			"type": "help",
            # 			"label": _("Setting up Employees"),
            # 			"youtube_id": "USfIUdZlUhw"
            # 		},
            # 		{
            # 			"type": "help",
            # 			"label": _("Leave Management"),
            # 			"youtube_id": "fc0p_AXebc8"
            # 		},
            # 		{
            # 			"type": "help",
            # 			"label": _("Expense Claims"),
            # 			"youtube_id": "5SZHJF--ZFY"
            # 		},
            # 		{
            # 			"type": "help",
            # 			"label": _("Processing Payroll"),
            # 			"youtube_id": "apgE-f25Rm0"
            # 		},
            # 	]
            # }
        ]
    else:
        columns =  [
            {
                "label": _("Employee and Attendance"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Employee",
                        "description": _("Employee records."),
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Attendance recapitulation",
                        "label": _("Attendance Summary"),
                        "doctype": "Attendance"
                    },
                    {
                        "type": "doctype",
                        "name": "Employee Attendance Tool",
                        "label": _("Employee Attendance Tool"),
                        "description":_("Mark Attendance for multiple employees"),
                        "hide_count": True
                    },
                    {
                        "label": _("Performance Management"),
                        "type": "doctype",
                        "name": "Appraisal",
                        "description":_("Upload attendance from a .csv file"),
                        "hide_count": True
                        # "hidden": 1
                    },
                    # {
                    #     "type": "doctype",
                    #     "name": "Attendance",
                    #     "description": _("Attendance record."),
                    # },
                    {
                        "type": "doctype",
                        "name": "Upload Attendance",
                        "description":_("Upload attendance from a .csv file"),
                        "hide_count": True
                    },
                ]
            },
            # {
            # 	"label": _("Recruitment"),
            # 	"items": [
            # 		{
            # 			"type": "doctype",
            # 			"name": "Job Opening",
            # 			"description": _("Opening for a Job."),
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Job Applicant",
            # 			"description": _("Applicant for a Job."),
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Offer Letter",
            # 			"description": _("Offer candidate a Job."),
            # 		},
                    
            # 	]
            # },
            {
                "label": _("Leaves and Holiday"),
                "items": [
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Employee Leave Balance",
                        "doctype": "Leave Application",
                        "hide_count": True
                    },
                    {
                        "type": "doctype",
                        "name": "Leave Application",
                        "description": _("Applications for leave."),
                        "hide_count": True
                    },
                    
                    {
                        "type": "doctype",
                        "label": _("On Duty Application"),
                        "name": "On Duty Application",
                        "description": _("Applications for OnDuty."),
                        "hide_count": True
                    },
                    {
                        "type": "doctype",
                        "label": _("Tour Application"),
                        "name": "Tour Application",
                        "description": _("Applications for OnDuty."),
                        "hide_count": True
                    },
                    
                    {
                        "type": "doctype",
                        "name": "Movement Register",
                        "description": _("Applications for Permission."),
                        "hide_count": True
                    },
                    {
                        "type": "doctype",
                        "name": "Leave Approval",
                        "description": _("Bulk Leave Approval")
                    },
                    {
                        "type": "doctype",
                        "name": "On Duty Approval",
                        "label": _("On Duty Approval"),
                        "description": _("Bulk On Duty Approval")
                    },
                    {
                        "type": "doctype",
                        "name": "Tour Application Approval",
                        "label": _("Tour Approval"),
                        "description": _("Bulk On Duty Approval")
                    },
                    {
                        "type": "doctype",
                        "name": "Movement Register Approval",
                        "description": _("Bulk Movement Register Approval")
                    },
                    # {
                    #     "type": "doctype",
                    #     "name": "Compensatory Off Application",
                    #     "description": _("Applications for Permission.")
                    # },
                    # {
                    #     "type": "doctype",
                    #     "name": "Compensatory Off Approval",
                    #     "description": _("Bulk Compensatory Off Approval")
                    # },
                    # {
                    #     "type": "doctype",
                    #     "name":"Leave Type",
                    #     "description": _("Type of leaves like casual, sick etc."),
                    # },
                    {
                        "type": "doctype",
                        "name": "Holiday List",
                        "description": _("Holiday master.")
                    },
                    # {
                    #     "type": "doctype",
                    #     "name": "Leave Allocation",
                    #     "description": _("Allocate leaves for a period.")
                    # },
                    {
                        "type": "doctype",
                        "name": "Leave Control Panel",
                        "label": _("Leave Allocation Tool"),
                        "description":_("Allocate leaves for the year."),
                        "hide_count": True
                    },
                    {
                        "type": "doctype",
                        "name": "Leave Block List",
                        "description": _("Block leave applications by department.")
                    },
                    

                ]
            },
            # {
            #     "label": _("Travel Management"),
            #     "items": [
            #         {
            #             "type": "doctype",
            #             "name": "Travel Management",
            #             "description": _("Bulk Movement Register Approval."),
            #         },
            #         {
            #             "type": "doctype",
            #             "name": "Travel Management Approval",
            #             "description": _("Bulk Movement Register Approval."),
            #         },
            #         {
            #             "type": "doctype",
            #             "name": "Expense Claim",
            #             "description": _("Claims for company expense."),
            #         },
            #         {
            #             "type": "doctype",
            #             "name": "Expense Claim Approval",
            #             "label": _("Expense Claim Approval"),
            #             "description": _("Bulk Expense Claim Approval")
            #         },
            #     ]
            # },
            {

                "label": _("Annual Appraisal (PMS)"),
                "items": [
                    # {
                    #     "type": "doctype",
                    #     "name": "PM Merit Increase",
                    #     "label":_("Merit Increase (Annexure) - 2019"),
                    #     "description": _("Performance Management."),
                    #     "hide_count": True
                    # },
                    # {
                    #     "type": "doctype",
                    #     "name": "Individual Performance",
                    #     "label":_("Performance Feedback & Merit Increase"),
                    #     "description": _("Performance Feedback & Merit Increase"),
                    #     "hide_count": True
                    # },
                    # {
                    #     "type": "doctype",
                    #     "name": "Performance Management Self",
                    #     "label":_("Performance Management System - Self & Merit Increase 2019"),
                    #     "description": _("Performance Management."),
                    #     "hide_count": True
                    # }
                ]
            },
            # {
            # 	"label": _("Payroll"),
            # 	"items": [
            # 		{
            # 			"type": "doctype",
            # 			"name": "Salary Slip",
            # 			"description": _("Monthly salary statement."),
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Payroll Entry",
            # 			"label": _("Payroll Entry"),
            # 			"description":_("Generate Salary Slips"),
            # 			"hide_count": True
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Salary Structure",
            # 			"description": _("Salary template master.")
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Salary Component",
            # 			"label": _("Salary Components"),
            # 			"description": _("Earnings, Deductions and other Salary components")
            # 		},

            # 	]
            # },
            # {
            # 	"label": _("Expense Claims"),
            # 	"items": [
            # 		{
            # 			"type": "doctype",
            # 			"name": "Employee Advance",
            # 			"description": _("Manage advance amount given to the Employee"),
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Expense Claim",
            # 			"description": _("Claims for company expense."),
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Expense Claim Type",
            # 			"description": _("Types of Expense Claim.")
            # 		},
            # 	]
            # },
            # {
            # 	"label": _("Appraisals"),
            # 	"items": [
            # 		{
            # 			"type": "doctype",
            # 			"name": "Appraisal",
            # 			"description": _("Performance appraisal."),
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Appraisal Template",
            # 			"description": _("Template for performance appraisals.")
            # 		},
            # 		{
            # 			"type": "page",
            # 			"name": "team-updates",
            # 			"label": _("Team Updates")
            # 		},
            # 	]
            # },
            # {
            # 	"label": _("Employee Loan Management"),
            # 	"icon": "icon-list",
            # 	"items": [
            # 		{
            # 			"type": "doctype",
            # 			"name": "Loan Type",
            # 			"description": _("Define various loan types")
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Employee Loan Application",
            # 			"description": _("Employee Loan Application")
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Employee Loan"
            # 		},
            # 	]
            # },
            # {
            # 	"label": _("Training"),
            # 	"items": [
            # 		{
            # 			"type": "doctype",
            # 			"name": "Training Program"
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Training Event"
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Training Result"
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Training Feedback"
            # 		},
            # 	]
            # },

            # {
            #     "label": _("Fleet Management"),
            #     "items": [
            #         {
            #             "type": "doctype",
            #             "name": "Vehicle"
            #         },
            #         {
            #             "type": "doctype",
            #             "name": "Vehicle Log"
            #         },
            #     ]
            # },
            # {
            # 	"label": _("Setup"),
            # 	"icon": "fa fa-cog",
            # 	"items": [
            # 		{
            # 			"type": "doctype",
            # 			"name": "HR Settings",
            # 			"description": _("Settings for HR Module")
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Employment Type",
            # 			"description": _("Types of employment (permanent, contract, intern etc.).")
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Branch",
            # 			"description": _("Organization branch master.")
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Department",
            # 			"description": _("Organization unit (department) master.")
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Designation",
            # 			"description": _("Employee designation (e.g. CEO, Director etc.).")
            # 		},
            # 		{
            # 			"type": "doctype",
            # 			"name": "Daily Work Summary Settings"
            # 		},
            # 	]
            # },
            {
                "label": _("Reports"),
                "icon": "fa fa-list",
                "items": [
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Employee Leave Balance",
                        "doctype": "Leave Application"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Employee Birthday",
                        "doctype": "Employee"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Employees working on a holiday",
                        "doctype": "Employee"
                    },
                    {
                        "type": "report",
                        "name": "Employee Information",
                        "doctype": "Employee"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Salary Register",
                        "doctype": "Salary Slip"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Monthly Attendance Sheet",
                        "doctype": "Attendance"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Vehicle Expenses",
                        "doctype": "Vehicle"
                    },

                ]
            },
            # {
            # 	"label": _("Help"),
            # 	"icon": "fa fa-facetime-video",
            # 	"items": [
            # 		{
            # 			"type": "help",
            # 			"label": _("Setting up Employees"),
            # 			"youtube_id": "USfIUdZlUhw"
            # 		},
            # 		{
            # 			"type": "help",
            # 			"label": _("Leave Management"),
            # 			"youtube_id": "fc0p_AXebc8"
            # 		},
            # 		{
            # 			"type": "help",
            # 			"label": _("Expense Claims"),
            # 			"youtube_id": "5SZHJF--ZFY"
            # 		},
            # 		{
            # 			"type": "help",
            # 			"label": _("Processing Payroll"),
            # 			"youtube_id": "apgE-f25Rm0"
            # 		},
            # 	]
            # }
        ]
        
        merit_viewer_ecode = frappe.get_value("Employee",{'user_id':frappe.session.user},'employee')
        merit_viewer = frappe.db.exists("Performance Management Calibration",{'employee_code':merit_viewer_ecode})
        if merit_viewer:  
            items = columns[2]['items']
            item = {}
            item.update({
                "type": "doctype",
                "name": "PM Merit Increase",
                "label":_("Merit Increase (Annexure) - 2019"),
                "description": _("Performance Management."),
                "hide_count": True
            })
            items.append(item)
        # manager = frappe.get_doc("User", frappe.session.user).get("roles",{"role": "One Above Manager"})
        # if manager:  
        #     items = columns[2]['items']
        #     item = {}
        #     item.update({
        #         "type": "doctype",
        #         "name": "Performance Management Manager",
        #         "label":_("Performance Management System - Manager"),
        #         "description": _("Performance Management."),
        #         "hide_count": True
        #     })
        #     items.append(item)

        # hod = frappe.get_doc("User", frappe.session.user).get("roles",{"role": "HOD"})
        # if hod:    
        #     items = columns[2]['items']
        #     item = {}
        #     item.update({
        #         "type": "doctype",
        #         "name": "Performance Management HOD",
        #         "label":_("Performance Management System - HOD"),
        #         "description": _("Performance Management."),
        #         "hide_count": True
        #     })
        #     items.append(item)

        # reviewer = frappe.get_doc("User", frappe.session.user).get("roles",{"role": "Reviewer"})
        # if reviewer:    
        #     items = columns[2]['items']
        #     item = {}
        #     item.update({
        #         "type": "doctype",
        #         "name": "Performance Management Reviewer",
        #         "label":_("Performance Management System - Principle Reviewer"),
        #         "description": _("Performance Management."),
        #         "hide_count": True
        #     })
        #     items.append(item)
            # items = columns[2]['items']
            # item = {}
            # item.update({
            #     "type": "doctype",
            #     "name": "Appraisal",
            #     "label":_("Non-Management PMS- Principle Reviewer"),
            #     "description": _("Non-Management PMS"),
            #     "hide_count": True
            # })
            # items.append(item)       
        
        stu = frappe.get_doc("User", frappe.session.user).get("roles",{"role": "Shift Tool User"})
        if stu:    
            items = columns[0]['items']
            item = {}
            item.update({
                "type": "doctype",
                "name": "Shift Assignment Tool",
                "label":_("Shift Assignment Tool"),
                "description": _("Shift Assignment Tool."),
                "hide_count": True
            })
            items.append(item)    
        sa = frappe.get_doc("User", frappe.session.user).get("roles",{"role": "Shift Tool User"})
        if sa:    
            items = columns[0]['items']
            item = {}
            item.update({
                "type": "doctype",
                "name": "Shift Assignment",
                "label":_("Shift Assignment"),
                "description": _("Shift Assignment."),
                "hide_count": True
            })
            items.append(item) 

        return columns
