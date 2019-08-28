frappe.listview_settings['Offer Letter'] = {
    refresh: function (frm) {
        if(frappe.session.user == "raghavan.s@hunterdouglas.in"){
            if (!frappe.route_options) {            
                frappe.route_options = {
                    "ok_for_salary": ["=", 0]
                };                       
            }
        }
    }
};