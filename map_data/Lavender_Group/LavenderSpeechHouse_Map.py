from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.LAVENDER_SPEECH_HOUSE

class LAVENDER_SPEECH_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	LAVENDER_TOWN_3 = 1


class Lavender_Speech_House_Warp_Points(Enum): 

	LAVENDER_SPEECH_HOUSE_TO_LAVENDER_TOWN_3_WP = WarpInstruction( 
		getHex(LAVENDER_SPEECH_HOUSE.LAVENDER_TOWN_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

