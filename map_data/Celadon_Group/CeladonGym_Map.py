from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_GYM

class CELADON_GYM(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_CITY_8 = 1



class Celadon_Gym_Warp_Points(Enum): 

	CELADON_GYM_TO_CELADON_CITY_8_WP = WarpInstruction( 
		getHex(CELADON_GYM.CELADON_CITY_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

