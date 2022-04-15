from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.RUINS_OF_ALPH_INNER_CHAMBER

class RUINS_OF_ALPH_INNER_CHAMBER(IntEnum):
	def __str__(self):
		return str(self.value)

	RUINS_OF_ALPH_OUTSIDE_5 = 1
	# RUINS_OF_ALPH_HO_OH_CHAMBER_3 = 2
	# RUINS_OF_ALPH_HO_OH_CHAMBER_4 = 3
	# RUINS_OF_ALPH_KABUTO_CHAMBER_3 = 4
	# RUINS_OF_ALPH_KABUTO_CHAMBER_4 = 5
	# RUINS_OF_ALPH_OMANYTE_CHAMBER_3 = 6
	# RUINS_OF_ALPH_OMANYTE_CHAMBER_4 = 7
	# RUINS_OF_ALPH_AERODACTYL_CHAMBER_3 = 8
	# RUINS_OF_ALPH_AERODACTYL_CHAMBER_4 = 9


class Ruins_Of_Alph_Inner_Chamber_Warp_Points(Enum): 

	RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_WP = WarpInstruction( 
		getHex(RUINS_OF_ALPH_INNER_CHAMBER.RUINS_OF_ALPH_OUTSIDE_5), 
		getHex(mapGroup),
		getHex(specificMap)
		)
	#
	# RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_3_WP = WarpInstruction(
	# 	getHex(RUINS_OF_ALPH_INNER_CHAMBER.RUINS_OF_ALPH_HO_OH_CHAMBER_3),
	# 	getHex(mapGroup),
	# 	getHex(specificMap)
	# 	)
	#
	# RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_4_WP = WarpInstruction(
	# 	getHex(RUINS_OF_ALPH_INNER_CHAMBER.RUINS_OF_ALPH_HO_OH_CHAMBER_4),
	# 	getHex(mapGroup),
	# 	getHex(specificMap)
	# 	)
	#
	# RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_KABUTO_CHAMBER_3_WP = WarpInstruction(
	# 	getHex(RUINS_OF_ALPH_INNER_CHAMBER.RUINS_OF_ALPH_KABUTO_CHAMBER_3),
	# 	getHex(mapGroup),
	# 	getHex(specificMap)
	# 	)
	#
	# RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_KABUTO_CHAMBER_4_WP = WarpInstruction(
	# 	getHex(RUINS_OF_ALPH_INNER_CHAMBER.RUINS_OF_ALPH_KABUTO_CHAMBER_4),
	# 	getHex(mapGroup),
	# 	getHex(specificMap)
	# 	)
	#
	# RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OMANYTE_CHAMBER_3_WP = WarpInstruction(
	# 	getHex(RUINS_OF_ALPH_INNER_CHAMBER.RUINS_OF_ALPH_OMANYTE_CHAMBER_3),
	# 	getHex(mapGroup),
	# 	getHex(specificMap)
	# 	)
	#
	# RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OMANYTE_CHAMBER_4_WP = WarpInstruction(
	# 	getHex(RUINS_OF_ALPH_INNER_CHAMBER.RUINS_OF_ALPH_OMANYTE_CHAMBER_4),
	# 	getHex(mapGroup),
	# 	getHex(specificMap)
	# 	)
	#
	# RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_AERODACTYL_CHAMBER_3_WP = WarpInstruction(
	# 	getHex(RUINS_OF_ALPH_INNER_CHAMBER.RUINS_OF_ALPH_AERODACTYL_CHAMBER_3),
	# 	getHex(mapGroup),
	# 	getHex(specificMap)
	# 	)
	#
	# RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_AERODACTYL_CHAMBER_4_WP = WarpInstruction(
	# 	getHex(RUINS_OF_ALPH_INNER_CHAMBER.RUINS_OF_ALPH_AERODACTYL_CHAMBER_4),
	# 	getHex(mapGroup),
	# 	getHex(specificMap)
	# 	)

