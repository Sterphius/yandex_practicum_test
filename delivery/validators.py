def validate_distance(distance):
    if not isinstance(distance, (int, float)) or distance < 0:
        raise ValueError("Distance must be a non-negative number.")
    return distance


def validate_fragility(fragile):
    if not isinstance(fragile, bool):
        raise ValueError("Fragile must be a boolean value.")
    return fragile


def validate_enum_value(value, enum_type):
    if not isinstance(value, enum_type):
        raise ValueError(f"Value must be a member of {enum_type.__name__}.")
    return value
