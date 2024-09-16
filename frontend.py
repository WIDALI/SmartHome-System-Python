from tkinter import *
from backend import SmartPlug, SmartDoor, SmartHome


class SmartHomeSystem:
    def __init__(self, smartPlug, smartDoor, smartHome):
        self.win = Tk()
        self.smartPlug = smartPlug
        self.smartDoor = smartDoor
        self.smartHome = smartHome
        self.win.title("Smart Home System")
        self.win.geometry("600x300")
        self.mainFrame = Frame(self.win)
        self.mainFrame.pack(padx=10, pady=10)

    def callTurnOnAll(self):
        self.smartHome.turnOnAllDevices()

    def callTurnOffAll(self):
        self.smartHome.turnOffAllDevices()

    def callDelete(self, index):
        self.smartHome.deleteDevice(index)
        self.removeDeviceWidgets(index)

    def removeDeviceWidgets(self, index):
        for widget in self.mainFrame.grid_slaves():
            if int(widget.grid_info()["row"]) == index + 1:
                widget.grid_remove()

    def addNewDevice(self):
        deviceType = input("Enter device type (SmartPlug or SmartDoor): ").lower()
        validConsumption = list(range(151))
        if deviceType == "smartplug":
            consumptionRate = float(input("Enter consumption rate for the SmartPlug: "))
            while consumptionRate not in validConsumption:
                print("Try again. Value outside of range.")
                consumptionRate = float(input("Enter consumption rate for the SmartPlug: "))
            self.smartHome.addDevice(SmartPlug(consumptionRate))
        elif deviceType == "smartdoor":
            locked = input("Is the door locked (True or False): ").lower() == "true"
            self.smartHome.addDevice(SmartDoor(locked))
        else:
            print("Invalid device type. Please enter 'SmartPlug' or 'SmartDoor'.")

    def createWidgets(self):
        btnTurnOnAll = Button(
            self.mainFrame,
            text="Turn ON All",
            command=self.callTurnOnAll
        )
        btnTurnOnAll.grid(
            row=0,
            column=0,
        )

        btnTurnOffAll = Button(
            self.mainFrame,
            text="Turn OFF All",
            width=15,
            command=self.callTurnOffAll
        )

        btnTurnOffAll.grid(
            row=0,
            column=1,
            columnspan=2,
            padx=1,
            pady=5
        )

        numDevices = self.smartHome.getNumDevices()
        for i in range(numDevices):

            device = self.smartHome.getDevice(i)
            deviceLabel = Label(
                self.mainFrame,
                text=device
            )
            deviceLabel.grid(
                row=i + 1,
                column=0,
            )
            btnToggleDevice = Button(
                self.mainFrame,
                text="Toggle",
                command=lambda index=i: self.smartHome.toggleDevice(index)
            )
            btnToggleDevice.grid(
                row=i + 1,
                column=1,
                padx=1,
                pady=5
            )

            if isinstance(device, SmartPlug):
                btnEditDevice = Button(
                    self.mainFrame,
                    text="Edit",
                    command=lambda index=i: self.editSmartPlug(index)
                )
                btnEditDevice.grid(
                    row=i + 1,
                    column=2,
                    padx=1,
                    pady=5,
                )
            elif isinstance(device, SmartDoor):
                btnEditDevice = Button(
                    self.mainFrame,
                    text="Edit",
                    command=lambda index=i: self.editSmartDoor(index)
                )
                btnEditDevice.grid(
                    row=i + 1,
                    column=2,
                    padx=1,
                    pady=5,
                )

            btnDeleteDevice = Button(
                self.mainFrame,
                text="Delete",
                command=lambda index=i: self.callDelete(index)
            )
            btnDeleteDevice.grid(
                row=i + 1,
                column=3,
                padx=5,
                pady=5,
            )

        addDevice = Button(
            self.mainFrame,
            text="Add Device",
            command=self.addNewDevice
        )
        addDevice.grid(
            row=numDevices + 1,
            column=0,
        )

    def editSmartPlug(self, index):
        device = self.smartHome.getDevice(index)
        if isinstance(device, SmartPlug):
            newRate = float(input("Enter new consumption rate: "))
            device.setConsumptionRate(newRate)
            deviceLabel = self.mainFrame.grid_slaves(row=index + 1, column=0)[0]
            deviceLabel.config(text=str(device))
        else:
            print("This device is not a SmartPlug.")

    def editSmartDoor(self, index):
        device = self.smartHome.getDevice(index)
        if isinstance(device, SmartDoor):
            while True:
                newOption = input("Is the door locked (True) or unlocked (False): ").lower()
                if newOption in ["locked", "true"]:
                    device.setOption(True)
                    break
                elif newOption in ["unlocked", "false"]:
                    device.setOption(False)
                    break
                else:
                    print("Invalid option. Please enter 'locked' or 'unlocked'.")
            deviceLabel = self.mainFrame.grid_slaves(row=index + 1, column=0)[0]
            deviceLabel.config(text=str(device))
        else:
            print("Invalid device index or device type.")

    def run(self):
        self.createWidgets()
        self.win.mainloop()


def setUpHome():
    myHome = SmartHome()

    myDevices = ['smartdoor', 'smartplug']
    validConsumption = list(range(151))

    print("Set up your smart home.")

    for i in range(5):
        deviceType = input(f"Enter device type for device {i + 1} (SmartPlug or SmartDoor): ").lower()
        while deviceType not in myDevices:
            print("Invalid device! Please enter either SmartPlug or SmartDoor")
            deviceType = input(f"Enter device type for device {i + 1} (SmartPlug or SmartDoor): ").lower()
        if deviceType == "smartplug":
            consumptionRate = float(input("Enter consumption rate for the SmartPlug: "))
            while consumptionRate not in validConsumption:
                print("Try again. Value outside of range.")
                consumptionRate = float(input("Enter consumption rate for the SmartPlug: "))
            myPlug = SmartPlug(consumptionRate)
            myHome.addDevice(myPlug)
        elif deviceType == "smartdoor":
            option = input("Is the door locked (True) or unlocked (False): ").lower()
            if option == "locked" or option == "true":
                myDoor = SmartDoor(True)
                myHome.addDevice(myDoor)
            elif option == "unlocked" or option == "false":
                myDoor = SmartDoor(False)
                myHome.addDevice(myDoor)
            else:
                option = input("Invalid option. Try again!\nIs the door locked (True) or unlocked (False):")

    else:
        print("Invalid device type. Please enter 'SmartPlug' or 'SmartDoor'.")

    print("\nSmart home setup completed!")
    print(myHome)

    system = SmartHomeSystem(myPlug, myDoor, myHome)
    system.run()


def main():
    setUpHome()


main()
