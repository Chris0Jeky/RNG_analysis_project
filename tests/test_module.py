# tests/test_module.py

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

