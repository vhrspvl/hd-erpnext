frappe.listview_settings['Leave Application'] = {
	add_fields: ["status", "leave_type", "employee", "employee_name", "total_leave_days", "from_date", "to_date"],
	filters:[["status","!=", "Rejected"]],
	get_indicator: function(doc) {
		return [__(doc.status), frappe.utils.guess_colour(doc.status),
			"status,=," + doc.status];
	},
	refresh:function(me){
		var emp = 0;
		me.page.sidebar.find(".list-link[data-view='Kanban']").addClass("hide");
		me.page.sidebar.find(".list-link[data-view='Tree']").addClass("hide");
		me.page.sidebar.find(".assigned-to-me a").addClass("hide");	
		frappe.model.get_value('Employee', { 'user_id': frappe.session.user }, 'employee_number',
            function (data) {
                if (data) {
                    me.filter_list.add_filter(me.doctype, "employee", '=', data.employee_number);
                    me.run()
                }
            })	
		frappe.call({
			"method": "frappe.client.get_list",
			args:{
				doctype: "Employee",
				filters: {"user_id": frappe.session.user}
			},
			callback: function(r){
				frappe.call({
					"method": "frappe.client.get",
					args:{
						doctype: "Employee",
						name: r.message[0].name
					},
					callback: function(r){
						emp = r.message.employee_number;
						if (!frappe.route_options) {
							frappe.route_options = {
								"employee": ["=", emp]
							};
					    }
					}
				})
			}
		})	
	}
};

