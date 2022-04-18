from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.LAVENDER_MART

class LAVENDER_MART(IntEnum):
	def __str__(self):
		return str(self.value)

	LAVENDER_TOWN_5 = 1


class Lavender_Mart_Warp_Points(Enum): 

	LAVENDER_MART_TO_LAVENDER_TOWN_5_WP = WarpInstruction( 
		getHex(LAVENDER_MART.LAVENDER_TOWN_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

