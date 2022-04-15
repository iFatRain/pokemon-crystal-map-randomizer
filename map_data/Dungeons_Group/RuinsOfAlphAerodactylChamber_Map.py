from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.RUINS_OF_ALPH_AERODACTYL_CHAMBER

class RUINS_OF_ALPH_AERODACTYL_CHAMBER(IntEnum):
	def __str__(self):
		return str(self.value)

	RUINS_OF_ALPH_OUTSIDE_4 = 1
	RUINS_OF_ALPH_INNER_CHAMBER_8 = 3
	RUINS_OF_ALPH_AERODACTYL_ITEM_ROOM_1 = 5


class Ruins_Of_Alph_Aerodactyl_Chamber_Warp_Points(Enum): 

	RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_4_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_AERODACTYL_CHAMBER.RUINS_OF_ALPH_OUTSIDE_4), 
		getHex(mapGroup),
		getHex(specificMap)
		)

	RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_8_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_AERODACTYL_CHAMBER.RUINS_OF_ALPH_INNER_CHAMBER_8), 
		getHex(mapGroup),
		getHex(specificMap)
		)

	RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_AERODACTYL_ITEM_ROOM_1_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_AERODACTYL_CHAMBER.RUINS_OF_ALPH_AERODACTYL_ITEM_ROOM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

