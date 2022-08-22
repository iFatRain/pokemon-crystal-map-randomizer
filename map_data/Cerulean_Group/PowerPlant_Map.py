from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.POWER_PLANT

class POWER_PLANT(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_10_NORTH_2 = 1



class Power_Plant_Warp_Points(Enum): 

	Power_Plant_Exit_WP = WarpInstruction(
		getHex(POWER_PLANT.ROUTE_10_NORTH_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


