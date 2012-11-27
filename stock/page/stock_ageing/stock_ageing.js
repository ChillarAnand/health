// ERPNext - web based ERP (http://erpnext.com)
// Copyright (C) 2012 Web Notes Technologies Pvt Ltd
// 
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.


wn.pages['stock-ageing'].onload = function(wrapper) { 
	wn.ui.make_app_page({
		parent: wrapper,
		title: 'Stock Ageing',
		single_column: true
	});

	new erpnext.StockAgeing(wrapper);
	
	wrapper.appframe.add_module_tab("Stock");
}

wn.require("app/js/stock_grid_report.js");

erpnext.StockAgeing = erpnext.StockGridReport.extend({
	init: function(wrapper) {
		this._super({
			title: "Stock Ageing",
			page: wrapper,
			parent: $(wrapper).find('.layout-main'),
			appframe: wrapper.appframe,
			doctypes: ["Item", "Warehouse", "Stock Ledger Entry", "Item Group"],
		})
	},
	setup_columns: function() {
		this.columns = [
			{id: "name", name: "Item", field: "name", width: 300,
				link_formatter: {
					open_btn: true,
					doctype: '"Item"'
				}},
			{id: "average_age", name: "Average Age", field: "average_age",
				formatter: this.currency_formatter},
			{id: "earliest", name: "Earliest", field: "earliest",
				formatter: this.currency_formatter},
			{id: "latest", name: "Latest", field: "latest",
				formatter: this.currency_formatter}
		];
	},
	filters: [
		{fieldtype:"Select", label: "Warehouse", link:"Warehouse", 
			default_value: "Select Warehouse..."},
		{fieldtype:"Select", label: "Plot By", 
			options: ["Average Age", "Earliest", "Latest"]},
		{fieldtype:"Date", label: "To Date"},
		{fieldtype:"Button", label: "Refresh", icon:"icon-refresh icon-white", cssClass:"btn-info"},
		{fieldtype:"Button", label: "Reset Filters"}
	],
	setup_filters: function() {
		var me = this;
		this._super();
		
		this.filter_inputs.warehouse.change(function() {
			me.filter_inputs.refresh.click();
		});
		this.filter_inputs.plot_by.change(function() {
			me.filter_inputs.refresh.click();
		});
	},
	init_filter_values: function() {
		this._super();
		this.filter_inputs.to_date.val(dateutil.obj_to_user(new Date()));
	},
	prepare_data: function() {
		var me = this;
				
		if(!this.data) {
			me.data = wn.report_dump.data["Item"];
			me.item_by_name = me.make_name_map(me.data);
		}
		
		$.each(this.data, function(i, d) {
			me.reset_item_values(d);
		});
		
		this.prepare_balances();		
	},
	prepare_balances: function() {
		var me = this;
		var to_date = dateutil.str_to_obj(this.to_date);
		var data = wn.report_dump.data["Stock Ledger Entry"];

		this.item_warehouse = {};

		for(var i=0, j=data.length; i<j; i++) {
			var sl = data[i];
			var posting_date = dateutil.str_to_obj(sl.posting_date);
			
			if(me.is_default("warehouse") ? true : me.warehouse == sl.warehouse) {
				var wh = me.get_item_warehouse(sl.warehouse, sl.item_code);
				
				// call diff to build fifo stack in item_warehouse
				var diff = me.get_value_diff(wh, sl, true);

				if(posting_date > to_date) 
					break;
			}
		}
		
		$.each(me.data, function(i, item) {
			var full_fifo_stack = [];
			if(me.is_default("warehouse")) {
				$.each(me.item_warehouse[item.name] || {}, function(i, wh) {
					full_fifo_stack = full_fifo_stack.concat(wh.fifo_stack || [])
				});
			} else {
				full_fifo_stack = me.get_item_warehouse(me.warehouse, item.name) || [];			
			}
			
			var age_qty = total_qty = 0.0;
			var min_age = max_age = null;
			
			$.each(full_fifo_stack, function(i, batch) {
				var batch_age = dateutil.get_diff(me.to_date, batch[2]);
				age_qty += batch_age * batch[0];
				total_qty += batch[0];
				max_age = Math.max(max_age, batch_age);
				if(min_age===null) min_age=batch_age;
				else min_age = Math.min(min_age, batch_age);
			});
			
			item.average_age = total_qty.toFixed(2)==0.0 ? 0 
				: (age_qty / total_qty).toFixed(2);
			item.earliest = max_age || 0.0;
			item.latest = min_age || 0.0;
		});
		
		this.data = this.data.sort(function(a, b) { 
			var sort_by = me.plot_by.replace(" ", "_").toLowerCase();
			return b[sort_by] - a[sort_by]; 
		});
	},
	get_plot_data: function() {
		var data = [];
		var me = this;

		data.push({
			label: me.plot_by,
			data: $.map(me.data, function(item, idx) {
				return [[idx+1, item[me.plot_by.replace(" ", "_").toLowerCase() ]]]
			}),
			bars: {show: true},
		});
				
		return data.length ? data : false;
	},
	get_plot_options: function() {
		var me = this;
		return {
			grid: { hoverable: true, clickable: true },
			xaxis: {  
				ticks: $.map(me.data, function(item, idx) { return [[idx+1, item.name]] }),
				max: 20
			}
		}
	}	
});