"""Tests for calculator_app.calculator module."""

import math

import pytest

from calculator_app.calculator import add, divide, multiply, power, sqrt, subtract


class TestAdd:
    def test_positive_numbers(self) -> None:
        assert add(2.0, 3.0) == 5.0

    def test_negative_numbers(self) -> None:
        assert add(-1.0, -4.0) == -5.0

    def test_mixed_signs(self) -> None:
        assert add(-3.0, 5.0) == 2.0

    def test_zero(self) -> None:
        assert add(0.0, 0.0) == 0.0

    def test_floats(self) -> None:
        assert add(1.1, 2.2) == pytest.approx(3.3)


class TestSubtract:
    def test_positive_numbers(self) -> None:
        assert subtract(10.0, 4.0) == 6.0

    def test_negative_result(self) -> None:
        assert subtract(3.0, 8.0) == -5.0

    def test_same_values(self) -> None:
        assert subtract(5.0, 5.0) == 0.0

    def test_floats(self) -> None:
        assert subtract(3.3, 1.1) == pytest.approx(2.2)


class TestMultiply:
    def test_positive_numbers(self) -> None:
        assert multiply(3.0, 4.0) == 12.0

    def test_negative_numbers(self) -> None:
        assert multiply(-2.0, -3.0) == 6.0

    def test_mixed_signs(self) -> None:
        assert multiply(-2.0, 5.0) == -10.0

    def test_multiply_by_zero(self) -> None:
        assert multiply(100.0, 0.0) == 0.0

    def test_floats(self) -> None:
        assert multiply(2.5, 4.0) == 10.0


class TestDivide:
    def test_positive_numbers(self) -> None:
        assert divide(10.0, 2.0) == 5.0

    def test_negative_dividend(self) -> None:
        assert divide(-9.0, 3.0) == -3.0

    def test_negative_divisor(self) -> None:
        assert divide(8.0, -2.0) == -4.0

    def test_zero_dividend(self) -> None:
        assert divide(0.0, 5.0) == 0.0

    def test_floats(self) -> None:
        assert divide(1.0, 3.0) == pytest.approx(1.0 / 3.0)

    def test_divide_by_zero_raises(self) -> None:
        with pytest.raises(ZeroDivisionError):
            divide(1.0, 0.0)

    def test_divide_by_zero_message(self) -> None:
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(5.0, 0.0)


class TestPower:
    def test_positive_exponent(self) -> None:
        assert power(2.0, 3.0) == 8.0

    def test_zero_exponent(self) -> None:
        assert power(2.0, 0.0) == 1.0

    def test_one_exponent(self) -> None:
        assert power(7.0, 1.0) == 7.0

    def test_negative_exponent(self) -> None:
        assert power(2.0, -1.0) == pytest.approx(0.5)

    def test_fractional_exponent(self) -> None:
        assert power(9.0, 0.5) == pytest.approx(3.0)

    def test_base_zero(self) -> None:
        assert power(0.0, 5.0) == 0.0

    def test_base_one(self) -> None:
        assert power(1.0, 100.0) == 1.0


class TestSqrt:
    def test_perfect_square(self) -> None:
        assert sqrt(4.0) == 2.0

    def test_nine(self) -> None:
        assert sqrt(9.0) == 3.0

    def test_zero(self) -> None:
        assert sqrt(0.0) == 0.0

    def test_non_perfect_square(self) -> None:
        assert sqrt(2.0) == pytest.approx(math.sqrt(2.0))

    def test_one(self) -> None:
        assert sqrt(1.0) == 1.0

    def test_negative_raises(self) -> None:
        with pytest.raises(ValueError):
            sqrt(-1.0)

    def test_negative_message(self) -> None:
        with pytest.raises(ValueError, match="negative"):
            sqrt(-4.0)
