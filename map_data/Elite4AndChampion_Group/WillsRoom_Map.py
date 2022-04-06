from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Indigo

mapGroup = MapGroup.INDIGO
specificMap = Indigo.WILLS_ROOM

class WILLS_ROOM(IntEnum):
    def __str__(self):
        return str(self.value)

    INDIGO_PLATEAU_POKECENTER_1F = 1
    KOGAS_ROOM = 2 # dual wide


class Wills_Room_Warp_Points(Enum):

    WILLS_ROOM_TO_INDIGO_PLATEAU_POKECENTER_1F_WP = WarpInstruction(
        getHex(WILLS_ROOM.INDIGO_PLATEAU_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap))

    WILLS_ROOM_TO_KOGAS_ROOM_WP = WarpInstruction(
        getHex(WILLS_ROOM.KOGAS_ROOM),
        getHex(mapGroup),
        getHex(specificMap))