from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.RUINS_OF_ALPH_OUTSIDE

class RUINS_OF_ALPH_OUTSIDE(IntEnum):
	def __str__(self):
		return str(self.value)

	RUINS_OF_ALPH_HO_OH_CHAMBER_1 = 1
	RUINS_OF_ALPH_KABUTO_CHAMBER_1 = 2
	RUINS_OF_ALPH_OMANYTE_CHAMBER_1 = 3
	RUINS_OF_ALPH_AERODACTYL_CHAMBER_1 = 4
	RUINS_OF_ALPH_INNER_CHAMBER_1 = 5
	RUINS_OF_ALPH_RESEARCH_CENTER_1 = 6
	UNION_CAVE_B1F_1 = 7
	UNION_CAVE_B1F_2 = 8
	ROUTE_36_RUINS_OF_ALPH_GATE_3 = 9
	ROUTE_32_RUINS_OF_ALPH_GATE_1 = 10



class Ruins_Of_Alph_Outside_Warp_Points(Enum): 

	RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OUTSIDE.RUINS_OF_ALPH_HO_OH_CHAMBER_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_KABUTO_CHAMBER_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OUTSIDE.RUINS_OF_ALPH_KABUTO_CHAMBER_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_OMANYTE_CHAMBER_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OUTSIDE.RUINS_OF_ALPH_OMANYTE_CHAMBER_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_AERODACTYL_CHAMBER_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OUTSIDE.RUINS_OF_ALPH_AERODACTYL_CHAMBER_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_INNER_CHAMBER_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OUTSIDE.RUINS_OF_ALPH_INNER_CHAMBER_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_RESEARCH_CENTER_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OUTSIDE.RUINS_OF_ALPH_RESEARCH_CENTER_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OUTSIDE.UNION_CAVE_B1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_2_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OUTSIDE.UNION_CAVE_B1F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_36_RUINS_OF_ALPH_GATE_3_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OUTSIDE.ROUTE_36_RUINS_OF_ALPH_GATE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_32_RUINS_OF_ALPH_GATE_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OUTSIDE.ROUTE_32_RUINS_OF_ALPH_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		)
