from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.CERULEAN_POLICE_STATION

class CERULEAN_POLICE_STATION(IntEnum):
	def __str__(self):
		return str(self.value)

	CERULEAN_CITY_2 = 1



class Cerulean_Police_Station_Warp_Points(Enum): 

	CERULEAN_POLICE_STATION_TO_CERULEAN_CITY_2_WP = WarpInstruction( 
		getHex(CERULEAN_POLICE_STATION.CERULEAN_CITY_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


