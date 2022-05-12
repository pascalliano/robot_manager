import tkinter as tk
from tkinter import ttk, messagebox

from lib.GUI.custom_widgets.StaffOverview.StaffOverviewToolbar import StaffOverviewToolbar
from lib.GUI.custom_widgets.StaffOverview.StaffOverviewTreeview import StaffOverviewTreeview


class StaffOverviewPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller

        toolbar = StaffOverviewToolbar(self, controller)
        toolbar.pack(side=tk.TOP, fill=tk.X, expand=False)

        content_LF = tk.LabelFrame(self)

        content_LF.columnconfigure(0, weight=1)
        content_LF.rowconfigure(0, weight=1)

        self.staff_overview_TV = StaffOverviewTreeview(content_LF, selectmode="browse")
        self.staff_overview_TV.grid(row=0, column=0, rowspan=2, sticky=tk.NSEW, padx=5, pady=5)
        toolbar.reload_button.config(command=self.staff_overview_TV.insert_all_staff)
        toolbar.edit_button.config(command=self.edit_staff)

        content_LF.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def edit_staff(self):
        item = self.staff_overview_TV.item(
            self.staff_overview_TV.focus()
        )

        if item["text"]:
            self.controller.frames["EditStaffPage"].fill_values(item)
            self.controller.show_frame("EditStaffPage")
        else:
            messagebox.showerror("Fehler", "Es wurde kein Eintrag ausgewählt.")

