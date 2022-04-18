from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.ROUTE_10_SOUTH

class ROUTE_10_SOUTH(IntEnum):
	def __str__(self):
		return str(self.value)

	ROCK_TUNNEL_1F_2 = 1


class Route_10_South_Warp_Points(Enum): 

	ROUTE_10_SOUTH_TO_ROCK_TUNNEL_1F_2_WP = WarpInstruction( 
		getHex(ROUTE_10_SOUTH.ROCK_TUNNEL_1F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

