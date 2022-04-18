from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Pewter
mapGroup = MapGroup.PEWTER
specificMap = Pewter.PEWTER_GYM

class PEWTER_GYM(IntEnum):
	def __str__(self):
		return str(self.value)

	PEWTER_CITY_2 = 1


class Pewter_Gym_Warp_Points(Enum): 

	PEWTER_GYM_TO_PEWTER_CITY_2_WP = WarpInstruction( 
		getHex(PEWTER_GYM.PEWTER_CITY_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


