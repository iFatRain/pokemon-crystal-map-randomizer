from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.TIN_TOWER_1F

class TIN_TOWER_1F(IntEnum):
    def __str__(self):
        return str(self.value)

    ECRUTEAK_CITY = 1  # dual wide
    TIN_TOWER_2F = 3


class Tin_Tower_1F_Warp_Points(Enum):

    TIN_TOWER_1F_TO_ECRUTEAK_CITY_WP = WarpInstruction(
        getHex(TIN_TOWER_1F.ECRUTEAK_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    TIN_TOWER_1F_TO_TIN_TOWER_2F_WP = WarpInstruction(
        getHex(TIN_TOWER_1F.TIN_TOWER_2F),
        getHex(mapGroup),
        getHex(specificMap))

