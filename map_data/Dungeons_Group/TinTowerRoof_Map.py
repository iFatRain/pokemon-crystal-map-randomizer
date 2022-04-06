from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fast_Ship

mapGroup = MapGroup.FAST_SHIP
specificMap = Fast_Ship.TIN_TOWER_ROOF

class TIN_TOWER_ROOF(IntEnum):
    def __str__(self):
        return str(self.value)

    TIN_TOWER_9F = 1


class Tin_Tower_Roof_Warp_Points(Enum):

    TIN_TOWER_ROOF_TO_TIN_TOWER_9F_WP = WarpInstruction(
        getHex(TIN_TOWER_ROOF.TIN_TOWER_9F),
        getHex(mapGroup),
        getHex(specificMap))

