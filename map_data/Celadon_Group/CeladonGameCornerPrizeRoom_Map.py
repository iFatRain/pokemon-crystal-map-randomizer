from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_GAME_CORNER_PRIZE_ROOM

class CELADON_GAME_CORNER_PRIZE_ROOM(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_CITY_7 = 1



class Celadon_Game_Corner_Prize_Room_Warp_Points(Enum): 

	Celadon_City_Game_Corner_Prize_Room_Exit_WP = WarpInstruction(
		getHex(CELADON_GAME_CORNER_PRIZE_ROOM.CELADON_CITY_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

