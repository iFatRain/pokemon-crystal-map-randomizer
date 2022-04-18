from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Pallet
mapGroup = MapGroup.PALLET
specificMap = Pallet.REDS_HOUSE_2F

class REDS_HOUSE_2F(IntEnum):
	def __str__(self):
		return str(self.value)

	REDS_HOUSE_1F_3 = 1


class Reds_House_2F_Warp_Points(Enum): 

	REDS_HOUSE_2F_TO_REDS_HOUSE_1F_3_WP = WarpInstruction( 
		getHex(REDS_HOUSE_2F.REDS_HOUSE_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

