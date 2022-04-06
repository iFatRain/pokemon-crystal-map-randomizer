from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_MAGNET_TRAIN_STATION

class GOLDENROD_MAGNET_TRAIN_STATION(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_CITY = 1  # dual wide


class Goldenrod_Magnet_Train_Station_Warp_Points(Enum):

    GOLDENROD_MAGNET_TRAIN_STATION_TO_GOLDENROD_CITY_WP = WarpInstruction(
        getHex(GOLDENROD_MAGNET_TRAIN_STATION.GOLDENROD_CITY),
        getHex(mapGroup),
        getHex(specificMap))