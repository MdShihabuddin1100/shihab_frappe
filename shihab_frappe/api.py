import frappe

@frappe.whitelist()
def printtext():

    return "Hey,text printed"
