from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.LAVENDER_POKECENTER_1F

class LAVENDER_POKECENTER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	LAVENDER_TOWN_1 = 1
	POKECENTER_2F_1 = 3


class Lavender_Pokecenter_1F_Warp_Points(Enum): 

	LAVENDER_POKECENTER_1F_TO_LAVENDER_TOWN_1_WP = WarpInstruction( 
		getHex(LAVENDER_POKECENTER_1F.LAVENDER_TOWN_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	LAVENDER_POKECENTER_1F_TO_POKECENTER_2F_1_WP = WarpInstruction( 
		getHex(LAVENDER_POKECENTER_1F.POKECENTER_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

