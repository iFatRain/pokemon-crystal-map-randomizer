from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Pewter
mapGroup = MapGroup.PEWTER
specificMap = Pewter.PEWTER_MART

class PEWTER_MART(IntEnum):
	def __str__(self):
		return str(self.value)

	PEWTER_CITY_3 = 1


class Pewter_Mart_Warp_Points(Enum): 

	PEWTER_MART_TO_PEWTER_CITY_3_WP = WarpInstruction( 
		getHex(PEWTER_MART.PEWTER_CITY_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


