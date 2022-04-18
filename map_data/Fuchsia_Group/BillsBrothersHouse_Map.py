from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fuchsia
mapGroup = MapGroup.FUCHSIA
specificMap = Fuchsia.BILLS_BROTHERS_HOUSE

class BILLS_BROTHERS_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	FUCHSIA_CITY_4 = 1



class Bills_Brothers_House_Warp_Points(Enum): 

	BILLS_BROTHERS_HOUSE_TO_FUCHSIA_CITY_4_WP = WarpInstruction( 
		getHex(BILLS_BROTHERS_HOUSE.FUCHSIA_CITY_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

