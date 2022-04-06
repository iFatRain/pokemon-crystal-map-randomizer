from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, New_Bark
mapGroup = MapGroup.NEW_BARK
specificMap = New_Bark.ROUTE_26

class ROUTE_26(IntEnum):
	def __str__(self):
		return str(self.value)

	VICTORY_ROAD_GATE_3 = 1
	ROUTE_26_HEAL_HOUSE_1 = 2
	DAY_OF_WEEK_SIBLINGS_HOUSE_1 = 3


class Route_26_Warp_Points(Enum):

	ROUTE_26_TO_VICTORY_ROAD_GATE_3_WP = WarpInstruction(
		getHex(ROUTE_26.VICTORY_ROAD_GATE_3),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_26_TO_ROUTE_26_HEAL_HOUSE_1_WP = WarpInstruction(
		getHex(ROUTE_26.ROUTE_26_HEAL_HOUSE_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_26_TO_DAY_OF_WEEK_SIBLINGS_HOUSE_1_WP = WarpInstruction(
		getHex(ROUTE_26.DAY_OF_WEEK_SIBLINGS_HOUSE_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 

