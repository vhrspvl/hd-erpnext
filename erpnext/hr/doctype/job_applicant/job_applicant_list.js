frappe.listview_settings['Job Applicant'] = {
    refresh: function (frm) {
        if(frappe.user.has_role("HR User") && !frappe.user.has_role("System Manager")){
            if (!frappe.route_options) {            
                frappe.route_options = {
                    "status": ["=", "Open"]
                };                       
            }
        }
    }
};