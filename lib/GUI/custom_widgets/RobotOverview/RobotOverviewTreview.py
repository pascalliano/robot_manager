import tkinter as tk
from tkinter import ttk
import locale

from lib.util.ContactPerson.ContactPersonManager import ContactPersonManager
from lib.util.Robot.RobotManager import RobotManager

locale.setlocale(locale.LC_ALL, "de")


class RobotOverviewTreeview(ttk.Treeview):
    def __init__(self, parent, **kwargs):
        ttk.Treeview.__init__(self, parent, **kwargs)

        style = ttk.Style()
        style.configure("Treeview", font=("Calibri",))
        self.tag_configure("o", background="#BFBFBF")
        self.tag_configure("e", background="#F2F2F2")

        self["columns"] = ("ipa", "name", "ansprechpartner", "kosten", "laufzeit", "zusatzzeit", "gesamtzeit", "gesamtkosten")

        self.heading("#0", text="ID")
        self.heading("ipa", text="IPA")
        self.heading("name", text="Name")
        self.heading("ansprechpartner", text="Ansprechpartner")
        self.heading("kosten", text="Kosten")
        self.heading("laufzeit", text="Laufzeit pro Woche")
        self.heading("zusatzzeit", text="Zusätzliche Zeit")
        self.heading("gesamtzeit", text="Gesamtzeit")
        self.heading("gesamtkosten", text="Gesamtkosten")

        self.insert_all_robots()

    def insert_all_robots(self):
        all_robots = RobotManager.get_instance().get_all_robots()

        self.delete(*self.get_children())

        for robot in all_robots:
            text = robot.id
            values = [
                robot.ipa,
                robot.name,
                ContactPersonManager.get_instance().get_contact_person_by_id_shortstr(robot.contact_person_id),
                locale.format("%.2f", robot.cost, True) + " €",
                locale.format("%.2f", robot.runtime, True) + " h",
                locale.format("%.2f", robot.add_time, True) + " h",
                locale.format("%.2f", robot.total_time, True) + " h",
                locale.format("%.2f", robot.total_cost, True) + " €"
            ]

            for i in range(len(values)):
                if values[i] is None:
                    values[i] = "-/-"

            tag = "e" if len(self.get_children()) % 2 == 0 else "o"
            self.insert("", tk.END, text=text, values=values, tag=tag)
