from Components.Component import Component
from Grid import Grid
class WiringLogic:
    """
    This class is responsible for the logic of the wiring diagram.

    This class will create, based on a set of components (including the Raspberry Pi itself), a wiring diagram in a human-readable manner to 
    help beginners who may never have wired anything before.

    The components will be placed in one of two "columns" on the diagram. The top column will contain any output components, such as LEDs, whle the
    bottom column will contain any input components, such as buttons or sensors. The Raspberry Pi GPIO pins will be placed in the center of the diagram.

    The wires will be drawn in a way that is easy to follow, and the diagram will be annotated to show which pins are connected to which components. The diagram will show all pin connections, including power, ground, and data pins (GPIO, I2C, etc).
    """
    def __init__(self, components: list[Component], grid: Grid):
        """
        Creates a new WiringLogic object.
        """
        
        self.components = components
        self.wireEndpoints ={}
        # uses this grid to represent components and their connections so 
        # that the diagram can be drawn and the connections can be checked 
        # for errors
        self.grid = grid
    def getWireEndCoordinates(self):
        """
        iterates through the components and gathers related endpoints (LMRM coordinates) to establish wire creation logic
        """
        # iterate through the components
            # for each component, check what GPIO pins are connected to it, if 
            # any, if it needs a ground or power connection, etc.   
        pass