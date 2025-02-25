import WiringDiagramScripts.WiringManager.Components.BaseClasses.Component as Component
import Coordinates
from Utilities.PinEnum import *

class LEDComponent(Component):
    def __init__(self, name:str, controllerInputGPIO:int):
        self.imagePath = "./Images/BasicLED.png"
        self.Label = name + " Basic LED"
        self.controllerInputGPIO = controllerInputGPIO
        self.electricalValuesDict = {"Voltage Input": [3.3, 5], "Current": 0.02, "Resistance": 120} # TODO add a "Required Components" key and a list of required components to be wired in for safe operation

        GROUND = PinEnum.GROUND
        OUTPUT = PinEnum.OUTPUT
        self.pinLMRMCoordinates = {
            1: {
                "Usage":GROUND,
                "LM": Coordinates("LM Ground",126, 309),
                "RM": Coordinates("RM Ground",146, 356)
                },

            2: {
                "Usage":OUTPUT,
                "PinDestination": self.controllerInputGPIO,
                "LM": Coordinates("LM INPUT",217, 309),
                "RM": Coordinates("RM INPUT",232, 413)
                }
            } # (left most, rightmost) based on the width of the pin in the image in pixels.
        
        
        
        
        



