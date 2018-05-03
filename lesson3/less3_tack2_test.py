import unittest

from lesson3.less3_tack2 import Ticket, Fuel, Staff, Airplane, Flight, Air_company


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
        mau.total_profit()


if __name__ == '__main__':
    unittest.main()
