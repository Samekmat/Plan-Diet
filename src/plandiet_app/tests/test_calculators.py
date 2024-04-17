from django.test import TestCase

from plandiet_app.calculators.bmr_calculator import bmr_calc
from plandiet_app.calculators.cpm_calculator import cpm_calc


class BMRCalculatorTest(TestCase):
    def test_male_bmr(self):
        self.assertEqual(bmr_calc("male", 70, 170, 30), 1619)

    def test_female_bmr(self):
        self.assertEqual(bmr_calc("female", 60, 160, 25), 1315)


class CPMCalculatorTest(TestCase):
    def test_reduce_goal_male(self):
        bmr_male = bmr_calc("male", 70, 170, 30)
        self.assertEqual(cpm_calc("reduce", bmr_male, 1.2), 1749)

    def test_reduce_goal_female(self):
        bmr_female = bmr_calc("female", 60, 160, 25)
        self.assertEqual(cpm_calc("reduce", bmr_female, 1.2), 1420)

    def test_maintain_goal_male(self):
        bmr_male = bmr_calc("male", 70, 170, 30)
        self.assertEqual(cpm_calc("maintain", bmr_male, 1.2), 1943)

    def test_maintain_goal_female(self):
        bmr_female = bmr_calc("female", 60, 160, 25)
        self.assertEqual(cpm_calc("maintain", bmr_female, 1.2), 1578)

    def test_increase_goal_male(self):
        bmr_male = bmr_calc("male", 70, 170, 30)
        self.assertEqual(cpm_calc("increase", bmr_male, 1.2), 2137)

    def test_increase_goal_female(self):
        bmr_female = bmr_calc("female", 60, 160, 25)
        self.assertEqual(cpm_calc("increase", bmr_female, 1.2), 1736)
