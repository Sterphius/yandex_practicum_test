from delivery.enums import Size, LoadMultiplier
from delivery.validators import validate_distance, validate_fragility, validate_enum_value


def calculate_distance_cost(distance, fragile=False):
    distance = validate_distance(distance)
    validate_fragility(fragile)

    match distance:
        case d if d > 30:
            if fragile:
                raise ValueError("Fragile items cannot be delivered for distances over 30 km.")
            return 300
        case d if 10 < d <= 30:
            return 200
        case d if 2 < d <= 10:
            return 100
        # TODO: Need to discuss with the team about minimum delivery distance
        case d if 0.002 <= d <= 2:
            return 50
        case _:
            raise ValueError(f"Item cannot be delivered to distance {d}")


def calculate_size_cost(size):
    size = validate_enum_value(size, Size)

    match size:
        case Size.BIG:
            return 200
        case Size.SMALL:
            return 100


def calculate_fragility_cost(fragile):
    validate_fragility(fragile)
    return 300 if fragile else 0


def calculate_load_multiplier(load_level):
    # TODO: Need to discuss with the team about adding new load_multipliers
    # Currently extreme level could return 1 too, but it's not fair
    if isinstance(load_level, LoadMultiplier):
        return load_level.value
    return 1


def calculate_delivery_cost(distance, size, fragile, load_level):
    """
    Calculate the delivery cost based on distance, size, fragility, and load level.

    :param distance: Distance to destination
    :param size: Size of the package
    :param fragile: Whether the package is fragile
    :param load_level: Load level of the service
    :return: Final delivery cost
    """
    cost = calculate_distance_cost(distance, fragile)
    cost += calculate_size_cost(size)
    cost += calculate_fragility_cost(fragile)

    multiplier = calculate_load_multiplier(load_level)
    cost *= multiplier

    return max(cost, 400)
