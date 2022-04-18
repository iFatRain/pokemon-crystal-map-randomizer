from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Vermilion
mapGroup = MapGroup.VERMILION
specificMap = Vermilion.VERMILION_CITY

class VERMILION_CITY(IntEnum):
	def __str__(self):
		return str(self.value)

	VERMILION_FISHING_SPEECH_HOUSE_1 = 1
	VERMILION_POKECENTER_1F_1 = 2
	POKEMON_FAN_CLUB_1 = 3
	VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_1 = 4
	VERMILION_MART_2 = 5
	VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_1 = 6
	VERMILION_GYM_1 = 7
	VERMILION_PORT_PASSAGE_1 = 8
	DIGLETTS_CAVE_1 = 10


class Vermilion_City_Warp_Points(Enum): 

	VERMILION_CITY_TO_VERMILION_FISHING_SPEECH_HOUSE_1_WP = WarpInstruction( 
		getHex(VERMILION_CITY.VERMILION_FISHING_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VERMILION_CITY_TO_VERMILION_POKECENTER_1F_1_WP = WarpInstruction( 
		getHex(VERMILION_CITY.VERMILION_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VERMILION_CITY_TO_POKEMON_FAN_CLUB_1_WP = WarpInstruction( 
		getHex(VERMILION_CITY.POKEMON_FAN_CLUB_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VERMILION_CITY_TO_VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_1_WP = WarpInstruction( 
		getHex(VERMILION_CITY.VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VERMILION_CITY_TO_VERMILION_MART_2_WP = WarpInstruction( 
		getHex(VERMILION_CITY.VERMILION_MART_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VERMILION_CITY_TO_VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_1_WP = WarpInstruction( 
		getHex(VERMILION_CITY.VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VERMILION_CITY_TO_VERMILION_GYM_1_WP = WarpInstruction( 
		getHex(VERMILION_CITY.VERMILION_GYM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VERMILION_CITY_TO_VERMILION_PORT_PASSAGE_1_WP = WarpInstruction( 
		getHex(VERMILION_CITY.VERMILION_PORT_PASSAGE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VERMILION_CITY_TO_DIGLETTS_CAVE_1_WP = WarpInstruction( 
		getHex(VERMILION_CITY.DIGLETTS_CAVE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

