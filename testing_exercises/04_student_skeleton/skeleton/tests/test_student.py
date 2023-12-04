from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student_1 = Student("Student 1", {"Python": ["n1", "n2", "n3"], "JS": ["n1", "n2"]})
        self.student_2 = Student("Student 2")

    def test_init_with_courses(self):
        self.assertEqual("Student 1", self.student_1.name)
        self.assertEqual({"Python": ["n1", "n2", "n3"], "JS": ["n1", "n2"]}, self.student_1.courses)

    def test_init_without_courses(self):
        self.assertEqual("Student 2", self.student_2.name)
        self.assertEqual({}, self.student_2.courses)

    def test_enroll_existing_course(self):
        result = self.student_1.enroll("Python", ["n4", "n5"], add_course_notes="N")

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["n1", "n2", "n3", "n4", "n5"], "JS": ["n1", "n2"]}, self.student_1.courses)

    def test_enroll_not_existing_course_with_y(self):
        result = self.student_1.enroll("C#", ["n1", "n2"], "Y")

        self.assertTrue("C#" in self.student_1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n1", "n2"], self.student_1.courses["C#"])

    def test_non_existing_course_with_empty_string(self):
        result = self.student_1.enroll("C#", ["n1", "n2"], "")

        self.assertTrue("C#" in self.student_1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n1", "n2"], self.student_1.courses["C#"])

    def test_not_existing_course_without_adding_notes(self):
        result = self.student_1.enroll("C#", ["n1", "n2"], "N")

        self.assertTrue("C#" in self.student_1.courses)
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student_1.courses["C#"])

    def test_add_notes_to_existing_course(self):
        self.student_2.enroll("C#", ["n1", "n2"])
        result = self.student_2.add_notes("C#", "n3")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["n1", "n2", "n3"], self.student_2.courses["C#"])

    def test_add_notes_to_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_2.add_notes("C#", "n3")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student_1.leave_course("Python")

        self.assertEqual("Course has been removed", result)
        self.assertNotIn("Python", self.student_1.courses)

    def test_leave_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("Java")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))





if __name__ == "__main__":
    main()
