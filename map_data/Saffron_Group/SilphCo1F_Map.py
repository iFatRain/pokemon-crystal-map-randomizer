from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.SILPH_CO_1F

class SILPH_CO_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	SAFFRON_CITY_7 = 1


class Silph_Co_1F_Warp_Points(Enum): 

	SILPH_CO_1F_TO_SAFFRON_CITY_7_WP = WarpInstruction( 
		getHex(SILPH_CO_1F.SAFFRON_CITY_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

