from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fast_Ship

mapGroup = MapGroup.FAST_SHIP
specificMap = Fast_Ship.OLIVINE_PORT_PASSAGE

class OLIVINE_PORT_PASSAGE(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_CITY = 1
    OLIVINE_PORT_PASSAGE_A = 3
    OLIVINE_PORT_PASSAGE_B = 4
    OLIVINE_PORT = 5


class Olivine_Port_Passage_Warp_Points(Enum):
    OLIVINE_PORT_PASSAGE_TO_OLIVINE_CITY_WP = WarpInstruction(
        getHex(OLIVINE_PORT_PASSAGE.OLIVINE_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    # OLIVINE_PORT_PASSAGE_A_TO_OLIVINE_PORT_PASSAGE_WP = WarpInstruction(
    #     getHex(OLIVINE_PORT_PASSAGE.OLIVINE_PORT_PASSAGE_A),
    #     getHex(mapGroup),
    #     getHex(specificMap))
    #
    # OLIVINE_PORT_PASSAGE_B_TO_OLIVINE_PORT_PASSAGE_WP = WarpInstruction(
    #     getHex(OLIVINE_PORT_PASSAGE.OLIVINE_PORT_PASSAGE_B),
    #     getHex(mapGroup),
    #     getHex(specificMap))
    #
    # OLIVINE_PORT_PASSAGE_TO_OLIVINE_PORT_WP = WarpInstruction(
    #     getHex(OLIVINE_PORT_PASSAGE.OLIVINE_PORT),
    #     getHex(mapGroup),
    #     getHex(specificMap))
