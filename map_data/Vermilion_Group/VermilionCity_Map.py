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

	Vermilion_City_Fishing_Speech_House_Entrance_WP = WarpInstruction(
		getHex(VERMILION_CITY.VERMILION_FISHING_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Vermilion_City_Pokecenter_Entrance_WP = WarpInstruction(
		getHex(VERMILION_CITY.VERMILION_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Pokemon_Fan_Club_Entrance_WP = WarpInstruction(
		getHex(VERMILION_CITY.POKEMON_FAN_CLUB_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Vermilion_City_Magnet_Train_Speech_House_Entrance_WP = WarpInstruction(
		getHex(VERMILION_CITY.VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Vermilion_City_Mart_Entrance_WP = WarpInstruction(
		getHex(VERMILION_CITY.VERMILION_MART_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Vermilion_City_Digletts_Cave_Speech_House_Entrance_WP = WarpInstruction(
		getHex(VERMILION_CITY.VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Vermilion_City_Gym_Entrance_WP = WarpInstruction(
		getHex(VERMILION_CITY.VERMILION_GYM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Vermilion_City_To_Port_Passage_WP = WarpInstruction(
		getHex(VERMILION_CITY.VERMILION_PORT_PASSAGE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Vermilion_City_Digletts_Cave_Entrance_WP = WarpInstruction(
		getHex(VERMILION_CITY.DIGLETTS_CAVE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

