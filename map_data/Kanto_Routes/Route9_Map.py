from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.ROUTE_9

class ROUTE_9(IntEnum):
	def __str__(self):
		return str(self.value)

	ROCK_TUNNEL_1F_1 = 1


class Route_9_Warp_Points(Enum): 

	ROUTE_9_TO_ROCK_TUNNEL_1F_1_WP = WarpInstruction( 
		getHex(ROUTE_9.ROCK_TUNNEL_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

