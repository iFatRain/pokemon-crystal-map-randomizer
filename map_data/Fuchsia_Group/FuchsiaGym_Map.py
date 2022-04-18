from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fuchsia
mapGroup = MapGroup.FUCHSIA
specificMap = Fuchsia.FUCHSIA_GYM

class FUCHSIA_GYM(IntEnum):
	def __str__(self):
		return str(self.value)

	FUCHSIA_CITY_3 = 1



class Fuchsia_Gym_Warp_Points(Enum): 

	FUCHSIA_GYM_TO_FUCHSIA_CITY_3_WP = WarpInstruction( 
		getHex(FUCHSIA_GYM.FUCHSIA_CITY_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

