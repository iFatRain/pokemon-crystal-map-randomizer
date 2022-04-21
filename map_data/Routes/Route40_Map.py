from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cianwood
mapGroup = MapGroup.CIANWOOD
specificMap = Cianwood.ROUTE_40

class ROUTE_40(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_40_BATTLE_TOWER_GATE_1 = 1


class Route_40_Warp_Points(Enum):

	ROUTE_40_TO_ROUTE_40_BATTLE_TOWER_GATE_1_WP = WarpInstruction(
		getHex(ROUTE_40.ROUTE_40_BATTLE_TOWER_GATE_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 




