import frappe
from german_accounting.overrides.delivery_note.custom_delivery_note import CustomDeliveryNote

class IMATDeliveryNote(CustomDeliveryNote):
	def validate(self):
		frappe.msgprint("IMAT APP")
		super().validate()