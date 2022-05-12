class Robot:
    id = None
    ipa = None
    name = None
    contact_person_id = None
    descr = None
    cost = None
    runtime = None
    add_time = None
    comment = None
    total_time = None
    total_cost = None
    contact_person_name = None

    def __init__(self, id, ipa, name, contact_person_id, descr, cost, runtime, add_time, comment):
        self.id = id
        self.ipa = ipa
        self.name = name
        self.contact_person_id = contact_person_id
        self.descr = descr
        self.cost = cost
        self.runtime = runtime
        self.add_time = add_time
        self.comment = comment

        self.total_time = self.runtime + self.add_time
        self.total_cost = self.cost * self.total_time
