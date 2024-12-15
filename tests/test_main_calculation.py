from delivery.calculations import calculate_delivery_cost


def test_calculate_delivery_cost_pairwise(pairwise_test_data):
    for distance, size, fragile, load_level, expected in pairwise_test_data:
        assert calculate_delivery_cost(distance, size, fragile, load_level) == expected
