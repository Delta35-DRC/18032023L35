class Human:
    def __init__(self, name="Human"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")


nick = Human("Nick")
kate = Human("Kate")
vasya = Human("Vasya")
car1 = Auto("Mercedes")
car2 = Auto("BMW")
car1.add_passenger(nick)
car1.add_passenger(kate)
car1.print_passengers_names()
car2.add_passenger(vasya)
car2.print_passengers_names()
