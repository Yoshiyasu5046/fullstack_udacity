#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

form = """
<form method="post">
	What is your birthday?
	<br>

	<label>Month
		<input type="text" name="month">
	</label>
	
	<label>Day
		<input type="text" name="day">
	</label>
	
	<label>Year
		<input type="text" name="year">
	</label>

	<div style="color: red">%(error)s</div> 

	<br>
	<br>
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
	def write_form(self, error=""):
		self.response.out.write(form % {"error": error})

	def get(self):
		self.write_form()

	  
	def valid_month(self, month):
		months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
		abbvs_month = dict((m[:3].lower(), m) for m in months)
		if month:
			short_month = month[:3].lower()
			return abbvs_month.get(short_month)

	def valid_day(self, day):
		if day and day.isdigit():
			int_day = int(day)
			if 0 < int_day and int_day < 31:
				return int_day
			return None

	def valid_year(self, year):
		if year and year.isdigit():
			int_year = int(year)
			if 1900 <= int_year and int_year <= 2020:
				return int_year
			return None


	def post(self):
		user_month = valid_month(self.request.get('month'))
		user_day = valid_day(self.request.get('day'))
		user_year = valid_year(self.request.get('year'))    	

		if not (user_month and user_day and user_year):
			self.write.form("That doesn't look valid to me...")
		else:
			self.response.out.write("Thanks!")


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)






