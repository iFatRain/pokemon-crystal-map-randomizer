from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.COPYCATS_HOUSE_2F

class COPYCATS_HOUSE_2F(IntEnum):
	def __str__(self):
		return str(self.value)

	COPYCATS_HOUSE_1F_3 = 1


class Copycats_House_2F_Warp_Points(Enum): 

	COPYCATS_HOUSE_2F_TO_COPYCATS_HOUSE_1F_3_WP = WarpInstruction( 
		getHex(COPYCATS_HOUSE_2F.COPYCATS_HOUSE_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

