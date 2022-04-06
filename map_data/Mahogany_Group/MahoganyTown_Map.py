from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Mahogany

mapGroup = MapGroup.MAHOGANY
specificMap = Mahogany.MAHOGANY_TOWN

class MAHOGANY_TOWN(IntEnum):
    def __str__(self):
        return str(self.value)

    MAHOGANY_MART_1F = 1
    MAHOGANY_RED_GYARADOS_SPEECH_HOUSE = 2
    MAHOGANY_GYM = 3
    MAHOGANY_POKECENTER_1F = 4
    ROUTE_43_MAHOGANY_GATE = 5


class Mahogany_Town_Warp_Points(Enum):

    MAHOGANY_TOWN_TO_MAHOGANY_MART_1F_WP = WarpInstruction(
        getHex(MAHOGANY_TOWN.MAHOGANY_MART_1F),
        getHex(mapGroup),
        getHex(specificMap))

    MAHOGANY_TOWN_TO_MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_WP = WarpInstruction(
        getHex(MAHOGANY_TOWN.MAHOGANY_RED_GYARADOS_SPEECH_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    MAHOGANY_TOWN_TO_MAHOGANY_GYM_WP = WarpInstruction(
        getHex(MAHOGANY_TOWN.MAHOGANY_GYM),
        getHex(mapGroup),
        getHex(specificMap))

    MAHOGANY_TOWN_TO_MAHOGANY_POKECENTER_1F_WP = WarpInstruction(
        getHex(MAHOGANY_TOWN.MAHOGANY_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap))

    MAHOGANY_TOWN_TO_ROUTE_43_MAHOGANY_GATE_WP = WarpInstruction(
        getHex(MAHOGANY_TOWN.ROUTE_43_MAHOGANY_GATE),
        getHex(mapGroup),
        getHex(specificMap))


