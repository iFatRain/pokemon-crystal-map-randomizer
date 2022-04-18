from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.LAVENDER_TOWN

class LAVENDER_TOWN(IntEnum):
	def __str__(self):
		return str(self.value)

	LAVENDER_POKECENTER_1F_1 = 1
	MR_FUJIS_HOUSE_1 = 2
	LAVENDER_SPEECH_HOUSE_1 = 3
	LAVENDER_NAME_RATER_1 = 4
	LAVENDER_MART_2 = 5
	SOUL_HOUSE_1 = 6
	LAV_RADIO_TOWER_1F_1 = 7


class Lavender_Town_Warp_Points(Enum): 

	LAVENDER_TOWN_TO_LAVENDER_POKECENTER_1F_1_WP = WarpInstruction( 
		getHex(LAVENDER_TOWN.LAVENDER_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	LAVENDER_TOWN_TO_MR_FUJIS_HOUSE_1_WP = WarpInstruction( 
		getHex(LAVENDER_TOWN.MR_FUJIS_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	LAVENDER_TOWN_TO_LAVENDER_SPEECH_HOUSE_1_WP = WarpInstruction( 
		getHex(LAVENDER_TOWN.LAVENDER_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	LAVENDER_TOWN_TO_LAVENDER_NAME_RATER_1_WP = WarpInstruction( 
		getHex(LAVENDER_TOWN.LAVENDER_NAME_RATER_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	LAVENDER_TOWN_TO_LAVENDER_MART_2_WP = WarpInstruction( 
		getHex(LAVENDER_TOWN.LAVENDER_MART_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	LAVENDER_TOWN_TO_SOUL_HOUSE_1_WP = WarpInstruction( 
		getHex(LAVENDER_TOWN.SOUL_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	LAVENDER_TOWN_TO_LAV_RADIO_TOWER_1F_1_WP = WarpInstruction( 
		getHex(LAVENDER_TOWN.LAV_RADIO_TOWER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

