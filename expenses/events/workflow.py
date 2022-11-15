# ERPNext Expenses © 2022
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


from frappe import _

from expenses.utils.common import error


def before_save(doc, method=None):
    evaluate(doc, "modified")


def before_rename(doc, method=None):
    evaluate(doc, "renamed")


def on_trash(doc, method=None):
    evaluate(doc, "trashed")


def evaluate(doc, action):
    name = "Expenses Request Review"
    if (
        (
            action == "renamed" and
            doc.get_doc_before_save().name == name and
            doc.name != name
        ) or
        (action != "renamed" and doc.name == name)
    ):
        error(_(
            "This workflow belongs to the Expenses plugin and should not be {0}."
        ).format(action))