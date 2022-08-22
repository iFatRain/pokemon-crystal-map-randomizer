from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Vermilion
mapGroup = MapGroup.VERMILION
specificMap = Vermilion.VERMILION_MART

class VERMILION_MART(IntEnum):
	def __str__(self):
		return str(self.value)

	VERMILION_CITY_5 = 1


class Vermilion_Mart_Warp_Points(Enum): 

	Vermilion_City_Mart_Exit_WP = WarpInstruction(
		getHex(VERMILION_MART.VERMILION_CITY_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


