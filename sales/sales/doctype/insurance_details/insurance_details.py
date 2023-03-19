# Copyright (c) 2023, Sales and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class InsuranceDetails(Document):
	pass

def validate(doc,method=None):
	year = frappe.db.get_value('insurance',{'customer':doc.customer},['year'])
	doc.year = year
	doc.policy_number = 'AA11BB8867554'
	doc.regristration_number = 'MH01TR0000'
	