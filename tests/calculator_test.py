"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations
@pytest.fixture
def clear_history_fixture():
    Calculations.clear_history()
def test_calculator_add_static(clear_history_fixture):
    assert Calculator.add_numbers(1.0,2.0) == 3.0

def test_calculator_subtract_static(clear_history_fixture):
    assert Calculator.subtract_numbers(1.0,2.0) == -3.0

def test_calculator_multiply_static(clear_history_fixture):
    assert Calculator.multiply_numbers(1.0,2.0) == 2.0

def test_calculator_divide_static(clear_history_fixture):
    assert Calculator.divide_numbers(1.0,2.0) == 0.5
