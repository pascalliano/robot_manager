import tkinter as tk
from tkinter import ttk

from lib.GUI.custom_widgets.Navbar import Navbar
from lib.GUI.pages.EditRobotPage import EditRobotPage
from lib.GUI.pages.EditStaffPage import EditStaffPage
from lib.GUI.pages.NewStaffPage import NewStaffPage
from lib.GUI.pages.StaffOverviewPage import StaffOverviewPage
from lib.GUI.pages.NewRobotPage import NewRobotPage
from lib.GUI.pages.RobotOverviewPage import RobotOverviewPage


class MainApplication(tk.Tk):
    frames = {}

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Robot Manager")
        self.state("zoomed")
        self.iconbitmap("res/img/robot.ico")

        navbar = Navbar(self, self)
        navbar.pack(side=tk.TOP, fill=tk.X, expand=False)

        container = tk.Frame(self)

        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {"RobotOverviewPage": RobotOverviewPage,
                      "NewRobotPage": NewRobotPage,
                      "StaffOverviewPage": StaffOverviewPage,
                      "NewStaffPage": NewStaffPage,
                      "EditRobotPage": EditRobotPage,
                      "EditStaffPage": EditStaffPage}

        for F in self.pages:
            frame = self.pages[F](container, self)
            frame.grid(row=0, column=0, sticky=tk.NSEW)
            self.frames[F] = frame

        self.show_frame("RobotOverviewPage")

        # updater = Updater.update(kwargs.get("version"))

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
