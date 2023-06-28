import numpy as np

from RNG_analysis.validation import *
from RNG_analysis.categorizer import *

def get_num_of_zones():
    return int(input("Enter the number of zones: "))

def generate_random_numbers(n):
    if validate_positive_integer(n):
        # generate n random numbers
        return np.random.random(n)

def generate_random_numbers_given_range(n, min_value, max_value):
    if validate_range(min_value, max_value):
        # generate n random numbers within range
        return np.random.uniform(min_value, max_value, n)

def main():
    # main function to interact with module
    n = int(input("Enter the number of random numbers to generate: "))
    random_numbers = generate_random_numbers(n)
    num_of_zones = get_num_of_zones()
    zone_range = define_zones_range(num_of_zones, random_numbers.size)
    print(f"Generated {n} random numbers: {random_numbers}")

if __name__ == "__main__":
    main()
