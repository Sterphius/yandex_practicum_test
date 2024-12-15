from enum import Enum


class Size(Enum):
    BIG = 'big'
    SMALL = 'small'


class LoadLevel(Enum):
    VERY_HIGH = 'very high'
    HIGH = 'high'
    INCREASED = 'increased'
    NORMAL = 'normal'


class LoadMultiplier(Enum):
    VERY_HIGH = 1.6
    HIGH = 1.4
    INCREASED = 1.2
    NORMAL = 1.0
