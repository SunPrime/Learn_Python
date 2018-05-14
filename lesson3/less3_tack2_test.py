import unittest

from lesson3.less3_tack2 import Ticket, Fuel, Staff, Airplane, Flight, Air_company, Freight, Cargo_Airplane, \
    Cargo_Fligth


class TestCase_less3_tack2(unittest.TestCase):
    def test_Air_company(self):
        ticket1 = Ticket(200)
        fuel = Fuel(10)  # per 1 kg
        staff_stewardess = Staff(200)
        staff_pilot = Staff(500)
        plane_A320 = Airplane(200, fuel, 3)
        flight444 = Flight(900)
        flight444.set_airplane(plane_A320)
        flight444.add_staff(staff_stewardess)
        flight444.add_staff(staff_pilot)
        for i in range(1, plane_A320.capasity):
            flight444.add_ticket(ticket1)
        mau = Air_company()
        mau.add_flight(flight444)
        freight1 = Freight(20000, 10)  # вес и цена за 1 кг груза
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
        mau.total_profit()


if __name__ == '__main__':
    unittest.main()
