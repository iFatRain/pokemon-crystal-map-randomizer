from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.ROUTE_4

class ROUTE_4(IntEnum):
	def __str__(self):
		return str(self.value)

	MOUNT_MOON_2 = 1


class Route_4_Warp_Points(Enum): 

	ROUTE_4_TO_MOUNT_MOON_2_WP = WarpInstruction( 
		getHex(ROUTE_4.MOUNT_MOON_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

