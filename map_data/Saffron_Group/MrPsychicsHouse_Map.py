from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.MR_PSYCHICS_HOUSE

class MR_PSYCHICS_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	SAFFRON_CITY_5 = 1


class Mr_Psychics_House_Warp_Points(Enum): 

	MR_PSYCHICS_HOUSE_TO_SAFFRON_CITY_5_WP = WarpInstruction( 
		getHex(MR_PSYCHICS_HOUSE.SAFFRON_CITY_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

