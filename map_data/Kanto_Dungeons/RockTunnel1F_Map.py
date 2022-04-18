from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.ROCK_TUNNEL_1F

class ROCK_TUNNEL_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_9_1 = 1
	ROUTE_10_SOUTH_1 = 2
	ROCK_TUNNEL_B1F_3 = 3
	ROCK_TUNNEL_B1F_2 = 4
	ROCK_TUNNEL_B1F_4 = 5
	ROCK_TUNNEL_B1F_1 = 6


class Rock_Tunnel_1F_Warp_Points(Enum): 

	ROCK_TUNNEL_1F_TO_ROUTE_9_1_WP = WarpInstruction( 
		getHex(ROCK_TUNNEL_1F.ROUTE_9_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROCK_TUNNEL_1F_TO_ROUTE_10_SOUTH_1_WP = WarpInstruction( 
		getHex(ROCK_TUNNEL_1F.ROUTE_10_SOUTH_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_3_WP = WarpInstruction( 
		getHex(ROCK_TUNNEL_1F.ROCK_TUNNEL_B1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_2_WP = WarpInstruction( 
		getHex(ROCK_TUNNEL_1F.ROCK_TUNNEL_B1F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_4_WP = WarpInstruction( 
		getHex(ROCK_TUNNEL_1F.ROCK_TUNNEL_B1F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_1_WP = WarpInstruction( 
		getHex(ROCK_TUNNEL_1F.ROCK_TUNNEL_B1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

