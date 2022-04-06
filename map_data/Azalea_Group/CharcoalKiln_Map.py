from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Azalea

mapGroup = MapGroup.AZALEA
specificMap = Azalea.CHARCOAL_KILN

class CHARCOAL_KILN(IntEnum):
    def __str__(self):
        return str(self.value)

    AZALEA_TOWN = 1  # dual wide


class Charcoal_Kiln_Warp_Points(Enum):

    CHARCOAL_KILN_TO_AZALEA_TOWN_WP = WarpInstruction(
        getHex(CHARCOAL_KILN.AZALEA_TOWN),
        getHex(mapGroup),
        getHex(specificMap))