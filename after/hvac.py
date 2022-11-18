from enum import Enum 

class SystemMode(Enum):
    OFF = "off"
    COOLING = "cooling"
    HEATING = "heating"


class Hvac:
    def __init__(self):
        self.mode = SystemMode.OFF
        self.cooling_setpoint = 74
        self.heating_setpoint = 70