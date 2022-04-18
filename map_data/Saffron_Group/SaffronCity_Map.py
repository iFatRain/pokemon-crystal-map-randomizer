from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.SAFFRON_CITY

class SAFFRON_CITY(IntEnum):
	def __str__(self):
		return str(self.value)

	FIGHTING_DOJO_1 = 1
	SAFFRON_GYM_1 = 2
	SAFFRON_MART_2 = 3
	SAFFRON_POKECENTER_1F_1 = 4
	MR_PSYCHICS_HOUSE_1 = 5
	SAFFRON_MAGNET_TRAIN_STATION_2 = 6
	SILPH_CO_1F_1 = 7
	COPYCATS_HOUSE_1F_1 = 8
	ROUTE_5_SAFFRON_GATE_3 = 9
	ROUTE_7_SAFFRON_GATE_3 = 10
	ROUTE_7_SAFFRON_GATE_4 = 11
	ROUTE_6_SAFFRON_GATE_1 = 12
	ROUTE_6_SAFFRON_GATE_2 = 13
	ROUTE_8_SAFFRON_GATE_1 = 14
	ROUTE_8_SAFFRON_GATE_2 = 15


class Saffron_City_Warp_Points(Enum): 

	SAFFRON_CITY_TO_FIGHTING_DOJO_1_WP = WarpInstruction( 
		getHex(SAFFRON_CITY.FIGHTING_DOJO_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_CITY_TO_SAFFRON_GYM_1_WP = WarpInstruction( 
		getHex(SAFFRON_CITY.SAFFRON_GYM_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_CITY_TO_SAFFRON_MART_2_WP = WarpInstruction( 
		getHex(SAFFRON_CITY.SAFFRON_MART_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_CITY_TO_SAFFRON_POKECENTER_1F_1_WP = WarpInstruction( 
		getHex(SAFFRON_CITY.SAFFRON_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_CITY_TO_MR_PSYCHICS_HOUSE_1_WP = WarpInstruction( 
		getHex(SAFFRON_CITY.MR_PSYCHICS_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_CITY_TO_SAFFRON_MAGNET_TRAIN_STATION_2_WP = WarpInstruction( 
		getHex(SAFFRON_CITY.SAFFRON_MAGNET_TRAIN_STATION_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_CITY_TO_SILPH_CO_1F_1_WP = WarpInstruction( 
		getHex(SAFFRON_CITY.SILPH_CO_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_CITY_TO_COPYCATS_HOUSE_1F_1_WP = WarpInstruction( 
		getHex(SAFFRON_CITY.COPYCATS_HOUSE_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_CITY_TO_ROUTE_5_SAFFRON_GATE_3_WP = WarpInstruction( 
		getHex(SAFFRON_CITY.ROUTE_5_SAFFRON_GATE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_CITY_TO_ROUTE_7_SAFFRON_GATE_3_WP = WarpInstruction( 
		getHex(SAFFRON_CITY.ROUTE_7_SAFFRON_GATE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_CITY_TO_ROUTE_6_SAFFRON_GATE_1_WP = WarpInstruction( 
		getHex(SAFFRON_CITY.ROUTE_6_SAFFRON_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_CITY_TO_ROUTE_8_SAFFRON_GATE_1_WP = WarpInstruction( 
		getHex(SAFFRON_CITY.ROUTE_8_SAFFRON_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

