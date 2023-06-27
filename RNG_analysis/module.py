import numpy as np

from RNG_analysis.validation import *
from RNG_analysis.categorizer import *


def generate_random_numbers(n):
    if validate_positive_integer(n):
        # generate n random numbers
        return np.random.random(n)

def main():
    # main function to interact with module
    n = int(input("Enter the number of random numbers to generate: "))
    random_numbers = generate_random_numbers(n)
    print(f"Generated {n} random numbers: {random_numbers}")

if __name__ == "__main__":
    main()
