class Point:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, person):
        if self.capacity - len(self.passengers) > 0:
            self.passengers.append(person)
            return True
        else:
            return False

    def remaining_capacity(self):
        return self.capacity - len(self.passengers)
caps = Point(3)
flight = ["Ayush", "Poonam", "Asmita", "Jay"]
for person in flight:
    if caps.add_passenger(person):
        print(f'{person} was added.')
    else:
        print(f'{person} was not added.')
