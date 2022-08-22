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

	Celadon_City_Dept_Store_1F_Entrance_WP = WarpInstruction(
		getHex(CELADON_CITY.CELADON_DEPT_STORE_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Mansion_1F_Front_Entrance_WP = WarpInstruction(
		getHex(CELADON_CITY.CELADON_MANSION_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Mansion_1F_Rear_Entrance_WP = WarpInstruction(
		getHex(CELADON_CITY.CELADON_MANSION_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Pokecenter_Entrance_WP = WarpInstruction(
		getHex(CELADON_CITY.CELADON_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Game_Corner_Entrance_WP = WarpInstruction(
		getHex(CELADON_CITY.CELADON_GAME_CORNER_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Game_Corner_Prize_Room_Entrance_WP = WarpInstruction(
		getHex(CELADON_CITY.CELADON_GAME_CORNER_PRIZE_ROOM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Gym_Entrance_WP = WarpInstruction(
		getHex(CELADON_CITY.CELADON_GYM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Cafe_Entrance_WP = WarpInstruction(
		getHex(CELADON_CITY.CELADON_CAFE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

