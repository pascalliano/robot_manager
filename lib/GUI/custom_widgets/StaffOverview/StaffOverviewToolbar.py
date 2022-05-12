import tkinter as tk
from tkinter import ttk


class StaffOverviewToolbar(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent, relief=tk.RIDGE)

        edit_icon = tk.PhotoImage(file="res/img/edit_icon.png")
        add_icon = tk.PhotoImage(file="res/img/add_icon.png")
        reload_icon = tk.PhotoImage(file="res/img/reload_icon.png")

        self.edit_button = tk.Button(self, image=edit_icon, relief=tk.FLAT)
        self.edit_button.photo = edit_icon
        self.edit_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.add_button = tk.Button(self, image=add_icon, relief=tk.FLAT, command=lambda: controller.show_frame("NewStaffPage"))
        self.add_button.photo = add_icon
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.reload_button = tk.Button(self, image=reload_icon, relief=tk.FLAT)
        self.reload_button.photo = reload_icon
        self.reload_button.pack(side=tk.LEFT, padx=5, pady=5)

        ttk.Label(self, text="Staff Overview", font=("Arial", 15, "bold")).pack(side=tk.RIGHT, padx=10, pady=2)