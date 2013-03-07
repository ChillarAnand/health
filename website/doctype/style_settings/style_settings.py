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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals
class DocType:
	def __init__(self, d, dl):
		self.doc, self.doclist = d, dl
		
	def validate(self):
		"""make custom css"""
		from jinja2 import Template
		import os
		
		with open(os.path.join(
				os.path.dirname(os.path.abspath(__file__)), 
				'custom_template.css'), 'r') as f:
			temp = Template(f.read())
		
		self.prepare()
		
		self.doc.custom_css = temp.render(doc = self.doc)
		if self.doc.add_css:
			self.doc.custom_css += '\n\n/* User CSS */\n\n' + self.doc.add_css
		
		from webnotes.sessions import clear_cache
		clear_cache('Guest')
		
		for f in ["small_font_size", "at_import"]:
			if f in self.doc.fields:
				del self.doc.fields[f]
	
	def prepare(self):
		if not self.doc.font_size:
			self.doc.font_size = '13px'
			
		self.doc.small_font_size = str(int(self.doc.font_size[:-2])-2) + 'px'
		self.doc.page_border = int(self.doc.page_border)
		
		fonts = []
		if self.doc.google_web_font_for_heading:
			fonts.append(self.doc.google_web_font_for_heading)
		if self.doc.google_web_font_for_text:
			fonts.append(self.doc.google_web_font_for_text)
			
		fonts = list(set(fonts))
		
		self.doc.at_import = ""
		for f in fonts:
			self.doc.at_import += "\n@import url(http://fonts.googleapis.com/css?family=%s);" % f.replace(" ", "+")
			

	
	def on_update(self):
		"""rebuild pages"""
		from website.helpers.make_web_include_files import make
		make()