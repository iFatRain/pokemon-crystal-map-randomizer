from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Azalea

mapGroup = MapGroup.AZALEA
specificMap = Azalea.KURTS_HOUSE

class KURTS_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    AZALEA_TOWN = 1  # dual wide


class Kurts_House_Warp_Points(Enum):

    Kurts_House_Exit_WP = WarpInstruction(
        getHex(KURTS_HOUSE.AZALEA_TOWN),
        getHex(mapGroup),
        getHex(specificMap))