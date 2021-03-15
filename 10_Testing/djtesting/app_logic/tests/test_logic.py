from django.test import SimpleTestCase
from ..helpers import check_access_by_age


class BusinessLogicTest(SimpleTestCase):
    def test_access_by_denied(self):
        self.assertFalse(check_access_by_age(17))
        # self.assertTrue(check_access_by_age(17))
        # self.assertEqual(check_access_by_age(17), True)
