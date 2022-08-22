from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.BILLS_HOUSE

class BILLS_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_25_1 = 1


class Bills_House_Warp_Points(Enum): 

	Bills_House_Exit_WP = WarpInstruction(
		getHex(BILLS_HOUSE.ROUTE_25_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


