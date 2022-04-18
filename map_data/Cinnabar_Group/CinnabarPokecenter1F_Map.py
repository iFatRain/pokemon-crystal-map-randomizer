from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cinnabar
mapGroup = MapGroup.CINNABAR
specificMap = Cinnabar.CINNABAR_POKECENTER_1F

class CINNABAR_POKECENTER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	CINNABAR_ISLAND_1 = 1
	POKECENTER_2F_1 = 3


class Cinnabar_Pokecenter_1F_Warp_Points(Enum): 

	CINNABAR_POKECENTER_1F_TO_CINNABAR_ISLAND_1_WP = WarpInstruction( 
		getHex(CINNABAR_POKECENTER_1F.CINNABAR_ISLAND_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	CINNABAR_POKECENTER_1F_TO_POKECENTER_2F_1_WP = WarpInstruction( 
		getHex(CINNABAR_POKECENTER_1F.POKECENTER_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

