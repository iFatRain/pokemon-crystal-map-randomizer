from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Olivine
mapGroup = MapGroup.OLIVINE
specificMap = Olivine.ROUTE_39_FARMHOUSE

class ROUTE39_FARMHOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_39_2 = 1


class Route_39_Farmhouse_Warp_Points(Enum):

	ROUTE39_FARMHOUSE_TO_ROUTE_39_2_WP = WarpInstruction( 
		getHex(ROUTE39_FARMHOUSE.ROUTE_39_2), 
		getHex(mapGroup),
		getHex(specificMap)
		)

