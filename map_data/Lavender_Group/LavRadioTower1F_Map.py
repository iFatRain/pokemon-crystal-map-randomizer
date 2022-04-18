from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.LAV_RADIO_TOWER_1F

class LAV_RADIO_TOWER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	LAVENDER_TOWN_7 = 1


class Lav_Radio_Tower_1F_Warp_Points(Enum): 

	LAV_RADIO_TOWER_1F_TO_LAVENDER_TOWN_7_WP = WarpInstruction( 
		getHex(LAV_RADIO_TOWER_1F.LAVENDER_TOWN_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

