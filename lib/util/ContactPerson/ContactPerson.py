class ContactPerson:
    id = None
    forename = None
    surname = None
    department = None
    email = None

    def __init__(self, id, forename, surname, department, email):
        self.id = id
        self.forename = forename
        self.surname = surname
        self.department = department
        self.email = email
