import re
import tkinter as tk
from tkinter import ttk, messagebox

from lib.util.ContactPerson.ContactPersonManager import ContactPersonManager
from lib.util.Robot.RobotManager import RobotManager


class NewRobotForm(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        font = ("Arial", 14)

        content_F = ttk.Frame(parent)

        ttk.Label(content_F, text="IPA*: ", font=font).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.ipa_E = tk.Entry(content_F, font=font, width=25)
        self.ipa_E.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(content_F, text="Name*: ", font=font).grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.name_E = tk.Entry(content_F, font=font, width=25)
        self.name_E.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(content_F, text="Kurzbeschreibung: ", font=font).grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.descr_E = tk.Entry(content_F, font=font, width=25)
        self.descr_E.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(content_F, text="Kosten pro Stunde*: ", font=font).grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.cost_E = tk.Entry(content_F, font=font, width=10)
        self.cost_E.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        self.cost_E.bind("<FocusIn>", lambda e: self.cost_E.select_range(0, tk.END))
        self.cost_E.bind("<FocusOut>", lambda e: self.append_to_entry(self.cost_E, ",00 €"))
        self.cost_E.bind("<Return>", lambda e: self.append_to_entry(self.cost_E, ",00 €"))

        ttk.Label(content_F, text="Laufzeit*: ", font=font).grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.runtime_E = tk.Entry(content_F, font=font, width=10)
        self.runtime_E.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
        self.runtime_E.bind("<FocusIn>", lambda e: self.runtime_E.select_range(0, tk.END))
        self.runtime_E.bind("<FocusOut>", lambda e: self.append_to_entry(self.runtime_E, ",00 h"))
        self.runtime_E.bind("<Return>", lambda e: self.append_to_entry(self.runtime_E, ",00 h"))

        ttk.Label(content_F, text="Kontaktperson: ", font=font).grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        self.contact_CB = ttk.Combobox(content_F, font=font, state="readonly", width=49)
        self.contact_CB.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
        self.contact_CB.bind(
            "<Button-1>", lambda e: self.contact_CB.config(
                values=[""] + ContactPersonManager.get_instance().get_all_contact_persons_longstr()
            )
        )

        ttk.Label(content_F, text="Kommentar: ", font=font).grid(row=6, column=0, padx=5, pady=5, sticky=tk.NW)
        self.comment_E = tk.Text(content_F, font=font, width=50, height=5)
        self.comment_E.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        content_F.pack(side=tk.TOP, anchor=tk.W, expand=False)

    def add_new_robot(self):
        ipa = self.ipa_E.get().strip()
        name = self.name_E.get().strip()
        sh_descr = self.descr_E.get().strip()
        cost = self.cost_E.get().strip()
        runtime = self.runtime_E.get().strip()
        contact_person = self.contact_CB.get().strip()
        comment = self.comment_E.get("1.0", tk.END).strip()

        cost = re.split("\D", cost)[0]
        runtime = re.split("\D", runtime)[0]
        contact_person_id = ContactPersonManager.get_instance().get_contact_person_id_by_longstr(contact_person)

        if not all([ipa, name, cost, runtime]):
            messagebox.showerror("Fehler", "Es wurden nicht alle Pflichtfelder ausgefüllt!")
        elif (not cost.isdigit()) or (not runtime.isdigit()):
            messagebox.showerror("Fehler", "Es wurden nicht alle Pflichtfelder ausgefüllt!")
        else:
            RobotManager.get_instance().add_new_robot(
                ipa, name, sh_descr, cost, runtime, contact_person_id, comment
            )
            self.ipa_E.delete(0, tk.END)
            self.name_E.delete(0, tk.END)
            self.descr_E.delete(0, tk.END)
            self.cost_E.delete(0, tk.END)
            self.runtime_E.delete(0, tk.END)
            self.contact_CB.set("")
            self.comment_E.delete("1.0", tk.END)

            self.controller.show_frame("RobotOverviewPage")

    def append_to_entry(self, widget, append):
        content = widget.get().strip()
        content = re.split("\D", content)[0]

        if content.isdigit():
            widget.config(background="white")
            content += append
            widget.delete(0, tk.END)
            widget.insert(0, content)
        else:
            widget.config(background="red")
