from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cianwood
mapGroup = MapGroup.CIANWOOD
specificMap = Cianwood.BATTLE_TOWER_OUTSIDE

class BATTLE_TOWER_OUTSIDE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_40_BATTLE_TOWER_GATE_3 = 1
	BATTLE_TOWER_1F_1 = 3



class Battle_Tower_Outside_Warp_Points(Enum): 

	BATTLE_TOWER_OUTSIDE_TO_ROUTE_40_BATTLE_TOWER_GATE_3_WP = WarpInstruction( 
		getHex(BATTLE_TOWER_OUTSIDE.ROUTE_40_BATTLE_TOWER_GATE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		)

	BATTLE_TOWER_OUTSIDE_TO_BATTLE_TOWER_1F_1_WP = WarpInstruction( 
		getHex(BATTLE_TOWER_OUTSIDE.BATTLE_TOWER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		)
