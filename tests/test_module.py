# tests/test_module.py
import pytest
from RNG_analysis import validation
import numpy as np
from RNG_analysis.module import generate_random_numbers


def test_generate_random_numbers():
    n = 10
    random_numbers = generate_random_numbers(n)

    # Test that the function returns a numpy array
    assert isinstance(random_numbers, np.ndarray)

    # Test that the length of the array is correct
    assert len(random_numbers) == n

    # Test that all numbers are between 0 and 1
    assert np.all((random_numbers >= 0) & (random_numbers < 1))

def test_validate_positive_integer():
    validation.validate_positive_integer(10)  # Should not raise an exception

    with pytest.raises(ValueError):
        validation.validate_positive_integer(-1)
    with pytest.raises(ValueError):
        validation.validate_positive_integer(0)
    with pytest.raises(ValueError):
        validation.validate_positive_integer(1.5)
    with pytest.raises(ValueError):
        validation.validate_positive_integer("10")

def test_validate_range():
    validation.validate_range(0, 10)  # Should not raise an exception

    with pytest.raises(ValueError):
        validation.validate_range(10, 0)
    with pytest.raises(ValueError):
        validation.validate_range(10, 10)
    with pytest.raises(ValueError):
        validation.validate_range("0", 10)
    with pytest.raises(ValueError):
        validation.validate_range(0, "10")

def test_validate_distribution_type():
    validation.validate_distribution_type('uniform')  # Should not raise an exception

    with pytest.raises(ValueError):
        validation.validate_distribution_type('unknown')
    with pytest.raises(ValueError):
        validation.validate_distribution_type(123)
