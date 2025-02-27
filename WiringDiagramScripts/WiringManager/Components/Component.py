from abc import ABC, abstractmethod
import json
from PIL import Image, UnidentifiedImageError
from Coordinates import Coordinates
from math import radians, cos, sin

class Component(ABC):
    """
    Abstract base class to represent a component.
    """

    def __init__(self, componentLabel: str, imagePath: str, electricalValuesDict: dict[str, dict[str, any]], pinsLMRMCoordinates: dict[int, dict[str,Coordinates]], isPowered: bool = False):
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
        
        self.pinLMRMCoordinates = pinsLMRMCoordinates # a dictionary of key int (representing physical pin number) and value tuple of (int, int) (representing the center of the pin). The tuple can be placed anywhere vertically on the pin but MUST be centered horizontally. The tuple represents the highest point the wire can be connected to the pin. This can be adjusted for aesthetic purposes.
        self.imageDimensions = self.getImageDimensions() # dimensions of the image file's contents in pixels to be used for placing the component on the canvas
        self.isPowered = isPowered # a boolean to indicate if the component is powered from something other than a GPIO Pin, like a power pin on the Pi or an external power source. This means another wire for the power source is needed for the wiring diagram.

    def __str__(self):
        return f"Component: {self.Label}\nImage Path: {self.imagePath}\nElectrical Values: {self.electricalValuesDict}\nPin Coordinates: {self.pinLMRMCoordinates}\nImage Dimensions: {self.imageDimensions}\nIs Powered: {self.isPowered}"

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

# Example of a concrete class inheriting from Component
class LED(Component):
    def getImageDimensions(self):
        # Implement logic to get image dimensions
        return (800, 1200)  # Example dimensions

    def getPinRectangles(self):
        # Implement logic to get pin rectangles
        return {
            "Ground": ((10, 10), (20, 20)),
            "Anode": ((30, 30), (40, 40))
        }
    


# Example usage
if __name__ == "__main__":
    pass