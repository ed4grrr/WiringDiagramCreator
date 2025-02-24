from PIL import Image, ImageDraw

from WiringDiagramScripts import Component, ImageTweaker








        
class CircuitDiagram:
    def __init__(self, components:dict[str, Component], imageTweaker:ImageTweaker):
        """
        Creates a new CircuitDiagram object.
        """
        self.components = components
        self.imageTweaker = imageTweaker


class ImageEditingTest:
    def __init__(self):
        """
        Creates a new WiringDiagram object.
        """
        self.imagePath = ""
        self.shapes = {}
        self.components = {}
        # create a new image

    def setImagePath(self, imagePath:str):
        """
        Sets the path to the input image file.
        Args:
            imagePath (str): Path to the input image file.
        """
        self.imagePath = imagePath

    def setShapes(self, shapes:dict[str, dict[str, any]]):
        """
        Sets the shapes to add.
        Args:
            shapes (list[dict]): List of shapes to add. Each shape is a dictionary with keys:
                'type' (str): The type of shape method in ImageDraw (e.g., 'rectangle', 'ellipse', 'line')
                'coordinates' (tuple): Coordinates for the shape
                'color' (tuple): Color of the shape in RGB format
                'width' (int, optional): Width of the shape outline (default is 3)
        """
        self.shapes = shapes
    
    def setComponents(self, components:dict[str, any]):
        """
        Sets the components and their relevant data.
        Args:
            components (dict): a dict containing the components and their their relevant data including the following:
                'type' (Type): The type of component (e.g., LED, Resistor, Capacitor, Button, etc.)
                "value" (int): The value of the component (e.g., 220 ohm, 10k ohm, 100uF, etc.)
                componentsAndPins (dict): a dict containing the components and their respective pins, the pins names, and the coordinates of the end points of the pins
                    "componentName" (str): The name of the component (e.g., LED1, R1, C1, etc.) 
                    "pins" (dict): a dict containing the pins and their respective coordinates
                        "pinName" (str): The name of the pin (e.g., A, B, C, etc.)
                        "coordinates" (tuple): The coordinates of the end points of the pin relative it its original image
                "imageFile" (str): The path to the image file of the component
        """
        self.components = components


    def addShapesToImage(self, outputPath):
        """
        Adds shapes to the image at specified coordinates.

        :param image_path: Path to the input image file.
        :param shapes: List of shapes to add. Each shape is a dictionary with keys:
                    'type' (str): The type of shape method in ImageDraw (e.g., 'rectangle', 'ellipse', 'line')
                    'coordinates' (tuple): Coordinates for the shape
                    'color' (tuple): Color of the shape in RGB format
                    'width' (int, optional): Width of the shape outline (default is 3)
        :param output_path: Path to save the output image file.
        """
        # Open the image file
        with Image.open(self.imagePath) as img:
            draw = ImageDraw.Draw(img)

            # Draw each shape
            for shape in self.shapes:
                shape_type = shape['type']
                coordinates = shape['coordinates']
                color = shape['color']
                width = shape.get('width', 3)

                draw_method = getattr(draw, shape_type, None)
                if draw_method:
                    if shape_type == 'line':
                        draw_method(coordinates, fill=color, width=width)
                    else:
                        draw_method(coordinates, outline=color, width=width)
                else:
                    raise ValueError(f"Unsupported shape type: {shape_type}")

            # Save the modified image
            img.save(outputPath)

if __name__ == "__main__":
    # Example usage
    imagePath = "image.png"
    outputPath = "output_image.png"


    # a dict of the int of the gpio pin to the rectangle it is connected to. Each rectangle is a dict with keys:
    # 'type' (str): The type of shape method in ImageDraw (e.g., 'rectangle', 'ellipse', 'line')
    # 'coordinates' (tuple): Coordinates for the shape
    # 'color' (tuple): Color of the shape in RGB format
    # 'width' (int, optional): Width of the shape outline (default is 3)
    
    pinToRectangleDict ={
        1:{'type': 'rectangle', 'coordinates': (30, 15, 50, 35), 'color': (255, 0, 0)},
        2:{'type': 'rectangle', 'coordinates': (70, 15, 90, 35), 'color': (255, 0, 0)},
        3:{'type': 'rectangle', 'coordinates': (30, 55, 50, 75), 'color': (255, 0, 0)},
        4:{'type': 'rectangle', 'coordinates': (70, 55, 90, 75), 'color': (255, 0, 0)},
        5:{'type': 'rectangle', 'coordinates': (30, 95, 50, 115), 'color': (255, 0, 0)},
        6:{'type': 'rectangle', 'coordinates': (70, 95, 90, 115), 'color': (255, 0, 0)},
        7:{'type': 'rectangle', 'coordinates': (30, 135, 50, 155), 'color': (255, 0, 0)},
        8:{'type': 'rectangle', 'coordinates': (70, 135, 90, 155), 'color': (255, 0, 0)},
        9:{'type': 'rectangle', 'coordinates': (30, 175, 50, 195), 'color': (255, 0, 0)},
        10:{'type': 'rectangle', 'coordinates': (70, 175, 90, 195), 'color': (255, 0, 0)},
        11:{'type': 'rectangle', 'coordinates': (30, 215, 50, 235), 'color': (255, 0, 0)},
        12:{'type': 'rectangle', 'coordinates': (70, 215, 90, 235), 'color': (255, 0, 0)},
        13:{'type': 'rectangle', 'coordinates': (30, 255, 50, 275), 'color': (255, 0, 0)},
        14:{'type': 'rectangle', 'coordinates': (70, 255, 90, 275), 'color': (255, 0, 0)},
        15:{'type': 'rectangle', 'coordinates': (30, 295, 50, 315), 'color': (255, 0, 0)},
        16:{'type': 'rectangle', 'coordinates': (70, 295, 90, 315), 'color': (255, 0, 0)},
        17:{'type': 'rectangle', 'coordinates': (30, 335, 50, 355), 'color': (255, 0, 0)},
        18:{'type': 'rectangle', 'coordinates': (70, 335, 90, 355), 'color': (255, 0, 0)},
        19:{'type': 'rectangle', 'coordinates': (30, 375, 50, 395), 'color': (255, 0, 0)},
        20:{'type': 'rectangle', 'coordinates': (70, 375, 90, 395), 'color': (255, 0, 0)},
        21:{'type': 'rectangle', 'coordinates': (30, 415, 50, 435), 'color': (255, 0, 0)},
        22:{'type': 'rectangle', 'coordinates': (70, 415, 90, 435), 'color': (255, 0, 0)},
        23:{'type': 'rectangle', 'coordinates': (30, 455, 50, 475), 'color': (255, 0, 0)},
        24:{'type': 'rectangle', 'coordinates': (70, 455, 90, 475), 'color': (255, 0, 0)},
        25:{'type': 'rectangle', 'coordinates': (30, 495, 50, 515), 'color': (255, 0, 0)},
        26:{'type': 'rectangle', 'coordinates': (70, 495, 90, 515), 'color': (255, 0, 0)},
        27:{'type': 'rectangle', 'coordinates': (30, 535, 50, 555), 'color': (255, 0, 0)},
        28:{'type': 'rectangle', 'coordinates': (70, 535, 90, 555), 'color': (255, 0, 0)},
        29:{'type': 'rectangle', 'coordinates': (30, 575, 50, 595), 'color': (255, 0, 0)},
        30:{'type': 'rectangle', 'coordinates': (70, 575, 90, 595), 'color': (255, 0, 0)},
        31:{'type': 'rectangle', 'coordinates': (30, 615, 50, 635), 'color': (255, 0, 0)},
        32:{'type': 'rectangle', 'coordinates': (70, 615, 90, 635), 'color': (255, 0, 0)},
        33:{'type': 'rectangle', 'coordinates': (30, 655, 50, 675), 'color': (255, 0, 0)},
        34:{'type': 'rectangle', 'coordinates': (70, 655, 90, 675), 'color': (255, 0, 0)},
        35:{'type': 'rectangle', 'coordinates': (30, 695, 50, 715), 'color': (255, 0, 0)},
        36:{'type': 'rectangle', 'coordinates': (70, 695, 90, 715), 'color': (255, 0, 0)},
        37:{'type': 'rectangle', 'coordinates': (30, 735, 50, 755), 'color': (255, 0, 0)},
        38:{'type': 'rectangle', 'coordinates': (70, 735, 90, 755), 'color': (255, 0, 0)}, 
        39:{'type': 'rectangle', 'coordinates': (30, 775, 50, 795), 'color': (255, 0, 0)},
        40:{'type': 'rectangle', 'coordinates': (70, 775, 90, 795), 'color': (255, 0, 0)}
 

    }

    # a collection of RGB-valued colors that are colorblind friendly
    colors = {
        "Black": (0, 0, 0),
        "Dark Red": (128, 0, 0),
        "Dark Green": (0, 128, 0),
        "Dark Blue": (0, 0, 128),
        "Olive": (128, 128, 0),
        "Teal": (0, 128, 128),
        "Purple": (128, 0, 128),
        "Deep Red": (192, 0, 0),
        "Deep Green": (0, 192, 0),
        "Deep Blue": (0, 0, 192),
        "Yellow-Green": (192, 192, 0),
        "Cyan": (0, 192, 192),
        "Magenta": (192, 0, 192),
        "Orange-Red": (255, 69, 0),
        "Dark Orange": (255, 140, 0),
        "Goldenrod": (184, 134, 11),
        "Saddle Brown": (139, 69, 19),
        "Dark Olive Green": (85, 107, 47),
        "Forest Green": (34, 139, 34),
        "Steel Blue": (70, 130, 180),
        "Dark Slate Blue": (72, 61, 139),
        "Dark Magenta": (139, 0, 139),
        "Indian Red": (205, 92, 92),
        "Sandy Brown": (244, 164, 96),
        "Dark Sea Green": (143, 188, 143),
        "Slate Gray": (112, 128, 144),
        "Near Black": (25, 25, 25),
        "Dim Gray": (105, 105, 105),
        "Dark Gray": (169, 169, 169),
        "Dark Slate Gray": (47, 79, 79),
        "Deep Navy Blue": (0, 51, 102),
        "Deep Maroon": (102, 0, 51),
        "Deep Green": (0, 102, 51),
        "Coral": (255, 127, 80),
        "Crimson": (220, 20, 60),
        "Yellow-Green": (154, 205, 50),
        "Gold": (255, 215, 0),
        "Goldenrod": (218, 165, 32),
        "Brown": (165, 42, 42),
        "Sienna": (160, 82, 45),
        "Dark Salmon": (233, 150, 122),
        "Steel Blue": (70, 130, 180),
        "Powder Blue": (176, 224, 230),
        "Dark Cyan": (0, 139, 139),
        "Sea Green": (46, 139, 87),
        "Medium Sea Green": (60, 179, 113),
        "Lawn Green": (124, 252, 0),
        "Cornflower Blue": (100, 149, 237),
        "Dark Slate Blue": (72, 61, 139),
        "Medium Violet Red": (199, 21, 133),
        "Dark Orchid": (153, 50, 204),
        "Medium Orchid": (186, 85, 211)
    }

    imageEditor=ImageEditingTest()
    imageEditor.setShapes(pinToRectangleDict.values())
    imageEditor.setImagePath(imagePath)
    imageEditor.addShapesToImage(outputPath)
    print("Image saved to:", outputPath)