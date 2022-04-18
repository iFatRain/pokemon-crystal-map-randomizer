from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.SAFFRON_MAGNET_TRAIN_STATION

class SAFFRON_MAGNET_TRAIN_STATION(IntEnum):
	def __str__(self):
		return str(self.value)

	SAFFRON_CITY_6 = 1
	GOLDENROD_MAGNET_TRAIN_STATION_4 = 3
	GOLDENROD_MAGNET_TRAIN_STATION_3 = 4


class Saffron_Magnet_Train_Station_Warp_Points(Enum): 

	SAFFRON_MAGNET_TRAIN_STATION_TO_SAFFRON_CITY_6_WP = WarpInstruction( 
		getHex(SAFFRON_MAGNET_TRAIN_STATION.SAFFRON_CITY_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_MAGNET_TRAIN_STATION_TO_GOLDENROD_MAGNET_TRAIN_STATION_4_WP = WarpInstruction( 
		getHex(SAFFRON_MAGNET_TRAIN_STATION.GOLDENROD_MAGNET_TRAIN_STATION_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_MAGNET_TRAIN_STATION_TO_GOLDENROD_MAGNET_TRAIN_STATION_3_WP = WarpInstruction( 
		getHex(SAFFRON_MAGNET_TRAIN_STATION.GOLDENROD_MAGNET_TRAIN_STATION_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

