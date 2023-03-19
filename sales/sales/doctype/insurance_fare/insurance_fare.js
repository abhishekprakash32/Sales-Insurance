// Copyright (c) 2023, Sales and contributors
// For license information, please see license.txt

frappe.ui.form.on('Insurance Fare', {
	customer: function(frm) {
		frappe.call({
			method: "sales.sales.api.insurance.get_year",
			args: {
				customer: frm.doc.customer,
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value('year',r.message)
					frm.set_value('own_damage_premium',1000)
					frm.set_value('gst',500)
					frm.set_value('final_premium',1500)
				}
			}
		});
	}
});
