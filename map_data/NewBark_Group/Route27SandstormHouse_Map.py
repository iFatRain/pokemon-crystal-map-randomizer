from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, New_Bark
mapGroup = MapGroup.NEW_BARK
specificMap = New_Bark.ROUTE_27_SANDSTORM_HOUSE

class ROUTE_27_SANDSTORM_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_27_1 = 1


class Route_27_Sandstorm_House_Warp_Points(Enum):

	ROUTE27_SANDSTORM_HOUSE_TO_ROUTE_27_1_WP = WarpInstruction( 
		getHex(ROUTE_27_SANDSTORM_HOUSE.ROUTE_27_1),
		getHex(mapGroup),
		getHex(specificMap)
		)
