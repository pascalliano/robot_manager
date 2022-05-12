import tkinter as tk
from tkinter import ttk

from lib.util.ContactPerson.ContactPersonManager import ContactPersonManager


class StaffOverviewTreeview(ttk.Treeview):
    def __init__(self, parent, **kwargs):
        ttk.Treeview.__init__(self, parent, **kwargs)

        style = ttk.Style()
        style.configure("Treeview", font=("Calibri",))
        self.tag_configure("o", background="#BFBFBF")
        self.tag_configure("e", background="#F2F2F2")

        self["columns"] = ("name", "vorname", "abteilung", "email")

        self.heading("#0", text="ID")
        self.heading("name", text="Name")
        self.heading("vorname", text="Vorname")
        self.heading("abteilung", text="Abteilung")
        self.heading("email", text="Email")

        self.insert_all_staff()

    def insert_all_staff(self):
        all_contact_persons = ContactPersonManager.get_instance().get_all_contact_persons()

        self.delete(*self.get_children())

        for cp in all_contact_persons:
            text = cp.id
            values = [
                cp.surname,
                cp.forename,
                cp.department,
                cp.email
            ]

            for i in range(len(values)):
                if values[i] is None:
                    values[i] = ""

            tag = "e" if len(self.get_children()) % 2 == 0 else "o"
            self.insert("", tk.END, text=text, values=values, tag=tag)
