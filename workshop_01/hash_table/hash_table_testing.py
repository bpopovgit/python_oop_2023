import unittest

from hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable(100)
        self.hash_table["hello"] = "Hello World!"
        self.hash_table[98.6] = 37
        self.hash_table[False] = True

    def test_create_hash_table(self):
        self.assertIsNotNone(HashTable(10))

    def test_report_capacity(self):
        self.assertEqual(3, len(self.hash_table.array))

    def test_create_empty_pair_slots(self):
        hash_table = HashTable(4)
        expected = [None, None, None, None]

        actual = hash_table._array

        self.assertEqual(expected, actual)

    def test_insert_key_value_pair(self):
        hash_table = HashTable(4)
        hash_table["hello"] = "Hello World!"

        self.assertIn(("hello", "Hello World!"), hash_table.array)


if __name__ == "__main__":
    unittest.main()
