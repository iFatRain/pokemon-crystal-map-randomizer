from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.DAY_CARE

class DAY_CARE(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_34A = 1  # dual wide
    ROUTE_34B = 3  # dual wide 10



class Day_Care_Warp_Points(Enum):

    DAY_CARE_TO_ROUTE_34_FRONT_WP = WarpInstruction(
        getHex(DAY_CARE.ROUTE_34A),
        getHex(mapGroup),
        getHex(specificMap))

    DAY_CARE_TO_ROUTE_34_SIDE_WP = WarpInstruction(
        getHex(DAY_CARE.ROUTE_34B),
        getHex(mapGroup),
        getHex(specificMap))


