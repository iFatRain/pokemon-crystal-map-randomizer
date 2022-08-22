from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Azalea

mapGroup = MapGroup.AZALEA
specificMap = Azalea.AZALEA_TOWN

class AZALEA_TOWN(IntEnum):
    def __str__(self):
        return str(self.value)

    AZALEA_POKECENTER_1F = 1
    CHARCOAL_KILN = 2
    AZALEA_MART = 3
    KURTS_HOUSE = 4
    AZALEA_GYM = 5
    SLOWPOKE_WELL_B1F = 6
    ILEX_FOREST_AZALEA_GATE = 7  # dual wide



class Azalea_Town_Warp_Points(Enum):

    Azalea_Pokecenter_Entrance_WP = WarpInstruction(
        getHex(AZALEA_TOWN.AZALEA_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap))

    Charcoal_Kiln_Entrance_WP = WarpInstruction(
        getHex(AZALEA_TOWN.CHARCOAL_KILN),
        getHex(mapGroup),
        getHex(specificMap))

    Azalea_Mart_Entrance_WP = WarpInstruction(
        getHex(AZALEA_TOWN.AZALEA_MART),
        getHex(mapGroup),
        getHex(specificMap))

    Kurts_House_Entrance_WP = WarpInstruction(
        getHex(AZALEA_TOWN.KURTS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    Slowpoke_Well_B1F_Entrance_WP = WarpInstruction(
        getHex(AZALEA_TOWN.SLOWPOKE_WELL_B1F),
        getHex(mapGroup),
        getHex(specificMap))

    Azalea_Gym_Entrance_WP = WarpInstruction(
        getHex(AZALEA_TOWN.AZALEA_GYM),
        getHex(mapGroup),
        getHex(specificMap))

    Azalea_Town_Ilex_Forest_Gate_Azalea_Entrance_WP = WarpInstruction(
        getHex(AZALEA_TOWN.ILEX_FOREST_AZALEA_GATE),
        getHex(mapGroup),
        getHex(specificMap))

