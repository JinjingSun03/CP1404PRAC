import unittest
from unreliable_car import Car, UnreliableCar

class TestUnreliableCar(unittest.TestCase):
    def test_drive_successful(self):
        car = UnreliableCar("Test Car", fuel=50, reliability=80)
        distance_driven = car.drive(30)
        self.assertGreater(distance_driven, 0)
        self.assertLessEqual(distance_driven, 30)
        self.assertEqual(car.fuel, 50 - distance_driven)

    def test_drive_unsuccessful(self):
        car = UnreliableCar("Test Car", fuel=50, reliability=20)
        distance_driven = car.drive(30)
        self.assertEqual(distance_driven, 0)
        self.assertEqual(car.fuel, 50)

if __name__ == '__main__':
    unittest.main()
