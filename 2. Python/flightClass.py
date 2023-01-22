class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.pasangers = []
    
    def add_pasanger(self, name):
        if not self.open_seats():
            return False
        self.pasangers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.pasangers)

flight = Flight(3)

people = ["abid", "bob", "zahin", "shanila"]

for person in people:
    success = flight.add_pasanger(person)
    if success:
        print (f"Successfully added {person}")
    else:
        print (f"Failed to add {person}")