import frappe
from german_accounting.overrides.sales_order.custom_sales_order import CustomSalesOrder

class IMATSalesOrder(CustomSalesOrder):
    def validate(self):
        frappe.msgprint("IMAT APP")
        super().validate()

 