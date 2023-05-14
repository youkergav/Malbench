from datetime import date
from malbench.celebrations import Celebrations
from unittest import TestCase


class TestCelebrations(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.celebrations = Celebrations(2023)

    def test_new_years(self):
        self.assertEqual(self.celebrations.new_years, date(2023, 1, 1))

    def test_valentines_day(self):
        self.assertEqual(self.celebrations.valentines_day, date(2023, 2, 14))

    def test_patricks_days(self):
        self.assertEqual(self.celebrations.st_patricks_day, date(2023, 3, 17))

    def test_birthday(self):
        self.assertEqual(self.celebrations.birthday, date(2023, 4, 1))

    def test_easter(self):
        self.assertEqual(self.celebrations.easter, date(2023, 4, 9))

    def test_star_wars_day(self):
        self.assertEqual(self.celebrations.star_wars_day, date(2023, 5, 4))

    def test_cinco_de_mayo(self):
        self.assertEqual(self.celebrations.cinco_de_mayo, date(2023, 5, 5))

    def test_mothers_day(self):
        self.assertEqual(self.celebrations.mothers_day, date(2023, 5, 14))

    def test_fathers_day(self):
        self.assertEqual(self.celebrations.fathers_day, date(2023, 6, 18))

    def test_labor_day(self):
        self.assertEqual(self.celebrations.labor_day, date(2023, 9, 4))

    def test_independence_day(self):
        self.assertEqual(self.celebrations.independence_day, date(2023, 7, 4))

    def test_halloween(self):
        self.assertEqual(self.celebrations.halloween, date(2023, 10, 31))

    def test_thanksgiving(self):
        self.assertEqual(self.celebrations.thanksgiving, date(2023, 11, 23))

    def test_christmas_eve(self):
        self.assertEqual(self.celebrations.christmas_eve, date(2023, 12, 24))

    def test_christmas(self):
        self.assertEqual(self.celebrations.christmas, date(2023, 12, 25))

    def test_new_years_eve(self):
        self.assertEqual(self.celebrations.new_years_eve, date(2023, 12, 31))
