from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.SAFFRON_GYM

class SAFFRON_GYM(IntEnum):
	def __str__(self):
		return str(self.value)

	SAFFRON_CITY_2 = 1
	SAFFRON_GYM_18 = 3
	SAFFRON_GYM_19 = 4
	SAFFRON_GYM_20 = 5
	SAFFRON_GYM_21 = 6
	SAFFRON_GYM_22 = 7
	SAFFRON_GYM_23 = 8
	SAFFRON_GYM_24 = 9
	SAFFRON_GYM_25 = 10
	SAFFRON_GYM_26 = 11
	SAFFRON_GYM_27 = 12
	SAFFRON_GYM_28 = 13
	SAFFRON_GYM_29 = 14
	SAFFRON_GYM_30 = 15
	SAFFRON_GYM_31 = 16
	SAFFRON_GYM_32 = 17
	SAFFRON_GYM_3 = 18
	SAFFRON_GYM_4 = 19
	SAFFRON_GYM_5 = 20
	SAFFRON_GYM_6 = 21
	SAFFRON_GYM_7 = 22
	SAFFRON_GYM_8 = 23
	SAFFRON_GYM_9 = 24
	SAFFRON_GYM_10 = 25
	SAFFRON_GYM_11 = 26
	SAFFRON_GYM_12 = 27
	SAFFRON_GYM_13 = 28
	SAFFRON_GYM_14 = 29
	SAFFRON_GYM_15 = 30
	SAFFRON_GYM_16 = 31
	SAFFRON_GYM_17 = 32


class Saffron_Gym_Warp_Points(Enum): 

	SAFFRON_GYM_TO_SAFFRON_CITY_2_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_CITY_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	SAFFRON_GYM_TO_SAFFRON_GYM_18_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_18), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_19_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_19), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_20_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_20), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_21_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_21), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_22_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_22), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_23_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_23), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_24_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_24), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_25_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_25), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_26_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_26), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_27_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_27), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_28_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_28), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_29_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_29), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_30_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_30), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_31_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_31), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_32_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_32), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_3_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_4_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_5_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_6_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_7_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_8_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_9_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_9), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_10_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_10), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_11_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_11), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_12_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_12), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_13_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_13), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_14_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_14), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_15_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_15), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_16_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_16), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SAFFRON_GYM_TO_SAFFRON_GYM_17_WP = WarpInstruction( 
		getHex(SAFFRON_GYM.SAFFRON_GYM_17), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

