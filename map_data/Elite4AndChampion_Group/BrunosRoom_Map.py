from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Indigo

mapGroup = MapGroup.INDIGO
specificMap = Indigo.BRUNOS_ROOM

class BRUNOS_ROOM(IntEnum):
    def __str__(self):
        return str(self.value)

    KOGAS_ROOM = 1  # dual wide
    KARENS_ROOM = 3 # dual wide


class Brunos_Room_Warp_Points(Enum):

    BRUNOS_ROOM_TO_KOGAS_ROOM_WP = WarpInstruction(
        getHex(BRUNOS_ROOM.KOGAS_ROOM),
        getHex(mapGroup),
        getHex(specificMap))

    BRUNOS_ROOM_TO_KARENS_ROOM_WP = WarpInstruction(
        getHex(BRUNOS_ROOM.KARENS_ROOM),
        getHex(mapGroup),
        getHex(specificMap))