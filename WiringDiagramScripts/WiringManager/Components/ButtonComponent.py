import Component
import Coordinates
class ButtonComponent(Component):
    def __init__(self, name):
        self.imagePath = "./Images/BasicButton.png"
        self.Label = name + " Basic Button"
        self.electricalValuesDict = {"Voltage Input": [3.3, 5]}
        
        self.pinLMRMCoordinates = {1: {"Usage":"GPIO Signal In","LM":Coordinates("LM GPIO Signal In",90, 300), "RM":Coordinates("LM GPIO Signal In",111, 360)}, 2: {"Usage":"Ground","LM":Coordinates("Ground Pin",255, 300),"RM": Coordinates(278, 360)}} # (left most, rightmost) based on the width of the pin in the image in pixels.