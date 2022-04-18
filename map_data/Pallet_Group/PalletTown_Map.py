from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Pallet
mapGroup = MapGroup.PALLET
specificMap = Pallet.PALLET_TOWN

class PALLET_TOWN(IntEnum):
	def __str__(self):
		return str(self.value)

	REDS_HOUSE_1F_1 = 1
	BLUES_HOUSE_1 = 2
	OAKS_LAB_1 = 3


class Pallet_Town_Warp_Points(Enum): 

	PALLET_TOWN_TO_REDS_HOUSE_1F_1_WP = WarpInstruction( 
		getHex(PALLET_TOWN.REDS_HOUSE_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	PALLET_TOWN_TO_BLUES_HOUSE_1_WP = WarpInstruction( 
		getHex(PALLET_TOWN.BLUES_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	PALLET_TOWN_TO_OAKS_LAB_1_WP = WarpInstruction( 
		getHex(PALLET_TOWN.OAKS_LAB_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

