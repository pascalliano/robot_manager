import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from lib.GUI.custom_widgets.RobotOverview.RobotOverviewTreview import RobotOverviewTreeview
from lib.GUI.custom_widgets.RobotOverview.RobotOverviewToolbar import RobotOverviewToolbar
from lib.util.Robot.RobotManager import RobotManager


class RobotOverviewPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller

        toolbar = RobotOverviewToolbar(self, controller)
        toolbar.pack(side=tk.TOP, fill=tk.X, expand=False)

        content_LF = tk.LabelFrame(self)

        content_LF.columnconfigure(0, weight=1)
        content_LF.rowconfigure(0, weight=1)

        self.robot_overview_TV = RobotOverviewTreeview(content_LF, selectmode="browse")
        self.robot_overview_TV.grid(row=0, column=0, rowspan=2, sticky=tk.NSEW, padx=5, pady=5)

        toolbar.reload_button.config(command=self.robot_overview_TV.insert_all_robots)
        toolbar.edit_button.config(command=self.edit_robot)
        toolbar.add_time_button.config(command=self.add_time_to_robot)

        content_LF.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def edit_robot(self):
        item = self.robot_overview_TV.item(
            self.robot_overview_TV.focus()
        )

        if item["text"]:
            self.controller.frames["EditRobotPage"].fill_values(item)
            self.controller.show_frame("EditRobotPage")
        else:
            messagebox.showerror("Fehler", "Es wurde kein Eintrag ausgewählt.")

    def add_time_to_robot(self):
        item = self.robot_overview_TV.item(
            self.robot_overview_TV.focus()
        )

        if item["text"]:
            id = item["text"]
            name = item['values'][1]
            value = simpledialog.askinteger("Zusätzliche Zeit Buchen", f"Zusätzliche Stunden für {name}:")
            RobotManager.get_instance().add_time_to_robot(id, value)
        else:
            messagebox.showerror("Fehler", "Es wurde kein Eintrag ausgewählt.")

