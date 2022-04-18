from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.CERULEAN_GYM

class CERULEAN_GYM(IntEnum):
	def __str__(self):
		return str(self.value)

	CERULEAN_CITY_5 = 1


class Cerulean_Gym_Warp_Points(Enum): 

	CERULEAN_GYM_TO_CERULEAN_CITY_5_WP = WarpInstruction( 
		getHex(CERULEAN_GYM.CERULEAN_CITY_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

