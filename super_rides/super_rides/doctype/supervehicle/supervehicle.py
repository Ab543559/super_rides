# Copyright (c) 2022, Arnold and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class SuperVehicle(WebsiteGenerator):
	def before_save(self):
		if not self.route:
			self.route = f"/vehicles/{self.name}"
