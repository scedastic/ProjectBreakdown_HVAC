# ProjectBreakdown_HVAC

### An attempt to describe work breakdown using a situation of an HVAC system regulating a "space."

### Prerequisite:
- Basic programming knowledge.
- Object Oriented Programming concepts.

We will start off with the following situation. We have a "space" which for now we will assume is a room. We would like to control the temperature of this room. For that we have a machine that can measure the room's temperature and heat it up or cool it down to the desired temperature. I am sure you are eager to start coding so let's do just that. Before writing code let's examine what we have:
- The Room - an object
- Room Temperature - property of the room
- Machine that heats or cools the room (HVAC system) - object
- Cooling Setpoint - the temperature the machine will try to have the room reach when in cooling mode
- Heating Setpoint - the temperature the machine will try to have the room reach when in heating mode

Set up your project environment to your liking.

Create `room.py` with the following code:
```
class Room:
  def __init__(self, temp):
    self.temp = temp
```

Now we will create the HVAC class in `hvac.py`. For safety reasons we will add an enumeration for the HVAC machine to indicate whether it is cooling, heating or off. The rest of this tutorial will revolve around this object and breaking it down to subcomponents. For now it will just be one single class.
```
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
```
The reason the cooling setpoint is set to 74 and the heating setpoint is 70 is because that's what I read in an ASHRAE book.
