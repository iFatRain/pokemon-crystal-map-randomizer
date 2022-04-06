from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.BURNED_TOWER_1F

class BURNED_TOWER_1F(IntEnum):
    def __str__(self):
        return str(self.value)

    ECRUTEAK_CITY = 1
    BURNED_TOWER_B1F = 3


class Burned_Tower_1F_Warp_Points(Enum):

    BURNED_TOWER_1F_TO_ECRUTEAK_CITY_WP = WarpInstruction(
        getHex(BURNED_TOWER_1F.ECRUTEAK_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    BURNED_TOWER_1F_TO_BURNED_TOWER_B1F_WP = WarpInstruction(
        getHex(BURNED_TOWER_1F.BURNED_TOWER_B1F),
        getHex(mapGroup),
        getHex(specificMap))

