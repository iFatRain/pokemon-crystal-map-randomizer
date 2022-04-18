from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fuchsia
mapGroup = MapGroup.FUCHSIA
specificMap = Fuchsia.SAFARI_ZONE_MAIN_OFFICE

class SAFARI_ZONE_MAIN_OFFICE(IntEnum):
	def __str__(self):
		return str(self.value)

	FUCHSIA_CITY_2 = 1


class Safari_Zone_Main_Office_Warp_Points(Enum): 

	SAFARI_ZONE_MAIN_OFFICE_TO_FUCHSIA_CITY_2_WP = WarpInstruction( 
		getHex(SAFARI_ZONE_MAIN_OFFICE.FUCHSIA_CITY_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

