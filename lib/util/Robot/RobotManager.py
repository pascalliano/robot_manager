from lib.DBConnector.DBConnector import DBConnector


class RobotManager:
    __instance = None
    all_robots = []

    def __init__(self):
        self.update_all_robots()

    @staticmethod
    def get_instance():
        if RobotManager.__instance is None:
            RobotManager.__instance = RobotManager()
        return RobotManager.__instance

    def update_all_robots(self):
        self.all_robots = DBConnector.get_instance().get_all_robots()

    def get_all_robots(self):
        self.update_all_robots()
        return self.all_robots

    def get_robot_by_id(self, id):
        for r in self.all_robots:
            if r.id == id:
                return r
        return None

    def add_time_to_robot(self, id, value):
        DBConnector.get_instance().add_time_to_robot(
            id, value
        )

    def add_new_robot(self, ipa, name, sh_descr, cost, runtime, contact_person, comment):
        DBConnector.get_instance().add_new_robot(
            ipa, name, sh_descr, cost, runtime, contact_person, comment
        )

    def update_robot(self, id, ipa, name, sh_descr, cost, runtime, contact_person, comment):
        DBConnector.get_instance().update_robot(
            id, ipa, name, sh_descr, cost, runtime, contact_person, comment
        )