from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.WHIRL_ISLAND_CAVE

class WHIRL_ISLAND_CAVE(IntEnum):
	def __str__(self):
		return str(self.value)

	WHIRL_ISLAND_B1F_9 = 1
	WHIRL_ISLAND_NW_4 = 2


class Whirl_Island_Cave_Warp_Points(Enum): 

	WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_B1F_9_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_CAVE.WHIRL_ISLAND_B1F_9), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_NW_4_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_CAVE.WHIRL_ISLAND_NW_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

