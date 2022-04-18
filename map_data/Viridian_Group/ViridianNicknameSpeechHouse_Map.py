from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Viridian
mapGroup = MapGroup.VIRIDIAN
specificMap = Viridian.VIRIDIAN_NICKNAME_SPEECH_HOUSE

class VIRIDIAN_NICKNAME_SPEECH_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	VIRIDIAN_CITY_2 = 1


class Viridian_Nickname_Speech_House_Warp_Points(Enum): 

	VIRIDIAN_NICKNAME_SPEECH_HOUSE_TO_VIRIDIAN_CITY_2_WP = WarpInstruction( 
		getHex(VIRIDIAN_NICKNAME_SPEECH_HOUSE.VIRIDIAN_CITY_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

