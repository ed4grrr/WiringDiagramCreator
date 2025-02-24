



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
    
    def setPixel(self, x:int, y:int):
        """
        Sets a pixel on the grid. If the pixel is already set, an exception is raised.
        Args:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
        """
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise ValueError(f"The pixel ({x}, {y}) is out of the grid bounds.")
        if x not in self.grid:
            self.grid[x] = {}
        if y in self.grid[x]:
            raise CellAlreadySetError(f"The pixel ({x}, {y}) is already set.")
        self.grid[x][y] = True
   

    def setPixels(self, pixels:list[tuple[int, int]]):
        """
        Sets multiple pixels on the grid.
        Args:
            pixels (list): A list of pixel coordinates to set.
        """
        for pixel in pixels:
            self.setPixel(pixel[0], pixel[1])
    
    def clearPixel(self, x:int, y:int):
        """
        Clears a pixel on the grid.
        Args:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
        """
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise ValueError(f"The pixel ({x}, {y}) is out of the grid bounds.")
        if x in self.grid and y in self.grid[x]:
            del self.grid[x][y]
    
    def isPixelSet(self, x:int, y:int) -> bool:
        """
        Checks if a pixel is set on the grid.
        Args:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
        Returns:
            bool: True if the pixel is set, False otherwise.
        """
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
    

if __name__ == "__main__":
    grid = Grid(12000, 12000)
    import sys
    print(sys.getsizeof(grid))
