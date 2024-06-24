class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print (f"{person.name} has gotten on the bus. ")
        else: 
            print("The bus is in it's full capacity. No more passengers can be added.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} has gotten off the bus.")
        else: 
            print(f"{person.name} is not on the bus.")

person1 = Person("Kevin")
person2 = Person("Adriana")
person3 = Person("Walter")
person4 = Person("Esther")
person5 = Person("Valery")
person6 = Person("Iann")
person7 = Person("Marissa")
person8 = Person("Jahel")
person9 = Person("Kylian")
person10 = Person("Kyran")
person11 = Person("Joselyn")

bus = Bus(10)

bus.add_passenger(person1)
bus.add_passenger(person2)
bus.add_passenger(person3)
bus.add_passenger(person4)
bus.add_passenger(person5)
bus.add_passenger(person6)
bus.add_passenger(person7)
bus.add_passenger(person8)
bus.add_passenger(person9)
bus.add_passenger(person10)
bus.add_passenger(person11)

bus.remove_passenger(person10)

bus.add_passenger(person11)

