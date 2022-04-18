from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fuchsia
mapGroup = MapGroup.FUCHSIA
specificMap = Fuchsia.FUCHSIA_POKECENTER_1F

class FUCHSIA_POKECENTER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	FUCHSIA_CITY_5 = 1
	POKECENTER_2F_1 = 3


class Fuchsia_Pokecenter_1F_Warp_Points(Enum): 

	FUCHSIA_POKECENTER_1F_TO_FUCHSIA_CITY_5_WP = WarpInstruction( 
		getHex(FUCHSIA_POKECENTER_1F.FUCHSIA_CITY_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	FUCHSIA_POKECENTER_1F_TO_POKECENTER_2F_1_WP = WarpInstruction( 
		getHex(FUCHSIA_POKECENTER_1F.POKECENTER_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

