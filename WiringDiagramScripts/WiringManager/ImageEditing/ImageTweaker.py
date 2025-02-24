class ImageTweaker:
    def __init__(self, imagePath:str | list[str], isOpeningOnCreation:bool = True):
        """
        Creates a new ImageTweaker object.
        """
        self.imagePath = imagePath
        self.image = None
        self.size = None

        if isOpeningOnCreation:
            self.openImage()       

    def openImage(self):
        """
        Opens the image file.
        """
        try:
            if isinstance(self.imagePath, str):
                self.image = Image.open(self.imagePath)
            elif isinstance(self.imagePath, list):
                self.image = {}
                for imagePath in self.imagePath:
                    self.image[imagePath] = Image.open(imagePath)
        except FileNotFoundError:
            raise ValueError(f"The image at \"{self.imagePath}\" cannot be opened")
        except PermissionError:
            raise ValueError(f"The image at \"{self.imagePath}\" cannot be opened. Permission denied.")
        except IsADirectoryError:
            raise ValueError(f"The image at \"{self.imagePath}\" cannot be opened. It is a directory.")
        except Exception as e:
            raise ValueError(f"An error occurred while opening the image at \"{self.imagePath}\". Error: {e}")


    # create methods to allow for use with context managers
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.image.close()

    def getImageSize(self):
        """
        Returns the size of the image.
        Returns:
            tuple: The width and height of the image.
        """
        if isinstance(self.imagePath, str):
                return self.image.size
        elif isinstance(self.imagePath, list):
            returnableDict = {}
            for imagePath, image in self.image.items():
                returnableDict[imagePath]= image.size 
            return returnableDict
        
    def getSpecificImageSize(self, imagePath:str):
        """
        Returns the size of the image.
        Returns:
            tuple: The width and height of the image.
        """
        if isinstance(self.imagePath, str):
            return self.image.size
        elif isinstance(self.imagePath, list):
            return self.image[imagePath].size
        else:
            raise ValueError(f"The image at \"{imagePath}\" cannot be opened")
            

    def resizeImage(self, width:int, height:int):
        """
        Resizes the image to the specified width and height.
        Args:
            width (int): The width of the resized image.
            height (int): The height of the resized image.
        """
        self.image = self.image.resize((width, height))

    def determineImageCenter(self):
        """
        Determines the center of the image.
        Returns:
            tuple: The x and y coordinates of the center of the image.
        """
        return (self.size[0] // 2, self.size[1] // 2)

    def cropImage(self, left:int, top:int, right:int, bottom:int):
        """
        Crops the image to the specified bounding box.
        Args:
            left (int): The x-coordinate of the left edge.
            top (int): The y-coordinate of the top edge.
            right (int): The x-coordinate of the right edge.
            bottom (int): The y-coordinate of the bottom edge.
        """
        self.image = self.image.crop((left, top, right, bottom))

    def saveAs(self, outputPath:str):
        """
        Saves the image to a file and closes the original image.
        Args:
            output_path (str): The path to save the image file.
        """
        try:            
            if isinstance(self.imagePath, str):
                self.image.save(outputPath)
            elif isinstance(self.imagePath, list):
                for imagePath in self.imagePath:
                    self.image[imagePath].save(outputPath)
            self.closeImage()
        except OSError:
            raise ValueError(f"The image at \"{self.imagePath}\" cannot be saved")
        except FileNotFoundError:
            raise ValueError(f"The image at \"{self.imagePath}\" cannot be saved")
        except PermissionError:
            raise ValueError(f"The image at \"{self.imagePath}\" cannot be saved. Permission denied.")
        except IsADirectoryError:
            raise ValueError(f"The image at \"{self.imagePath}\" cannot be saved. It is a directory.")
        except Exception as e:
            raise ValueError(f"An error occurred while saving the image at \"{self.imagePath}\". Error: {e}")

    def closeImage(self):
        """
        Closes the image file.
        """
        try:
            if isinstance(self.imagePath, str):
                self.image.close()
            elif isinstance(self.imagePath, list):
                for imagePath in self.imagePath:
                    self.image[imagePath].close()
        except Exception as e:
            raise ValueError(f"An error occurred while closing the image at \"{self.imagePath}\". Error: {e}")