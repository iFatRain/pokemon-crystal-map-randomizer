from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cianwood

mapGroup = MapGroup.CIANWOOD
specificMap = Cianwood.CIANWOOD_PHARMACY

class CIANWOOD_PHARMACY(IntEnum):
    def __str__(self):
        return str(self.value)

    CIANWOOD_CITY = 1  # dual wide


class Cianwood_Pharmacy_Warp_Points(Enum):

    CIANWOOD_PHARMACY_TO_CIANWOOD_CITY_WP = WarpInstruction(
        getHex(CIANWOOD_PHARMACY.CIANWOOD_CITY),
        getHex(mapGroup),
        getHex(specificMap))