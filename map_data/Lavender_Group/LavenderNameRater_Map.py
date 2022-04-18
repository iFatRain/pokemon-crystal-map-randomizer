from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.LAVENDER_NAME_RATER

class LAVENDER_NAME_RATER(IntEnum):
	def __str__(self):
		return str(self.value)

	LAVENDER_TOWN_4 = 1


class Lavender_Name_Rater_Warp_Points(Enum): 

	LAVENDER_NAME_RATER_TO_LAVENDER_TOWN_4_WP = WarpInstruction( 
		getHex(LAVENDER_NAME_RATER.LAVENDER_TOWN_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

