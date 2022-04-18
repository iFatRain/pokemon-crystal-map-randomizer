from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.DIGLETTS_CAVE

class DIGLETTS_CAVE(IntEnum):
	def __str__(self):
		return str(self.value)

	VERMILION_CITY_10 = 1
	DIGLETTS_CAVE_5 = 2
	ROUTE_2_5 = 3
	DIGLETTS_CAVE_6 = 4
	DIGLETTS_CAVE_2 = 5
	DIGLETTS_CAVE_4 = 6


class Digletts_Cave_Warp_Points(Enum): 

	DIGLETTS_CAVE_TO_VERMILION_CITY_10_WP = WarpInstruction( 
		getHex(DIGLETTS_CAVE.VERMILION_CITY_10), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	DIGLETTS_CAVE_TO_DIGLETTS_CAVE_5_WP = WarpInstruction( 
		getHex(DIGLETTS_CAVE.DIGLETTS_CAVE_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	DIGLETTS_CAVE_TO_ROUTE_2_5_WP = WarpInstruction( 
		getHex(DIGLETTS_CAVE.ROUTE_2_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	DIGLETTS_CAVE_TO_DIGLETTS_CAVE_6_WP = WarpInstruction( 
		getHex(DIGLETTS_CAVE.DIGLETTS_CAVE_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	DIGLETTS_CAVE_TO_DIGLETTS_CAVE_2_WP = WarpInstruction( 
		getHex(DIGLETTS_CAVE.DIGLETTS_CAVE_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	DIGLETTS_CAVE_TO_DIGLETTS_CAVE_4_WP = WarpInstruction( 
		getHex(DIGLETTS_CAVE.DIGLETTS_CAVE_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

