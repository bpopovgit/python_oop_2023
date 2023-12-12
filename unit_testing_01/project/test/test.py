from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot('R1', 'Education', 200, 100)

    def test_init(self):
        self.assertEqual("R1", self.robot.robot_id)
        self.assertEqual("Education", self.robot.category)
        self.assertEqual(200, self.robot.available_capacity)
        self.assertEqual(100, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_value_not_in_allowed_categories_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Test"

        self.assertEqual(f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
                         , str(ve.exception))

    def test_price_negative_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -10

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_not_existing_component(self):
        self.robot.upgrade("FirstTest", 100)
        self.assertEqual(["FirstTest"], self.robot.hardware_upgrades)
        self.assertEqual(self.robot.price, 250)

        result = self.robot.upgrade('TestComponent', 100)
        self.assertEqual("Robot R1 was upgraded with TestComponent.", result)
        self.assertEqual(["FirstTest", "TestComponent"], self.robot.hardware_upgrades)
        self.assertEqual(self.robot.price, 400)

    def test_upgrade_hardware_component_exists(self):
        self.robot.upgrade("TestComponent", 100)
        self.assertEqual(["TestComponent"], self.robot.hardware_upgrades)
        self.assertEqual(250, self.robot.price)

        result = self.robot.upgrade("TestComponent", 100)
        self.assertEqual("Robot R1 was not upgraded.", result)
        self.assertEqual(self.robot.hardware_upgrades, ['TestComponent'])
        self.assertEqual(self.robot.price, 250)

    def test_successful_update(self):
        result = self.robot.update(1.5, 10)
        expected_result = 'Robot R1 was updated to version 1.5.'
        self.assertEqual(result, expected_result)
        self.assertEqual(self.robot.software_updates, [1.5])
        self.assertEqual(self.robot.available_capacity, 190)

    def test_unsuccessful_update_due_to_version(self):
        # Adding an initial software update
        self.robot.software_updates.append(1.0)

        result = self.robot.update(1.0, 20)
        expected_result = 'Robot R1 was not updated.'
        self.assertEqual(result, expected_result)
        self.assertEqual(self.robot.software_updates, [1.0])
        self.assertEqual(self.robot.available_capacity, 200)

    def test_update__lower_version_and_enough_capacity__should_not_update(self):
        self.robot.update(2.22, 50)
        self.assertEqual(self.robot.software_updates, [2.22])
        result = self.robot.update(2.20, 50)
        self.assertEqual(result, 'Robot R1 was not updated.')
        self.assertEqual(self.robot.software_updates, [2.22])
        self.assertEqual(self.robot.available_capacity, 150)

    def test_unsuccessful_update_due_to_both_conditions(self):
        # Both conditions should trigger an unsuccessful update
        self.robot.software_updates.append(1.0)

        result = self.robot.update(1.0, 20)
        expected_result = 'Robot R1 was not updated.'
        self.assertEqual(result, expected_result)
        self.assertEqual(self.robot.software_updates, [1.0])
        self.assertEqual(self.robot.available_capacity, 200)

    def test__gt__should_return_first_robot_is_more_expensive(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.other_robot = Robot('R2', 'Education', 200, 99.99)

        result = self.robot > self.other_robot
        self.assertEqual(result, "Robot with ID R1 is more expensive than Robot with ID R2.")

    def test__gt__should_return_first_robot_is_cheaper(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.other_robot = Robot('R2', 'Education', 200, 100.01)

        result = self.robot > self.other_robot
        self.assertEqual(result, "Robot with ID R1 is cheaper than Robot with ID R2.")

    def test__gt__should_return_robots_are_equal(self):
        self.robot = Robot('R1', 'Education', 200, 100.01)
        self.other_robot = Robot('R2', 'Education', 200, 100.01)

        result = self.robot > self.other_robot
        self.assertEqual(result, "Robot with ID R1 costs equal to Robot with ID R2.")



if __name__ == "__main__":
    main()
