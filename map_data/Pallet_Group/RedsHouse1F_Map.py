from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Pallet
mapGroup = MapGroup.PALLET
specificMap = Pallet.REDS_HOUSE_1F

class REDS_HOUSE_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	PALLET_TOWN_1 = 1
	REDS_HOUSE_2F_1 = 3


class Reds_House_1F_Warp_Points(Enum): 

	REDS_HOUSE_1F_TO_PALLET_TOWN_1_WP = WarpInstruction( 
		getHex(REDS_HOUSE_1F.PALLET_TOWN_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	REDS_HOUSE_1F_TO_REDS_HOUSE_2F_1_WP = WarpInstruction( 
		getHex(REDS_HOUSE_1F.REDS_HOUSE_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

