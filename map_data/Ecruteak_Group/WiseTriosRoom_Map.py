from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Ecruteak

mapGroup = MapGroup.ECRUTEAK
specificMap = Ecruteak.WISE_TRIOS_ROOM

class WISE_TRIOS_ROOM(IntEnum):
    def __str__(self):
        return str(self.value)

    ECRUTEAK_CITY = 1  # dual wide
    ECRUTEAK_TIN_TOWER_ENTRANCE = 3


class Wise_Trios_Room_Warp_Points(Enum):

    WISE_TRIOS_ROOM_TO_ECRUTEAK_CITY_WP = WarpInstruction(
        getHex(WISE_TRIOS_ROOM.ECRUTEAK_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    WISE_TRIOS_ROOM_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_WP = WarpInstruction(
        getHex(WISE_TRIOS_ROOM.ECRUTEAK_TIN_TOWER_ENTRANCE),
        getHex(mapGroup),
        getHex(specificMap))