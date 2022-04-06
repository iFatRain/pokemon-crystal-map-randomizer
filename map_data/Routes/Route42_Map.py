from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Mahogany

mapGroup = MapGroup.MAHOGANY
specificMap = Mahogany.ROUTE_42

class ROUTE_42(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_42_ECRUTEAK_GATE = 1
    MOUNT_MORTAR_1F_OUTSIDE_LEFT = 3
    MOUNT_MORTAR_1F_OUTSIDE_MIDDLE = 4
    MOUNT_MORTAR_1F_OUTSIDE_RIGHT = 5

class Route_42_Warp_Points(Enum):

    ROUTE_42_TO_ROUTE_42_ECRUTEAK_GATE_WP = WarpInstruction(
        getHex(ROUTE_42. ROUTE_42_ECRUTEAK_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_LEFT_WP = WarpInstruction(
        getHex(ROUTE_42.MOUNT_MORTAR_1F_OUTSIDE_LEFT),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_MIDDLE_WP = WarpInstruction(
        getHex(ROUTE_42.MOUNT_MORTAR_1F_OUTSIDE_MIDDLE),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_RIGHT_WP = WarpInstruction(
        getHex(ROUTE_42.MOUNT_MORTAR_1F_OUTSIDE_RIGHT),
        getHex(mapGroup),
        getHex(specificMap))

