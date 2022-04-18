from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Vermilion
mapGroup = MapGroup.VERMILION
specificMap = Vermilion.VERMILION_GYM

class VERMILION_GYM(IntEnum):
	def __str__(self):
		return str(self.value)

	VERMILION_CITY_7 = 1


class Vermilion_Gym_Warp_Points(Enum): 

	VERMILION_GYM_TO_VERMILION_CITY_7_WP = WarpInstruction( 
		getHex(VERMILION_GYM.VERMILION_CITY_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


