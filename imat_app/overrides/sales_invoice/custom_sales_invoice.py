import frappe
from german_accounting.overrides.sales_invoice.custom_sales_invoice import CustomSalesInvoice

class IMATSalesInvoice(CustomSalesInvoice):
	def validate(self):
		frappe.msgprint("IMAT APP")
		super().validate()