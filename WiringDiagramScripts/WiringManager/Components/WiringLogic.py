from WiringDiagramScripts.WiringManager.Components.Component import (
    Component,
)
from Components.Coordinates import Coordinates
from Components.Utilities.PinEnum import PinEnum
from Grid import Grid
from Components.Wire import Wire, WireSegment


class WiringLogic:
    """
    This class is responsible for the logic of the wiring diagram.

    This class will create, based on a set of components (including the Raspberry Pi itself), a wiring diagram in a human-readable manner to
    help beginners who may never have wired anything before.

    The components will be placed in one of two "columns" on the diagram. The top column will contain any output components, such as LEDs, whle the
    bottom column will contain any input components, such as buttons or sensors. The Raspberry Pi GPIO pins will be placed in the center of the diagram.

    The wires will be drawn in a way that is easy to follow, and the diagram will be annotated to show which pins are connected to which components. The diagram will show all pin connections, including power, ground, and data pins (GPIO, I2C, etc).
    """

    def __init__(
        self,
        components: list[Component],
        controllerComponent: Component,
        grid: Grid,
        minSafeDistance: int = 25,
        arbitraryDistance: int = 50,
        wireSegmentLength: int = 50,
    ):
        """
        Creates a new WiringLogic object.
        """

        self.wireSegmentLength = wireSegmentLength

        # the minimum safe distance to create the first wires segement from a ControllerComponent's GPIO pin to a component's pin. These should be updated by some arbitrary amount to ensure that the wires are drawn in a visually appealing way.
        self.LEFT_MINIMUM_SAFE_DISTANCE = minSafeDistance
        self.RIGHT_MINIMUM_SAFE_DISTANCE = minSafeDistance
        self.ARBITRARY_DISTANCE = arbitraryDistance
        self.components = components
        self.wireEndpoints = {}
        self.controllerComponent = controllerComponent
        # uses this grid to represent components and their connections so
        # that the diagram can be drawn and the connections can be checked
        # for errors
        self.grid = grid

    def _createWire(
        self,
        componentPinLabel: str,
        pinNumber: int,
        pinDict: dict,
        controllerComponent: Component,
        color: str = "black",
        width: int = 3,
    ):
        """
        Creates a wire between a component and the Raspberry Pi. This wire will be drawn on the diagram and will be annotated to show which pins are connected.
        """
        controllerGPIOPin = pinDict["PinDestination"]
        wire = Wire(
            f"{componentPinLabel} to {controllerComponent.Label} {controllerGPIOPin}",
            color,
            width,
        )

        # get component's pin's endpoint coordinates
        componentEndpoint = self._getWireEndCoordinates(
            componentPinLabel, pinNumber, pinDict
        )
        # get controller's GPIO pin's endpoint coordinates
        controllerEndpoint, isEven = self._getGPIOEndpointCoordinates(controllerGPIOPin)

        # determine which direction to draw the wire from at controllerEndpoint
        isGoingLeft = True
        if isEven:
            isGoingLeft = False

        # create first line segment based off controller's gpio pin and the current minimum safe distance
        currentEndpoint = Coordinates(
            f"{controllerComponent.Label} GPIO Pin {controllerGPIOPin} Endpoint",
            (
                controllerEndpoint.x + self.RIGHT_MINIMUM_SAFE_DISTANCE
                if not isGoingLeft
                else 0
            ),
           controllerEndpoint.y
        )

        # add the first wire segment to the wire and grid
        self._addNewSegment(wire, controllerEndpoint, currentEndpoint)

        # increment the minimum safe distance for the next wire segment to be drawn
        self._IncrementMinimumSafeDistance(isGoingLeft)

        # iterate through alternating vertical and horizontal fixed length wire segments until the component's endpoint is reached
        while currentEndpoint != componentEndpoint:
            # determine the next wire segment's endpoint
            nextWireSegmentEndpoint = self._determineNextWireSegmentEndpoint(
                componentEndpoint, currentEndpoint
            )

            # add the next wire segment to the wire
            self._addNewSegment(wire, currentEndpoint, nextWireSegmentEndpoint)

        # return the wire to be drawn
        return wire

    def _addNewSegment(
        self, wire: Wire, endPoint1: Coordinates, endPoint2: Coordinates
    ):
        """
        Adds a new segment to the grid.
        """
        wire.addSegment(endPoint1, endPoint2)
        try:
            self.grid.setPixelLine(endPoint1, endPoint2)
        except:
            pass
            # TODO fix this horrendous error handling to account for minimal overlap scenarios (not implemented currently)

    def _IncrementMinimumSafeDistance(self, isGoingLeft: bool):
        """
        Increments the minimum safe distance for the next wire segment to be drawn. This will be used to ensure that the wires are drawn in a visually appealing way.
        """
        if isGoingLeft:
            self.LEFT_MINIMUM_SAFE_DISTANCE += self.ARBITRARY_DISTANCE
        else:
            self.RIGHT_MINIMUM_SAFE_DISTANCE += self.ARBITRARY_DISTANCE

    def _determineNextWireSegmentEndpoint(
        self, componentEndpoint: Coordinates, currentEndpoint: Coordinates
    ):
        """
        Determines the path of the wire between two endpoints gained from _getWireEndCoordinates and _getGPIOEndpointCoordinates.

        This path must be made up of WireSegment objects that will be used to draw the wire on the diagram. the wireSegments must be connected at right angles to each other to make the wire look neat and organized. this means that from one wire segment to the next, the x or y coordinate of the end of one segment must be the same as the x or y coordinate of the start of the next segment.

        A line segment should be as long as possible before turning to make the wire look neat and organized. Each line segement (and each pair of integer coordinates) should be added to the grid to ensure that the intersections are minimized and that the wire is drawn correctly.
        """
        # the wire will be drawn from the controllerEndpoint to the componentEndpoint

        # create first wire segement from controllerEndpoint to the right or left and arbitraty distance depending on isGoingLeft

        if self.grid.isLongestPath(componentEndpoint, currentEndpoint):
            # x distance is longer than y distance

            # if the wire seggment should be shorter than the standard distance (i.e. the wire segment is close to the component's endpoint), then the wire segment should be the distance between the currentEndpoint and the componentEndpoint
            coordinateDelta = min(
                self.wireSegmentLength, abs(componentEndpoint.x - currentEndpoint.x)
            )
            return Coordinates(currentEndpoint.x + coordinateDelta, currentEndpoint.y)

        else:
            # see above for explanation
            coordinateDelta = min(
                self.wireSegmentLength, abs(componentEndpoint.y - currentEndpoint.y)
            )
            return Coordinates(currentEndpoint.x, currentEndpoint.y + coordinateDelta)
            # y distance is longer than x distance

    def _getWireEndCoordinates(
        self, componentPinLabel: str, pinNumber: int, pinDict: dict
    ):
        """
        Given a pin number and its dictionary, this function will return the endpoint of the wire that will connect to the component's pin.
        This will be based on the LM and RM coordinates of the component's pin.
        """
        return self._calculateEndPoint(componentPinLabel, pinDict["LM"], pinDict["RM"])

    def _getGPIOEndpointCoordinates(self, physicalPinNumber: int):
        """
        Returns the endpoint of the wire that will connect to the GPIO pin of the Raspberry Pi. This will be based on the Usage key and its enum value within the pinDict found within the component's pinsLMRMCoordinates dictionary.

        The returned coordinate will indicate the center of the bottom part of the wire covering the pin. This will be used as the Raspberry Pi's endpoint of the wire.

        Returns a Coordinates object of the endpoint of the wire.
        """

        # the second value returned is a (very hacky) way to determine which side the gpio pin is on and therefore which direction to start drawing the wire from
        return (
            self._calculateEndPoint(
                f"GPIO Pin {physicalPinNumber}",
                self.controllerComponent.pinLMRMCoordinates[physicalPinNumber]["LM"],
                self.controllerComponent.pinLMRMCoordinates[physicalPinNumber]["RM"],
            ),
            physicalPinNumber % 2 == 0,
        )

    def _calculateEndPoint(
        self, pinName: str, LMCoordinates: Coordinates, RMCoordinates: Coordinates
    ):
        """
        Calculates the endpoint of the component's end of the wire based on the LM and RM coordinates of the component's pin.

        MAKE SURE THESE COORDINATES FORM A RECTANGLE THAT COVERS THE PIN BASED ON AESTHETIC PREFERENCES

        The returned coordinate will indicate the center of the top part of the wire covering the pin. This will be used as the component's endpoint of the wire.

        Returns a Coordinates object of the endpoint of the wire.
        """
        return Coordinates(
            f"{pinName}'s Endpoint",
            (LMCoordinates.x + RMCoordinates.x) / 2,
            LMCoordinates.y,
        )
