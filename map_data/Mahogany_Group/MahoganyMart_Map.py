from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.MAHOGANY_MART_1F

class MAHOGANY_MART_1F(IntEnum):
    def __str__(self):
        return str(self.value)

    MAHOGANY_TOWN = 1  # dual wide
    TEAM_ROCKET_BASE_B1F = 3


class Mahogany_Mart_Warp_Points(Enum):

    MAHOGANY_MART_1F_TO_MAHOGANY_TOWN_WP = WarpInstruction(
        getHex(MAHOGANY_MART_1F.MAHOGANY_TOWN),
        getHex(mapGroup),
        getHex(specificMap))

    MAHOGANY_MART_1F_TO_TEAM_ROCKET_BASE_B1F_WP = WarpInstruction(
        getHex(MAHOGANY_MART_1F.TEAM_ROCKET_BASE_B1F),
        getHex(mapGroup),
        getHex(specificMap))




