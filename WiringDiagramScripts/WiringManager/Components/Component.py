from abc import ABC, abstractmethod
import json
from PIL import Image, UnidentifiedImageError
from Coordinates import Coordinates
from math import radians, cos, sin
from Utilities.DirectionEnum import *

from Wire import WireLines
class Component(ABC):
    """
    Abstract base class to represent a component.
    """

    def __init__(self, componentLabel: str, imagePath: str, electricalValuesDict: dict[str, dict[str, any]], pinLMRMCoordinates: dict[int, dict[str,Coordinates]], isPowered: bool = False, controllerKey: int = None):
        """
        Initializes a new Component object

        The pins should be 1-indexed, with 1 being the first pin of the component on the bottom left corner and increasing in a clockwise direction. This is to match the convention of the pin numbers on the physical Pi's Physical Pin Numbers.

        Args:
            componentLabel (str): The name of the component, to be used as a label.
            
            imagePath (str): The path to the image file of the component.
            
            electricalValuesDict (dict): A dictionary of electrical measurements and their rated values.
            
        
            pinsLMRMCoordinates (dict): A dictionary of key int (representing physical pin number of the component) and value is a dict with the following key and a description of its value:

                "Usage": A string representing the usage of the pin. This can be "Ground", "Power", "Input", "Output", "Signal", etc.
                
                "LM": A Coordinates object representing the leftmost point of the pin. This is the highest point where the wire will be connected to the pin. This can be adjust for aesthetic purposes.

                "RM": A Coordinates object representing the rightmost point of the pin. This is where the lowest point where the wire will be connected to the pin. Assure that the RM is to the right of the LM. This can be adjust for aesthetic purposes. Make sure to make this value as the absolute rightmost point of the pin. This is to ensure that the wire is connected in a visually appealing way.

            isPowered (bool): A boolean to indicate if the component is powered from a power pin on the Pi or an external power source.
        """
        self.Label = componentLabel # label for the component
        self.imagePath = imagePath  # path to image file of the component
        self.electricalValuesDict = electricalValuesDict # a dictionary of electrical measurements relevant to the component and their rated values
        
        self.pinLMRMCoordinates = pinLMRMCoordinates # a dictionary of key int (representing physical pin number) and value tuple of (int, int) (representing the center of the pin). The tuple can be placed anywhere vertically on the pin but MUST be centered horizontally. The tuple represents the highest point the wire can be connected to the pin. This can be adjusted for aesthetic purposes.
        self.imageDimensions = self.getImageDimensions() # dimensions of the image file's contents in pixels to be used for placing the component on the canvas
        self.isPowered = isPowered # a boolean to indicate if the component is powered from something other than a GPIO Pin, like a power pin on the Pi or an external power source. This means another wire for the power source is needed for the wiring diagram.
        self.controllerKey = controllerKey # a key to identify the controller that the component is connected to. This is used to identify the controller that the component is connected to in the wiring diagram.

        self.wires = {} # a dictionary of wires that are connected to the component. The key is an int and the value is the wire object.

    def __str__(self):
        return f"Component: {self.Label}\nImage Path: {self.imagePath}\nElectrical Values: {self.electricalValuesDict}\nPin Coordinates: {self.pinLMRMCoordinates}\nImage Dimensions: {self.imageDimensions}\nIs Powered: {self.isPowered}"
    
    def addWire(self, wire: WireLines, pinDestinationNumber: int):
        """
        Adds a wire to the component.
        Args:
            wire (Wire): The wire to add to the component.
        """
        self.wires[pinDestinationNumber] = wire

    def returnPinLabel(self, pinNumber:int):
        """
        Returns the label of the pin based on the pin number.
        Args:
            pinNumber (int): The number of the pin.
        Returns:
            str: The label of the pin.
        """
        return f"{self.Label}'s {self.pinLMRMCoordinates[pinNumber]["Usage"]} Pin {pinNumber}"


    def adjustCoordinatesAfterPlacement(self, topLeftCoordinates: tuple[int, int]):
        """
        given the top left pixel of where the component will be placed on the canvas, adjust the coordinates of the pins to match the placement of the component on the canvas

        This will require adjusting all the coordinates of the pins to match the new placement of the component on the canvas.
        
        Args:
        
            xPlacement (int): The x-coordinate of the top left corner of the component on the canvas.
            yPlacement (int): The y-coordinate of the top left corner of the component on the canvas.


        """

        xPlacement, yPlacement = topLeftCoordinates

        for values in self.pinLMRMCoordinates.values():
            for value in values.values():
                if isinstance(value, Coordinates):
                    value.x += xPlacement
                    value.y += yPlacement

    def printCoordinates(self):
        for values in self.pinLMRMCoordinates.values():
            for value in values.values():
                if isinstance(value, Coordinates):
                    print(f"({value.x}, {value.y})")
    
    def adjustCoordinatesAfterScaling(self, xDestinationResolution: int, yDestinationResolution: int):
        """
        Adjusts the coordinates of the pins of the component after the image has been scaled to a new resolution.
        
        Args:
        
            xDestinationResolution (int): The new x-resolution.
            yDestinationResolution (int): The new y-resolution.


        """
        for values in self.pinLMRMCoordinates.values():
            for value in values.values():
                if isinstance(value, Coordinates):
                    xResolution, yResolution = self.getImageDimensions()

                    # use old and new resolution to create a ratio to scale the coordinates
                    value.x = int(value.x * xDestinationResolution / xResolution)
                    value.y = int(value.y * yDestinationResolution / yResolution)
                    # I HAVE ABSOLUTELY NO IDEA IF THIS WILL WORK. I'M JUST GUESSING.

    def adjustCoordinatesAfterRotation(self, rotation: int):

        def rotate_point(x, y, angle):
            rad = radians(angle)
            new_x = x * cos(rad) - y * sin(rad)
            new_y = x * sin(rad) + y * cos(rad)
            return new_x, new_y


        for values in self.pinLMRMCoordinates.values():
            for info in values.values():
                if isinstance(info, Coordinates):
                    info.x, info.y = rotate_point(info.x, info.y, rotation)

    def getImageDimensions(self):
        """
        Abstract method to get the dimensions of the component's image file.
        Returns:
            tuple: The width and height of the image file in pixels.
        """
        
        try:
            with Image.open(self.imagePath) as img:
                return img.size
        except FileNotFoundError:
            raise ValueError(f"Image file not found at path: {self.imagePath}")
        except IOError:
            raise ValueError(f"Error occurred while opening the image file at path: {self.imagePath}")
        except UnidentifiedImageError:
            raise ValueError(f"Image file at path: {self.imagePath} is not a valid image file")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred while getting image dimensions: {e}")
        
       

    


    def getComponentType(self):
        """
        Returns the type of the component.
        Returns:
            str: The type of the component.
        """
        return self.Label

    def getElectricalValuesDict(self):
        """
        Returns the electrical values of the component.
        Returns:
            dict: The electrical values of the component.
        """
        return self.electricalValuesDict



    def saveAsJSON(self, outputPath: str):
        """
        Saves the component to a JSON file.
        Args:
            outputPath (str): The path to save the component file.
        """
        try:
            with open(outputPath, 'w') as f:
                json.dump(self.__dict__, f)
        except Exception as e:
            raise ValueError(f"An error occurred while saving the component. Error: {e}")

    def adjustCoordinates(self, original_size, new_size, rotation_angle, new_position):
        """
        Adjusts the coordinates of the pins due to resizing, rotation, and new position.

        :param original_size: The original size of the image (width, height).
        :param new_size: The new size of the image (width, height).
        :param rotation_angle: The rotation angle in degrees.
        :param new_position: The new position of the top-left corner of the image (x, y).
        """


        # Adjust for rotation
        # account for only 90, 180, 270 degrees
        
        if rotation_angle == 90:
            for values in self.pinLMRMCoordinates.values():
                for value in values.values():
                    if isinstance(value, Coordinates):
                        value.x, value.y = value.y, value.x
        elif rotation_angle == 180:
            for values in self.pinLMRMCoordinates.values():
                for value in values.values():
                    if isinstance(value, Coordinates):
                        value.x, value.y = -value.x, -value.y
        elif rotation_angle == 270:
            for values in self.pinLMRMCoordinates.values():
                for value in values.values():
                    if isinstance(value, Coordinates):
                        value.x, value.y = -value.y, value.x
        elif rotation_angle == 0:
            pass
        else:
            raise ValueError("Invalid rotation angle. Only 0, 90, 180, and 270 degrees are supported.")
        self._determinePinLocationAfterRotation(rotation_angle)

                
        # Adjust for resizing
        scale_x = new_size[0] / original_size[0]
        scale_y = new_size[1] / original_size[1]
        #print(f"scale_x: {scale_x}, scale_y: {scale_y}")
        for values in self.pinLMRMCoordinates.values():
            for value in values.values():
                if isinstance(value, Coordinates):
                    value.x *= scale_x
                    #print(f"new x: {value.x}")
                    value.y *= scale_y
                    #print(f"new y: {value.y}")
        
        #print(f"Adjusting for new position")
        # Adjust for new position
        for values in self.pinLMRMCoordinates.values():
            for value in values.values():
                if isinstance(value, Coordinates):
                    value.x += new_position[0]
                   # print(f"new x: {value.x}")
                    value.y += new_position[1]
                  #  print(f"new y: {value.y}")


    def _determinePinLocationAfterRotation(self, rotationAngle):
        """
        changes the Direction enum that represent what side fo the component that pin is on (relative to the component's original image) based on the rotation of the component's original image.
        Args:
            rotationAngle (int): The angle of rotation in degrees.
        """

        for key1,values in self.pinLMRMCoordinates.items():
               # print(f"FIRST SEARCH ME {key1}\n{values}")
                for key2,value in values.items():
                    
                    if isinstance(value, DirectionEnum):
                       # print(f"SECOND SEARCH ME {key2}\n{value.value}\nrotation {rotationAngle}")
                        self.pinLMRMCoordinates[key1][key2] = self._determineNewDirection(value, rotationAngle)
                       # print(f"DID I CHANGE? {key1} {key2}\n{self.pinLMRMCoordinates[key1][key2].value}")


    @staticmethod                    
    def _determinePinCenter(pinLM, pinRM):
        """
        Determines the center of the pin based on the leftmost and rightmost points of the pin.
        Args:
            pinLM (Coordinates): The leftmost point of the pin.
        """
        return Coordinates("PinCenter",(pinLM.x + pinRM.x) / 2, (pinLM.y + pinRM.y) / 2)

    def _determineNewDirection(self, currentDirection, rotationAngle):
        """
        changes the Direction enum that represent what side fo the component that pin is on (relative to the component's original image) based on the rotation of the component's original image.
        Args:
            currentDirection (DirectionEnum): The current direction of the pin.
            rotationAngle (int): The angle of rotation in degrees.
        Returns:
            DirectionEnum: The new direction of the pin.
        """
        if rotationAngle == 270:
            if currentDirection == UP:
                return RIGHT
            elif currentDirection == RIGHT:
                return DOWN
            elif currentDirection == DOWN:
                return LEFT
            elif currentDirection == LEFT:
                return UP
        elif rotationAngle == 180:
            if currentDirection == UP:
                return DOWN
            elif currentDirection == RIGHT:
                return LEFT
            elif currentDirection == DOWN:
                return UP
            elif currentDirection == LEFT:
                return RIGHT
        elif rotationAngle == 90:
            if currentDirection == UP:
                return LEFT
            elif currentDirection == RIGHT:
                return UP
            elif currentDirection == DOWN:
                return RIGHT
            elif currentDirection == LEFT:
                return DOWN
        elif rotationAngle == 0:
            return currentDirection
        else:
            raise ValueError("Invalid rotation angle. Only 0, 90, 180, and 270 degrees are supported.")


# Example usage
if __name__ == "__main__":
    pass