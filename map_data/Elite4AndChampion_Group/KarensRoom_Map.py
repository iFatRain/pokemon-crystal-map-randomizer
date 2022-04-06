from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Indigo

mapGroup = MapGroup.INDIGO
specificMap = Indigo.KARENS_ROOM

class KARENS_ROOM(IntEnum):
    def __str__(self):
        return str(self.value)

    BRUNOS_ROOM = 1  # dual wide
    LANCES_ROOM = 3 # dual wide


class Karens_Room_Warp_Points(Enum):

    KARENS_ROOM_TO_BRUNOS_ROOM_WP = WarpInstruction(
        getHex(KARENS_ROOM.BRUNOS_ROOM),
        getHex(mapGroup),
        getHex(specificMap))

    KARENS_ROOM_TO_LANCES_ROOM_WP = WarpInstruction(
        getHex(KARENS_ROOM.LANCES_ROOM),
        getHex(mapGroup),
        getHex(specificMap))