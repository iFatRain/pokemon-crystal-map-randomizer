from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.MR_FUJIS_HOUSE

class MR_FUJIS_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	LAVENDER_TOWN_2 = 1


class Mr_Fujis_House_Warp_Points(Enum): 

	MR_FUJIS_HOUSE_TO_LAVENDER_TOWN_2_WP = WarpInstruction( 
		getHex(MR_FUJIS_HOUSE.LAVENDER_TOWN_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

