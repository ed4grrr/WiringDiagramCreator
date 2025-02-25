import enum

class PinEnum(enum.Enum):
    """
    Enum for the different types of pins on components

    """
    GROUND = 1 # Ground Pin of a component
    V3_3 = 2 # 3.3V Pin of a component
    V5 = 3 # 5V Pin of a component
    VOTHER = 4 # Other Voltage Pin of a component 
    INPUT = 5 # Input Pin of a component, like getting a user's input from a button connected to a GPIO pin (the output of the button!)
    OUTPUT = 6 # Output Pin of a component, like powering a an LED from a GPIO pin (the input being the anode of the LED)
    PASSIVE = 7 # Passive Pin of a component, like a resistor or capacitor
    def __str__(self):
        return self.name

