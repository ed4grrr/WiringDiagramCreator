import WiringDiagramScripts.WiringManager.Components.Component as Component
import Coordinates
from Utilities.PinEnum import *


class ResistorComponent(Component):
    def __init__(self, name, resistanceValue: float):
        self.imagePath = "./Images/Resistor.png"
        self.Label = name + " Basic Resistor"
        self.electricalValuesDict = {"Resistance": resistanceValue}
        self.pinLMRMCoordinates = {
            1: {
                "Usage": PinEnum.PASSIVE,
                "LM": Coordinates("LM Pin 1", 30, 203),
                "RM": Coordinates("RM Pin 1", 61, 207),
            },
            2: {
                "Usage": PinEnum.PASSIVE,
                "LM": Coordinates("LM Pin 2", 287, 203),
                "RM": Coordinates("RM Pin 2", 317, 209),
            },
        }  # (left most, rightmost) based on the width of the pin in the image in pixels.
