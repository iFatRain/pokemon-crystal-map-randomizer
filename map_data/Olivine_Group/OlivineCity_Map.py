from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex, WarpLink
from map_data.map_constants import MapGroup, Olivine

mapGroup = MapGroup.OLIVINE
specificMap = Olivine.OLIVINE_CITY

class OLIVINE_CITY(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_POKECENTER_1F = 1
    OLIVINE_GYM = 2
    OLIVINE_TIMS_HOUSE = 3
    OLIVINE_PUNISHMENT_SPEECH_HOUSE = 5
    OLIVINE_GOOD_ROD_HOUSE = 6
    OLIVINE_CAFE = 7
    OLIVINE_MART = 8
    OLIVINE_LIGHTHOUSE_1F = 9
    OLIVINE_PORT_PASSAGE = 10  # dual wide


class Olivine_City_Warp_Points(Enum):

    OLIVINE_CITY_TO_OLIVINE_POKECENTER_1F_WP = WarpInstruction(
        getHex(OLIVINE_CITY.OLIVINE_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap),
        )

    OLIVINE_CITY_TO_OLIVINE_GYM_WP = WarpInstruction(
        getHex(OLIVINE_CITY.OLIVINE_GYM),
        getHex(mapGroup),
        getHex(specificMap),
        )

    OLIVINE_CITY_TO_OLIVINE_TIMS_HOUSE_WP = WarpInstruction(
        getHex(OLIVINE_CITY.OLIVINE_TIMS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )


    OLIVINE_CITY_TO_OLIVINE_PUNISHMENT_SPEECH_HOUSE_WP = WarpInstruction(
        getHex(OLIVINE_CITY.OLIVINE_PUNISHMENT_SPEECH_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )

    OLIVINE_CITY_TO_OLIVINE_GOOD_ROD_HOUSE_WP = WarpInstruction(
        getHex(OLIVINE_CITY.OLIVINE_GOOD_ROD_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )

    OLIVINE_CITY_TO_OLIVINE_CAFE_WP = WarpInstruction(
        getHex(OLIVINE_CITY.OLIVINE_CAFE),
        getHex(mapGroup),
        getHex(specificMap),
        )

    OLIVINE_CITY_TO_OLIVINE_MART_WP = WarpInstruction(
        getHex(OLIVINE_CITY.OLIVINE_MART),
        getHex(mapGroup),
        getHex(specificMap),
        )

    OLIVINE_CITY_TO_OLIVINE_LIGHTHOUSE_1F_WP = WarpInstruction(
        getHex(OLIVINE_CITY.OLIVINE_LIGHTHOUSE_1F),
        getHex(mapGroup),
        getHex(specificMap),
        )

    OLIVINE_CITY_TO_OLIVINE_PORT_PASSAGE_WP = WarpInstruction(
        getHex(OLIVINE_CITY.OLIVINE_PORT_PASSAGE),
        getHex(mapGroup),
        getHex(specificMap),
        )


