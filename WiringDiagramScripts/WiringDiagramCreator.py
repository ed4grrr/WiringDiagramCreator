from PIL import Image, ImageDraw, ImageFont
from WiringDiagramScripts.ImageTweaker import ImageTweaker
from WiringDiagramScripts.Component import Component


class WiringDiagramCreator:
    def __init__(self):
        self.wiring_diagram = None
        self.components = []
        self.GPIOImagePath = "./images/GPIO.png"
        self.circuitImage = None
        self.circuitImageOutputPath = ""
        self.circuitImageSize = None


    def createWiringDiagram(self):
        """
        Creates a wiring diagram.
        """
        # must have the following data before creating the wiring diagram:
        # - dict containing three keys, "inputComponents",
        # "outputComponents", and "Controller Component" and the values are 
        # lists of components for Input and Output components and a single 
        # controller component (Raspberry Pi or other microComputer/
        # microController) respectively. The Input and Output components'   
        # argument can be None if there are no components of that type. 
        # However, the Controller Component must be present.
        # 
        #       - the Component objects will have all the data necessary to 
        #           allow for adding them to the wiring diagram. (Pins      
        #           (uses, its image, coordinates for wiring to that pin, 
        #           its center point, etc.), 
        # Assuming this data is present, the wiring diagram can be created.
        #

        # ************Step 1: Create the Basic Circuit Image****************

        # determine the size of the image based on the number of components 
        # and the size of the components' images 

        

        # create the blank image using the dimensions determined above

        # add title to the top of the image


        # add circuit name and info in square at the bottom right of the    
        # image

        # create Legend for the image and add it to the to the bottom left # of the image


        # draw the GPIO image in the center of the image


        # draw top and bottom component rows in the image

        # ***********Step 2: Add Components to Component Rows***************

        # add input components to the top row
        # add output components to the bottom row


        # *******Step 3: Determine and Draw Wires Between Components********

        # determine the wired connections between the components based on 
        # their pins and the provided mappings

        # create Wire objects for each connection, which will be wire 
        # segment objects that are connected at right angles with each 
        # other to form organized, readable wires.
        #   - use the Grid object to determine the path of the wire between
        #     the components
        # 

        # draw the wires on the image

        # fill out Legend with wire information


        # ********Step 4: Save the Image to the Specified Path**************

        # save the image to the specified path




    # create function to determine number of grounds

    # create function to determine number of power sources and voltages

    # create function to determine number of GPIO pins used, including which pin from the Pi goes to which pin on the component

    # create function to determine number of components

    # create function to determine number of connections between components

    # create function to determine number of connections between components and power sources

    # create function to determine number of connections between components and grounds

    # create function to determine number of connections between components and GPIO pins

    # create function to determine number of connections between components and other components

    def setCircuitImageOutputPath(self, circuitImageOutputPath:str):
        """
        Sets the output path for the circuit image.
        Args:
            circuitImageOutputPath (str): The output path for the circuit image.
        """
        self.circuitImageOutputPath = circuitImageOutputPath

    def getCircuitImageOutputPath(self):
        return self.circuitImageOutputPath
    
    def createCircuitImage(self, circuitImageSize:tuple[int, int]):
        """
        Creates a new circuit image.
        Args:
            circuitImageSize (tuple): The size of the circuit image.
        """
        self.circuitImageSize = circuitImageSize
        self.circuitImage = Image.new("RGB", circuitImageSize, "white")

    def getCircuitImage(self):
        """
        Returns the circuit image.
        Returns:
            Image: The circuit image."""
        return self.circuitImage
    


    def addComponent(self, component:Component | list[Component]):
        """
        Adds a component to the wiring diagram.
        Args:
            component (Component): The component to add to the wiring diagram.
        """
        if isinstance(component, Component):
            self.components.append(component)
        elif isinstance(component, list):
            for comp in component:
                if not isinstance(comp, Component):
                    raise ValueError(f"The component {comp} must be an instance of the Component class.")
            self.components.extend(component)
        else:
            raise ValueError(f"The component {component} must be an instance of the Component class or a list-like collection of component instances.")


    def removeComponent(self, component:Component | list[Component]):
        """
        Removes a component from the wiring diagram.
        Args:
            component (Component(or list[Components])): The component(s) to remove from the wiring diagram.
        """
        if isinstance(component, Component):
            self.components.remove(component)
        elif isinstance(component, list):
            for comp in component:
                if not isinstance(comp, Component):
                    raise ValueError(f"The component {comp} must be an instance of the Component class.")
            for comp in component:
                self.components.remove(comp)
        else:
            raise ValueError(f"The component {component} must be an instance of the Component class or a list-like collection of component instances.")



    def create_wiring_diagram(self, wiring_diagram):
        self.wiring_diagram = wiring_diagram

    def get_wiring_diagram(self):
        return self.wiring_diagram