from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.RUINS_OF_ALPH_KABUTO_ITEM_ROOM

class RUINS_OF_ALPH_KABUTO_ITEM_ROOM(IntEnum):
	def __str__(self):
		return str(self.value)

	RUINS_OF_ALPH_KABUTO_CHAMBER_5 = 1
	RUINS_OF_ALPH_KABUTO_WORD_ROOM_1 = 3


class Ruins_Of_Alph_Kabuto_Item_Room_Warp_Points(Enum): 

	RUINS_OF_ALPH_KABUTO_ITEM_ROOM_TO_RUINS_OF_ALPH_KABUTO_CHAMBER_5_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_KABUTO_ITEM_ROOM.RUINS_OF_ALPH_KABUTO_CHAMBER_5), 
		getHex(mapGroup),
		getHex(specificMap)
		)

	RUINS_OF_ALPH_KABUTO_ITEM_ROOM_TO_RUINS_OF_ALPH_KABUTO_WORD_ROOM_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_KABUTO_ITEM_ROOM.RUINS_OF_ALPH_KABUTO_WORD_ROOM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		)
