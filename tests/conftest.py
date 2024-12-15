import pytest

from delivery.enums import LoadMultiplier, Size


@pytest.fixture
def pairwise_test_data():
    return [
        (1, Size.SMALL, False, LoadMultiplier.NORMAL, 400),
        # Минимальная дистанция, маленький размер, не хрупкий, нормальная загруженность
        (8, Size.BIG, True, LoadMultiplier.INCREASED, 720),
        # Средняя дистанция, большой размер, хрупкий, повышенная загруженность
        (25, Size.SMALL, True, LoadMultiplier.HIGH, 840),
        # Дальняя дистанция, маленький размер, хрупкий, высокая загруженность
        (35, Size.BIG, False, LoadMultiplier.VERY_HIGH, 800),
        # Очень дальняя дистанция, большой размер, не хрупкий, очень высокая загруженность
        (10, Size.SMALL, False, LoadMultiplier.HIGH, 400),
        # Граничная дистанция, маленький размер, не хрупкий, высокая загруженность
        (30, Size.BIG, True, LoadMultiplier.NORMAL, 700),
        # Граничная дальность, большой размер, хрупкий груз, нормальная загруженность
        (5, Size.SMALL, True, LoadMultiplier.INCREASED, 600),
        # Ближняя дистанция, маленький размер, хрупкий груз, повышенная загруженность
        (15, Size.BIG, False, LoadMultiplier.VERY_HIGH, 640),
        # Средняя дистанция, большой размер, не хрупкий груз, очень высокая загруженность
    ]
