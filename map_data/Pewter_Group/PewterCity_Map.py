from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Pewter
mapGroup = MapGroup.PEWTER
specificMap = Pewter.PEWTER_CITY

class PEWTER_CITY(IntEnum):
	def __str__(self):
		return str(self.value)

	PEWTER_NIDORAN_SPEECH_HOUSE_1 = 1
	PEWTER_GYM_1 = 2
	PEWTER_MART_2 = 3
	PEWTER_POKECENTER_1F_1 = 4
	PEWTER_SNOOZE_SPEECH_HOUSE_1 = 5


class Pewter_City_Warp_Points(Enum): 

	PEWTER_CITY_TO_PEWTER_NIDORAN_SPEECH_HOUSE_1_WP = WarpInstruction( 
		getHex(PEWTER_CITY.PEWTER_NIDORAN_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	PEWTER_CITY_TO_PEWTER_GYM_1_WP = WarpInstruction( 
		getHex(PEWTER_CITY.PEWTER_GYM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	PEWTER_CITY_TO_PEWTER_MART_2_WP = WarpInstruction( 
		getHex(PEWTER_CITY.PEWTER_MART_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	PEWTER_CITY_TO_PEWTER_POKECENTER_1F_1_WP = WarpInstruction( 
		getHex(PEWTER_CITY.PEWTER_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	PEWTER_CITY_TO_PEWTER_SNOOZE_SPEECH_HOUSE_1_WP = WarpInstruction( 
		getHex(PEWTER_CITY.PEWTER_SNOOZE_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

