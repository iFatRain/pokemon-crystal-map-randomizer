from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.FIGHTING_DOJO

class FIGHTING_DOJO(IntEnum):
	def __str__(self):
		return str(self.value)

	SAFFRON_CITY_1 = 1


class Fighting_Dojo_Warp_Points(Enum): 

	FIGHTING_DOJO_TO_SAFFRON_CITY_1_WP = WarpInstruction( 
		getHex(FIGHTING_DOJO.SAFFRON_CITY_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

