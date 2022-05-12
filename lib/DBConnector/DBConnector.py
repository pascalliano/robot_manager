import sqlite3
import os

from lib.util.ContactPerson.ContactPerson import ContactPerson
from lib.util.Robot.Robot import Robot

DB_PATH = "res/db/robot.db"
INIT_FILE = "res/db/init.sql"


class DBConnector:
    __instance = None

    def __init__(self):
        if os.path.exists(DB_PATH):
            self.connection = sqlite3.connect(DB_PATH)
            self.cursor = self.connection.cursor()

        else:
            with open(INIT_FILE, "r") as f:
                query = f.read()

            self.connection = sqlite3.connect(DB_PATH)
            self.cursor = self.connection.cursor()

            try:
                self.cursor.executescript(query)
                self.connection.commit()

            except sqlite3.OperationalError as e:
                self.connection.close()
                os.unlink(DB_PATH)

    @staticmethod
    def get_instance():
        if DBConnector.__instance is None:
            DBConnector.__instance = DBConnector()
        return DBConnector.__instance

    # DB Methods
    def get_all_robots(self):
        query = "SELECT * from robot"

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        return [
            Robot(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]) for r in result
        ]

    def get_all_contactPersons(self):
        query = "SELECT * from contactPerson"

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        return [
            ContactPerson(r[0], r[1], r[2], r[3], r[4]) for r in result
        ]

    def get_add_time_for_robot(self, id):
        query = "SELECT add_time from robot WHERE id=?"

        self.cursor.execute(query, (id, ))
        result = self.cursor.fetchall()

        return result[0][0]

    def add_time_to_robot(self, id, value):
        old_value = int(self.get_add_time_for_robot(id))

        query = "UPDATE robot SET add_time=? WHERE id=?"

        self.cursor.execute(query, (old_value + value, id))
        self.connection.commit()

    def add_new_contactPerson(self, name, forename, dep, email):
        query = "INSERT INTO contactPerson(forname, surname, department, email) VALUES (?, ?, ?, ?)"

        self.cursor.execute(query, (forename, name, dep, email))
        self.connection.commit()

    def add_new_robot(self, ipa, name, sh_descr, cost, runtime, contact_person, comment):
        query = "INSERT INTO robot(ipa, name, contactPersonID, descr, cost, runtime, add_time, comment) " \
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

        self.cursor.execute(query, (ipa, name, contact_person, sh_descr, cost, runtime, 0, comment))
        self.connection.commit()

    def update_robot(self, id, ipa, name, sh_descr, cost, runtime, contact_person, comment):
        query = "UPDATE robot SET ipa=?, name=?, contactPersonID=?, descr=?, cost=?, runtime=?, comment=?" \
                "WHERE id=?"

        self.cursor.execute(query, (ipa, name, contact_person, sh_descr, cost, runtime, comment, id))
        self.connection.commit()

    def update_contactPerson(self, id, name, forename, dep, email):
        query = "UPDATE contactPerson SET forname=?, surname=?, department=?, email=?" \
                "WHERE id=?"

        self.cursor.execute(query, (forename, name, dep, email, id))
        self.connection.commit()
