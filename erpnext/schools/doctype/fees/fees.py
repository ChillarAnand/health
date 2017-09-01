# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document
import frappe
from frappe import _
from frappe.utils import money_in_words
from erpnext.accounts.doctype.payment_request.payment_request import make_payment_request
from frappe.utils.csvutils import getlink
from erpnext.controllers.accounts_controller import AccountsController
from erpnext.accounts.general_ledger import delete_gl_entries


class Fees(AccountsController):
	def set_indicator(self):
		"""Set indicator for portal"""
		if self.outstanding_amount > 0:
			self.indicator_color = "orange"
			self.indicator_title = _("Unpaid")
		else:
			self.indicator_color = "green"
			self.indicator_title = _("Paid")

	def validate(self):
		self.calculate_total()
		self.set_missing_accounts_and_fields()

	def set_missing_accounts_and_fields(self):
		if not self.company:
			self.company = frappe.defaults.get_defaults().company
		if not self.currency:
			self.currency = frappe.defaults.get_defaults().currency
		if not (self.debit_to and self.against_income_account and self.cost_center):
			accounts_details = frappe.get_all("Company", fields=["default_receivable_account",
				"default_income_account", "cost_center"], filters={"name": self.company})[0]
		if not self.debit_to:
			self.debit_to = accounts_details.default_receivable_account
		if not self.against_income_account:
			self.against_income_account = accounts_details.default_income_account
		if not self.cost_center:
			self.cost_center = accounts_details.cost_center

	def calculate_total(self):
		"""Calculates total amount."""
		self.grand_total = 0
		for d in self.components:
			self.grand_total += d.amount
		self.outstanding_amount = self.grand_total
		self.grand_total_in_words = money_in_words(self.grand_total)

	def on_submit(self):

		self.make_gl_entries()

		if self.send_payment_request and self.student_email:
			pr = make_payment_request(dt="Fees", dn=self.name, recipient_id=self.contact_email,
					submit_doc=True, use_dummy_message=True)
			frappe.msgprint(_("Payment request {0} created").format(getlink("Payment Request", pr.name)))

	def on_cancel(self):
		delete_gl_entries(voucher_type=self.doctype, voucher_no=self.name)
		# frappe.db.set(self, 'status', 'Cancelled')


	def make_gl_entries(self):
		if not self.grand_total:
			return
		student_gl_entries =  self.get_gl_dict({
			"account": self.debit_to,
			"party_type": "Student",
			"party": self.student,
			"against": self.against_income_account,
			"debit": self.grand_total,
			"debit_in_account_currency": self.grand_total,
			"against_voucher": self.name,
			"against_voucher_type": self.doctype
		})
		fee_gl_entry = self.get_gl_dict({
			"account": self.against_income_account,
			"against": self.student,
			"credit": self.grand_total,
			"credit_in_account_currency": self.grand_total,
			"cost_center": self.cost_center
		})
		from erpnext.accounts.general_ledger import make_gl_entries
		make_gl_entries([student_gl_entries, fee_gl_entry], cancel=(self.docstatus == 2),
			update_outstanding="Yes", merge_entries=False)

def get_fee_list(doctype, txt, filters, limit_start, limit_page_length=20, order_by="modified"):
	user = frappe.session.user
	student = frappe.db.sql("select name from `tabStudent` where student_email_id= %s", user)
	if student:
		return frappe. db.sql('''select name, program, due_date, paid_amount, outstanding_amount, total_amount from `tabFees`
			where student= %s and docstatus=1
			order by due_date asc limit {0} , {1}'''
			.format(limit_start, limit_page_length), student, as_dict = True)

def get_list_context(context=None):
	return {
		"show_sidebar": True,
		"show_search": True,
		'no_breadcrumbs': True,
		"title": _("Fees"),
		"get_list": get_fee_list,
		"row_template": "templates/includes/fee/fee_row.html"
	}