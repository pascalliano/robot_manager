import tkinter as tk
from tkinter import ttk

from lib.GUI.custom_widgets.NewStaff.NewStaffForm import NewStaffForm
from lib.GUI.custom_widgets.NewStaff.NewStaffToolbar import NewStaffToolbar


class NewStaffPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        toolbar = NewStaffToolbar(self, controller)
        toolbar.pack(side=tk.TOP, fill=tk.X, expand=False)

        content_LF = tk.LabelFrame(self)

        content_LF.columnconfigure(0, weight=1)
        content_LF.rowconfigure(0, weight=1)

        self.new_staff_form = NewStaffForm(content_LF, controller)
        toolbar.save_button.config(command=self.new_staff_form.add_new_staff)

        content_LF.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
