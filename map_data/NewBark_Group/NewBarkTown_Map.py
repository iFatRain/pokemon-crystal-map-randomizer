from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, New_Bark

mapGroup = MapGroup.NEW_BARK
specificMap = New_Bark.NEW_BARK_TOWN

class NEW_BARK_TOWN(IntEnum):
    def __str__(self):
        return str(self.value)

    ELMS_LAB = 1
    PLAYERS_HOUSE_1F = 2
    PLAYERS_NEIGHBORS_HOUSE = 3
    ELMS_HOUSE = 4


class New_Bark_Warp_Points(Enum):

    # NEW_BARK_TO_ELMS_LAB_WP = WarpInstruction(
    #     getHex(NEW_BARK_TOWN.ELMS_LAB),
    #     getHex(mapGroup),
    #     getHex(specificMap),
    #     )

    NEW_BARK_TO_PLAYERS_NEIGHBORS_HOUSE_WP = WarpInstruction(
        getHex(NEW_BARK_TOWN.PLAYERS_NEIGHBORS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )

    NEW_BARK_TO_ELMS_HOUSE_WP = WarpInstruction(
        getHex(NEW_BARK_TOWN.ELMS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )

#     This is only for testing
#     NEW_BARK_TO_PLAYERS_HOUSE = WarpInstruction(
#         getHex(NEW_BARK_TOWN.PLAYERS_HOUSE_1F),
#         getHex(mapGroup),
#         getHex(specificMap),
#         
#     )

