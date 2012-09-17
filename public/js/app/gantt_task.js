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

// gantt chart for project tasks

wn.require('js/lib/jQuery.Gantt/css/style.css');
wn.require('js/lib/jQuery.Gantt/js/jquery.fn.gantt.min.js');

erpnext.show_task_gantt = function(parent, project) {
	
	$(parent).css('min-height', '300px').html('<div class="help-box">Loading...</div>')
	
	var get_source = function(r) {
		var source = [];
		// projects
		$.each(r.message, function(i,v) {
			source.push({
				name: v.project, 
				desc: v.subject,
				values: [{
					label: v.subject,
					desc: v.description || v.subject,
					from: '/Date("'+v.exp_start_date+'")/',
					to: '/Date("'+v.exp_end_date+'")/',
					customClass: {
						'Open':'ganttRed',
						'Pending Review':'ganttOrange',
						'Working':'',
						'Completed':'ganttGreen',
						'Cancelled':'ganttGray'
					}[v.status],
					dataObj: v
				}]
			})
		});
		return source	
	}
	wn.call({
		method: 'projects.page.projects.projects.get_tasks',
		args: {
			project: project || ''
		},
		callback: function(r) {
			$(parent).empty();
			if(!r.message.length) {
				$(parent).html('<div class="help-box">No Tasks Yet.</div>');
			} else {
				var gantt_area = $('<div class="gantt">').appendTo(parent);
				gantt_area.gantt({
					source: get_source(r),
					navigate: project ? "button" : "scroll",
					scale: "weeks",
					minScale: "weeks",
					maxScale: "months",
					onItemClick: function(data) {
						wn.set_route('Form', 'Task', data.name);
					},
					onAddClick: function(dt, rowId) {
						newdoc('Task');
					}
				});				
			}

			$('<button class="btn"><i class="icon icon-plus"></i>\
				Create a new Task</button>').click(function() {
				wn.model.with_doctype('Task', function() {
					var new_name = LocalDB.create('Task');
					if(project)
						locals.Task[new_name].project = project;
					wn.set_route('Form', 'Task', new_name);
				});
			}).appendTo(parent);
		}
	})	
}
