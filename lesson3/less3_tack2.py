class Air_company:
    def __init__(self):
        self.flights = []
        self.cargo_flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def add_cargo_flight(self, cargo_flight):
        self.cargo_flights.append(cargo_flight)

    def total_profit(self):
        total = 0
        total_flight = 0
        total_cargo = 0
        for flight in self.flights:
            total_flight += flight.profit()
        for cargo_flight in self.cargo_flights:
            total_cargo += cargo_flight.profit_cargo()
        total = total_flight + total_cargo
        return total

class Flight:
    def __init__(self, distance):
        self.distance = distance
        self.airplane = None
        self.staff = []
        self.tickets = []

    def set_airplane(self, airplane):
        self.airplane = airplane

    def add_staff(self, staff):
        self.staff.append(staff)

    def add_ticket(self, ticket):
        if self.airplane.capasity > len(self.tickets):
            self.tickets.append(ticket)
        else:
            raise Exception("Capasity error")

    def profit(self):
        total = 0
        for ticket in self.tickets:
            total += ticket.price
        for staff in self.staff:
            total -= staff.salary
        total -= self.airplane.consumption * self.distance * self.airplane.fuel.price
        return total

class Cargo_Fligth(Flight):
    def __init__(self, distance):
        Flight.__init__(self, distance)
        self.cargos = []

    def add_cargo(self, freight):
        if self.airplane.cargo_mass - self.calculate_weight() >= freight.weight: #проверка превышения грузоподъемности
            self.cargos.append(freight)
        else:
            raise Exception("Overweight")

    def calculate_weight(self):
        total = 0
        for freight in self.cargos:
            total += freight.weight
        return total

    def profit_cargo(self):
        total = 0
        for freight in self.cargos:
            total += freight.price * freight.weight
        for staff in self.staff:
            total -= staff.salary
        total -= self.airplane.consumption * self.distance * self.airplane.fuel.price
        return total

class Airplane:
    def __init__(self, capasity, fuel, consumption):
        self.capasity = capasity
        self.fuel = fuel
        self.consumption = consumption

class Cargo_Airplane(Airplane):
    def __init__(self, capasity, fuel, consumption, cargo_mass):
        Airplane.__init__(self, capasity, fuel, consumption)
        self.cargo_mass = cargo_mass

class Staff:
    def __init__(self, salary):
        self.salary = salary

class Fuel:
    def __init__(self, price):
        self.price = price

class Ticket:
    def __init__(self, price):
        self.price = price

class Freight:
    def __init__(self, weigth, price):
        self.weight = weigth
        self.price = price

mau = Air_company()
ticket1 = Ticket(200) #стоимость билета
fuel = Fuel(10) #per 1 kg
staff_stewardess = Staff(200)
staff_pilot = Staff(500)
plane_A320 = Airplane(200, fuel, 3)
flight444 = Flight(900)
flight444.set_airplane(plane_A320)
flight444.add_staff(staff_stewardess)
flight444.add_staff(staff_pilot)
for i in range(1, plane_A320.capasity):
    flight444.add_ticket(ticket1)
mau.add_flight(flight444)
print(mau.total_profit())

freight1 = Freight(20000, 10) #вес и цена за 1 кг груза
freight2 = Freight(50000, 20)
freight3 = Freight(10000, 30)
fuel_cargo = Fuel(20)
staff_crew = Staff(1000)
plane_An225 = Cargo_Airplane(10, fuel_cargo, 5, 250000)
flight555 = Cargo_Fligth(1200)
flight555.set_airplane(plane_An225)
flight555.add_staff(staff_crew)
flight555.add_cargo(freight1)
flight555.add_cargo(freight2)
flight555.add_cargo(freight3)
mau.add_cargo_flight(flight555)
print(mau.total_profit())


