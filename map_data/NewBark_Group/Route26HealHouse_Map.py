from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, New_Bark
mapGroup = MapGroup.NEW_BARK
specificMap = New_Bark.ROUTE_26_HEAL_HOUSE

class ROUTE_26_HEAL_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_26_2 = 1


class Route_26_Heal_House_Warp_Points(Enum):

	ROUTE_26_HEAL_HOUSE_TO_ROUTE_26_2_WP = WarpInstruction(
		getHex(ROUTE_26_HEAL_HOUSE.ROUTE_26_2),
		getHex(mapGroup),
		getHex(specificMap)
		)
