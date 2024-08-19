import frappe
from german_accounting.overrides.journal_entry.custom_journal_entry import CustomJournalEntry

class IMATJournalEntry(CustomJournalEntry):
	def validate(self):
		frappe.msgprint("IMAT APP")
		super().validate()