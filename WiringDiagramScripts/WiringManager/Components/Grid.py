
from Components.Coordinates import Coordinates


class CellAlreadySetError(Exception):
    """ Exception raised when a cell is already set. """
    def __init__(self, message:str):
        self.message = message
        super().__init__(self.message)

class Grid:
    """ this class uses a sparse matrix to store only the used pixels of the grid. """
    def __init__(self, width:int, height:int):
        """
        Creates a new Grid object.
        Args:
            width (int): The width of the grid.
            height (int): The height of the grid.
        """
        self.width = width
        self.height = height
        self.centerPixel = (width//2, height//2)
        self.grid = {}

    def isLongestPath(self, start:Coordinates, end:Coordinates) -> bool:
        """
        Given two points, determines the which of the two (distance to x end or distance to y end) is longer.
        Args:
            start (Coordinates): The starting coordinates.
            end (Coordinates): The ending coordinates.
            Returns:
            true if the x distance is longer than the y distance, false otherwise."""
        return abs(end.x - start.x) > abs(end.y - start.y)
    
    def setPixelLine(self, start:Coordinates, end:Coordinates):
        """
        Sets a line of pixels on the grid.
        Args:
            start (Coordinates): The starting coordinates of the line.
            end (Coordinates): The ending coordinates of the line.
        """
        x0=start.x
        y0=start.y
        x1=end.x
        y1=end.y
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        err = dx - dy
        while x0 != x1 or y0 != y1:
            self.setPixel(Coordinates(x0, y0))
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
        self.setPixel(Coordinates(x1, y1))

    def setPixel(self, coord:Coordinates):
        """
        Sets a pixel on the grid. If the pixel is already set, an exception is raised.
        Args:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
        """
        x=coord.x
        y=coord.y
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise ValueError(f"The pixel ({x}, {y}) is out of the grid bounds.")
        if x not in self.grid:
            self.grid[x] = {}
        if y in self.grid[x]:
            raise CellAlreadySetError(f"The pixel ({x}, {y}) is already set.")
        self.grid[x][y] = True
   

    def setPixels(self, pixels:list[Coordinates]):
        """
        Sets multiple pixels on the grid.
        Args:
            pixels (list): A list of pixel coordinates to set.
        """
        for pixel in pixels:
            self.setPixel(pixel)
    
    def clearPixel(self, coord:Coordinates):
        """
        Clears a pixel on the grid.
        Args:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
        """
        x=coord.x
        y=coord.y

        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise ValueError(f"The pixel ({x}, {y}) is out of the grid bounds.")
        if x in self.grid and y in self.grid[x]:
            del self.grid[x][y]
    
    def isPixelSet(self, coord:Coordinates) -> bool:
        """
        Checks if a pixel is set on the grid.
        Args:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
        Returns:
            bool: True if the pixel is set, False otherwise.
        """
        x=coord.x
        y=coord.y
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise ValueError(f"The pixel ({x}, {y}) is out of the grid bounds.")
        if x in self.grid and y in self.grid[x]:
            return True
        return False
    
    def getGrid(self) -> dict[int, dict[int, bool]]:
        """
        Returns the grid.
        Returns:
            dict: The grid.
        """
        return self.grid
    
    def getWidth(self) -> int:
        """
        Returns the width of the grid.
        Returns:
            int: The width of the grid.
        """
        return self.width
    
    def getHeight(self) -> int:
        """
        Returns the height of the grid.
        Returns:
            int: The height of the grid.
        """
        return self.height
    

