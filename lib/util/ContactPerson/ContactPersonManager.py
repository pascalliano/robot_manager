import re

from lib.DBConnector.DBConnector import DBConnector
from lib.util.ContactPerson.ContactPerson import ContactPerson


class ContactPersonManager:
    __instance = None
    all_contact_persons = []

    def __init__(self):
        self.update_all_contact_persons()

    @staticmethod
    def get_instance():
        if ContactPersonManager.__instance is None:
            ContactPersonManager.__instance = ContactPersonManager()
        return ContactPersonManager.__instance

    def update_all_contact_persons(self):
        self.all_contact_persons = DBConnector.get_instance().get_all_contactPersons()

    def get_all_contact_persons(self):
        self.update_all_contact_persons()
        return self.all_contact_persons

    def get_all_contact_persons_longstr(self):
        self.update_all_contact_persons()
        return sorted([
            f"{cp.surname}, {cp.forename} ({cp.department})" for cp in self.all_contact_persons
        ])

    def get_contact_person_by_id(self, id):
        for cp in self.all_contact_persons:
            if cp.id == id:
                return cp
        return None

    def get_contact_person_by_id_shortstr(self, id):
        for cp in self.all_contact_persons:
            if cp.id == id:
                return f"{cp.surname}, {cp.forename}"
        return None

    def get_contact_person_by_id_longstr(self, id):
        for cp in self.all_contact_persons:
            if cp.id == id:
                return f"{cp.surname}, {cp.forename} ({cp.department})"
        return ""

    def add_new_contactPerson(self, name, forename, dep, email):
        DBConnector.get_instance().add_new_contactPerson(
            name, forename, dep, email
        )

    def update_contactPerson(self, id, name, forename, dep, email):
        DBConnector.get_instance().update_contactPerson(
            id, name, forename, dep, email
        )

    def get_contact_person_id_by_longstr(self, longstr):
        if not longstr.strip():
            return None

        group = re.match("(.*), (.*) [(](.*)[)]", longstr)
        if group:
            surename = group.group(1)
            forename = group.group(2)
            dep = group.group(3)
            for cp in self.all_contact_persons:
                if cp.surname == surename and cp.forename == forename and cp.department == dep:
                    return cp.id
        return "Fehler"
