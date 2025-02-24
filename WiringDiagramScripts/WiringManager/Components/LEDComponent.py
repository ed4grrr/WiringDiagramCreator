import Component
import Coordinates

class LEDComponent(Component):
    def __init__(self, name):
        self.imagePath = "./Images/BasicLED.png"
        self.Label = name + " Basic LED"
        self.electricalValuesDict = {"Voltage Input": [3.3, 5], "Current": 0.02, "Resistance": 120} # TODO add a "Required Components" key and a list of required components to be wired in for safe operation

        self.pinLMRMCoordinates = {1: {"Usage":"Cathode (-)","LM":Coordinates("LM Cathode",126, 309), "RM":Coordinates("RM Cathode",146, 356)}, 2: {"Usage":"Anode (+)","LM":Coordinates("LM Anode",217, 309),"RM": Coordinates("RM Anode",232, 413)}} # (left most, rightmost) based on the width of the pin in the image in pixels.
        
        
        
        
        



