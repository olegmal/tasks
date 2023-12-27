import pytest

from hw21_tests.fibo import Fibonacci


def test_fibonacci_positive_integers():
    """Test Fibonacci numbers for valid positive integer inputs."""
    fibo = Fibonacci()
    assert fibo(0) == 0
    assert fibo(1) == 1
    assert fibo(5) == 5
    assert fibo(10) == 55


def test_negative_input():
    fibo = Fibonacci()
    with pytest.raises(ValueError):
        fibo(-1)


def test_non_integer_input():
    fibo = Fibonacci()
    with pytest.raises(ValueError):
        fibo(0.5)


def test_string_input():
    fibo = Fibonacci()
    with pytest.raises(ValueError):
        fibo("a string")


def test_fibonacci_caching():
    """Test caching of Fibonacci numbers."""
    fibo = Fibonacci()
    assert fibo(5) == fibo(5)  # Should return cached value


def test_fibonacci_large_numbers():
    """Test Fibonacci for larger numbers."""
    fibo = Fibonacci()
    assert fibo(45) == 1134903170
