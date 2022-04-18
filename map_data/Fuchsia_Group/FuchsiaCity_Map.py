from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fuchsia
mapGroup = MapGroup.FUCHSIA
specificMap = Fuchsia.FUCHSIA_CITY

class FUCHSIA_CITY(IntEnum):
	def __str__(self):
		return str(self.value)

	FUCHSIA_MART_2 = 1
	SAFARI_ZONE_MAIN_OFFICE_1 = 2
	FUCHSIA_GYM_1 = 3
	BILLS_BROTHERS_HOUSE_1 = 4
	FUCHSIA_POKECENTER_1F_1 = 5
	SAFARI_ZONE_WARDENS_HOME_1 = 6

	ROUTE_15_FUCHSIA_GATE_1 = 8
	ROUTE_15_FUCHSIA_GATE_2 = 9
	ROUTE_19_FUCHSIA_GATE_1 = 10
	ROUTE_19_FUCHSIA_GATE_2 = 11


class Fuchsia_City_Warp_Points(Enum): 

	FUCHSIA_CITY_TO_FUCHSIA_MART_2_WP = WarpInstruction( 
		getHex(FUCHSIA_CITY.FUCHSIA_MART_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FUCHSIA_CITY_TO_SAFARI_ZONE_MAIN_OFFICE_1_WP = WarpInstruction( 
		getHex(FUCHSIA_CITY.SAFARI_ZONE_MAIN_OFFICE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FUCHSIA_CITY_TO_FUCHSIA_GYM_1_WP = WarpInstruction( 
		getHex(FUCHSIA_CITY.FUCHSIA_GYM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FUCHSIA_CITY_TO_BILLS_BROTHERS_HOUSE_1_WP = WarpInstruction( 
		getHex(FUCHSIA_CITY.BILLS_BROTHERS_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FUCHSIA_CITY_TO_FUCHSIA_POKECENTER_1F_1_WP = WarpInstruction( 
		getHex(FUCHSIA_CITY.FUCHSIA_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FUCHSIA_CITY_TO_SAFARI_ZONE_WARDENS_HOME_1_WP = WarpInstruction( 
		getHex(FUCHSIA_CITY.SAFARI_ZONE_WARDENS_HOME_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 



	FUCHSIA_CITY_TO_ROUTE_15_FUCHSIA_GATE_1_WP = WarpInstruction( 
		getHex(FUCHSIA_CITY.ROUTE_15_FUCHSIA_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FUCHSIA_CITY_TO_ROUTE_19_FUCHSIA_GATE_1_WP = WarpInstruction( 
		getHex(FUCHSIA_CITY.ROUTE_19_FUCHSIA_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

