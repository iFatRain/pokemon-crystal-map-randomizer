from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.CERULEAN_POKECENTER_1F

class CERULEAN_POKECENTER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	CERULEAN_CITY_4 = 1
	POKECENTER_2F_1 = 3


class Cerulean_Pokecenter_1F_Warp_Points(Enum): 

	CERULEAN_POKECENTER_1F_TO_CERULEAN_CITY_4_WP = WarpInstruction( 
		getHex(CERULEAN_POKECENTER_1F.CERULEAN_CITY_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CERULEAN_POKECENTER_1F_TO_POKECENTER_2F_1_WP = WarpInstruction( 
		getHex(CERULEAN_POKECENTER_1F.POKECENTER_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

