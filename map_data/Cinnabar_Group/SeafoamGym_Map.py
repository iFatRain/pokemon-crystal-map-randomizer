from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cinnabar
mapGroup = MapGroup.CINNABAR
specificMap = Cinnabar.SEAFOAM_GYM

class SEAFOAM_GYM(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_20_1 = 1


class Seafoam_Gym_Warp_Points(Enum): 

	Seafoam_Gym_Exit_WP = WarpInstruction(
		getHex(SEAFOAM_GYM.ROUTE_20_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

