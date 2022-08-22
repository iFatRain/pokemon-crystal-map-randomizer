from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Azalea

mapGroup = MapGroup.AZALEA
specificMap = Azalea.AZALEA_MART

class AZALEA_MART(IntEnum):
    def __str__(self):
        return str(self.value)

    AZALEA_TOWN = 1  # dual wide


class Azalea_Mart_Warp_Points(Enum):

    Azalea_Mart_Exit_WP = WarpInstruction(
        getHex(AZALEA_MART.AZALEA_TOWN),
        getHex(mapGroup),
        getHex(specificMap))