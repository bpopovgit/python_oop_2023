import collections
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.t1 = RailwayStation("t123")
        self.t2 = RailwayStation("TestRailway2")

    def test_init_railway_station(self):
        self.assertEqual("t1", self.t1.name)
        self.assertEqual( "TestRailway2", self.t2.name)

    def test_name_setter_value_lower_than_3_value_error(self):

        with self.assertRaises(ValueError) as cm:
            self.t1.name = "t1"
        self.assertEqual(
            'Name should be more than 3 symbols!',
            str(cm.exception)
        )

    def test_name_setter_value_equal_to_3_value_error(self):

        with self.assertRaises(ValueError) as cm:
            self.t1.name = "t12"
        self.assertEqual(
            'Name should be more than 3 symbols!',
            str(cm.exception)
        )

    def test_new_arrival_on_board(self):
        tr_info = "info1"
        arr_trains = collections.deque().append(tr_info)
        result = self.t1.new_arrival_on_board("info1")
        self.assertEqual(arr_trains, result)

    def test_arrival_of_wrong_train(self):
        self.t2.new_arrival_on_board("info1")
        result = self.t2.train_has_arrived("info2")
        self.assertEqual("There are other trains to arrive before info2.", result)

    def test_arrival_of_correct_train(self):
        self.t2.new_arrival_on_board("info2")
        result = self.t2.train_has_arrived("info2")
        self.assertEqual("info2 is on the platform and will leave in 5 minutes.", result)

    def test_correct_train_has_left(self):
        self.t2.new_arrival_on_board("info2")
        self.t2.train_has_arrived("info2")
        expected = True
        result = self.t2.train_has_left("info2")
        self.assertEqual(expected, result)

    def test_wrong_train_has_left(self):
        self.t2.new_arrival_on_board("info2")
        self.t2.train_has_arrived("info1")
        expected = False
        result = self.t2.train_has_left("info2")
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
