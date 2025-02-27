from PIL import Image, ImageDraw, ImageFont
from Component import Component
from datetime import datetime

from ButtonComponent import ButtonComponent
from LEDComponent import LEDComponent
from PiGPIOPinHeader import PiGPIOPinHeader


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
        self.xResolution = xResolution
        self.yResolution = yResolution
        self.wiringDiagram = Image.new("RGB", (xResolution,yResolution), "white")
        self.canvas = ImageDraw.Draw(self.wiringDiagram)

        self.inputComponentLocations = {}
        self.outputComponentLocations = {}
        self.controllerComponentLocation = {}
        self.inputComponentObjects = {}
        self.outputComponentObjects= {}
        self.controllerComponentObject = {}

        self.outputComponentTopLine = self.yResolution * BaseWiringDiagram.DISTANCE_BETWEEN_TOP_COMPONENTS_AND_TOP
        self.outputComponentBottomLine = self.outputComponentTopLine+self.yResolution * 0.12
        self.inputComponentTopLine = self.outputComponentBottomLine+self.yResolution * 0.32
        self.inputCompounentBottomLine = self.inputComponentTopLine+self.yResolution * 0.12



    def addTitle(self, title, fontSize):
        """
        Adds a title to the wiring diagram.

        :param title: The title to add to the wiring diagram.
        """


        # create a rectangle that is about 3% of the height below the top of the image 

        padding =10


       
        
        
        # determine the center point of the rectangle
        centerPoint = (self.xResolution/2, self.yResolution * 0.05)
        print(F"the font size is {fontSize}")
        
        



        topLeftTitleFramePixel = (padding,padding)

        self.createFramedText(title, fontSize, topLeftTitleFramePixel,padding)

        
    def createFramedText(self, title, fontSize, topLeftTitleFramePixel,padding):
        
        font = ImageFont.load_default(fontSize)
        lm =self.canvas.textbbox(topLeftTitleFramePixel, title,  align="center", font_size=fontSize,font=font)



        lm = (lm[0]-padding+1, lm[1]-padding, lm[2]+padding, lm[3]+padding)
        self.canvas.rectangle(lm, outline="black", width=2)


        self.canvas.text(topLeftTitleFramePixel, title, fill="black", align="center", font_size=fontSize, font=font)

        


    def drawHorizontalLine(self, height):
        """
        Draws a line on the wiring diagram.

        :param start: The starting point of the line.
        :param end: The ending point of the line.
        """
        self.canvas.line([(0,height),(self.xResolution, height)], fill="black")

    def saveDiagram(self, outputPath):
        """
        Saves the wiring diagram to a file.

        :param outputPath: The path to save the wiring diagram.
        """
        self.wiringDiagram.save(outputPath)


    def drawComponentRows(self, numberOfInputComponents, numberOfOutputComponents):
        """
        Draws the component rows on the wiring diagram.

        :param numberOfComponents: The number of components in each row.
        """
        self.drawComponentRectangles(self.outputComponentTopLine, self.outputComponentBottomLine, self.outputComponentLocations, self.outputComponentObjects, numberOfOutputComponents)

        self.drawComponentRectangles(self.inputComponentTopLine, self.inputCompounentBottomLine, self.inputComponentLocations,self.inputComponentObjects ,numberOfInputComponents)

    def drawComponentRectangles(self, topLine, bottomLine, dictToUse, objectDictToUse,numberOfComponents,outline="black"):
        """ 
            Draws all of the component rectanges on one of the component rows.

        """
        # determine dimensions of each component rectangle based on the number of components, the size of a row, and a small vertical padding and a large padding value

        verticalPadding = 10

        horizontalPadding = 20

        componentWidth = (self.xResolution - 2*horizontalPadding)/numberOfComponents


        componentHeight = (bottomLine-topLine - 2*verticalPadding)

        for i in range(numberOfComponents):
            topLeft = (horizontalPadding+i*componentWidth, topLine+verticalPadding)
            bottomRight = ((i+1)*componentWidth- horizontalPadding, bottomLine-verticalPadding)
            self.drawComponentRectangle(topLeft, bottomRight, dictToUse, objectDictToUse,outline=outline)
        
        


    def drawComponentRectangle(self, topLeft, bottomRight, dictLocationToUse, dictComponentToUse, outline=None):
        """
        Draws a rectangle on the wiring diagram.

        :param topLeft: The top left point of the rectangle.
        :param bottomRight: The bottom right point of the rectangle.
        """
        # so we can reference it when we add component images
        componentKey = len(dictLocationToUse)
        
        # used to determine where to place the component image
        dictLocationToUse[componentKey] = (topLeft, bottomRight)

        # used to determine what component to add to the diagram, and for WiringLogic
        dictComponentToUse[componentKey] = None
        
        
        self.canvas.rectangle([topLeft, bottomRight], outline=outline, width=2
        )

    @staticmethod
    def findRectangularDimensions(topLeft, bottomRight):
        """
        Finds the dimensions of a rectangle.

        :param topLeft: The top left point of the rectangle.
        :param bottomRight: The bottom right point of the rectangle.
        :return: The width and height of the rectangle.
        """
        return (int(bottomRight[0] - topLeft[0]), int(bottomRight[1] - topLeft[1]))

    @staticmethod
    def findCenter(topLeft, bottomRight):
        """
        Finds the center point of a rectangle.

        :param topLeft: The top left point of the rectangle.
        :param bottomRight: The bottom right point of the rectangle.
        :return: The center point of the rectangle.
        """
        return (int((topLeft[0] + bottomRight[0]) // 2), int((topLeft[1] + bottomRight[1]) // 2))

    def addResizedImage(self, component:Component, centerPoint, destinationDimensions, rotationAngle=0):
        """
        Adds an image to the wiring diagram.

        :param imagePath: The path to the image to add.
        :param centerPoint: The center point of the image.
        """
        image = Image.open(component.imagePath)
        
        
        
        image = image.resize(destinationDimensions)
        # pin coordinates are based on the original image size, so we need to adjust them after scaling
        component.adjustCoordinatesAfterScaling(destinationDimensions[0], destinationDimensions[1])

        
        image = image.rotate(rotationAngle, expand=True)
        
        # pin coordinates are based on the original image orientation, so we need to adjust them after rotating
        component.adjustCoordinatesAfterRotation(rotationAngle)

        position = (int(centerPoint[0]-destinationDimensions[0]//2), int(centerPoint[1]-destinationDimensions[1]//2))


        self.wiringDiagram.paste(image, position)
        component.adjustCoordinatesAfterPlacement(position)


    def addImage(self, component:Component, centerPoint,  rotationAngle=0):
        """
        Adds an image to the wiring diagram.

        :param imagePath: The path to the image to add.
        :param centerPoint: The center point of the image.
        """
        


        with Image.open(component.imagePath) as image:
            print(f"**************************Start here**************************")
            component.printCoordinates()
            
            position = (int(centerPoint[0]-image.width//2), int(centerPoint[1]-image.height//2))
            component.adjustCoordinatesAfterScaling(image.width, image.height)
            component.printCoordinates()
            
            
            
            image = image.rotate(rotationAngle, expand=True)
            component.adjustCoordinatesAfterRotation(rotationAngle)
            component.printCoordinates()
            
            
            
            self.wiringDiagram.paste(image, position)
            component.adjustCoordinatesAfterPlacement(position)
            component.printCoordinates()

            print(f"**************************End here**************************")
    def addComponent(self, component:Component, slotKey, compDict, objectDict,rotationAngle=0):
        """
        Adds an input component to the wiring diagram at a relative position.

        :param component: The component to add (an instance of a Component subclass).
        :param relative_x: The relative x position (0 to 1).
        """
        self.addResizedImage(component, self.findCenter(*compDict[slotKey]), self.findRectangularDimensions(*compDict[slotKey]), rotationAngle=rotationAngle)
        objectDict[slotKey] = component


    def addComponentRows(self):
        self.outputComponentTopLine = self.yResolution * BaseWiringDiagram.DISTANCE_BETWEEN_TOP_COMPONENTS_AND_TOP
        self.drawHorizontalLine(self.outputComponentTopLine)

        self.outputComponentBottomLine = self.outputComponentTopLine+self.yResolution * 0.12
        self.drawHorizontalLine(self.outputComponentBottomLine)


        self.inputComponentTopLine = self.outputComponentBottomLine+self.yResolution * 0.32
        self.drawHorizontalLine(self.inputComponentTopLine)

        self.inputCompounentBottomLine = self.inputComponentTopLine+self.yResolution * 0.12
        self.drawHorizontalLine(self.inputCompounentBottomLine)

    
    def addInfoRectangle(self, lmInfoRectangle,title,author):
        dateTimeAndnanoSeconds = datetime.now()
        dateTime = dateTimeAndnanoSeconds.strftime("%d/%m/%Y %H:%M:%S")

        text = f"Title: {title}\nAuthor: {author}\nDate: {dateTime}\nNot Drawn to Scale" 

        wiringDiagram.createFramedText(text, 30, (0,lmInfoRectangle),10)
 
    
    def addLegend(self, lmInfoRectangle):
        wiringDiagram.createFramedText("Legend", 30, (wiringDiagram.xResolution*0.40,lmInfoRectangle),10)

    def addOtherRequirements(self, lmInfoRectangle):
        wiringDiagram.createFramedText("Other Requirements", 30, (wiringDiagram.xResolution*0.77,lmInfoRectangle),10)

    def addControllerComponent(self,component:Component):
        middleOfSecondandThirdLine = int((self.inputComponentTopLine+self.outputComponentBottomLine)//2)

        centerOfMiddleArea = (self.xResolution//2,middleOfSecondandThirdLine)
        imageDimensions = component.getImageDimensions()
       
        topLeftPixel = (centerOfMiddleArea[0]-imageDimensions[0]//2, centerOfMiddleArea[1]-imageDimensions[1]//2)

        bottomRightPixel = (centerOfMiddleArea[0]+imageDimensions[0]//2, centerOfMiddleArea[1]+imageDimensions[1]//2)
        
        self.controllerComponentLocation[0] = (topLeftPixel, bottomRightPixel)
        
        rectDimensions = self.findRectangularDimensions(topLeftPixel,bottomRightPixel)

        print(f"\n\n%%%%%%%%%%%%%%%%%%%%%%%%topLeftPixel: {topLeftPixel}, bottomRightPixel: {bottomRightPixel} centerofMiddleArear {centerOfMiddleArea}   rectdimension {rectDimensions}\n\n")


        
        self.addResizedImage(component, self.findCenter(topLeftPixel,bottomRightPixel), rectDimensions,  rotationAngle=90)
        self.controllerComponentObject[0] = component


    def printAllComponents(self):
        print("Input Components:")
        for key, value in self.inputComponentLocations.items():
            print(key, value)
            print(self.inputComponentObjects[key])
        print("\n\nOutput Components:")
        for key, value in self.outputComponentLocations.items():
            print(key, value)
            print(self.outputComponentObjects[key])

        print("\n\nController Components:")
        for key, value in self.controllerComponentLocation.items():
            print(key, value)
            print(self.controllerComponentObject[key])
        

if __name__ == "__main__":
    wiringDiagram = BaseWiringDiagram(1920, 1080)
    wiringDiagram.addTitle("Edgar's Wrath Exhibit Diagram",70)

    wiringDiagram.addComponentRows()




    lmInfoRectangle = wiringDiagram.yResolution * (1-0.18)


    wiringDiagram.addInfoRectangle(lmInfoRectangle, "Edgar's Bird Exhibit Diagram", "Edgar")
    
    wiringDiagram.addLegend(lmInfoRectangle)
    wiringDiagram.addOtherRequirements(lmInfoRectangle)

    
    wiringDiagram.addControllerComponent(PiGPIOPinHeader("Pi GPIO Pin Header"))

    wiringDiagram.drawComponentRows(12,12)
 
    for each,value in wiringDiagram.inputComponentLocations.items():
        wiringDiagram.addComponent(ButtonComponent("Button", 1),2, wiringDiagram.inputComponentLocations, wiringDiagram.inputComponentObjects, rotationAngle=0 )

    for each,value in wiringDiagram.outputComponentLocations.items():
        wiringDiagram.addComponent(LEDComponent("LED", 1),2, wiringDiagram.outputComponentLocations, wiringDiagram.outputComponentObjects)


    wiringDiagram.saveDiagram(r"C:\Users\edgar\Documents\WiringDiagram\WiringDiagramScripts\WiringManager\Components\diagramTest\wiringDiagram.png")

    wiringDiagram.printAllComponents()

