from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.DARK_CAVE_VIOLET_ENTRANCE

class DARK_CAVE_VIOLET_ENTRANCE(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_31 = 1
    DARK_CAVE_BLACKTHORN_ENTRANCE = 2
    ROUTE_46 = 3


class Dark_Cave_Violet_Entrance_Warp_Points(Enum):

    DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_31_WP = WarpInstruction(
        getHex(DARK_CAVE_VIOLET_ENTRANCE.ROUTE_31),
        getHex(mapGroup),
        getHex(specificMap),
        )

    DARK_CAVE_VIOLET_ENTRANCE_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_WP = WarpInstruction(
        getHex(DARK_CAVE_VIOLET_ENTRANCE.DARK_CAVE_BLACKTHORN_ENTRANCE),
        getHex(mapGroup),
        getHex(specificMap),
        )

    DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_46_WP = WarpInstruction(
        getHex(DARK_CAVE_VIOLET_ENTRANCE.ROUTE_46),
        getHex(mapGroup),
        getHex(specificMap),
        )
