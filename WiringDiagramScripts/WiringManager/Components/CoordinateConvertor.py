from Coordinates import Coordinates



class CoordinateConvertor:
    """
    A class that provides static methods to convert the various coordinates

    This class is to be used to convert the various Coordinates objects used in the WiringManager package. The methods are static and can be used without creating an instance of the class.

    All Components contain Coordinates objects to represent where the area where the wire can be connected to the pin. However, these images will be placed within a larger image that represents the wiring diagram. The WiringManager package will need to convert the coordinates of the pins to the larger image's coordinates to draw the wires correctly.

    This class takes into account the following:
    - The center pixel of the component slot to be used in the larger image
    - the dimensions of the component image

    Using these two things, the WiringManager package can convert the coordinates of the component's image to the larger image's coordinates. This will allow the WiringManager package to draw the wires correctly.


    """
