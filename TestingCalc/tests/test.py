import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    # Позитивный тест для метода multiply
    def test_multiply(self):
        assert self.calc.multiply(2, 3) == 6

    # Позитивный тест для метода division
    def test_division(self):
        assert self.calc.division(10, 2) == 5

    # Позитивный тест для метода subtraction
    def test_subtraction(self):
        assert self.calc.subtraction(8, 3) == 5

    # Позитивный тест для метода adding
    def test_adding(self):
        assert self.calc.adding(4, 6) == 10

    def teardown(self):
        print('Выполнение метода Teardown')