from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Indigo

mapGroup = MapGroup.INDIGO
specificMap = Indigo.KOGAS_ROOM

class KOGAS_ROOM(IntEnum):
    def __str__(self):
        return str(self.value)

    WILLS_ROOM = 1  # dual wide
    BRUNOS_ROOM = 3 # dual wide


class Kogas_Room_Warp_Points(Enum):

    KOGAS_ROOM_TO_WILLS_ROOM_WP = WarpInstruction(
        getHex(KOGAS_ROOM.WILLS_ROOM),
        getHex(mapGroup),
        getHex(specificMap))

    KOGAS_ROOM_TO_BRUNOS_ROOM_WP = WarpInstruction(
        getHex(KOGAS_ROOM.BRUNOS_ROOM),
        getHex(mapGroup),
        getHex(specificMap))