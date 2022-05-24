from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, New_Bark
mapGroup = MapGroup.NEW_BARK
specificMap = New_Bark.DAY_OF_WEEK_SIBLINGS_HOUSE

class DAY_OF_WEEK_SIBLINGS_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_26_3 = 1 #dual wide


class Day_Of_Week_Siblings_House_Warp_Points(Enum): 

	DAY_OF_WEEK_SIBLINGS_HOUSE_TO_ROUTE_26_3_WP = WarpInstruction( 
		getHex(DAY_OF_WEEK_SIBLINGS_HOUSE.ROUTE_26_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

