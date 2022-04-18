from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.SAFFRON_MART

class SAFFRON_MART(IntEnum):
	def __str__(self):
		return str(self.value)

	SAFFRON_CITY_3 = 1


class Saffron_Mart_Warp_Points(Enum): 

	SAFFRON_MART_TO_SAFFRON_CITY_3_WP = WarpInstruction( 
		getHex(SAFFRON_MART.SAFFRON_CITY_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


