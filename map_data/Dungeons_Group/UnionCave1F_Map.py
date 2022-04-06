from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.UNION_CAVE_1F

class UNION_CAVE_1F(IntEnum):
    def __str__(self):
        return str(self.value)

    UNION_CAVE_B1FA = 1
    UNION_CAVE_B1FB = 2
    ROUTE_33 = 3
    ROUTE_32 = 4


class Union_Cave_1F_Warp_Points(Enum):

    UNION_CAVE_1F_TO_UNION_CAVE_B1FA_WP = WarpInstruction(
        getHex(UNION_CAVE_1F.UNION_CAVE_B1FA),
        getHex(mapGroup),
        getHex(specificMap))

    UNION_CAVE_1F_TO_UNION_CAVE_B1FB_WP = WarpInstruction(
        getHex(UNION_CAVE_1F.UNION_CAVE_B1FB),
        getHex(mapGroup),
        getHex(specificMap))

    UNION_CAVE_1F_TO_ROUTE_33_WP = WarpInstruction(
        getHex(UNION_CAVE_1F.ROUTE_33),
        getHex(mapGroup),
        getHex(specificMap))

    UNION_CAVE_1F_TO_ROUTE_32_WP = WarpInstruction(
        getHex(UNION_CAVE_1F.ROUTE_32),
        getHex(mapGroup),
        getHex(specificMap))

