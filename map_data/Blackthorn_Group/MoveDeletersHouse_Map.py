from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Blackthorn

mapGroup = MapGroup.BLACKTHORN
specificMap = Blackthorn.MOVE_DELETERS_HOUSE


class MOVE_DELETERS_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    BLACKTHORN_CITY = 1


class Move_Deleters_House_Warp_Points(Enum):

    MOVE_DELETERS_HOUSE_TO_BLACKTHORN_CITY_WP = WarpInstruction(
        getHex(MOVE_DELETERS_HOUSE.BLACKTHORN_CITY),
        getHex(mapGroup),
        getHex(specificMap))
