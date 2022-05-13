import frappe


def get_context(context):
	patient = get_patient()
	fields = ['name', 'lab_test_name', 'result_date', 'status']
	lab_tests = frappe.get_all('Lab Test', fields=fields, filters={'patient': patient})
	context.lab_tests = lab_tests


def get_patient():
	return frappe.get_value("Patient", {"email": frappe.session.user}, "name")
