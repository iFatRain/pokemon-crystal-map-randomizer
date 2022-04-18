from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Pewter
mapGroup = MapGroup.PEWTER
specificMap = Pewter.PEWTER_POKECENTER_1F

class PEWTER_POKECENTER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	PEWTER_CITY_4 = 1
	POKECENTER_2F_1 = 3


class Pewter_Pokecenter_1F_Warp_Points(Enum): 

	PEWTER_POKECENTER_1F_TO_PEWTER_CITY_4_WP = WarpInstruction( 
		getHex(PEWTER_POKECENTER_1F.PEWTER_CITY_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	PEWTER_POKECENTER_1F_TO_POKECENTER_2F_1_WP = WarpInstruction( 
		getHex(PEWTER_POKECENTER_1F.POKECENTER_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

