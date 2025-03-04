from Component import Component
from Coordinates import Coordinates
from Utilities.PinEnum import *
from Utilities.DirectionEnum import *
import os

class LEDComponent(Component):
    def __init__(self, name:str, controllerInputGPIO:int, controllerKey:int = 0):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "Images/BasicLED.png")
        self.imagePath = filename
        self.controllerKey = controllerKey   
        self.Label = name + " Basic LED"
        self.controllerInputGPIO = controllerInputGPIO
        self.electricalValuesDict = {"Voltage Input": [3.3, 5], "Current": 0.02, "Resistance": 120} # TODO add a "Required Components" key and a list of required components to be wired in for safe operation

        GROUND = PinEnum.GROUND
        OUTPUT = PinEnum.OUTPUT
        self.pinLMRMCoordinates = {
            1: {
                "Usage":GROUND,
                "LM": Coordinates("LM Ground",126, 309),
                "RM": Coordinates("RM Ground",146, 356),
                "PinDestination": GROUND,
                "PinLocation": DirectionEnum.DOWN
                },

            2: {
                "Usage":OUTPUT,
                "PinDestination": self.controllerInputGPIO,
                "LM": Coordinates("LM INPUT",217, 309),
                "RM": Coordinates("RM INPUT",232, 413)
                ,
                "PinDestination": self.controllerInputGPIO,
                "PinLocation": DirectionEnum.DOWN
                },
                
            } # (left most, rightmost) based on the width of the pin in the image in pixels.
        super().__init__(self.Label, self.imagePath, self.electricalValuesDict, self.pinLMRMCoordinates, isPowered=False, controllerKey=controllerKey)
        
        
        
        
        



