from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.RUINS_OF_ALPH_OMANYTE_CHAMBER

class RUINS_OF_ALPH_OMANYTE_CHAMBER(IntEnum):
	def __str__(self):
		return str(self.value)

	RUINS_OF_ALPH_OUTSIDE_3 = 1
	RUINS_OF_ALPH_INNER_CHAMBER_6 = 3
	RUINS_OF_ALPH_OMANYTE_ITEM_ROOM_1 = 5


class Ruins_Of_Alph_Omanyte_Chamber_Warp_Points(Enum): 

	RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_3_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OMANYTE_CHAMBER.RUINS_OF_ALPH_OUTSIDE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		)

	RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_6_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OMANYTE_CHAMBER.RUINS_OF_ALPH_INNER_CHAMBER_6), 
		getHex(mapGroup),
		getHex(specificMap)
		)

	RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_OMANYTE_ITEM_ROOM_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_OMANYTE_CHAMBER.RUINS_OF_ALPH_OMANYTE_ITEM_ROOM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

