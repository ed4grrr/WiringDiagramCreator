from PIL import Image, ImageDraw, ImageFont


class BaseWiringDiagram:
    """
    Base class for creating wiring diagrams. Contains all basic elements of a wiring diagram.


    """
    # Different percentages to describe the relative positions of wiring diagram elements.
    DISTANCE_BETWEEN_TITLE_AND_TOP = 0.03
    DISTANCE_BETWEEN_TOP_COMPONENTS_AND_TOP = 0.19
    DISTANCE_BETWEEN_BOTTOM_COMPONENTS_AND_BOTTOM = 0.25
    COMPONENT_HEIGHT_AND_WIDTH = 0.06
    DISTANCE_BETWEEN_COMP_ROWS_AND_CONTROL_COMP = 0.125

    def __init__(self, xResolution, yResolution):
        
        self.wiringDiagram = Image.new("RGB", (xResolution,yResolution), "white")
        self.canvas = ImageDraw.Draw(self.wiringDiagram)


    def addTitle(self, title):
        """
        Adds a title to the wiring diagram.

        :param title: The title to add to the wiring diagram.
        """
        self.canvas.text((10,10), title, fill="black")
        
        