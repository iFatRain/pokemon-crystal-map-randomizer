from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cinnabar
mapGroup = MapGroup.CINNABAR
specificMap = Cinnabar.ROUTE_20

class ROUTE_20(IntEnum):
	def __str__(self):
		return str(self.value)

	SEAFOAM_GYM_1 = 1


class Route_20_Warp_Points(Enum): 

	ROUTE_20_TO_SEAFOAM_GYM_1_WP = WarpInstruction( 
		getHex(ROUTE_20.SEAFOAM_GYM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

