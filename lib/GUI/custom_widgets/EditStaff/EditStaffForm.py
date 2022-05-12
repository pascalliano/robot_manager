import tkinter as tk
from tkinter import ttk, messagebox

from lib.util.ContactPerson.ContactPersonManager import ContactPersonManager


class EditStaffForm(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        font = ("Arial", 14)

        content_F = ttk.Frame(parent)

        ttk.Label(content_F, text="ID: ", font=font).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.id_E = ttk.Entry(content_F, font=font, width=10)
        self.id_E.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(content_F, text="Name*: ", font=font).grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.name_E = ttk.Entry(content_F, font=font, width=25)
        self.name_E.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(content_F, text="Vorname*: ", font=font).grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.forename_E = ttk.Entry(content_F, font=font, width=25)
        self.forename_E.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(content_F, text="Abteilung*: ", font=font).grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.dep_E = ttk.Entry(content_F, font=font, width=25)
        self.dep_E.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(content_F, text="Email*: ", font=font).grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.email_E = ttk.Entry(content_F, font=font, width=25)
        self.email_E.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        content_F.pack(side=tk.TOP, anchor=tk.W, expand=False)

    def save_changes(self):
        id = self.id_E.get().strip()
        name = self.name_E.get().strip()
        forename = self.forename_E.get().strip()
        dep = self.dep_E.get().strip()
        email = self.email_E.get().strip()

        if not all([name, forename, dep, email]):
            messagebox.showerror("Fehler", "Es wurden nicht alle Felder ausgefüllt!")
        else:
            ContactPersonManager.get_instance().update_contactPerson(
                id, name, forename, dep, email
            )
            self.name_E.delete(0, tk.END)
            self.forename_E.delete(0, tk.END)
            self.dep_E.delete(0, tk.END)
            self.email_E.delete(0, tk.END)

            self.controller.show_frame("StaffOverviewPage")
