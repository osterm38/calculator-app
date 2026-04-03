"""Core arithmetic operations for the calculator app."""

import math


def add(a: float, b: float) -> float:
    """Return the sum of a and b.

    Args:
        a: The first operand.
        b: The second operand.

    Returns:
        The sum a + b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b.

    Args:
        a: The minuend.
        b: The subtrahend.

    Returns:
        The difference a - b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b.

    Args:
        a: The first factor.
        b: The second factor.

    Returns:
        The product a * b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient a / b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the given exponent.

    Args:
        base: The base value.
        exponent: The exponent to raise the base to.

    Returns:
        The value base ** exponent.
    """
    return base**exponent


def sqrt(x: float) -> float:
    """Return the square root of x.

    Args:
        x: The value to take the square root of.

    Returns:
        The square root of x.

    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError(f"Cannot take the square root of a negative number: {x}")
    return math.sqrt(x)
