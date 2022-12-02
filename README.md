# ProjectBreakdown_HVAC

## Enhance the HVAC

Right now in our little world we have a Room, which is the space whose temperature we want to control and HVAC which is the machine we use to control it. A real HVAC system takes in air from the controlled space, heats or cools it and puts it back. In order to do that, we need a fan to pull in the air and force it back out. We will also need a cooler -- for now it will be a cooling coil, and a heater -- which will be a heating coil.
Let's create a new file `fans.py` with the following:
```
class Fan:
    def __init__(self):
        self.status = "Off"
```
Let's create a new file `coolers.py` with the following:
```
class CoolingCoil:
    def __init__(self):
        self.status = "Off"
```
Let's create a new file `heaters.py` with the following:
```
class HeatingCoil:
    def __init__(self):
        self.status = "Off"
```
Now we have to bring these new items into `hvac.py` At the top of the file add
```
from fans import Fan
from coolers import CoolingCoil
from heaters import HeatingCoil
```
Inside the `__init__` method add the following between `self.mode` and declaration of the setpoints
```
self.fan = Fan()
self.cooler = CoolingCoil()
self.heater = HeatingCoil()
```
## Testing

At this point it is important start testing our application. Specifically, we want to make testing easy to create and run. We need to create tests that are meaningful. There are different testing frameworks available for python. Here, we will be using pytest. First, we need to include it in our environment. At the command line, run `pip install pytest`.