from Coordinates import Coordinates
from Wire import WireLines, WireSegmentLines
from Utilities.DirectionEnum import DirectionEnum
from Utilities.PinEnum import PinEnum
from Component import Component
from Grid import Grid
from Logger import Logger

class WiringLogic:
    def __init__(
        self,
        inputComponentsDict: dict[int, Component],
        outputComponentsDict: dict[int, Component],
        controllerComponentsDict: dict[int, Component],
        imageDimensions: tuple[int, int],
        testing=None
    ):
        self.testing = testing
      
        self.maxLengthOfWire = 0.035 * imageDimensions[1]
        self.maxWidthOfWire = self.maxLengthOfWire
        self.logger = Logger("WiringLogic")
        self.logger.addMessage("Wiring Logic Logger Initialized")
        self.logger.addMessage(
            f"Max Length of Wire: {self.maxLengthOfWire}\nMax Width of Wire: {self.maxWidthOfWire}"
        )
        self.grid = Grid(imageDimensions[0], imageDimensions[1])
        self.wires = {}
        self.inputComponentsDict = inputComponentsDict
        self.outputComponentsDict = outputComponentsDict
        self.controllerComponentsDict = controllerComponentsDict
        self.timesGoneTheSameDirection = 0
        self.lastDirectionUsed = None

    def createWires(self):
        self.logger.addMessage("Creating Wires")
        self.logger.addMessage("Creating Wires for Input Components")
        for component in self.inputComponentsDict.values():
            self.logger.addMessage(f"&&&Creating Wires for {component.Label}")
            label = component.Label
            self._loopThroughComps(component, label)

        self.logger.addMessage("Creating Wires for Output Components")
        for component in self.outputComponentsDict.values():
            self.logger.addMessage(f"&&&Creating Wires for {component.Label}")
            label = component.Label
            self._loopThroughComps(component, label)

    def _loopThroughComps(self, component, label):
        for pinDict in component.pinLMRMCoordinates.values():
            self.logger.addMessage(
                f"Creating Wire for {label} with pinDict {pinDict}"
            )
            if pinDict["Usage"].value != PinEnum.GROUND.value:
                wire = self._createWire(
                    f"{label} {pinDict["Usage"]}", pinDict, component.controllerKey, color="red"
                )
            else:
                wire = self._createWire(
                    f"{label} {pinDict["Usage"]}", pinDict, component.controllerKey, color="black"
                )
            component.addWire(wire,pinDict["PinDestination"])
            self.logger.addMessage(f"Wire Created for {label} {pinDict['Usage']}")

    def _createWire(
        self,
        componentLabel: str,
        pinDict: dict[str, any],
        controllerKey: int,
        color: str = "black",
    ):
        wire = WireLines(componentLabel)
        compPinCenterCoordinates = Component._determinePinCenter(
            pinDict["LM"], pinDict["RM"]
        )
                
                
        print(f"compPinDestination: {pinDict['PinDestination']}")
        compPinDestination = pinDict["PinDestination"]
                # reassign power and ground pins as they do not come with a specific GPIO pin assigned (as there are multiple power and ground pins)
        if compPinDestination not in [PinEnum.INPUT, PinEnum.OUTPUT]:

            if compPinDestination == PinEnum.GROUND:
                # TODO: add a common ground connection and allow for the use of multiple grounds
                compPinDestination = 6

            if compPinDestination == PinEnum.V3_3:
                # TODO: add a common 3.3V connection and allow for the use of multiple 3.3V connections
                compPinDestination = 1

            if compPinDestination == PinEnum.V5:
                # TODO: add a common 5V connection and allow for the use of multiple 5V connections
                compPinDestination = 2


        pinDestinationCoordinates = Component._determinePinCenter(
            self.controllerComponentsDict[controllerKey].pinLMRMCoordinates[
                compPinDestination
            ]["LM"],
            self.controllerComponentsDict[controllerKey].pinLMRMCoordinates[
                compPinDestination
            ]["RM"],
        )
        sendThisDict = pinDict["PinLocation"]


        nextEndpoint = self._getFirstSegmentNextEndpoint(compPinCenterCoordinates, sendThisDict)

        wire.addSegment(compPinCenterCoordinates, nextEndpoint, color=color)
        previousEndpoint = nextEndpoint
        print(f"compPinCenterCoordinates: {compPinCenterCoordinates}")
        print(f"nextEndpoint: {nextEndpoint}")
        self.grid.setPixelLine(compPinCenterCoordinates, nextEndpoint, componentLabel)

        while previousEndpoint != pinDestinationCoordinates:
            nextEndpoint = self._getNextEndpoint(previousEndpoint, pinDestinationCoordinates)
            wire.addSegment(previousEndpoint, nextEndpoint, color=color)
            previousEndpoint = nextEndpoint
            self.grid.setPixelLine(previousEndpoint, nextEndpoint, componentLabel)
        self.lastDirectionUsed = None
        self.timesGoneTheSameDirection = 0
        return wire

    def _getNextEndpoint(self, currentPoint: Coordinates, destination: Coordinates):
        direction = self._determineNextDirectionLine(currentPoint, destination)
        if self._limitSameDirectionSegments(direction[0][0]):
            direction[0][0] = "y" if direction[0][0] == "x" else "x"
            direction[0][1] = direction[0][1] if direction[0][0] == "x" else direction[1][1]
            self.lastDirectionUsed = direction[0][0]
            self.timesGoneTheSameDirection = 0

        if direction[0][0] == "x":
            if abs(direction[0][1]) < self.maxWidthOfWire:
                nextEndpoint = Coordinates("nextWireEndpoint", currentPoint.x + direction[0][1], currentPoint.y)
            else:
                toAdd = self.maxWidthOfWire if direction[0][1] > 0 else -self.maxWidthOfWire
                nextEndpoint = Coordinates("nextWireEndpoint", currentPoint.x + toAdd, currentPoint.y)
        else:
            if abs(direction[0][1]) < self.maxLengthOfWire:
                nextEndpoint = Coordinates("nextWireEndpoint", currentPoint.x, currentPoint.y + direction[0][1])
            else:
                toAdd = self.maxLengthOfWire if direction[0][1] > 0 else -self.maxLengthOfWire
                nextEndpoint = Coordinates("nextWireEndpoint", currentPoint.x, currentPoint.y + toAdd)
        return nextEndpoint

    def _limitSameDirectionSegments(self, directionStr:str):
        if self.lastDirectionUsed == directionStr:
            self.timesGoneTheSameDirection += 1
            if self.timesGoneTheSameDirection == 3:
                return True
        else:
            self.lastDirectionUsed = directionStr
            self.timesGoneTheSameDirection = 0



    def _determineNextDirectionLine(self, currentEndPoint: Coordinates, destination: Coordinates):
        currentX = currentEndPoint.x
        currentY = currentEndPoint.y
        destinationX = destination.x
        destinationY = destination.y

        rawXDistance = destinationX - currentX
        rawYDistance = destinationY - currentY

        xDistance = abs(rawXDistance)
        yDistance = abs(rawYDistance)

        if xDistance >= yDistance:
            return [["x", rawXDistance], ["y", rawYDistance]]
        else:
            return [["y", rawYDistance], ["x", rawXDistance]]

    def _getFirstSegmentNextEndpoint(self, currentPoint: Coordinates, pinLocation: DirectionEnum):
        scaler = 3
        pinLocation = pinLocation.value
        print(f"pinLocation: {pinLocation}")
        if pinLocation == DirectionEnum.LEFT.value:
            return Coordinates("nextWireEndpoint", currentPoint.x - self.maxWidthOfWire*scaler, currentPoint.y)
        elif pinLocation == DirectionEnum.RIGHT.value:
            return Coordinates("nextWireEndpoint", currentPoint.x + self.maxWidthOfWire*scaler, currentPoint.y)
        elif pinLocation == DirectionEnum.UP.value:
            return Coordinates("nextWireEndpoint", currentPoint.x, currentPoint.y - self.maxLengthOfWire*scaler)
        elif pinLocation == DirectionEnum.DOWN.value:
            return Coordinates("nextWireEndpoint", currentPoint.x, currentPoint.y + self.maxLengthOfWire*scaler)
        else:
            raise ValueError("Invalid pin location direction")

