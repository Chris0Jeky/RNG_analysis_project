import numpy as np

def generate_random_numbers(n):
    # generate n random numbers
    return np.random.random(n)

def main():
    # main function to interact with module
    n = int(input("Enter the number of random numbers to generate: "))
    random_numbers = generate_random_numbers(n)
    print(f"Generated {n} random numbers: {random_numbers}")

if __name__ == "__main__":
    main()
