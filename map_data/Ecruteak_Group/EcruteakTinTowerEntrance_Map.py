from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Ecruteak

mapGroup = MapGroup.ECRUTEAK
specificMap = Ecruteak.ECRUTEAK_TIN_TOWER_ENTRANCE

class ECRUTEAK_TIN_TOWER_ENTRANCE(IntEnum):
    def __str__(self):
        return str(self.value)

    ECRUTEAK_CITY = 1  # dual wide
    ECRUTEAK_TIN_TOWER_ENTRANCEA = 3
    ECRUTEAK_TIN_TOWER_ENTRANCEB = 4
    WISE_TRIOS_ROOM = 5

class Ecruteak_Tin_Tower_Entrance_Warp_Points(Enum):

    ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_CITY_WP = WarpInstruction(
        getHex(ECRUTEAK_TIN_TOWER_ENTRANCE.ECRUTEAK_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_TIN_TOWER_ENTRANCEA_WP = WarpInstruction(
        getHex(ECRUTEAK_TIN_TOWER_ENTRANCE.ECRUTEAK_TIN_TOWER_ENTRANCEA),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_TIN_TOWER_ENTRANCEB_WP = WarpInstruction(
        getHex(ECRUTEAK_TIN_TOWER_ENTRANCE.ECRUTEAK_TIN_TOWER_ENTRANCEB),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_TIN_TOWER_ENTRANCE_TO_WISE_TRIOS_ROOM_WP = WarpInstruction(
        getHex(ECRUTEAK_TIN_TOWER_ENTRANCE.WISE_TRIOS_ROOM),
        getHex(mapGroup),
        getHex(specificMap))

