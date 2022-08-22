from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cianwood

mapGroup = MapGroup.CIANWOOD
specificMap = Cianwood.CIANWOOD_PHOTO_STUDIO

class CIANWOOD_PHOTO_STUDIO(IntEnum):
    def __str__(self):
        return str(self.value)

    CIANWOOD_CITY = 1  # dual wide


class Cianwood_Photo_Studio_Warp_Points(Enum):

    Cianwood_City_Photo_Studio_Exit_WP = WarpInstruction(
        getHex(CIANWOOD_PHOTO_STUDIO.CIANWOOD_CITY),
        getHex(mapGroup),
        getHex(specificMap))