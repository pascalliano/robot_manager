import tkinter as tk
from tkinter import ttk, messagebox


class EditStaffToolbar(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent, relief=tk.RIDGE)

        save_icon = tk.PhotoImage(file="res/img/save_icon.png")
        cancel_icon = tk.PhotoImage(file="res/img/cancel_icon.png")

        self.save_button = tk.Button(self, image=save_icon, relief=tk.FLAT)
        self.save_button.photo = save_icon
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.cancel_button = tk.Button(self, image=cancel_icon, relief=tk.FLAT,
                                       command=lambda: controller.show_frame("StaffOverviewPage"))
        self.cancel_button.photo = cancel_icon
        self.cancel_button.pack(side=tk.LEFT, padx=5, pady=5)

        ttk.Label(self, text="Add new Staff", font=("Arial", 15, "bold")).pack(side=tk.RIGHT, padx=10, pady=2)
