from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Vermilion
mapGroup = MapGroup.VERMILION
specificMap = Vermilion.POKEMON_FAN_CLUB

class POKEMON_FAN_CLUB(IntEnum):
	def __str__(self):
		return str(self.value)

	VERMILION_CITY_3 = 1


class Pokemon_Fan_Club_Warp_Points(Enum): 

	POKEMON_FAN_CLUB_TO_VERMILION_CITY_3_WP = WarpInstruction( 
		getHex(POKEMON_FAN_CLUB.VERMILION_CITY_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

