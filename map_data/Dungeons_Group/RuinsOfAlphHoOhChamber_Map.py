from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.RUINS_OF_ALPH_HO_OH_CHAMBER

class RUINS_OF_ALPH_HO_OH_CHAMBER(IntEnum):
	def __str__(self):
		return str(self.value)

	RUINS_OF_ALPH_OUTSIDE_1 = 1
	RUINS_OF_ALPH_INNER_CHAMBER_2 = 3
	RUINS_OF_ALPH_HO_OH_ITEM_ROOM_1 = 5


class Ruins_Of_Alph_Ho_Oh_Chamber_Warp_Points(Enum): 

	RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_HO_OH_CHAMBER.RUINS_OF_ALPH_OUTSIDE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		)

	RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_2_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_HO_OH_CHAMBER.RUINS_OF_ALPH_INNER_CHAMBER_2), 
		getHex(mapGroup),
		getHex(specificMap)
		)

	RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_HO_OH_ITEM_ROOM_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_HO_OH_CHAMBER.RUINS_OF_ALPH_HO_OH_ITEM_ROOM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

