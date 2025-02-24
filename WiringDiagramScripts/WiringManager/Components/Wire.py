import PIL
import Coordinates
class WireSegment:
    def __init__(self, label:str, endPoint1: Coordinates, endPoint2: Coordinates, color:str="black", width:int=3):
        """
        Creates a new Wire object representing a wire to be drawn.
        
        Args:
        
            label (str): The label of the wire.
            start (tuple): The starting coordinates of the wire.
            end (tuple): The ending coordinates of the wire.
            color (str): The color of the wire.
            width (int): The width of the wire.
        """
        self.label = label
        self.endPoint1 = endPoint1
        self.endPoint2 = endPoint2
        self.color = color.lower()
        self.width = width

    def returnWireSegmentDict(self):
        """
        Returns the wire object's attributes within a dictionary.
        
        Returns:
        
            dict: The wire object's attributes.
        """
        return {"label": self.label, "endPoint1": self.endPoint1, "endPoint2": self.endPoint2, "color": self.color, "width": self.width}
    
    def returnWireSegmentString(self):
        """
        Returns the wire object's attributes within a string.
        
        Returns:
        
            str: The wire object's attributes.
        """
        return f"WireSegment: {self.label} from {self.endPoint1} to {self.endPoint2} with color {self.color} and width {self.width}"
    def __str__(self):
        return self.returnWireSegmentString()
    def __repr__(self):
        return f"WireSegment({self.label}, {self.endPoint1}, {self.endPoint2}, {self.color}, {self.width})"
    def __eq__(self, other):
        return self.label == other.label and self.endPoint1 == other.endPoint1 and self.endPoint2 == other.endPoint2 and self.color == other.color and self.width == other.width
    def __ne__(self, other):
        return not self == other
    # TODO add more geometric methods that can be performed on line segments
    

class Wire:
    def __init__(self, label:str, segments:list[WireSegment]):
        """
        Creates a new Wire object representing a wire to be drawn.
        
        Args:
        
            label (str): The label of the wire.
            segments (list): A list of WireSegment objects representing the wire's segments. These segments will be drawn in order. These segments **should** be connected and ordered from one end of the wire to the other.

        """
        self.label = label

        # the reason segements should be ordered from one end of the wire to the other.
        self.segments = {number: segment for number, segment in enumerate(segments)}

    def returnWireDict(self):
        """
        Returns the wire object's attributes within a dictionary.
        
        Returns:
        
            dict: The wire object's attributes.
        """
        return {"label": self.label, "segments": self.segments}
    
    def returnWireString(self):
        """
        Returns the wire object's attributes within a string.
        
        Returns:
        
            str: The wire object's attributes.
        """
        return f"Wire: {self.label} with {len(self.segments)} segments.\n The segments are: {self.segments}"
    
    def __str__(self):
        return self.returnWireString()
    
    def __repr__(self):
        return f"Wire({self.label}, {self.segments})"
    
    def __getitem__(self, key):
        return self.segments[key]
    
    def __setitem__(self, key, value):
        self.segments[key] = value

    def __delitem__(self, key):
        del self.segments[key]

    def __len__(self):
        return len(self.segments)
    
    def __iter__(self):
        return iter(self.segments)
    
    def __reversed__(self):
        return reversed(self.segments)
    
    def __contains__(self, item):
        return item in self.segments
    
    def __eq__(self, other):
        return self.label == other.label and self.segments == other.segments
    
if __name__ == "__main__":
    wireSegment1 = WireSegment("Segment 1", Coordinates.Coordinates("A", 0, 0), Coordinates.Coordinates("B", 0, 10))
    wireSegment2 = WireSegment("Segment 2", Coordinates.Coordinates("B", 0, 10), Coordinates.Coordinates("C", 10, 10))
    wireSegment3 = WireSegment("Segment 3", Coordinates.Coordinates("C", 10, 10), Coordinates.Coordinates("D", 10, 0))
    wireSegment4 = WireSegment("Segment 4", Coordinates.Coordinates("D", 10, 0), Coordinates.Coordinates("E", 20, 0))
    wire = Wire("Wire 1", [wireSegment1, wireSegment2, wireSegment3, wireSegment4])
    print(wire)
    print(wire[0])
    print(wire[1])
    print(wire[2])
    print(wire[3])
