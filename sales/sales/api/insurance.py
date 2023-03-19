import frappe

@frappe.whitelist()
def get_year(customer):
    year = frappe.db.get_value('Insurance Details',{'customer':customer},['year'])
    return year