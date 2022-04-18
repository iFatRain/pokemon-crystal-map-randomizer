from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.CERULEAN_GYM_BADGE_SPEECH_HOUSE

class CERULEAN_GYM_BADGE_SPEECH_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	CERULEAN_CITY_1 = 1


class Cerulean_Gym_Badge_Speech_House_Warp_Points(Enum): 

	CERULEAN_GYM_BADGE_SPEECH_HOUSE_TO_CERULEAN_CITY_1_WP = WarpInstruction( 
		getHex(CERULEAN_GYM_BADGE_SPEECH_HOUSE.CERULEAN_CITY_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

