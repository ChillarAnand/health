# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
# License: GNU General Public License v3. See license.txt

# For license information, please see license.txt

from __future__ import unicode_literals
import webnotes
from accounts.utils import validate_fiscal_year
from webnotes import _

class DocType:
	def __init__(self, d, dl):
		self.doc, self.doclist = d, dl
		
	def validate(self):
		dates = []
		for d in self.doclist.get({"doctype":"Leave Block List Date"}):
			# validate fiscal year
			validate_fiscal_year(d.block_date, self.doc.year, _("Block Date"))
			
			# date is not repeated
			if d.block_date in dates:
				webnotes.msgprint(_("Date is repeated") + ":" + d.block_date, raise_exception=1)
			dates.append(d.block_date)

@webnotes.whitelist()
def get_applicable_block_dates(from_date, to_date, employee=None, 
	company=None, all_lists=False):
	block_dates = []
	for block_list in get_applicable_block_lists(employee, company, all_lists):
		block_dates.extend(webnotes.conn.sql("""select block_date, reason 
			from `tabLeave Block List Date` where parent=%s 
			and block_date between %s and %s""", (block_list, from_date, to_date), 
			as_dict=1))
			
	return block_dates
		
def get_applicable_block_lists(employee=None, company=None, all_lists=False):
	block_lists = []
	
	if not employee:
		employee = webnotes.conn.get_value("Employee", {"user_id":webnotes.session.user})
		if not employee:
			return []
	
	if not company:
		company = webnotes.conn.get_value("Employee", employee, "company")
		
	def add_block_list(block_list):
		if block_list:
			if all_lists or not is_user_in_allow_list(block_list):
				block_lists.append(block_list)

	# per department
	department = webnotes.conn.get_value("Employee",employee, "department")
	if department:
		block_list = webnotes.conn.get_value("Department", department, "leave_block_list")
		add_block_list(block_list)

	# global
	for block_list in webnotes.conn.sql_list("""select name from `tabLeave Block List`
		where ifnull(applies_to_all_departments,0)=1 and company=%s""", company):
		add_block_list(block_list)
		
	return list(set(block_lists))
	
def is_user_in_allow_list(block_list):
	return webnotes.session.user in webnotes.conn.sql_list("""select allow_user
		from `tabLeave Block List Allow` where parent=%s""", block_list)