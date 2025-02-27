from Component import Component
from Coordinates import Coordinates
from Utilities.PinEnum import *
import os
from math import radians, cos, sin

class ButtonComponent(Component):
    def __init__(self, name:str, controllerInputGPIO:int):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "Images/BasicButton.png")
        self.imagePath = filename
        self.Label = name + " Basic Button"

        # the following is used to map the components made from the GUI 
        # portion of Exhibit Creator to the wiring diagram components to 
        # allow for a wiring diagram to be created
        self.controllerInputGPIO = controllerInputGPIO
        
        self.electricalValuesDict = {"Voltage Input": [3.3, 5]}

        self.pinLMRMCoordinates = {
            1: {
                "Usage": PinEnum.INPUT,
                "PinDestination": self.controllerInputGPIO,
                "LM": Coordinates("LM GPIO Signal In", 90, 300),
                "RM": Coordinates("LM GPIO Signal In", 111, 360),
            },
            2: {
                "Usage": PinEnum.GROUND,
                "LM": Coordinates("Ground Pin", 255, 300),
                "RM": Coordinates("Ground Pin",278, 360),
            },
        }  # (left most, rightmost) based on the width of the pin in the image in pixels.
        super().__init__(self.Label, self.imagePath, self.electricalValuesDict, self.pinLMRMCoordinates, False)


 
