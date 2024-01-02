from unittest import TestCase, main

from workshop_02.custom_list import CustomList


class TestCustomList(TestCase):

    def setUp(self):
        self.cl = CustomList(5, "asd", 3.6)

    def test_initialise(self):
        cl = CustomList()
        self.assertEqual(cl._CustomList__values, [])

        cl = CustomList(5, "asd", 3.6)
        self.assertEqual(cl._CustomList__values, [5, "asd", 3.6])

    def test_append_no_argument_raises(self):
        # Usually this is not tested.
        with self.assertRaises(TypeError) as ex:
            self.cl.append()

        self.assertIn("missing 1 required positional argument", str(ex.exception))

    def test_append_adds_element_to_the_end(self):
        # Pre preparation (arrange), assumptions
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.append(100)
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, 100])
        self.assertEqual(self.cl._CustomList__values[-1], 100)
        self.assertEqual(self.cl._CustomList__values, result)

    def test_append_element_to_empty_list(self):
        cl = CustomList()
        self.assertEqual(cl._CustomList__values, [])

        cl.append(5)
        self.assertEqual(cl._CustomList__values, [5])

    def test_invalid_index_type_raises(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        invalid_index_values = [3.6, "asd", "3", [12, 3], {"a": 1}]

        for invalid_index in invalid_index_values:
            with self.assertRaises(ValueError) as ex:
                self.cl.remove(invalid_index)
            self.assertIn("Invalid index type", str(ex.exception))

    def test_remove_invalid_index_raises(self):
        # This means that the last index is 2, or -3
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        with self.assertRaises(IndexError) as ex:
            self.cl.remove(3)
        self.assertIn("Invalid index", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            self.cl.remove(-4)
        self.assertIn("Invalid index", str(ex.exception))

        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

    def test_remove_multiple_same_elements_are_not_removed(self):
        self.cl.append("asd")
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6, "asd"])

        result = self.cl.remove(1)
        self.assertEqual(result, "asd")
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, 3.6, "asd"])

    def test_remove_returns_element(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.remove(1)

        self.assertEqual(result, "asd")
        self.assertEqual(len(self.cl._CustomList__values), 2)
        self.assertEqual(self.cl._CustomList__values, [5, 3.6])

    def test_safe_remove_invalid_index_type_raises(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        invalid_index_values = [3.6, "asd", "3", [12, 3], {"a": 1}]

        for invalid_index in invalid_index_values:
            with self.assertRaises(ValueError) as ex:
                self.cl.safe_remove(invalid_index)
            self.assertIn("Invalid index type", str(ex.exception))

    def test_safe_remove_invalid_index_return_none(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual(self.cl._CustomList__values, [5, "asd", 3.6])

        result = self.cl.safe_remove(12)
        self.assertIsNone(result)

    def test_safe_remove_returns(self):
        pass


if __name__ == "__main__":
    main()
