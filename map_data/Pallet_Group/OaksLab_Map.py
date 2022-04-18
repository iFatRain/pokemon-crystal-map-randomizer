from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Pallet
mapGroup = MapGroup.PALLET
specificMap = Pallet.OAKS_LAB

class OAKS_LAB(IntEnum):
	def __str__(self):
		return str(self.value)

	PALLET_TOWN_3 = 1


class Oaks_Lab_Warp_Points(Enum): 

	OAKS_LAB_TO_PALLET_TOWN_3_WP = WarpInstruction( 
		getHex(OAKS_LAB.PALLET_TOWN_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


