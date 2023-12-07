from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("TestModel", "TestType", 9000, 12000)
        self.car_two = SecondHandCar("NewModel", "NewType", 8000, 10000)
        self.car_three = SecondHandCar("TestModel", "TestType", 7000, 11000)

    def test_init(self):
        self.assertEqual("TestModel", self.car.model)
        self.assertEqual("TestType", self.car.car_type)
        self.assertEqual(9000, self.car.mileage)
        self.assertEqual(12000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_lower_than_one_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.9

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_mileage_lower_than_one_hundred_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_mileage_equal_to_one_hundred_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_set_promo_price_that_is_higher_than_current_price_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(self.car.price + 1)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promo_price_as_expected(self):
        self.assertEqual('The promotional price has been successfully set.',
                         self.car.set_promotional_price(self.car.price - 1))

    def test_repair_result_impossible_repair(self):
        self.assertEqual("Repair is impossible!",
                         self.car.need_repair(6001, "test description"))

    def test_repair_expected_result(self):
        self.assertEqual("Price has been increased due to repair charges.",
                         self.car.need_repair(3000, "test_descr"))

    def test_cannot_compare_cars(self):
        result = self.car_two > self.car
        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test_compare(self):
        result = self.car > self.car_three
        self.assertTrue(result)

    def test_string(self):
        self.assertEqual(str(self.car), 'Model TestModel | Type TestType | Milage 9000km\nCurrent price: 12000.00 | Number of Repairs: 0')




if __name__ == "__main__":
    main()
