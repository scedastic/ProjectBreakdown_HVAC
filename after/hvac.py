from enum import Enum 
from fans import Fan
from coolers import CoolingCoil
from heaters import HeatingCoil

class SystemMode(Enum):
    OFF = "off"
    COOLING = "cooling"
    HEATING = "heating"


class Hvac:
    def __init__(self):
        self.mode = SystemMode.OFF
        self.fan = Fan()
        self.cooler = CoolingCoil()
        self.heater = HeatingCoil()
        self.cooling_setpoint = 74
        self.heating_setpoint = 70