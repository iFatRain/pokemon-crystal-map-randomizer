from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.CERULEAN_MART

class CERULEAN_MART(IntEnum):
	def __str__(self):
		return str(self.value)

	CERULEAN_CITY_6 = 1


class Cerulean_Mart_Warp_Points(Enum): 

	CERULEAN_MART_TO_CERULEAN_CITY_6_WP = WarpInstruction( 
		getHex(CERULEAN_MART.CERULEAN_CITY_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

