import Component
import Coordinates

class ResistorComponent(Component):
    def __init__(self, name, resistanceValue:float):
        self.imagePath = "./Images/Resistor.png"
        self.Label = name + " Basic Resistor"
        self.electricalValuesDict = {"Resistance": resistanceValue}
        self.pinLMRMCoordinates = {1: {"Usage":"Pin 1","LM":Coordinates("LM Pin 1",30, 203), "RM":Coordinates("RM Pin 1",61, 207)}, 2:{"Usage":"Pin 2","LM":Coordinates("LM Pin 2",287, 203),"RM": Coordinates("RM Pin 2",317, 209)}} # (left most, rightmost) based on the width of the pin in the image in pixels.
        
        