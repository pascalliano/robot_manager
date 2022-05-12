import os
import tkinter as tk
from tkinter import ttk

from lib.util.ContactPerson.ContactPersonManager import ContactPersonManager


class Navbar(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent, relief=tk.RIDGE)

        overview_icon = tk.PhotoImage(file="res/img/overview_icon.png")
        staff_icon = tk.PhotoImage(file="res/img/staff_icon.png")
        logo_icon = tk.PhotoImage(file="res/img/logo.png")

        # style = ttk.Style(self)
        # style.configure("flat.TButton", relief="FLAT")

        self.overview_button = tk.Button(self, image=overview_icon, relief=tk.FLAT,
                                          command=lambda: controller.show_frame("RobotOverviewPage"))
        self.overview_button.photo = overview_icon
        self.overview_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.staff_button = tk.Button(self, image=staff_icon, relief=tk.FLAT,
                                         command=lambda: controller.show_frame("StaffOverviewPage"))
        self.staff_button.photo = staff_icon
        self.staff_button.pack(side=tk.LEFT, padx=5, pady=5)

        logo_label = ttk.Label(self, image=logo_icon)
        logo_label.photo = logo_icon
        logo_label.pack(side=tk.RIGHT, padx=10, pady=2)
