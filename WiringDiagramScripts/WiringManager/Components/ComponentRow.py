import WiringDiagramScripts.WiringManager.Components.Component as Component
import Components.Coordinates as Coordinates


class ComponentRow:
    """
    Represent a row of components to be drawn in a wiring diagram using PIL through WiringManager.

    This class is used to represent a row of components to be drawn in a wiring diagram using PIL through WiringManager. The components will be drawn in order from left to right. The row will create an arbitrary number of slots for components to be drawn in. The slots will be equidistant from each other (providing empty space in between) and will be drawn in order from left to right. The row will also have a label that will be drawn at the top of the row.
    
    """
    def __init__(self, label:str, topYCoordinate:int, topXCoordinate:int, widthOfImage: int,maxNumberOfComps:int, components:list[Component] =[]):
        """
        Creates a new ComponentRow object representing a row of components to be drawn.
        
        Args:
        
            label (str): The label of the component row.
            topYCoordinate (int): The y-coordinate of the top of the row.
            topXCoordinate (int): The x-coordinate of the top of the row.
            components (list): A list of Component objects representing the components in the row. These components will be drawn in order from left to right.
        """
        self.label = label
        self.topYCoordinate = topYCoordinate
        self.topXCoordinate = topXCoordinate
        self.components = components
        self.maxNumberOfComps = maxNumberOfComps
        self.widthOfImage = widthOfImage

    # must be able to determine the width of a component's image based on the number of components in the row and the width of the row

    # must be able to determine the x-coordinate of the center of the component based on the number of components in the row and the width of the row

    # must be able to determine the y-coordinate of the center of the component based on the number of components in the row and the width of the row

    # must be able to determine the amount of "white" space between components based on the number of components in the row and the width of the row

    # must override the __str__ method to return a string representation of the ComponentRow object

    # must override the __repr__ method to return a string representation of the ComponentRow object that can be used to recreate the object

    # must ovveride the __getitem__ method to return the component at the specified index

    # must override the __setitem__ method to set the component at the specified index

    # must override the __delitem__ method to delete the component at the specified index

    # must override the __len__ method to return the number of components in the row, not the number of slots

    # must override the __iter__ method to iterate over the components in the row

    # must override the __reversed__ method to iterate over the components in the row in reverse order  
    
    # must be able to add a component to the row, throwing an exception if the row is full

    # must be able to remove a component from the row, throwing an exception if the row is empty, key is out of range, or the component is not in the row

    # must override the __contains__ method to return True if the component is in the row, False otherwise

