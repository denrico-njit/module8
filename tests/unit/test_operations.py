# tests/test_operations.py
import pytest
from app.operations import add, subtract, multiply, divide


# addition tests

def test_add_two_ints():
    assert add(2, 3) == 5

def test_add_two_floats():
    assert add(2.5, 1.5) == 4.0

def test_add_int_and_float():
    assert add(2, 3.5) == 5.5

def test_add_negatives():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 5) == 5


# subtraction tests

def test_subtract_two_ints():
    assert subtract(5, 3) == 2

def test_subtract_two_floats():
    assert subtract(5.5, 2.0) == 3.5

def test_subtract_negative_result():
    assert subtract(3, 5) == -2

def test_subtract_zero():
    assert subtract(7, 0) == 7


# multiplication tests

def test_multiply_two_ints():
    assert multiply(2, 3) == 6

def test_multiply_float():
    assert multiply(2.5, 4) == 10.0

def test_multiply_by_zero():
    assert multiply(5, 0) == 0

def test_multiply_negatives():
    assert multiply(-2, 3) == -6

def test_multiply_two_negatives():
    assert multiply(-2, -3) == 6


# division tests

def test_divide_returns_float():
    assert isinstance(divide(6, 3), float)

def test_divide_float_result():
    assert divide(5.5, 2) == 2.75

def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(5, 0)

def test_divide_negative():
    assert divide(-6, 3) == -2.0