from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.CERULEAN_CITY

class CERULEAN_CITY(IntEnum):
	def __str__(self):
		return str(self.value)

	CERULEAN_GYM_BADGE_SPEECH_HOUSE_1 = 1
	CERULEAN_POLICE_STATION_1 = 2
	CERULEAN_TRADE_SPEECH_HOUSE_1 = 3
	CERULEAN_POKECENTER_1F_1 = 4
	CERULEAN_GYM_1 = 5
	CERULEAN_MART_2 = 6


class Cerulean_City_Warp_Points(Enum): 

	CERULEAN_CITY_TO_CERULEAN_GYM_BADGE_SPEECH_HOUSE_1_WP = WarpInstruction( 
		getHex(CERULEAN_CITY.CERULEAN_GYM_BADGE_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CERULEAN_CITY_TO_CERULEAN_POLICE_STATION_1_WP = WarpInstruction( 
		getHex(CERULEAN_CITY.CERULEAN_POLICE_STATION_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CERULEAN_CITY_TO_CERULEAN_TRADE_SPEECH_HOUSE_1_WP = WarpInstruction( 
		getHex(CERULEAN_CITY.CERULEAN_TRADE_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CERULEAN_CITY_TO_CERULEAN_POKECENTER_1F_1_WP = WarpInstruction( 
		getHex(CERULEAN_CITY.CERULEAN_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CERULEAN_CITY_TO_CERULEAN_GYM_1_WP = WarpInstruction( 
		getHex(CERULEAN_CITY.CERULEAN_GYM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CERULEAN_CITY_TO_CERULEAN_MART_2_WP = WarpInstruction( 
		getHex(CERULEAN_CITY.CERULEAN_MART_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

