from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lake_Of_Rage

mapGroup = MapGroup.LAKE_OF_RAGE
specificMap = Lake_Of_Rage.LAKE_OF_RAGE_MAGIKARP_HOUSE

class LAKE_OF_RAGE_MAGIKARP_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    LAKE_OF_RAGE = 1  # dual wide


class Lake_Of_Rage_Magikarp_House_Warp_Points(Enum):

    LAKE_OF_RAGE_MAGIKARP_HOUSE_TO_LAKE_OF_RAGE_WP = WarpInstruction(
        getHex(LAKE_OF_RAGE_MAGIKARP_HOUSE.LAKE_OF_RAGE),
        getHex(mapGroup),
        getHex(specificMap))

