from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Viridian
mapGroup = MapGroup.VIRIDIAN
specificMap = Viridian.VIRIDIAN_CITY

class VIRIDIAN_CITY(IntEnum):
	def __str__(self):
		return str(self.value)

	VIRIDIAN_GYM_1 = 1
	VIRIDIAN_NICKNAME_SPEECH_HOUSE_1 = 2
	TRAINER_HOUSE_1F_1 = 3
	VIRIDIAN_MART_2 = 4
	VIRIDIAN_POKECENTER_1F_1 = 5


class Viridian_City_Warp_Points(Enum): 

	Viridian_City_Gym_Entrance_WP = WarpInstruction(
		getHex(VIRIDIAN_CITY.VIRIDIAN_GYM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Viridian_City_Nickname_Speech_House_Entrance_WP = WarpInstruction(
		getHex(VIRIDIAN_CITY.VIRIDIAN_NICKNAME_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Trainer_House_Entrance_WP = WarpInstruction(
		getHex(VIRIDIAN_CITY.TRAINER_HOUSE_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Viridian_City_Mart_Entrance_WP = WarpInstruction(
		getHex(VIRIDIAN_CITY.VIRIDIAN_MART_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Viridian_City_Pokecenter_Entrance_WP = WarpInstruction(
		getHex(VIRIDIAN_CITY.VIRIDIAN_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

