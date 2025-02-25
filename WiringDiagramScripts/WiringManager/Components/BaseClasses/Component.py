from abc import ABC, abstractmethod
import json
from PIL import Image, UnidentifiedImageError
from Components.Coordinates import Coordinates
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
        
        self.pinsLMRMCoordinates = pinsLMRMCoordinates # a dictionary of key int (representing physical pin number) and value tuple of (int, int) (representing the center of the pin). The tuple can be placed anywhere vertically on the pin but MUST be centered horizontally. The tuple represents the highest point the wire can be connected to the pin. This can be adjusted for aesthetic purposes.
        self.imageDimensions = self.getImageDimensions() # dimensions of the image file's contents in pixels to be used for placing the component on the canvas
        self.isPowered = isPowered # a boolean to indicate if the component is powered from something other than a GPIO Pin, like a power pin on the Pi or an external power source. This means another wire for the power source is needed for the wiring diagram.

    def returnPinLabel(self, pinNumber:int):
        """
        Returns the label of the pin based on the pin number.
        Args:
            pinNumber (int): The number of the pin.
        Returns:
            str: The label of the pin.
        """
        return f"{self.Label}'s {self.pinsLMRMCoordinates[pinNumber]["Usage"]} Pin {pinNumber}"


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
    led = LED(
        componentLabel="LED",
        imagePath="led.png",
        electricalValuesDict={"Voltage": {"min": 1.8, "max": 2.2}},
        pinsUsageDictionary={
            1: {"Name": "Ground", "endpointCoords": (10, 10)},
            2: {"Name": "Anode", "endpointCoords": (30, 30)}
        }
    )
    print(led.getComponentType())
    print(led.getImageDimensions())
    print(led.getPinRectangles())