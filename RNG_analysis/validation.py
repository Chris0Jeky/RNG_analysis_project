def validate_positive_integer(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"Expected a positive integer, but received: {value}")
    else: return True

def validate_range(min_value, max_value):
    if not (isinstance(min_value, (int, float)) and isinstance(max_value, (int, float))):
        raise ValueError(f"Both min and max must be numbers, but received: {min_value} and max: {max_value}")
    if min_value >= max_value:
        raise ValueError(f"min must be greater than max, but received: {min_value} and max: {max_value}")

def validate_distribution_type(distribution_type):
    valid_distribution_types = ['uniform', 'normal', 'binomial']
    if distribution_type not in valid_distribution_types:
        raise ValueError(f"distribution type must be one of {valid_distribution_types}, but received: {distribution_type}")

