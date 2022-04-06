from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.GOLDENROD_UNDERGROUND_WAREHOUSE

class GOLDENROD_UNDERGROUND_WAREHOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_DEPT_STORE_B1F = 3


class Goldenrod_Underground_Warehouse_Warp_Points(Enum):


    GOLDENROD_UNDERGROUND_WAREHOUSE_TO_GOLDENROD_DEPT_STORE_B1F_WP = WarpInstruction(
        getHex(GOLDENROD_UNDERGROUND_WAREHOUSE.GOLDENROD_DEPT_STORE_B1F),
        getHex(mapGroup),
        getHex(specificMap)
    )