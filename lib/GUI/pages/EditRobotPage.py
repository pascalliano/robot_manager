import tkinter as tk
from tkinter import ttk, messagebox

from lib.GUI.custom_widgets.EditRobot.EditRobotForm import EditRobotForm
from lib.GUI.custom_widgets.EditRobot.EditRobotToolbar import EditRobotToolbar
from lib.GUI.custom_widgets.NewRobot.NewRobotForm import NewRobotForm
from lib.GUI.custom_widgets.NewRobot.NewRobotToolbar import NewRobotToolbar
from lib.util.ContactPerson.ContactPersonManager import ContactPersonManager
from lib.util.Robot.RobotManager import RobotManager


class EditRobotPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        toolbar = EditRobotToolbar(self, controller)
        toolbar.pack(side=tk.TOP, fill=tk.X, expand=False)

        content_LF = tk.LabelFrame(self)

        content_LF.columnconfigure(0, weight=1)
        content_LF.rowconfigure(0, weight=1)

        self.edit_robot_form = EditRobotForm(content_LF, controller)
        toolbar.save_button.config(command=self.edit_robot_form.save_changes)

        content_LF.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def fill_values(self, item):
        id = int(item["text"])
        robot = RobotManager.get_instance().get_robot_by_id(id)

        self.edit_robot_form.id_E.config(state="normal")

        self.edit_robot_form.id_E.delete(0, tk.END)
        self.edit_robot_form.ipa_E.delete(0, tk.END)
        self.edit_robot_form.name_E.delete(0, tk.END)
        self.edit_robot_form.descr_E.delete(0, tk.END)
        self.edit_robot_form.cost_E.delete(0, tk.END)
        self.edit_robot_form.runtime_E.delete(0, tk.END)
        self.edit_robot_form.contact_CB.set("")
        self.edit_robot_form.comment_E.delete("1.0", tk.END)

        self.edit_robot_form.id_E.insert(0, robot.id)
        self.edit_robot_form.ipa_E.insert(0, robot.ipa)
        self.edit_robot_form.name_E.insert(0, robot.name)
        self.edit_robot_form.descr_E.insert(0, robot.descr)
        self.edit_robot_form.cost_E.insert(0, robot.cost)
        self.edit_robot_form.runtime_E.insert(0, robot.runtime)
        self.edit_robot_form.contact_CB.set(
            ContactPersonManager.get_instance().get_contact_person_by_id_longstr(robot.contact_person_id)
        )
        self.edit_robot_form.comment_E.insert("1.0", robot.comment)

        self.edit_robot_form.append_to_entry(self.edit_robot_form.cost_E, ",00 €")
        self.edit_robot_form.append_to_entry(self.edit_robot_form.runtime_E, ",00 h")

        self.edit_robot_form.id_E.config(state="readonly")