from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    fuel = 3.5
    horse_power = 115.5

    def setUp(self):
        self.test_vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        self.assertEqual(self.fuel, self.test_vehicle.fuel)
        self.assertEqual(self.fuel, self.test_vehicle.capacity)
        self.assertEqual(self.horse_power, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)

    def test_attributes_types(self):
        self.assertTrue(isinstance(self.test_vehicle.fuel, float))
        self.assertTrue(isinstance(self.test_vehicle.capacity, float))
        self.assertTrue(isinstance(self.test_vehicle.horse_power, float))
        self.assertTrue(isinstance(self.test_vehicle.fuel_consumption, float))
        self.assertTrue(isinstance(self.test_vehicle.DEFAULT_FUEL_CONSUMPTION, float))

    def test_drive_successful(self):
        self.test_vehicle.drive(2)
        self.assertEqual(1, self.test_vehicle.fuel)

    def test_drive_not_enough_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(3)

        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel_successful(self):
        self.test_vehicle.fuel = 1
        self.test_vehicle.refuel(1.5)
        self.assertEqual(2.5, self.test_vehicle.fuel)

    def test_refuel_too_much_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(8)

        self.assertEqual('Too much fuel', str(ex.exception))

    def test_str(self):
        self.test_vehicle.fuel = 2.5

        expected = f"The vehicle has {self.test_vehicle.horse_power} " \
               f"horse power with 2.5 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected, str(self.test_vehicle))



if __name__ == '__main__':
    main()