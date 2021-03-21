from django.test import SimpleTestCase
from ..helpers import check_access_by_age, string_concatenation, division, work_time_check


class BusinessLogicTest(SimpleTestCase):
    def test_access_by_denied(self):
        self.assertFalse(check_access_by_age(17))
        # self.assertTrue(check_access_by_age(17))
        # self.assertEqual(check_access_by_age(17), True)

    def test_string_concatenation(self):
        self.assertEqual(string_concatenation('First', 'Second'), 'FirstSecond')
        self.assertEqual(string_concatenation('First', 42), False)
        self.assertEqual(string_concatenation(True, 'Second'), False)

    def test_division(self):
        self.assertEqual(division(51.4, 25.4), 2.0236220472440944)
        self.assertEqual(division(10, 2), 5.0)
        self.assertEqual(division(10, 2.55), 3.9215686274509807)
        self.assertEqual(division('10', 2.55), False)
        self.assertEqual(division(10, True), False)

    def test_work_time_check(self):
        self.assertEqual(work_time_check(0), 'Closed')
        self.assertEqual(work_time_check(7), 'Closed')
        self.assertEqual(work_time_check(8), 'Work')
        self.assertEqual(work_time_check(9), 'Work')
        self.assertEqual(work_time_check(13), 'Closed')
        self.assertEqual(work_time_check(14), 'Work')
        self.assertEqual(work_time_check(16), 'Work')
        self.assertEqual(work_time_check(19), 'Work')
        self.assertEqual(work_time_check(20), 'Closed')
        self.assertEqual(work_time_check(23), 'Closed')
        self.assertEqual(work_time_check(24), 'Closed')
        self.assertEqual(work_time_check(25), False)
        self.assertEqual(work_time_check(19.0), False)
        self.assertEqual(work_time_check(-23), False)
        self.assertEqual(work_time_check('24'), False)
        self.assertEqual(work_time_check(True), False)
        self.assertEqual(work_time_check(False), False)

