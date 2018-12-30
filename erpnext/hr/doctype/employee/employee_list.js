frappe.listview_settings['Employee'] = {
	add_fields: ["status", "branch", "department", "designation","image"],
	filters: [["user_id","=", "vijayakumar.j@hunterdouglas.in"]],
	get_indicator: function(doc) {
		var indicator = [__(doc.status), frappe.utils.guess_colour(doc.status), "status,=," + doc.status];
		indicator[1] = {"Active": "green", "Left": "darkgrey"}[doc.status];
		return indicator;
	},
	refresh:function(me){
		me.page.sidebar.find(".list-link[data-view='Kanban']").addClass("hide");
		me.page.sidebar.find(".list-link[data-view='Tree']").addClass("hide");
		me.page.sidebar.find(".assigned-to-me a").addClass("hide");
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
						emp = r.message.employee;
						if (!frappe.route_options) {
							frappe.route_options = {
								"employee": ["=", emp],
							};
					    }
					}
				})
			}
		})
	}
	
	
};