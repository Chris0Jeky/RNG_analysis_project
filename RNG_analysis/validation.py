def validation_positive_integer(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"Expected a positive integer, but received: {value}")

def validate_range(min, max):
    if not (isinstance(min, (int, float)) and isinstance(max, (int, float))):
        raise ValueError(f"Both min and max must be numbers, but received: {min} and max: {max}")
    if min >= max:
        raise ValueError(f"min must be greater than max, but received: {min} and max: {max}")

def validate_distribution_type(distribution_type):
    valid_distribution_types = ['uniform', 'normal', 'binominal']
    if distribution_type not in valid_distribution_types:
        raise ValueError(f"distribution type must be one of {valid_distribution_types}, but received: {distribution_type}")

