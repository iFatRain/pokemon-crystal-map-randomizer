from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES

class GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_UNDERGROUND = 1 # Top right on map
    GOLDENROD_UNDERGROUND_WAREHOUSE = 2  # DUAL WIDE Double door top right 5
    GOLDENROD_UNDERGROUND_SOUTH = 4 #To underground corridor NOT SOUTH CITY 15
    GOLDENROD_CITY_SOUTH = 5  # DUAL WIDE 20
    GOLDENROD_UNDERGROUND_NORTH = 7 # 30
    GOLDENROD_CITY_NORTH = 8  # DUAL WIDE 35



class Goldenrod_Underground_Switch_Room_Entrances_Warp_Points(Enum):

    # This is the entrance of the switch room section (from the room behind basement key)
    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_WP = WarpInstruction(
        getHex(GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES.GOLDENROD_UNDERGROUND),
        getHex(mapGroup),
        getHex(specificMap))

    # This is the double door exit to the northern Goldenrod entrance
    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_NORTH_WP = WarpInstruction(
        getHex(GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES.GOLDENROD_CITY_NORTH),
        getHex(mapGroup),
        getHex(specificMap))

    # This is the double door exit to the southern Goldenrod entrance
    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_SOUTH_WP = WarpInstruction(
            getHex(GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES.GOLDENROD_CITY_SOUTH),
            getHex(mapGroup),
            getHex(specificMap))

    # This is the stair in northern room entrance to enter the underground (where you use basement key)
    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_NORTH_WP = WarpInstruction(
        getHex(GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES.GOLDENROD_UNDERGROUND_NORTH),
        getHex(mapGroup),
        getHex(specificMap))

    # This is the stair in southern room entrance to enter the underground (where you use basement key)
    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_SOUTH_WP = WarpInstruction(
        getHex(GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES.GOLDENROD_UNDERGROUND_SOUTH),
        getHex(mapGroup),
        getHex(specificMap))

    # MORE WARPS TO BE FILLED OUT LATER