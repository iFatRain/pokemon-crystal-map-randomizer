from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Viridian
mapGroup = MapGroup.VIRIDIAN
specificMap = Viridian.VIRIDIAN_MART

class VIRIDIAN_MART(IntEnum):
	def __str__(self):
		return str(self.value)

	VIRIDIAN_CITY_4 = 1


class Viridian_Mart_Warp_Points(Enum): 

	VIRIDIAN_MART_TO_VIRIDIAN_CITY_4_WP = WarpInstruction( 
		getHex(VIRIDIAN_MART.VIRIDIAN_CITY_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

