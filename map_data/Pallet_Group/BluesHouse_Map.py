from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Pallet
mapGroup = MapGroup.PALLET
specificMap = Pallet.BLUES_HOUSE

class BLUES_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	PALLET_TOWN_2 = 1


class Blues_House_Warp_Points(Enum): 

	BLUES_HOUSE_TO_PALLET_TOWN_2_WP = WarpInstruction( 
		getHex(BLUES_HOUSE.PALLET_TOWN_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

