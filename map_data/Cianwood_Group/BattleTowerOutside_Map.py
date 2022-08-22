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

	Battle_Tower_Outside_To_Gate_WP = WarpInstruction(
		getHex(BATTLE_TOWER_OUTSIDE.ROUTE_40_BATTLE_TOWER_GATE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		)

	Battle_Tower_Outside_To_Battle_Tower_WP = WarpInstruction(
		getHex(BATTLE_TOWER_OUTSIDE.BATTLE_TOWER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		)
