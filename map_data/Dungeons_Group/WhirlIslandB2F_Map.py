from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.WHIRL_ISLAND_B2F

class WHIRL_ISLAND_B2F(IntEnum):
	def __str__(self):
		return str(self.value)

	WHIRL_ISLAND_B1F_7 = 1
	WHIRL_ISLAND_B1F_8 = 2
	WHIRL_ISLAND_LUGIA_CHAMBER_1 = 3
	WHIRL_ISLAND_SW_5 = 4


class Whirl_Island_B2F_Warp_Points(Enum): 

	WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_7_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B2F.WHIRL_ISLAND_B1F_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_8_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B2F.WHIRL_ISLAND_B1F_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_LUGIA_CHAMBER_1_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B2F.WHIRL_ISLAND_LUGIA_CHAMBER_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_SW_5_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B2F.WHIRL_ISLAND_SW_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

