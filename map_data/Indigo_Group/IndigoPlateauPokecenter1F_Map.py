from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Indigo
mapGroup = MapGroup.INDIGO
specificMap = Indigo.INDIGO_PLATEAU_POKECENTER_1F

class INDIGO_PLATEAU_POKECENTER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_23_1 = 1
	ROUTE_23_2 = 2
	POKECENTER_2F_1 = 3
	WILLS_ROOM_1 = 4


class Indigo_Plateau_Pokecenter_1F_Warp_Points(Enum): 

	INDIGO_PLATEAU_POKECENTER_1F_TO_ROUTE_23_1_WP = WarpInstruction( 
		getHex(INDIGO_PLATEAU_POKECENTER_1F.ROUTE_23_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	INDIGO_PLATEAU_POKECENTER_1F_TO_ROUTE_23_2_WP = WarpInstruction( 
		getHex(INDIGO_PLATEAU_POKECENTER_1F.ROUTE_23_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	INDIGO_PLATEAU_POKECENTER_1F_TO_POKECENTER_2F_1_WP = WarpInstruction( 
		getHex(INDIGO_PLATEAU_POKECENTER_1F.POKECENTER_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	INDIGO_PLATEAU_POKECENTER_1F_TO_WILLS_ROOM_1_WP = WarpInstruction( 
		getHex(INDIGO_PLATEAU_POKECENTER_1F.WILLS_ROOM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

