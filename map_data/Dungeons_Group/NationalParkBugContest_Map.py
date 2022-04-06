from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.NATIONAL_PARK_BUG_CONTEST

class NATIONAL_PARK_BUG_CONTEST(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_36_NATIONAL_PARK_GATE_1 = 1
	ROUTE_35_NATIONAL_PARK_GATE_1 = 3


class National_Park_Bug_Contest_Warp_Points(Enum): 

	NATIONAL_PARK_BUG_CONTEST_TO_ROUTE_36_NATIONAL_PARK_GATE_1_WP = WarpInstruction( 
		getHex(NATIONAL_PARK_BUG_CONTEST.ROUTE_36_NATIONAL_PARK_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	NATIONAL_PARK_BUG_CONTEST_TO_ROUTE_35_NATIONAL_PARK_GATE_1_WP = WarpInstruction( 
		getHex(NATIONAL_PARK_BUG_CONTEST.ROUTE_35_NATIONAL_PARK_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 
