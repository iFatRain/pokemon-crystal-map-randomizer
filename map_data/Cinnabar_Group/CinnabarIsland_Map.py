from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cinnabar
mapGroup = MapGroup.CINNABAR
specificMap = Cinnabar.CINNABAR_ISLAND

class CINNABAR_ISLAND(IntEnum):
	def __str__(self):
		return str(self.value)

	CINNABAR_POKECENTER_1F_1 = 1


class Cinnabar_Island_Warp_Points(Enum): 

	CINNABAR_ISLAND_TO_CINNABAR_POKECENTER_1F_1_WP = WarpInstruction( 
		getHex(CINNABAR_ISLAND.CINNABAR_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

