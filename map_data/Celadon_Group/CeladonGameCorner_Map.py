from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_GAME_CORNER

class CELADON_GAME_CORNER(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_CITY_6 = 1



class Celadon_Game_Corner_Warp_Points(Enum): 

	Celadon_City_Game_Corner_Exit_WP = WarpInstruction(
		getHex(CELADON_GAME_CORNER.CELADON_CITY_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 



