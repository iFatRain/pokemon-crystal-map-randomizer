from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Indigo

mapGroup = MapGroup.INDIGO
specificMap = Indigo.LANCES_ROOM

class LANCES_ROOM(IntEnum):
    def __str__(self):
        return str(self.value)

    KARENS_ROOM = 1 # dual wide


class Lances_Room_Warp_Points(Enum):

    LANCES_ROOM_TO_KARENS_ROOM_WP = WarpInstruction(
        getHex(LANCES_ROOM.KARENS_ROOM),
        getHex(mapGroup),
        getHex(specificMap))
