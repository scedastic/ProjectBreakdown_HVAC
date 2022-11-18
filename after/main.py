from hvac import Hvac, SystemMode
from room import Room

def main():
    bms = Hvac()
    bedroom = Room(45)

    if bedroom.temp < 65:
        bms.mode = SystemMode.HEATING
    elif bms.temp > 75:
        bms.mode = SystemMode.COOLING

    print(f"The room is currently {bedroom.temp} so the machine will be put into {bms.mode}")

main()