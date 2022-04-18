from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_CITY

class CELADON_CITY(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_DEPT_STORE_1F_1 = 1
	CELADON_MANSION_1F_1 = 2
	CELADON_MANSION_1F_3 = 3
	CELADON_POKECENTER_1F_1 = 5
	CELADON_GAME_CORNER_1 = 6
	CELADON_GAME_CORNER_PRIZE_ROOM_1 = 7
	CELADON_GYM_1 = 8
	CELADON_CAFE_1 = 9


class Celadon_City_Warp_Points(Enum): 

	CELADON_CITY_TO_CELADON_DEPT_STORE_1F_1_WP = WarpInstruction( 
		getHex(CELADON_CITY.CELADON_DEPT_STORE_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_CITY_TO_CELADON_MANSION_1F_1_WP = WarpInstruction( 
		getHex(CELADON_CITY.CELADON_MANSION_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_CITY_TO_CELADON_MANSION_1F_3_WP = WarpInstruction( 
		getHex(CELADON_CITY.CELADON_MANSION_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_CITY_TO_CELADON_POKECENTER_1F_1_WP = WarpInstruction( 
		getHex(CELADON_CITY.CELADON_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_CITY_TO_CELADON_GAME_CORNER_1_WP = WarpInstruction( 
		getHex(CELADON_CITY.CELADON_GAME_CORNER_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_CITY_TO_CELADON_GAME_CORNER_PRIZE_ROOM_1_WP = WarpInstruction( 
		getHex(CELADON_CITY.CELADON_GAME_CORNER_PRIZE_ROOM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_CITY_TO_CELADON_GYM_1_WP = WarpInstruction( 
		getHex(CELADON_CITY.CELADON_GYM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_CITY_TO_CELADON_CAFE_1_WP = WarpInstruction( 
		getHex(CELADON_CITY.CELADON_CAFE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

