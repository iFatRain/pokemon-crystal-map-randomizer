from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Viridian
mapGroup = MapGroup.VIRIDIAN
specificMap = Viridian.VIRIDIAN_POKECENTER_1F

class VIRIDIAN_POKECENTER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	VIRIDIAN_CITY_5 = 1
	POKECENTER_2F_1 = 3


class Viridian_Pokecenter_1F_Warp_Points(Enum): 

	VIRIDIAN_POKECENTER_1F_TO_VIRIDIAN_CITY_5_WP = WarpInstruction( 
		getHex(VIRIDIAN_POKECENTER_1F.VIRIDIAN_CITY_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	VIRIDIAN_POKECENTER_1F_TO_POKECENTER_2F_1_WP = WarpInstruction( 
		getHex(VIRIDIAN_POKECENTER_1F.POKECENTER_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

