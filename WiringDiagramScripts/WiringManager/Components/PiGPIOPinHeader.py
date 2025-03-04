from Component import Component
from Coordinates import Coordinates
import os
from Utilities.DirectionEnum import DirectionEnum


class PiGPIOPinHeader(Component):
    def __init__(self, name:str, controllerKey:int = 0):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "Images\\PiGPIOImage.png")
        self.imagePath = filename
        self.Label = name + " Pi GPIO Pin Header"
        self.electricalValuesDict = {"Voltage Output": [3.3, 5]}
        self.controllerKey = controllerKey

        
        self.physicalToBCMDict = { # a dictionary of the available GPIO pins on the Raspberry Pi in BCM numbering
            1: '3.3V Power',
            2: '5V Power',
            3: '2',
            4: '5V Power',
            5: '3',
            6: 'Ground',
            7: '4',
            8: '14',
            9: 'Ground',
            10: '15',
            11: '17',
            12: '18',
            13: '27',
            14: 'Ground',
            15: '22',
            16: '23',
            17: '3.3V Power',
            18: '24',
            19: '10',
            20: 'Ground',
            21: '9',
            22: '25',
            23: '11',
            24: '8',
            25: 'Ground',
            26: '7',
            27: None,
            28: None,
            29: '5',
            30: 'Ground',
            31: '6',
            32: '12',
            33: '13',
            34: 'Ground',
            35: '19',
            36: '16',
            37: '26',
            38: '20',
            39: 'Ground',
            40: '21'
        }
        self.pinLMRMCoordinates = {
            1: {
                "Usage": "3.3V Power",
                "LM": Coordinates("LM Pin 1", 30, 15),
                "RM": Coordinates("RM Pin 1", 50, 35),
                "PinLocation": DirectionEnum.LEFT
            },
            2: {
                "Usage": "5V Power",
                "LM": Coordinates("LM Pin 2", 70, 15),
                "RM": Coordinates("RM Pin 2", 90, 35),
                "PinLocation": DirectionEnum.RIGHT
            },
            3: {
                "Usage": "2",
                "LM": Coordinates("LM Pin 3", 30, 55),
                "RM": Coordinates("RM Pin 3", 50, 75),
                "PinLocation": DirectionEnum.LEFT
            },
            4: {
                "Usage": "5V Power",
                "LM": Coordinates("LM Pin 4", 70, 55),
                "RM": Coordinates("RM Pin 4", 90, 75),
                "PinLocation": DirectionEnum.RIGHT
            },
            5: {
                "Usage": "3",
                "LM": Coordinates("LM Pin 5", 30, 95),
                "RM": Coordinates("RM Pin 5", 50, 115),
                "PinLocation": DirectionEnum.LEFT
            },
            6: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 6", 70, 95),
                "RM": Coordinates("RM Pin 6", 90, 115),
                "PinLocation": DirectionEnum.RIGHT
            },
            7: {
                "Usage": "4",
                "LM": Coordinates("LM Pin 7", 30, 135),
                "RM": Coordinates("RM Pin 7", 50, 155),
                "PinLocation": DirectionEnum.LEFT
            },
            8: {
                "Usage": "14",
                "LM": Coordinates("LM Pin 8", 70, 135),
                "RM": Coordinates("RM Pin 8", 90, 155),
                "PinLocation": DirectionEnum.RIGHT

            },
            9: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 9", 30, 175),
                "RM": Coordinates("RM Pin 9", 50, 195),
                "PinLocation": DirectionEnum.LEFT
            },
            10: {
                "Usage": "15",
                "LM": Coordinates("LM Pin 10", 70, 175),
                "RM": Coordinates("RM Pin 10", 90, 195),
                "PinLocation": DirectionEnum.RIGHT
            },
            11: {
                "Usage": "17",
                "LM": Coordinates("LM Pin 11", 30, 215),
                "RM": Coordinates("RM Pin 11", 50, 235),
                "PinLocation": DirectionEnum.LEFT
            },
            12: {
                "Usage": "18",
                "LM": Coordinates("LM Pin 12", 70, 215),
                "RM": Coordinates("RM Pin 12", 90, 235),
                "PinLocation": DirectionEnum.RIGHT
            },
            13: {
                "Usage": "27",
                "LM": Coordinates("LM Pin 13", 30, 255),
                "RM": Coordinates("RM Pin 13", 50, 275),
                "PinLocation": DirectionEnum.LEFT
            },
            14: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 14", 70, 255),
                "RM": Coordinates("RM Pin 14", 90, 275),
                "PinLocation": DirectionEnum.RIGHT
            },
            15: {
                "Usage": "22",
                "LM": Coordinates("LM Pin 15", 30, 295),
                "RM": Coordinates("RM Pin 15", 50, 315),
                "PinLocation": DirectionEnum.LEFT
            },
            16: {
                "Usage": "23",
                "LM": Coordinates("LM Pin 16", 70, 295),
                "RM": Coordinates("RM Pin 16", 90, 315),
                "PinLocation": DirectionEnum.RIGHT
            },
            17: {
                "Usage": "3.3V Power",
                "LM": Coordinates("LM Pin 17", 30, 335),
                "RM": Coordinates("RM Pin 17", 50, 355),
                "PinLocation": DirectionEnum.LEFT
            },
            18: {
                "Usage": "24",
                "LM": Coordinates("LM Pin 18", 70, 335),
                "RM": Coordinates("RM Pin 18", 90, 355),
                "PinLocation": DirectionEnum.RIGHT
            },
            19: {
                "Usage": "10",
                "LM": Coordinates("LM Pin 19", 30, 375),
                "RM": Coordinates("RM Pin 19", 50, 395),
                "PinLocation": DirectionEnum.LEFT
            },
            20: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 20", 70, 375),
                "RM": Coordinates("RM Pin 20", 90, 395),
                "PinLocation": DirectionEnum.RIGHT
            },
            21: {
                "Usage": "9",
                "LM": Coordinates("LM Pin 21", 30, 415),
                "RM": Coordinates("RM Pin 21", 50, 435),
                "PinLocation": DirectionEnum.LEFT
            },
            22: {
                "Usage": "25",
                "LM": Coordinates("LM Pin 22", 70, 415),
                "RM": Coordinates("RM Pin 22", 90, 435),
                "PinLocation": DirectionEnum.RIGHT
            },
            23: {
                "Usage": "11",
                "LM": Coordinates("LM Pin 23", 30, 455),
                "RM": Coordinates("RM Pin 23", 50, 475),
                "PinLocation": DirectionEnum.LEFT
            },
            
            24: {
                "Usage": "8",
                "LM": Coordinates("LM Pin 24", 70, 455),
                "RM": Coordinates("RM Pin 24", 90, 475),
                "PinLocation": DirectionEnum.RIGHT
            },
            25: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 25", 30, 495),
                "RM": Coordinates("RM Pin 25", 50, 515),
                "PinLocation": DirectionEnum.LEFT
            },
            26: {
                "Usage": "7",
                "LM": Coordinates("LM Pin 26", 70, 495),
                "RM": Coordinates("RM Pin 26", 90, 515),
                "PinLocation": DirectionEnum.RIGHT
            },
            27: {
                "Usage": None,
                "LM": Coordinates("LM Pin 27", 30, 535),
                "RM": Coordinates("RM Pin 27", 50, 555),
                "PinLocation": DirectionEnum.LEFT
            },
            28: {
                "Usage": None,
                "LM": Coordinates("LM Pin 28", 70, 535),
                "RM": Coordinates("RM Pin 28", 90, 555),
                "PinLocation": DirectionEnum.RIGHT
            },
            29: {
                "Usage": "5",
                "LM": Coordinates("LM Pin 29", 30, 575),
                "RM": Coordinates("RM Pin 29", 50, 595),
                "PinLocation": DirectionEnum.LEFT
            },
            30: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 30", 70, 575),
                "RM": Coordinates("RM Pin 30", 90, 595),
                "PinLocation": DirectionEnum.RIGHT
            },
            31: {
                "Usage": "6",
                "LM": Coordinates("LM Pin 31", 30, 615),
                "RM": Coordinates("RM Pin 31", 50, 635),
                "PinLocation": DirectionEnum.LEFT
            },
            32: {
                "Usage": "12",
                "LM": Coordinates("LM Pin 32", 70, 615),
                "RM": Coordinates("RM Pin 32", 90, 635),
                "PinLocation": DirectionEnum.RIGHT
            },
            33: {
                "Usage": "13",
                "LM": Coordinates("LM Pin 33", 30, 655),
                "RM": Coordinates("RM Pin 33", 50, 675),
                "PinLocation": DirectionEnum.LEFT
            },
            34: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 34", 70, 655),
                "RM": Coordinates("RM Pin 34", 90, 675),
                "PinLocation": DirectionEnum.RIGHT
            },
            35: {
                "Usage": "19",
                "LM": Coordinates("LM Pin 35", 30, 695),
                "RM": Coordinates("RM Pin 35", 50, 715),
                "PinLocation": DirectionEnum.LEFT
            },
            36: {
                "Usage": "16",
                "LM": Coordinates("LM Pin 36", 70, 695),
                "RM": Coordinates("RM Pin 36", 90, 715),
                "PinLocation": DirectionEnum.RIGHT
            },
            37: {
                "Usage": "26",
                "LM": Coordinates("LM Pin 37", 30, 735),
                "RM": Coordinates("RM Pin 37", 50, 755),
                "PinLocation": DirectionEnum.LEFT
            },
            38: {
                "Usage": "20",
                "LM": Coordinates("LM Pin 38", 70, 735),
                "RM": Coordinates("RM Pin 38", 90, 755),
                "PinLocation": DirectionEnum.RIGHT
            },
            39: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 39", 30, 775),
                "RM": Coordinates("RM Pin 39", 50, 795),
                "PinLocation": DirectionEnum.LEFT
            },
            40: {
                "Usage": "21",
                "LM": Coordinates("LM Pin 40", 70, 775),
                "RM": Coordinates("RM Pin 40", 90, 795),
                "PinLocation": DirectionEnum.RIGHT
            }
        }
        super().__init__(self.Label, self.imagePath, self.electricalValuesDict, self.pinLMRMCoordinates, isPowered=True, controllerKey=controllerKey)
