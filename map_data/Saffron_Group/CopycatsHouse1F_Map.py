from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.COPYCATS_HOUSE_1F

class COPYCATS_HOUSE_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	SAFFRON_CITY_8 = 1
	COPYCATS_HOUSE_2F_1 = 3


class Copycats_House_1F_Warp_Points(Enum): 

	COPYCATS_HOUSE_1F_TO_SAFFRON_CITY_8_WP = WarpInstruction( 
		getHex(COPYCATS_HOUSE_1F.SAFFRON_CITY_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	COPYCATS_HOUSE_1F_TO_COPYCATS_HOUSE_2F_1_WP = WarpInstruction( 
		getHex(COPYCATS_HOUSE_1F.COPYCATS_HOUSE_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

