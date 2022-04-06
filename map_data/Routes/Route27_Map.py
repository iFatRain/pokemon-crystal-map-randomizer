from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, New_Bark
mapGroup = MapGroup.NEW_BARK
specificMap = New_Bark.ROUTE_27

class ROUTE_27(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_27_SANDSTORM_HOUSE_1 = 1
	TOHJO_FALLS_1 = 2
	TOHJO_FALLS_2 = 3


class Route_27_Warp_Points(Enum):

	ROUTE_27_TO_ROUTE_27_SANDSTORM_HOUSE_1_WP = WarpInstruction(
		getHex(ROUTE_27.ROUTE_27_SANDSTORM_HOUSE_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_27_TO_TOHJO_FALLS_1_WP = WarpInstruction(
		getHex(ROUTE_27.TOHJO_FALLS_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_27_TO_TOHJO_FALLS_2_WP = WarpInstruction(
		getHex(ROUTE_27.TOHJO_FALLS_2),
		getHex(mapGroup),
		getHex(specificMap)
		) 

