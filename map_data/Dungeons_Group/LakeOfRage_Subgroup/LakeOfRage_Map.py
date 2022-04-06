from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lake_Of_Rage

mapGroup = MapGroup.LAKE_OF_RAGE
specificMap = Lake_Of_Rage.LAKE_OF_RAGE

class LAKE_OF_RAGE(IntEnum):
    def __str__(self):
        return str(self.value)

    LAKE_OF_RAGE_HIDDEN_POWER_HOUSE = 1
    LAKE_OF_RAGE_MAGIKARP_HOUSE = 2


class Lake_Of_Rage_Warp_Points(Enum):

    LAKE_OF_RAGE_TO_LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_WP = WarpInstruction(
        getHex(LAKE_OF_RAGE.LAKE_OF_RAGE_HIDDEN_POWER_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    LAKE_OF_RAGE_TO_LAKE_OF_RAGE_MAGIKARP_HOUSE_WP = WarpInstruction(
        getHex(LAKE_OF_RAGE.LAKE_OF_RAGE_MAGIKARP_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))


