import WiringDiagramScripts.WiringManager.Components.BaseClasses.Component as Component
import Coordinates


class PiGPIOPinHeader(Component):
    def __init__(self, name):
        self.imagePath = "./Images/PiGPIOPinHeader.png"
        self.Label = name + " Pi GPIO Pin Header"
        self.electricalValuesDict = {"Voltage Output": [3.3, 5]}

        self.pinsLMRMCoordinates = {
            1: {
                "Usage": "3.3V Power",
                "LM": Coordinates("LM Pin 1", 30, 15),
                "RM": Coordinates("RM Pin 1", 50, 35),
            },
            2: {
                "Usage": "5V Power",
                "LM": Coordinates("LM Pin 2", 30, 50),
                "RM": Coordinates("RM Pin 2", 50, 70),
            },
            3: {
                "Usage": "GPIO2",
                "LM": Coordinates("LM Pin 3", 30, 85),
                "RM": Coordinates("RM Pin 3", 50, 105),
            },
            4: {
                "Usage": "5V Power",
                "LM": Coordinates("LM Pin 4", 30, 120),
                "RM": Coordinates("RM Pin 4", 50, 140),
            },
            5: {
                "Usage": "GPIO3",
                "LM": Coordinates("LM Pin 5", 30, 155),
                "RM": Coordinates("RM Pin 5", 50, 175),
            },
            6: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 6", 30, 190),
                "RM": Coordinates("RM Pin 6", 50, 210),
            },
            7: {
                "Usage": "GPIO4",
                "LM": Coordinates("LM Pin 7", 30, 225),
                "RM": Coordinates("RM Pin 7", 50, 245),
            },
            8: {
                "Usage": "GPIO14",
                "LM": Coordinates("LM Pin 8", 30, 260),
                "RM": Coordinates("RM Pin 8", 50, 280),
            },
            9: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 9", 30, 295),
                "RM": Coordinates("RM Pin 9", 50, 315),
            },
            10: {
                "Usage": "GPIO15",
                "LM": Coordinates("LM Pin 10", 30, 330),
                "RM": Coordinates("RM Pin 10", 50, 350),
            },
            11: {
                "Usage": "GPIO17",
                "LM": Coordinates("LM Pin 11", 30, 365),
                "RM": Coordinates("RM Pin 11", 50, 385),
            },
            12: {
                "Usage": "GPIO18",
                "LM": Coordinates("LM Pin 12", 30, 400),
                "RM": Coordinates("RM Pin 12", 50, 420),
            },
            13: {
                "Usage": "GPIO27",
                "LM": Coordinates("LM Pin 13", 30, 435),
                "RM": Coordinates("RM Pin 13", 50, 455),
            },
            14: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 14", 30, 470),
                "RM": Coordinates("RM Pin 14", 50, 490),
            },
            15: {
                "Usage": "GPIO22",
                "LM": Coordinates("LM Pin 15", 30, 505),
                "RM": Coordinates("RM Pin 15", 50, 525),
            },
            16: {
                "Usage": "GPIO23",
                "LM": Coordinates("LM Pin 16", 30, 540),
                "RM": Coordinates("RM Pin 16", 50, 560),
            },
            17: {
                "Usage": "3.3V Power",
                "LM": Coordinates("LM Pin 17", 30, 575),
                "RM": Coordinates("RM Pin 17", 50, 595),
            },
            18: {
                "Usage": "GPIO24",
                "LM": Coordinates("LM Pin 18", 30, 610),
                "RM": Coordinates("RM Pin 18", 50, 630),
            },
            19: {
                "Usage": "GPIO10",
                "LM": Coordinates("LM Pin 19", 30, 645),
                "RM": Coordinates("RM Pin 19", 50, 665),
            },
            20: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 20", 30, 680),
                "RM": Coordinates("RM Pin 20", 50, 700),
            },
            21: {
                "Usage": "GPIO9",
                "LM": Coordinates("LM Pin 21", 30, 715),
                "RM": Coordinates("RM Pin 21", 50, 735),
            },
            22: {
                "Usage": "GPIO25",
                "LM": Coordinates("LM Pin 22", 30, 750),
                "RM": Coordinates("RM Pin 22", 50, 770),
            },
            23: {
                "Usage": "GPIO11",
                "LM": Coordinates("LM Pin 23", 30, 785),
                "RM": Coordinates("RM Pin 23", 50, 805),
            },
            24: {
                "Usage": "GPIO8",
                "LM": Coordinates("LM Pin 24", 30, 820),
                "RM": Coordinates("RM Pin 24", 50, 840),
            },
            25: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 25", 30, 855),
                "RM": Coordinates("RM Pin 25", 50, 875),
            },
            26: {
                "Usage": "GPIO7",
                "LM": Coordinates("LM Pin 26", 30, 890),
                "RM": Coordinates("RM Pin 26", 50, 910),
            },
            27: {
                "Usage": None,
                "LM": Coordinates("LM Pin 27", 30, 925),
                "RM": Coordinates("RM Pin 27", 50, 945),
            },
            28: {
                "Usage": None,
                "LM": Coordinates("LM Pin 28", 30, 960),
                "RM": Coordinates("RM Pin 28", 50, 980),
            },
            29: {
                "Usage": "GPIO5",
                "LM": Coordinates("LM Pin 29", 30, 995),
                "RM": Coordinates("RM Pin 29", 50, 1015),
            },
            30: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 30", 30, 1030),
                "RM": Coordinates("RM Pin 30", 50, 1050),
            },
            31: {
                "Usage": "GPIO6",
                "LM": Coordinates("LM Pin 31", 30, 1065),
                "RM": Coordinates("RM Pin 31", 50, 1085),
            },
            32: {
                "Usage": "GPIO12",
                "LM": Coordinates("LM Pin 32", 30, 1100),
                "RM": Coordinates("RM Pin 32", 50, 1120),
            },
            33: {
                "Usage": "GPIO13",
                "LM": Coordinates("LM Pin 33", 30, 1135),
                "RM": Coordinates("RM Pin 33", 50, 1155),
            },
            34: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 34", 30, 1170),
                "RM": Coordinates("RM Pin 34", 50, 1190),
            },
            35: {
                "Usage": "GPIO19",
                "LM": Coordinates("LM Pin 35", 30, 1205),
                "RM": Coordinates("RM Pin 35", 50, 1225),
            },
            36: {
                "Usage": "GPIO16",
                "LM": Coordinates("LM Pin 36", 30, 1240),
                "RM": Coordinates("RM Pin 36", 50, 1260),
            },
            37: {
                "Usage": "GPIO26",
                "LM": Coordinates("LM Pin 37", 30, 1275),
                "RM": Coordinates("RM Pin 37", 50, 1295),
            },
            38: {
                "Usage": "GPIO20",
                "LM": Coordinates("LM Pin 38", 30, 1310),
                "RM": Coordinates("RM Pin 38", 50, 1330),
            },
            39: {
                "Usage": "Ground",
                "LM": Coordinates("LM Pin 39", 30, 1345),
                "RM": Coordinates("RM Pin 39", 50, 1365),
            },
            40: {
                "Usage": "GPIO21",
                "LM": Coordinates("LM Pin 40", 30, 1380),
                "RM": Coordinates("RM Pin 40", 50, 1400),
            },
        }
