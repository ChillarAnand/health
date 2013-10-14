# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
patch_list = [
	"execute:webnotes.reload_doc('core', 'doctype', 'doctype', force=True) #2013-07-15",
	"execute:webnotes.reload_doc('core', 'doctype', 'docfield', force=True) #2013-07-15",
	"execute:webnotes.reload_doc('core', 'doctype', 'doctype', force=True) #2013-07-16",
	"execute:webnotes.reload_doc('core', 'doctype', 'docfield', force=True) #2013-07-16",
	"execute:webnotes.reload_doc('core', 'doctype', 'docperm') #2013-07-16",
	"execute:webnotes.reload_doc('core', 'doctype', 'page') #2013-07-16",
	"execute:webnotes.reload_doc('core', 'doctype', 'report') #2013-07-16",
	"patches.september_2012.stock_report_permissions_for_accounts", 
	"patches.september_2012.communication_delete_permission", 
	"patches.september_2012.all_permissions_patch", 
	"patches.september_2012.customer_permission_patch", 
	"patches.september_2012.add_stock_ledger_entry_index", 
	"patches.september_2012.plot_patch", 
	"patches.september_2012.event_permission", 
	"patches.september_2012.repost_stock", 
	"patches.september_2012.rebuild_trees", 
	"patches.september_2012.deprecate_account_balance", 
	"patches.september_2012.profile_delete_permission", 
	"patches.october_2012.update_permission", 
	"patches.october_2012.fix_wrong_vouchers", 
	"patches.october_2012.company_fiscal_year_docstatus_patch", 
	"patches.october_2012.update_account_property", 
	"patches.october_2012.fix_cancelled_gl_entries", 
	"patches.october_2012.custom_script_delete_permission", 
	"patches.november_2012.custom_field_insert_after", 
	"patches.november_2012.report_permissions", 
	"patches.november_2012.customer_issue_allocated_to_assigned", 
	"patches.november_2012.reset_appraisal_permissions", 
	"patches.november_2012.disable_cancelled_profiles", 
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
	"patches.december_2012.website_cache_refactor", 
	"patches.december_2012.production_cleanup", 
	"patches.december_2012.fix_default_print_format", 
	"patches.december_2012.file_list_rename", 
	"patches.december_2012.replace_createlocal", 
	"patches.december_2012.remove_quotation_next_contact", 
	"patches.december_2012.stock_entry_cleanup", 
	"patches.december_2012.production_order_naming_series", 
	"patches.december_2012.rebuild_item_group_tree", 
	"patches.december_2012.address_title", 
	"patches.december_2012.delete_form16_print_format", 
	"patches.december_2012.update_print_width", 
	"patches.january_2013.remove_bad_permissions", 
	"patches.january_2013.holiday_list_patch", 
	"patches.january_2013.stock_reconciliation_patch", 
	"patches.january_2013.report_permission", 
	"patches.january_2013.give_report_permission_on_read", 
	"patches.january_2013.update_closed_on",
	"patches.january_2013.change_patch_structure",
	"patches.january_2013.update_country_info",
	"patches.january_2013.remove_tds_entry_from_gl_mapper",
	"patches.january_2013.update_number_format",
	"execute:webnotes.reload_doc('core', 'doctype', 'print_format') #2013-01",
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
	"execute:webnotes.delete_doc('DocType', 'Service Order')",
	"execute:webnotes.delete_doc('DocType', 'Service Quotation')",
	"execute:webnotes.delete_doc('DocType', 'Service Order Detail')",
	"execute:webnotes.delete_doc('DocType', 'Service Quotation Detail')",
	"execute:webnotes.delete_doc('Page', 'Query Report')",
	"patches.february_2013.repost_reserved_qty",
	"execute:webnotes.reload_doc('core', 'doctype', 'report') # 2013-02-25",
	"execute:webnotes.conn.sql(\"update `tabReport` set report_type=if(ifnull(query, '')='', 'Report Builder', 'Query Report') where is_standard='No'\")",
	"execute:webnotes.conn.sql(\"update `tabReport` set report_name=name where ifnull(report_name,'')='' and is_standard='No'\")",
	"patches.february_2013.p08_todo_query_report",
	"execute:(not webnotes.conn.exists('Role', 'Projects Manager')) and webnotes.doc({'doctype':'Role', 'role_name':'Projects Manager'}).insert()",
	"patches.february_2013.p09_remove_cancelled_warehouses",
	"patches.march_2013.update_po_prevdoc_doctype",
	"patches.february_2013.p09_timesheets",
	"execute:(not webnotes.conn.exists('UOM', 'Hour')) and webnotes.doc({'uom_name': 'Hour', 'doctype': 'UOM', 'name': 'Hour'}).insert()",
	"patches.march_2013.p01_c_form",
	"execute:webnotes.conn.sql('update tabDocPerm set `submit`=1, `cancel`=1, `amend`=1 where parent=\"Time Log\"')",
	"execute:webnotes.delete_doc('DocType', 'Attendance Control Panel')",
	"patches.march_2013.p02_get_global_default",
	"patches.march_2013.p03_rename_blog_to_blog_post",
	"patches.march_2013.p04_pos_update_stock_check",
	"patches.march_2013.p05_payment_reconciliation",
	"patches.march_2013.p06_remove_sales_purchase_return_tool",
	"execute:webnotes.bean('Global Defaults').save()",
	"patches.march_2013.p07_update_project_in_stock_ledger",
	"execute:webnotes.reload_doc('stock', 'doctype', 'item') #2013-03-25",
	"execute:webnotes.reload_doc('setup', 'doctype', 'item_group') #2013-03-25",
	"execute:webnotes.reload_doc('website', 'doctype', 'blog_post') #2013-03-25",
	"execute:webnotes.reload_doc('website', 'doctype', 'web_page') #2013-03-25",
	"execute:webnotes.reload_doc('setup', 'doctype', 'sales_partner') #2013-06-25",
	"execute:webnotes.conn.set_value('Email Settings', None, 'send_print_in_body_and_attachment', 1)",
	"patches.march_2013.p10_set_fiscal_year_for_stock",
	"patches.march_2013.p10_update_against_expense_account",
	"patches.march_2013.p11_update_attach_files",
	"patches.march_2013.p12_set_item_tax_rate_in_json",
	"patches.march_2013.p07_update_valuation_rate",
	"patches.march_2013.p08_create_aii_accounts",
	"patches.april_2013.p01_update_serial_no_valuation_rate",
	"patches.april_2013.p02_add_country_and_currency",
	"patches.april_2013.p03_fixes_for_lead_in_quotation",
	"patches.april_2013.p04_reverse_modules_list",
	"patches.april_2013.p04_update_role_in_pages",
	"patches.april_2013.p05_update_file_data",
	"patches.april_2013.p06_update_file_size",
	"patches.april_2013.p05_fixes_in_reverse_modules",
	"patches.april_2013.p07_rename_cost_center_other_charges",
	"patches.april_2013.p06_default_cost_center",
	"execute:webnotes.reset_perms('File Data')",
	"patches.april_2013.p07_update_file_data_2",
	"patches.april_2013.rebuild_sales_browser",
	"patches.may_2013.p01_selling_net_total_export",
	"patches.may_2013.repost_stock_for_no_posting_time",
	"patches.may_2013.p02_update_valuation_rate",
	"patches.may_2013.p03_update_support_ticket",
	"patches.may_2013.p04_reorder_level",
	"patches.may_2013.p05_update_cancelled_gl_entries",
	"patches.may_2013.p06_make_notes",
	"patches.may_2013.p06_update_billed_amt_po_pr",
	"patches.may_2013.p07_move_update_stock_to_pos",
	"patches.may_2013.p08_change_item_wise_tax",
	"patches.june_2013.p01_update_bom_exploded_items",
	"patches.june_2013.p02_update_project_completed",
	"execute:webnotes.delete_doc('DocType', 'System Console')",
	"patches.june_2013.p03_buying_selling_for_price_list",
	"patches.june_2013.p04_fix_event_for_lead_oppty_project",
	"patches.june_2013.p05_remove_search_criteria_reports",
	"execute:webnotes.delete_doc('Report', 'Sales Orders Pending To Be Delivered')",
	"patches.june_2013.p05_remove_unused_doctypes",
	"patches.june_2013.p06_drop_unused_tables",
	"patches.june_2013.p07_taxes_price_list_for_territory",
	"patches.june_2013.p08_shopping_cart_settings",
	"patches.june_2013.p09_update_global_defaults",
	"patches.june_2013.p10_lead_address",
	"patches.july_2013.p01_remove_doctype_mappers",
	"execute:webnotes.delete_doc('Report', 'Delivered Items To Be Billed')",
	"execute:webnotes.delete_doc('Report', 'Received Items To Be Billed')",
	"patches.july_2013.p02_copy_shipping_address",
	"patches.july_2013.p03_cost_center_company",
	"patches.july_2013.p04_merge_duplicate_leads",
	"patches.july_2013.p05_custom_doctypes_in_list_view",
	"patches.july_2013.p06_same_sales_rate",
	"patches.july_2013.p07_repost_billed_amt_in_sales_cycle",
	"execute:webnotes.reload_doc('accounts', 'Print Format', 'Sales Invoice Classic') # 2013-07-22",
	"execute:webnotes.reload_doc('accounts', 'Print Format', 'Sales Invoice Modern') # 2013-07-22",
	"execute:webnotes.reload_doc('accounts', 'Print Format', 'Sales Invoice Spartan') # 2013-07-22",
	"execute:webnotes.reload_doc('selling', 'Print Format', 'Quotation Classic') # 2013-07-22",
	"execute:webnotes.reload_doc('selling', 'Print Format', 'Quotation Modern') # 2013-07-22",
	"execute:webnotes.reload_doc('selling', 'Print Format', 'Quotation Spartan') # 2013-07-22",
	"execute:webnotes.reload_doc('selling', 'Print Format', 'Sales Order Classic') # 2013-07-22",
	"execute:webnotes.reload_doc('selling', 'Print Format', 'Sales Order Modern') # 2013-07-22",
	"execute:webnotes.reload_doc('selling', 'Print Format', 'Sales Order Spartan') # 2013-07-22",
	"execute:webnotes.reload_doc('stock', 'Print Format', 'Delivery Note Classic') # 2013-07-22",
	"execute:webnotes.reload_doc('stock', 'Print Format', 'Delivery Note Modern') # 2013-07-22",
	"execute:webnotes.reload_doc('stock', 'Print Format', 'Delivery Note Spartan') # 2013-07-22",
	"patches.july_2013.p08_custom_print_format_net_total_export",
	"patches.july_2013.p09_remove_website_pyc",
	"patches.july_2013.p10_change_partner_user_to_website_user",
	"patches.july_2013.p11_update_price_list_currency",
	"execute:webnotes.bean('Selling Settings').save() #2013-07-29",
	"execute:webnotes.reload_doc('accounts', 'doctype', 'accounts_settings') # 2013-09-24",
	"patches.august_2013.p01_auto_accounting_for_stock_patch",
	"patches.august_2013.p01_hr_settings",
	"patches.august_2013.p02_rename_price_list",
	"patches.august_2013.p03_pos_setting_replace_customer_account",
	"patches.august_2013.p05_update_serial_no_status",
	"patches.august_2013.p05_employee_birthdays",
	"execute:webnotes.reload_doc('accounts', 'Print Format', 'POS Invoice') # 2013-08-16",
	"execute:webnotes.delete_doc('DocType', 'Stock Ledger')",
	"patches.august_2013.p06_deprecate_is_cancelled",
	"patches.august_2013.p06_fix_sle_against_stock_entry",
	"patches.september_2013.p01_add_user_defaults_from_pos_setting",
	"execute:webnotes.reload_doc('accounts', 'Print Format', 'POS Invoice') # 2013-09-02",
	"patches.september_2013.p01_fix_buying_amount_gl_entries",
	"patches.september_2013.p01_update_communication",
	"execute:webnotes.reload_doc('setup', 'doctype', 'features_setup') # 2013-09-05",
	"patches.september_2013.p02_fix_serial_no_status",
	"patches.september_2013.p03_modify_item_price_include_in_price_list",
	"patches.august_2013.p06_deprecate_is_cancelled",
	"execute:webnotes.delete_doc('DocType', 'Budget Control')",
	"patches.september_2013.p03_update_stock_uom_in_sle",
	"patches.september_2013.p03_move_website_to_framework",
	"execute:webnotes.bean('Style Settings').save() #2013-09-19",
	"execute:webnotes.conn.set_value('Accounts Settings', None, 'frozen_accounts_modifier', 'Accounts Manager') # 2013-09-24",
	"patches.september_2013.p04_unsubmit_serial_nos",
	"patches.september_2013.p05_fix_customer_in_pos",
	"patches.october_2013.fix_is_cancelled_in_sle",
	"patches.october_2013.repost_ordered_qty",
	"patches.october_2013.repost_planned_qty",
]