wn.query_reports["Item-wise Sales Register"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": "From Date",
			"fieldtype": "Date",
			"default": wn.defaults.get_user_default("year_start_date"),
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": "To Date",
			"fieldtype": "Date",
			"default": get_today()
		},
		{
			"fieldname": "item_code",
			"label": "Item",
			"fieldtype": "Link",
			"options": "Item",
		},
		{
			"fieldname":"account",
			"label": "Account",
			"fieldtype": "Link",
			"options": "Account",
			"get_query": function() {
				return {
					"query": "accounts.utils.get_account_list", 
					"filters": {
						"is_pl_account": "No",
						"debit_or_credit": "Debit",
						"master_type": "Customer"
					}
				}
			}
		}
	]
}