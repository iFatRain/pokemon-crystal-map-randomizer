from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.GOLDENROD_UNDERGROUND

class GOLDENROD_UNDERGROUND(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_NORTH = 1 #top stair
    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH = 2 #Bottom stair
    GOLDENROD_UNDERGROUND_KEY_DOOR = 3 #Basement key door
    GOLDENROD_UNDERGROUND_WAREHOUSE_STAIR = 4 #dual width in small room
    GOLDENROD_UNDERGROUND_SWITCH_ROOM = 6 #single stair in small room
#123 is a hub, 4 and 6 are corridor


class Goldenrod_Underground_Warp_Points(Enum):

    GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_NORTH_WP = WarpInstruction(
        getHex(GOLDENROD_UNDERGROUND.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_NORTH),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH_WP = WarpInstruction(
        getHex(GOLDENROD_UNDERGROUND.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_KEY_DOOR_WP = WarpInstruction(
        getHex(GOLDENROD_UNDERGROUND.GOLDENROD_UNDERGROUND_KEY_DOOR),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_STAIR_WP = WarpInstruction(
        getHex(GOLDENROD_UNDERGROUND.GOLDENROD_UNDERGROUND_WAREHOUSE_STAIR),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_WP = WarpInstruction(
        getHex(GOLDENROD_UNDERGROUND.GOLDENROD_UNDERGROUND_SWITCH_ROOM),
        getHex(mapGroup),
        getHex(specificMap))

    # MORE WARPS TO BE FILLED OUT LATER