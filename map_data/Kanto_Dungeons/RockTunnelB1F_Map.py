from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.ROCK_TUNNEL_B1F

class ROCK_TUNNEL_B1F(IntEnum):
	def __str__(self):
		return str(self.value)

	ROCK_TUNNEL_1F_6 = 1
	ROCK_TUNNEL_1F_4 = 2
	ROCK_TUNNEL_1F_3 = 3
	ROCK_TUNNEL_1F_5 = 4


class Rock_Tunnel_B1F_Warp_Points(Enum): 

	ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_6_WP = WarpInstruction( 
		getHex(ROCK_TUNNEL_B1F.ROCK_TUNNEL_1F_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_4_WP = WarpInstruction( 
		getHex(ROCK_TUNNEL_B1F.ROCK_TUNNEL_1F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_3_WP = WarpInstruction( 
		getHex(ROCK_TUNNEL_B1F.ROCK_TUNNEL_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_5_WP = WarpInstruction( 
		getHex(ROCK_TUNNEL_B1F.ROCK_TUNNEL_1F_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

