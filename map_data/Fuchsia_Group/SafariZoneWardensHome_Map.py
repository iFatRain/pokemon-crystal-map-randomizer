from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fuchsia
mapGroup = MapGroup.FUCHSIA
specificMap = Fuchsia.SAFARI_ZONE_WARDENS_HOME

class SAFARI_ZONE_WARDENS_HOME(IntEnum):
	def __str__(self):
		return str(self.value)

	FUCHSIA_CITY_6 = 1


class Safari_Zone_Wardens_Home_Warp_Points(Enum): 

	SAFARI_ZONE_WARDENS_HOME_TO_FUCHSIA_CITY_6_WP = WarpInstruction( 
		getHex(SAFARI_ZONE_WARDENS_HOME.FUCHSIA_CITY_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

