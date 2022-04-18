from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Pewter
mapGroup = MapGroup.PEWTER
specificMap = Pewter.PEWTER_NIDORAN_SPEECH_HOUSE

class PEWTER_NIDORAN_SPEECH_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	PEWTER_CITY_1 = 1


class Pewter_Nidoran_Speech_House_Warp_Points(Enum): 

	PEWTER_NIDORAN_SPEECH_HOUSE_TO_PEWTER_CITY_1_WP = WarpInstruction( 
		getHex(PEWTER_NIDORAN_SPEECH_HOUSE.PEWTER_CITY_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


