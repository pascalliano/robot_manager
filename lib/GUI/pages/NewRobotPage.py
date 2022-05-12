import tkinter as tk
from tkinter import ttk

from lib.GUI.custom_widgets.NewRobot.NewRobotForm import NewRobotForm
from lib.GUI.custom_widgets.NewRobot.NewRobotToolbar import NewRobotToolbar


class NewRobotPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        toolbar = NewRobotToolbar(self, controller)
        toolbar.pack(side=tk.TOP, fill=tk.X, expand=False)

        content_LF = tk.LabelFrame(self)

        content_LF.columnconfigure(0, weight=1)
        content_LF.rowconfigure(0, weight=1)

        self.new_robot_form = NewRobotForm(content_LF, controller)
        toolbar.save_button.config(command=self.new_robot_form.add_new_robot)

        content_LF.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
