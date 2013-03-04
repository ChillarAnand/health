# ERPNext - web based ERP (http://erpnext.com)
# Copyright (C) 2012 Web Notes Technologies Pvt Ltd
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals
patch_list = [
	"patches.mar_2012.so_rv_mapper_fix", 
	"patches.mar_2012.clean_property_setter", 
	"patches.april_2012.naming_series_patch", 
	"patches.mar_2012.cleanup_control_panel", 
	"patches.mar_2012.doctype_get_refactor", 
	"patches.mar_2012.delete_docformat", 
	"patches.mar_2012.usertags", 
	"patches.april_2012.reload_c_form", 
	"patches.april_2012.after_sync_cleanup", 
	"patches.april_2012.remove_default_from_rv_detail", 
	"patches.april_2012.update_role_in_address", 
	"patches.april_2012.update_permlevel_in_address", 
	"patches.april_2012.update_appraisal_permission", 
	"patches.april_2012.serial_no_fixes", 
	"patches.april_2012.repost_stock_for_posting_time", 
	"patches.may_2012.cleanup_property_setter", 
	"patches.may_2012.rename_prev_doctype", 
	"patches.may_2012.cleanup_notification_control", 
	"patches.may_2012.renamedt_in_custom_search_criteria", 
	"patches.may_2012.stock_reco_patch", 
	"patches.may_2012.reload_reports", 
	"patches.may_2012.page_role_series_fix", 
	"patches.may_2012.reload_sales_invoice_pf", 
	"patches.may_2012.std_pf_readonly", 
	"patches.may_2012.reload_so_pending_items", 
	"patches.may_2012.customize_form_cleanup", 
	"patches.may_2012.cs_server_readonly", 
	"patches.may_2012.clear_session_cache", 
	"patches.may_2012.same_purchase_rate_patch", 
	"patches.may_2012.create_report_manager_role", 
	"patches.may_2012.reload_customer_address_contact", 
	"patches.may_2012.profile_perm_patch", 
	"patches.may_2012.remove_euro_currency", 
	"patches.may_2012.remove_communication_log", 
	"patches.june_2012.barcode_in_feature_setup", 
	"patches.june_2012.copy_uom_for_pur_inv_item", 
	"patches.june_2012.fetch_organization_from_lead", 
	"patches.june_2012.reports_list_permission", 
	"patches.june_2012.support_ticket_autoreply", 
	"patches.june_2012.series_unique_patch", 
	"patches.june_2012.set_recurring_type", 
	"patches.june_2012.alter_tabsessions", 
	"patches.june_2012.delete_old_parent_entries", 
	"patches.april_2012.delete_about_contact", 
	"patches.july_2012.reload_pr_po_mapper", 
	"patches.july_2012.address_contact_perms", 
	"patches.july_2012.packing_list_cleanup_and_serial_no", 
	"patches.july_2012.deprecate_import_data_control", 
	"patches.july_2012.default_freeze_account", 
	"patches.july_2012.update_purchase_tax", 
	"patches.june_2012.cms2", 
	"patches.july_2012.auth_table", 
	"patches.july_2012.remove_event_role_owner_match", 
	"patches.july_2012.deprecate_bulk_rename", 
	"patches.july_2012.blog_guest_permission", 
	"patches.july_2012.bin_permission", 
	"patches.july_2012.project_patch_repeat", 
	"patches.july_2012.repost_stock_due_to_wrong_packing_list", 
	"patches.july_2012.supplier_quotation", 
	"patches.august_2012.report_supplier_quotations", 
	"patches.august_2012.task_allocated_to_assigned", 
	"patches.august_2012.change_profile_permission", 
	"patches.august_2012.changed_blog_date_format", 
	"patches.august_2012.repost_billed_amt", 
	"patches.august_2012.remove_cash_flow_statement", 
	"patches.september_2012.stock_report_permissions_for_accounts", 
	"patches.september_2012.communication_delete_permission", 
	"patches.september_2012.all_permissions_patch", 
	"patches.september_2012.customer_permission_patch", 
	"patches.september_2012.add_stock_ledger_entry_index", 
	"patches.september_2012.plot_patch", 
	"patches.september_2012.event_permission", 
	"patches.september_2012.repost_stock", 
	"patches.september_2012.reload_gross_profit", 
	"patches.september_2012.rebuild_trees", 
	"patches.september_2012.deprecate_account_balance", 
	"patches.september_2012.profile_delete_permission", 
	"patches.october_2012.update_permission", 
	"patches.october_2012.reload_gl_mapper", 
	"patches.october_2012.fix_wrong_vouchers", 
	"patches.october_2012.remove_old_customer_contact_address", 
	"patches.october_2012.company_fiscal_year_docstatus_patch", 
	"patches.october_2012.update_account_property", 
	"patches.october_2012.remove_old_trial_bal", 
	"patches.october_2012.fix_cancelled_gl_entries", 
	"patches.october_2012.custom_script_delete_permission", 
	"patches.november_2012.custom_field_insert_after", 
	"patches.november_2012.delete_item_sales_register1", 
	"patches.november_2012.rename_employee_leave_balance_report", 
	"patches.november_2012.report_permissions", 
	"patches.november_2012.customer_issue_allocated_to_assigned", 
	"patches.november_2012.reset_appraisal_permissions", 
	"patches.november_2012.disable_cancelled_profiles", 
	"patches.november_2012.remove_old_unbilled_items_report", 
	"patches.november_2012.support_ticket_response_to_communication", 
	"patches.november_2012.cancelled_bom_patch", 
	"patches.november_2012.communication_sender_and_recipient", 
	"patches.november_2012.update_delivered_billed_percentage_for_pos", 
	"patches.november_2012.add_theme_to_profile", 
	"patches.november_2012.add_employee_field_in_employee", 
	"patches.november_2012.leave_application_cleanup", 
	"patches.november_2012.production_order_patch", 
	"patches.november_2012.gle_floating_point_issue", 
	"patches.december_2012.deprecate_tds", 
	"patches.december_2012.expense_leave_reload", 
	"patches.december_2012.repost_ordered_qty", 
	"patches.december_2012.repost_projected_qty", 
	"patches.december_2012.reload_debtors_creditors_ledger", 
	"patches.december_2012.website_cache_refactor", 
	"patches.december_2012.production_cleanup", 
	"patches.december_2012.fix_default_print_format", 
	"patches.december_2012.file_list_rename", 
	"patches.december_2012.replace_createlocal", 
	"patches.december_2012.clear_web_cache", 
	"patches.december_2012.remove_quotation_next_contact", 
	"patches.december_2012.stock_entry_cleanup", 
	"patches.december_2012.production_order_naming_series", 
	"patches.december_2012.rebuild_item_group_tree", 
	"patches.december_2012.address_title", 
	"patches.december_2012.delete_form16_print_format", 
	"patches.december_2012.remove_project_mapper", 
	"patches.december_2012.update_print_width", 
	"patches.january_2013.remove_bad_permissions", 
	"patches.january_2013.deprecate_stock_search_criteria", 
	"patches.january_2013.remove_support_search_criteria", 
	"patches.january_2013.holiday_list_patch", 
	"patches.january_2013.stock_reconciliation_patch", 
	"patches.january_2013.report_permission", 
	"patches.january_2013.give_report_permission_on_read", 
	"patches.january_2013.update_closed_on",
	"patches.january_2013.change_patch_structure",
	"patches.january_2013.update_country_info",
	"patches.january_2013.remove_tds_entry_from_gl_mapper",
	"patches.january_2013.update_number_format",
	"patches.january_2013.purchase_price_list",
	"execute:webnotes.reload_doc('accounts','Print Format','Payment Receipt Voucher')",
	"patches.january_2013.update_fraction_for_usd",
	"patches.january_2013.enable_currencies",
	"patches.january_2013.remove_unwanted_permission",
	"patches.january_2013.remove_landed_cost_master",
	"patches.january_2013.reload_print_format",
	"patches.january_2013.rebuild_tree",
	"execute:webnotes.reload_doc('core','doctype','docfield') #2013-01-28",
	"patches.january_2013.tabsessions_to_myisam",
	"patches.february_2013.remove_gl_mapper",
	"patches.february_2013.reload_bom_replace_tool_permission",
	"patches.february_2013.payment_reconciliation_reset_values",
	"patches.february_2013.remove_sales_order_pending_items",
	"patches.february_2013.account_negative_balance",
	"patches.february_2013.remove_account_utils_folder",
	"patches.february_2013.update_company_in_leave_application",
	"execute:webnotes.conn.sql_ddl('alter table tabSeries change `name` `name` varchar(100)')",
	"execute:webnotes.conn.sql('update tabUserRole set parentfield=\"user_roles\" where parentfield=\"userroles\"')",
	"patches.february_2013.p01_event",
	"execute:webnotes.delete_doc('Page', 'Calendar')",
	"patches.february_2013.p02_email_digest",
	"patches.february_2013.p03_material_request",
	"patches.february_2013.p04_remove_old_doctypes",
	"execute:webnotes.delete_doc('DocType', 'Plot Control')",
	"patches.february_2013.p05_leave_application",
	"patches.february_2013.gle_floating_point_issue_revisited",
	"patches.february_2013.fix_outstanding",
	'execute:webnotes.reload_doc("selling", "Print Format", "Quotation Classic") # 2013-02-19',
	'execute:webnotes.reload_doc("selling", "Print Format", "Quotation Modern") # 2013-02-19',
	'execute:webnotes.reload_doc("selling", "Print Format", "Quotation Spartan") # 2013-02-19',
	"execute:webnotes.delete_doc('DocType', 'Service Order')",
	"execute:webnotes.delete_doc('DocType', 'Service Quotation')",
	"execute:webnotes.delete_doc('DocType', 'Service Order Detail')",
	"execute:webnotes.delete_doc('DocType', 'Service Quotation Detail')",
	"patches.february_2013.p06_material_request_mappers",
	"patches.february_2013.p07_clear_web_cache",
	"execute:webnotes.delete_doc('Page', 'Query Report')",
	"execute:webnotes.delete_doc('Search Criteria', 'employeewise_balance_leave_report')",
	"execute:webnotes.delete_doc('Search Criteria', 'employee_leave_balance_report')",
	"patches.february_2013.repost_reserved_qty",
	"execute:webnotes.reload_doc('core', 'doctype', 'report') # 2013-02-25",
	"execute:webnotes.conn.sql(\"update `tabReport` set report_type=if(ifnull(query, '')='', 'Report Builder', 'Query Report') where is_standard='No'\")",
	"execute:webnotes.conn.sql(\"update `tabReport` set report_name=name where ifnull(report_name,'')='' and is_standard='No'\")",
	"patches.february_2013.p08_todo_query_report",
	"execute:webnotes.delete_doc('Search Criteria', 'gross_profit') # 2013-02-26",
	'execute:webnotes.reload_doc("accounts", "Print Format", "Sales Invoice Classic") # 2013-02-26',
	'execute:webnotes.reload_doc("accounts", "Print Format", "Sales Invoice Modern") # 2013-02-26',
	'execute:webnotes.reload_doc("accounts", "Print Format", "Sales Invoice Spartan") # 2013-02-26',
	"execute:(not webnotes.conn.exists('Role', 'Projects Manager')) and webnotes.doc({'doctype':'Role', 'role_name':'Projects Manager'}).insert()",
	"patches.february_2013.p09_remove_cancelled_warehouses",
	"patches.march_2013.update_po_prevdoc_doctype",
	"patches.february_2013.p09_timesheets",
	"execute:(not webnotes.conn.exists('UOM', 'Hour')) and webnotes.doc({'uom_name': 'Hour', 'doctype': 'UOM', 'name': 'Hour'}).insert()",
]