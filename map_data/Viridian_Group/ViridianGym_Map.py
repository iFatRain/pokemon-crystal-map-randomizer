from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Viridian
mapGroup = MapGroup.VIRIDIAN
specificMap = Viridian.VIRIDIAN_GYM

class VIRIDIAN_GYM(IntEnum):
	def __str__(self):
		return str(self.value)

	VIRIDIAN_CITY_1 = 1


class Viridian_Gym_Warp_Points(Enum): 

	VIRIDIAN_GYM_TO_VIRIDIAN_CITY_1_WP = WarpInstruction( 
		getHex(VIRIDIAN_GYM.VIRIDIAN_CITY_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

