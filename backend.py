class SmartPlug:
    def __init__(self, consumptionRate):
        self.switchedOn = False
        self.setConsumptionRate(consumptionRate)

    def setConsumptionRate(self, rate):
        if 0 <= rate <= 150:
            self.consumptionRate = rate
        else:
            print("Consumption rate out of range. Should be within the range of 0 to 150.")

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getConsumptionRate(self):
        return self.consumptionRate

    def getSwitchStatus(self):
        return "On" if self.switchedOn else "Off"

    def __str__(self):
        return f"SmartPlug Status: {self.getSwitchStatus()}, Consumption Rate: {self.getConsumptionRate()}"

class SmartDoor:
    def __init__(self, option):
        self.switchedOn = True
        self.setOption(option)

    def setOption(self, option):
        if option in (True, False):
            self.switchedOn = option
        else:
            print("Invalid option. The smart door can either be locked or unlocked (True or False).")

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getOption(self):
        return self.switchedOn

    def __str__(self):
        status = "On" if self.switchedOn else "Off"
        doorKey = "Locked" if self.switchedOn else "Unlocked"
        return f"SmartDoor Switch Status: {status}, Door Status: {doorKey}"

class SmartHome:
    def __init__(self):
        self.devices = []

    def addDevice(self, device):
        self.devices.append(device)

    def getAllDevices(self):
        return self.devices

    def getDevice(self, index):
        if 0 <= index < len(self.devices):
            return self.devices[index]
        else:
            print("Invalid index.")
            return None

    def getNumDevices(self):
        return len(self.devices)

    def deleteDevice(self, index):
        if 0 <= index < len(self.devices):
            del self.devices[index]
            print(f"Device at index {index} deleted.")
        else:
            print("Invalid index. Cannot delete device.")

    def toggleDevice(self, index):
        device = self.getDevice(index)
        if device:
            try:
                device.toggleSwitch()
            except AttributeError:
                print("Device does not support toggling.")
        else:
            print("Device not found or index invalid.")

    def toggleAllDevices(self):
        for device in self.devices:
            try:
                device.switchedOn = not device.switchedOn
            except AttributeError:
                print("Device does not support toggling.")

    def turnOnAllDevices(self):
        for device in self.devices:
            try:
                device.switchedOn = True
            except AttributeError:
                print("Device does not support turning on.")

    def turnOffAllDevices(self):
        for device in self.devices:
            try:
                device.switchedOn = False
            except AttributeError:
                print("Device does not support turning off.")

    def __str__(self):
        deviceInfo = "\n".join([f"{i+1}. {device}" for i, device in enumerate(self.devices)])
        return f"SmartHome Devices:\n{deviceInfo}"


def testHome():
    home = SmartHome()

    plugOne = SmartPlug(45)
    plugTwo = SmartPlug(45)

    smartDoor = SmartDoor(False)

    plugOne.toggleSwitch()
    plugOne.consumptionRate = 150

    plugTwo.consumptionRate = 25

    smartDoor.setOption(False)

    home.addDevice(plugOne)
    home.addDevice(plugTwo)
    home.addDevice(smartDoor)

    home.toggleDevice(1)

    print("Smart home before turning on all devices:")
    print(home)

    home.turnOnAllDevices()

    # Print the smart home object again
    print("\nSmart home after turning on all devices:")
    print(home)

    home.deleteDevice(0)

    print("\nSmart home after removing the first device:")
    print(home)


def testSmartPlug():
    plug = SmartPlug(45)

    plug.toggleSwitch()
    print("Switched On:", plug.getSwitchStatus())
    print("Consumption Rate:", plug.getConsumptionRate())

    plug.setConsumptionRate(80)
    print("New Consumption Rate:", plug.getConsumptionRate())

    print(plug)

def testDevice():
    device = SmartDoor(True)
    device.toggleSwitch()

    print("Switched On:", device.getOption())
    print("Current Option Value:", device.getOption())

    device.setOption(True)

    print("New Option Value:", device.getOption())

    print(device)
