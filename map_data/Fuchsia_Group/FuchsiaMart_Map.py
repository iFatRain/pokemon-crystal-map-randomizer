from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fuchsia
mapGroup = MapGroup.FUCHSIA
specificMap = Fuchsia.FUCHSIA_MART

class FUCHSIA_MART(IntEnum):
	def __str__(self):
		return str(self.value)

	FUCHSIA_CITY_1 = 1



class Fuchsia_Mart_Warp_Points(Enum): 

	FUCHSIA_MART_TO_FUCHSIA_CITY_1_WP = WarpInstruction( 
		getHex(FUCHSIA_MART.FUCHSIA_CITY_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

