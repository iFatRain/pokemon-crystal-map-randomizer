from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Silver
mapGroup = MapGroup.SILVER
specificMap = Silver.ROUTE_28

class ROUTE28(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_28_STEEL_WING_HOUSE_1 = 1
	VICTORY_ROAD_GATE_7 = 2


class Route_28_Warp_Points(Enum):

	ROUTE_28_TO_ROUTE_28_STEEL_WING_HOUSE_1_WP = WarpInstruction(
		getHex(ROUTE28.ROUTE_28_STEEL_WING_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_28_TO_VICTORY_ROAD_GATE_7_WP = WarpInstruction(
		getHex(ROUTE28.VICTORY_ROAD_GATE_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

