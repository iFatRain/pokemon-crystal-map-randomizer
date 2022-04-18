from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Pewter
mapGroup = MapGroup.PEWTER
specificMap = Pewter.PEWTER_SNOOZE_SPEECH_HOUSE

class PEWTER_SNOOZE_SPEECH_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	PEWTER_CITY_5 = 1


class Pewter_Snooze_Speech_House_Warp_Points(Enum): 

	PEWTER_SNOOZE_SPEECH_HOUSE_TO_PEWTER_CITY_5_WP = WarpInstruction( 
		getHex(PEWTER_SNOOZE_SPEECH_HOUSE.PEWTER_CITY_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

