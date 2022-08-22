from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cianwood

mapGroup = MapGroup.CIANWOOD
specificMap = Cianwood.CIANWOOD_CITY

class CIANWOOD_CITY(IntEnum):
    def __str__(self):
        return str(self.value)

    MANIAS_HOUSE = 1
    CIANWOOD_GYM = 2
    CIANWOOD_POKECENTER_1F = 3
    CIANWOOD_PHARMACY = 4
    CIANWOOD_PHOTO_STUDIO = 5
    CIANWOOD_LUGIA_SPEECH_HOUSE = 6
    POKE_SEERS_HOUSE = 7


class Cianwood_City_Warp_Points(Enum):

    Cianwood_City_Shuckle_House_Entrance_WP = WarpInstruction(
        getHex(CIANWOOD_CITY.MANIAS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    Cianwood_City_Gym_Entrance_WP = WarpInstruction(
        getHex(CIANWOOD_CITY.CIANWOOD_GYM),
        getHex(mapGroup),
        getHex(specificMap))

    Cianwood_City_Pokecenter_Entrance_WP = WarpInstruction(
        getHex(CIANWOOD_CITY.CIANWOOD_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap))

    Cianwood_City_Pharmacy_Entrance_WP = WarpInstruction(
        getHex(CIANWOOD_CITY.CIANWOOD_PHARMACY),
        getHex(mapGroup),
        getHex(specificMap))

    Cianwood_City_Photo_Studio_Entrance_WP = WarpInstruction(
        getHex(CIANWOOD_CITY.CIANWOOD_PHOTO_STUDIO),
        getHex(mapGroup),
        getHex(specificMap))

    Cianwood_City_Lugia_Speech_House_Entrance_WP = WarpInstruction(
        getHex(CIANWOOD_CITY.CIANWOOD_LUGIA_SPEECH_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    Cianwood_City_Poke_Seers_House_Entrance_WP = WarpInstruction(
        getHex(CIANWOOD_CITY.POKE_SEERS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))
