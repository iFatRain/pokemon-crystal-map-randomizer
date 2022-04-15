from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Olivine
mapGroup = MapGroup.OLIVINE
specificMap = Olivine.ROUTE_39_BARN

class ROUTE39_BARN(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_39_1 = 1


class Route_39_Barn_Warp_Points(Enum):

	ROUTE_39_BARN_TO_ROUTE_39_1_WP = WarpInstruction(
		getHex(ROUTE39_BARN.ROUTE_39_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 



