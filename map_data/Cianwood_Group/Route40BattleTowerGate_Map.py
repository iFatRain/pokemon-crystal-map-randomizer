from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cianwood
mapGroup = MapGroup.CIANWOOD
specificMap = Cianwood.ROUTE_40_BATTLE_TOWER_GATE

class ROUTE_40_BATTLE_TOWER_GATE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_40_1 = 1
	BATTLE_TOWER_OUTSIDE_1 = 3


class Route_40_Battle_Tower_Gate_Warp_Points(Enum):

	ROUTE_40_BATTLE_TOWER_GATE_TO_ROUTE_40_1_WP = WarpInstruction(
		getHex(ROUTE_40_BATTLE_TOWER_GATE.ROUTE_40_1),
		getHex(mapGroup),
		getHex(specificMap)
		)

	ROUTE_40_BATTLE_TOWER_GATE_TO_BATTLE_TOWER_OUTSIDE_1_WP = WarpInstruction(
		getHex(ROUTE_40_BATTLE_TOWER_GATE.BATTLE_TOWER_OUTSIDE_1),
		getHex(mapGroup),
		getHex(specificMap)
		)
