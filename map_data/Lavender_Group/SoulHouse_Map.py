from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.SOUL_HOUSE

class SOUL_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	LAVENDER_TOWN_6 = 1


class Soul_House_Warp_Points(Enum): 

	SOUL_HOUSE_TO_LAVENDER_TOWN_6_WP = WarpInstruction( 
		getHex(SOUL_HOUSE.LAVENDER_TOWN_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

