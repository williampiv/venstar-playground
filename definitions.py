from enum import Enum

class FanMode(Enum):
    AUTO = 0
    ON = 1

class Modes(Enum):
    OFF =  0
    HEAT = 1
    COOL = 2
    AUTO = 3

class Schedule(Enum):
    DISABLED = 0
    ENABLED = 1
