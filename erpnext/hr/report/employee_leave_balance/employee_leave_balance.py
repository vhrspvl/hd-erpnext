# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from erpnext.hr.doctype.leave_application.leave_application \
    import get_leave_allocation_records, get_leave_balance_on, get_approved_leaves_for_period


def execute(filters=None):
    leave_types = frappe.db.sql_list("select name from `tabLeave Type` order by name asc")
    columns = get_columns(leave_types)
    data = get_data(filters, leave_types)
    
    return columns, data
    
def get_columns(leave_types):
    columns = [
        _("Employee") + ":Link/Employee:80", 
        _("Employee Name") + "::120", 
        _("Department") +"::120"
    ]

    for leave_type in leave_types:
        if leave_type == 'Casual Leave':
            short_code = 'CL'
        elif leave_type == 'Privilege Leave':
            short_code = 'PL'  
        elif leave_type == 'Sick Leave':
            short_code = 'SL'  
        elif leave_type == 'Compensatory Off':
            short_code = 'C-Off'  
        elif leave_type == 'Leave Without Pay':
            short_code = 'LWP'       
        else:
            short_code = leave_type       
        columns.append(_(short_code) + " " + _("Opening") + ":Data:100")
        columns.append(_(short_code) + " " + _("Taken") + ":Data:100")
        columns.append(_(short_code) + " " + _("Balance") + ":Data  :100")
        
    return columns
    
def get_data(filters, leave_types):
    user = frappe.session.user
    allocation_records_based_on_to_date = get_leave_allocation_records(filters.to_date)
    allocation_records_based_on_from_date = get_leave_allocation_records(filters.from_date)
    hr_manager = frappe.get_doc("User", frappe.session.user).get("roles",{"role": "HR Manager"})
    if hr_manager:
        emp_filters = { "status": "Active", "company": filters.company,"department": filters.department} 
    else:
        emp_filters = { "status": "Active", "company": filters.company,"department": filters.department,"user_id":frappe.session.user} 
    
    active_employees = frappe.get_all("Employee", 
        filters = emp_filters, 
        fields = ["name", "employee_name", "department", "user_id"],
        order_by="name desc")
    
    data = []
    for employee in active_employees:
        leave_approvers = [l.leave_approver for l in frappe.db.sql("""select leave_approver from `tabEmployee Leave Approver` where parent = %s""",
                            (employee.name),as_dict=True)]
        if (len(leave_approvers) and user in leave_approvers) or (user in ["Administrator", employee.user_id]) or ("HR Manager" in frappe.get_roles(user)):
            row = [employee.name, employee.employee_name, employee.department]

            for leave_type in leave_types:
                # leaves taken
                leaves_taken = get_approved_leaves_for_period(employee.name, leave_type,
                    filters.from_date, filters.to_date)

                # opening balance
                opening = get_leave_balance_on(employee.name, leave_type, filters.from_date,
                    allocation_records_based_on_from_date.get(employee.name, frappe._dict()))

                # closing balance
                closing = get_leave_balance_on(employee.name, leave_type, filters.to_date,
                    allocation_records_based_on_to_date.get(employee.name, frappe._dict()))

                row += [opening, leaves_taken, closing]
            
            data.append(row)
        
    return data
