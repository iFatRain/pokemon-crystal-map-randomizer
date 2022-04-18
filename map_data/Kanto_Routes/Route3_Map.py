from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Pewter
mapGroup = MapGroup.PEWTER
specificMap = Pewter.ROUTE_3

class ROUTE_3(IntEnum):
	def __str__(self):
		return str(self.value)

	MOUNT_MOON_1 = 1


class Route_3_Warp_Points(Enum): 

	ROUTE_3_TO_MOUNT_MOON_1_WP = WarpInstruction( 
		getHex(ROUTE_3.MOUNT_MOON_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

