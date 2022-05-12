import tkinter as tk
from tkinter import ttk

from lib.GUI.custom_widgets.EditStaff.EditStaffForm import EditStaffForm
from lib.GUI.custom_widgets.EditStaff.EditStaffToolbar import EditStaffToolbar
from lib.GUI.custom_widgets.NewStaff.NewStaffForm import NewStaffForm
from lib.GUI.custom_widgets.NewStaff.NewStaffToolbar import NewStaffToolbar
from lib.util.ContactPerson.ContactPersonManager import ContactPersonManager


class EditStaffPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        toolbar = EditStaffToolbar(self, controller)
        toolbar.pack(side=tk.TOP, fill=tk.X, expand=False)

        content_LF = tk.LabelFrame(self)

        content_LF.columnconfigure(0, weight=1)
        content_LF.rowconfigure(0, weight=1)

        self.edit_staff_form = EditStaffForm(content_LF, controller)
        toolbar.save_button.config(command=self.edit_staff_form.save_changes)

        content_LF.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def fill_values(self, item):
        id = int(item["text"])
        cp = ContactPersonManager.get_instance().get_contact_person_by_id(id)

        self.edit_staff_form.id_E.config(state="normal")

        self.edit_staff_form.id_E.delete(0, tk.END)
        self.edit_staff_form.name_E.delete(0, tk.END)
        self.edit_staff_form.forename_E.delete(0, tk.END)
        self.edit_staff_form.dep_E.delete(0, tk.END)
        self.edit_staff_form.email_E.delete(0, tk.END)

        self.edit_staff_form.id_E.insert(0, cp.id)
        self.edit_staff_form.name_E.insert(0, cp.surname)
        self.edit_staff_form.forename_E.insert(0, cp.forename)
        self.edit_staff_form.dep_E.insert(0, cp.department)
        self.edit_staff_form.email_E.insert(0, cp.email)

        self.edit_staff_form.id_E.config(state="readonly")
