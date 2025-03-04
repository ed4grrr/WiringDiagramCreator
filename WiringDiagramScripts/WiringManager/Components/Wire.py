from __future__ import annotations

import Coordinates
from Utilities.DirectionEnum import *

class WireSegmentLines:
    def __init__(self, label:str, wireStartPoint:Coordinates, wireEndPoint:Coordinates, color:str="black", width:int=3):
        """
        Creates a new Wire object representing a wire to be drawn.
        
        Args:
        

        """
        self.label = label
        self.wireStartPoint = wireStartPoint
        self.wireEndPoint = wireEndPoint
        self.color = color.lower()
        self.width = width

    def __str__(self):
        return f"WireSegmentLines: {self.label} from {self.wireStartPoint} with color {self.color} and width {self.width}"
    def __repr__(self):
        return f"WireSegmentLines({self.label}, {self.wireStartPoint}, {self.color}, {self.width})"
    def intersects(self, other:WireSegmentLines):
        """
        Checks if the wire segment intersects with another wire segment.
        
        Args:
        
            other (WireSegment): The wire segment to check if it intersects with.
        
        Returns:
        
            bool: True if the wire segment intersects with the other wire segment, False otherwise.
        """
        # check if the wire segment intersects with the other wire segment
        return self.wireStartPoint.x < other.wireEndPoint.x and self.wireEndPoint.x > other.wireStartPoint.x and self.wireStartPoint.y < other.wireEndPoint.y and self.wireEndPoint.y > other.wireStartPoint.y
    
    
class WireLines:
    def __init__(self, label:str, segments:list[WireSegmentLines] =[], color:str="black", width:int=3):
        """
        Creates a new Wire object representing a wire to be drawn.
        
        Args:
        
            label (str): The label of the wire.
            segments (list): A list of WireSegment objects representing the wire's segments. These segments will be drawn in order. These
            segments **should** be connected and ordered from one end of the wire to the other.

        
        """

        self.color = color
        self.width = width
        self.label = label

        # the reason segements should be ordered from one end of the wire to the other.
        if segments != []:
            self.segments = {number: segment for number, segment in enumerate(segments)}
        else:
            self.segments = {}

    def checkIfWireIntersects(self, wire:WireLines):
        """
        Checks if the wire intersects with another wire.
        
        Args:
        
            wire (Wire): The wire to check if it intersects with.
        
        Returns:
        
            bool: True if the wire intersects with the other wire, False otherwise.
        """
        for segment in self.segments.values():
            for otherSegment in wire.segments.values():
                if segment.intersects(otherSegment):
                    return True
        return False


    def addSegment(self, wireStartPoint:Coordinates, wireEndPoint:Coordinates, color:str="", width:int=-1):
        """
        Adds a wire segment to the wire.
        
        Args:
        
            segment (WireSegment): The wire segment to be added to the wire.
        """
        if color == "":
            color = "black"
        if width == -1:
            width = self.width
       
        # the plus one is to make the segment number start at 1 instead of 0
        # as an empty dict would have a length of 0. Works in all other 
        # cases too
        self.segments[len(self.segments)+1] = WireSegmentLines(f"{self.label} Segment {len(self.segments)+1}", wireStartPoint, wireEndPoint, color=color, width =width)

    def __str__(self):
        segments = ""
        for key,segment in self.segments.items():
            segments += f"Wire Segment {key}: {segment}\n"
        return f"Wire: {self.label} with {len(self.segments)} segments.\n The segments are: {segments}"
        



class WireSegment:
    def __init__(self, label:str, LMCoord: Coordinates, RMCoord: Coordinates, pinLocation:DirectionEnum, color:str="black", width:int=3):
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
        self.LMCoord = LMCoord
        self.RMCoord = RMCoord
        self.color = color.lower()
        self.width = width
        self.pinLocation = pinLocation
        self.direction = pinLocation

    def returnWireSegmentDict(self):
        """
        Returns the wire object's attributes within a dictionary.
        
        Returns:
        
            dict: The wire object's attributes.
        """
        return {"label": self.label, "LM": self.LMCoord, "RM": self.RMCoord, "color": self.color, "width": self.width}
    
    def returnWireSegmentString(self):
        """
        Returns the wire object's attributes within a string.
        
        Returns:
        
            str: The wire object's attributes.
        """
        return f"WireSegment: {self.label} from {self.LMCoord} to {self.RMCoord} with color {self.color} and width {self.width}"
    def __str__(self):
        return self.returnWireSegmentString()
    def __repr__(self):
        return f"WireSegment({self.label}, {self.LMCoord}, {self.RMCoord}, {self.color}, {self.width})"
    def __eq__(self, other:WireSegment):
        return self.label == other.label and self.LMCoord == other.LMCoord and self.RMCoord == other.RMCoord and self.color == other.color and self.width == other.width
    def __ne__(self, other: WireSegment):
        return not self == other
    # TODO add more geometric methods that can be performed on line segments
    

class Wire:
    def __init__(self, label:str, segments:list[WireSegment] =[], color:str="black", width:int=3):
        """
        Creates a new Wire object representing a wire to be drawn.
        
        Args:
        
            label (str): The label of the wire.
            segments (list): A list of WireSegment objects representing the wire's segments. These segments will be drawn in order. These segments **should** be connected and ordered from one end of the wire to the other.

        """
        self.color = color
        self.width = width
        self.label = label

        # the reason segements should be ordered from one end of the wire to the other.
        if segments != []:
            self.segments = {number: segment for number, segment in enumerate(segments)}
        else:
            self.segments = {}


    def addSegment(self, LM:Coordinates, RM:Coordinates, pinLocation:DirectionEnum, color:str="", width:int=-1):
        """
        Adds a wire segment to the wire.
        
        Args:
        
            segment (WireSegment): The wire segment to be added to the wire.
        """
        if color == "":
            color = "black"
        if width == -1:
            width = self.width
       
        # the plus one is to make the segment number start at 1 instead of 0
        # as an empty dict would have a length of 0. Works in all other 
        # cases too
        self.segments[len(self.segments)+1] = WireSegment(f"{self.label} Segment {len(self.segments)+1}", LM, RM, pinLocation, color=color, width =width)

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
    
    def __eq__(self, other:Wire):
        return self.label == other.label and self.segments == other.segments
    
    def __ne__(self, other:Wire):
        return not self == other
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
