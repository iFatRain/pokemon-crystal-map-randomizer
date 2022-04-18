from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.SAFFRON_POKECENTER_1F

class SAFFRON_POKECENTER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	SAFFRON_CITY_4 = 1
	POKECENTER_2F_1 = 3


class Saffron_Pokecenter_1F_Warp_Points(Enum): 

	SAFFRON_POKECENTER_1F_TO_SAFFRON_CITY_4_WP = WarpInstruction( 
		getHex(SAFFRON_POKECENTER_1F.SAFFRON_CITY_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	SAFFRON_POKECENTER_1F_TO_POKECENTER_2F_1_WP = WarpInstruction( 
		getHex(SAFFRON_POKECENTER_1F.POKECENTER_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

