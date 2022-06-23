from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Silver
mapGroup = MapGroup.SILVER
specificMap = Silver.ROUTE_28_STEEL_WING_HOUSE

class ROUTE_28_STEEL_WING_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_28_1 = 1



class Route_28_Steel_Wing_House_Warp_Points(Enum):

	ROUTE_28_STEEL_WING_HOUSE_TO_ROUTE_28_1_WP = WarpInstruction(
		getHex(ROUTE_28_STEEL_WING_HOUSE.ROUTE_28_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 

