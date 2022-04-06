from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Azalea

mapGroup = MapGroup.AZALEA
specificMap = Azalea.AZALEA_POKECENTER_1F

class AZALEA_POKECENTER(IntEnum):
    def __str__(self):
        return str(self.value)

    AZALEA_TOWN = 1  # dual wide
    POKECENTER_2F = 3


class Azalea_Pokecenter_Warp_Points(Enum):

    AZALEA_POKECENTER_TO_AZALEA_TOWN_WP = WarpInstruction(
        getHex(AZALEA_POKECENTER.AZALEA_TOWN),
        getHex(mapGroup),
        getHex(specificMap))

    AZALEA_POKECENTER_TO_AZALEA_POKECENTER_2F_WP = WarpInstruction(
        getHex(AZALEA_POKECENTER.POKECENTER_2F),
        getHex(mapGroup),
        getHex(specificMap))
