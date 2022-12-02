import pytest
from hvac import Hvac, SystemMode

def test_hvac_init_off():
    unit = Hvac()
    assert unit.mode == SystemMode.OFF

def test_hvac_init_fan_off():
    unit = Hvac()
    assert unit.fan.mode == SystemMode.OFF
