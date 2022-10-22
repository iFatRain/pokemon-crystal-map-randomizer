import time

import links_and_nodes.johto_all_warp_points
import links_and_nodes.kanto_all_warp_points
import links_and_nodes.johto_node_containers as Johto
import links_and_nodes.kanto_node_containers as Kanto
from links_and_nodes.johto_all_warp_points_dict import buildJohtoWarpLinks
from links_and_nodes.johto_node_dictionary_containers import buildJohtoMajorNodes, buildJohtoHubs, buildJohtoImportantDeadEnds, buildJohtoReachableDeadEnds, buildJohtoUselessDeadEnds, buildJohtoCorridors
from links_and_nodes.kanto_all_warp_points_dict import buildKantoWarpLinks
from links_and_nodes.kanto_node_dictionary_containers import buildKantoMajorNodes, buildKantoHubNodes, buildKantoImportantDeadEnds, buildKantoUselessDeadEnds, buildKantoCorridors
from logic import AutomaticWarpLocator
from logic.MemoryAddressReader import buildMemoryLocationsFromSym
from logic.DictionaryRandomizerLogic import randomizationStep1, randomizationStep2, randomizationStep3, randomizationStep4, \
    checkJohtoCompletability, randomizationStep5, checkKantoCompletability, checkFullCompletability
from class_definitions import WarpInstruction, getHex

# def randomizeWarps(combinedRegions, addNewBark):
#     print("Randomizing..")
#     if combinedRegions:
#         combinedFullyCompletable = False
#         while combinedFullyCompletable is False:
#             if addNewBark:
#                 print("ADDING NEWBARK")
#                 randomizedNodes = randomizationStep1(list(Johto.MajorNodes_Johto) + list(Kanto.MajorNodes_Kanto))
#             else:
#                 randomizedNodes = randomizationStep1(list(Johto.MajorNodes_Johto) + list(Kanto.MajorNodes_Kanto))
#             randomizedNodes = randomizationStep2(randomizedNodes, list(Johto.HubNodes_Johto) + list(Kanto.HubNodes_Kanto))
#             randomizedNodes = randomizationStep3(randomizedNodes,
#                                                  list(Johto.ImportantDeadEndNodes_Johto) + list(Kanto.ImportantDeadEndNodes_Kanto),
#                                                  list(Johto.ReachableUselessDeadEndNodes_Johto) + list(Kanto.ReachableUselessDeadEndNodes_Kanto),
#                                                  list(Johto.UnreachableUselessDeadEndNodes_Johto) + list(Kanto.UnreachableUselessDeadEndNodes_Kanto))
#             randomizedNodes = randomizationStep4(randomizedNodes)
#             randomizedNodes = randomizationStep5(randomizedNodes, list(Johto.TwoWayCorridorNodes_Johto) + list(Kanto.TwoWayCorridorNodes_Kanto))
#             combinedFullyCompletable = checkFullCompletability(randomizedNodes)
#
#
#
#
#
#     else:
#         johtoFullyCompletable = False
#         while johtoFullyCompletable is False:
#             randomizedJohto = randomizationStep1(list(Johto.MajorNodes_Johto))
#             randomizedJohto = randomizationStep2(randomizedJohto, list(Johto.HubNodes_Johto))
#             randomizedJohto = randomizationStep3(randomizedJohto, list(Johto.ImportantDeadEndNodes_Johto),
#                                                  list(Johto.ReachableUselessDeadEndNodes_Johto),
#                                                  list(Johto.UnreachableUselessDeadEndNodes_Johto))
#             randomizedJohto = randomizationStep4(randomizedJohto)
#             randomizedJohto = randomizationStep5(randomizedJohto, list(Johto.TwoWayCorridorNodes_Johto))
#             johtoFullyCompletable = checkJohtoCompletability(randomizedJohto)
#
#         kantoFullyCompletable = False
#         while kantoFullyCompletable is False:
#             randomizedKanto = randomizationStep1(list(Kanto.MajorNodes_Kanto))
#             randomizedKanto = randomizationStep2(randomizedKanto, list(Kanto.HubNodes_Kanto))
#             randomizedKanto = randomizationStep3(randomizedKanto, list(Kanto.ImportantDeadEndNodes_Kanto),
#                                                  list(Kanto.ReachableUselessDeadEndNodes_Kanto),
#                                                  list(Kanto.UnreachableUselessDeadEndNodes_Kanto))
#             randomizedKanto = randomizationStep4(randomizedKanto)
#             randomizedKanto = randomizationStep5(randomizedKanto, list(Kanto.TwoWayCorridorNodes_Kanto))
#
#
#             kantoFullyCompletable = checkKantoCompletability(randomizedKanto)
#
#         randomizedNodes = randomizedJohto + randomizedKanto
#
#
#
#     return randomizedNodes


def randomizeWarpsNew(combinedRegions,unrandomMart):
    print("Randomizing..")
    if combinedRegions:
        combinedFullyCompletable = False
        while combinedFullyCompletable is False:
            randomizedNodes = randomizationStep1(dict(**buildJohtoMajorNodes(unrandomMart),**buildKantoMajorNodes()))
            randomizedNodes = randomizationStep2(randomizedNodes, dict(**buildJohtoHubs(),**buildKantoHubNodes()))
            randomizedNodes = randomizationStep3(randomizedNodes,
                                                 dict(**buildJohtoImportantDeadEnds(unrandomMart),**buildKantoImportantDeadEnds()),
                                                 dict(**buildJohtoReachableDeadEnds()),
                                                 dict(**buildJohtoUselessDeadEnds(),**buildKantoUselessDeadEnds()))
            randomizedNodes = randomizationStep4(randomizedNodes)
            randomizedNodes = randomizationStep5(randomizedNodes, dict(**buildJohtoCorridors(),**buildKantoCorridors()))
            combinedFullyCompletable = checkFullCompletability(randomizedNodes)

    else:
        johtoFullyCompletable = False
        while johtoFullyCompletable is False:
            randomizedJohto = randomizationStep1(buildJohtoMajorNodes(unrandomMart))
            randomizedJohto = randomizationStep2(randomizedJohto, buildJohtoHubs())
            randomizedJohto = randomizationStep3(randomizedJohto, buildJohtoImportantDeadEnds(unrandomMart),
                                                 buildJohtoReachableDeadEnds(),
                                                 buildJohtoUselessDeadEnds())
            randomizedJohto = randomizationStep4(randomizedJohto)
            randomizedJohto = randomizationStep5(randomizedJohto, buildJohtoCorridors())
            johtoFullyCompletable = checkJohtoCompletability(randomizedJohto)

        kantoFullyCompletable = False
        while kantoFullyCompletable is False:
            randomizedKanto = randomizationStep1(buildKantoMajorNodes())
            randomizedKanto = randomizationStep2(randomizedKanto, buildKantoHubNodes())
            randomizedKanto = randomizationStep3(randomizedKanto, buildKantoImportantDeadEnds(),
                                                 dict(),
                                                 buildKantoUselessDeadEnds())
            randomizedKanto = randomizationStep4(randomizedKanto)
            randomizedKanto = randomizationStep5(randomizedKanto, buildKantoCorridors())


            kantoFullyCompletable = checkKantoCompletability(randomizedKanto)

        randomizedNodes = randomizedJohto + randomizedKanto



    return randomizedNodes

def checkForDoubles(inputLink, inputROM, warpLocations, johtoWarps):
    if inputLink.OWN == johtoWarps.get("Ruins_Of_Alph_Ho_Oh_Chamber_Links").get("RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_2_LINK").OWN:
        print("Fixing Ho Oh Chamber Double!")
        standardLink = johtoWarps.get("Ruins_Of_Alph_Ho_Oh_Item_Room_Links")
        inputROM.seek(warpLocations[standardLink.get("RUINS_OF_ALPH_HO_OH_ITEM_ROOM_TO_RUINS_OF_ALPH_HO_OH_WORD_ROOM_1_LINK").MEMORY_ORIGIN]
                      + standardLink.get("RUINS_OF_ALPH_HO_OH_ITEM_ROOM_TO_RUINS_OF_ALPH_HO_OH_WORD_ROOM_1_LINK").OFFSET)
        inputROM.write(WarpInstruction.getInstruction(inputLink.LINK.value))
        inputROM.read(2)
        inputROM.write(WarpInstruction.getInstruction(inputLink.LINK.value))
        print("Done Fixing Ho Oh Double")

    if inputLink.OWN == johtoWarps.get("Ruins_Of_Alph_Kabuto_Chamber_Links").get("RUINS_OF_ALPH_KABUTO_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_4_LINK").OWN:
        print("Fixing Kabuto Chamber Double!")
        standardLink = johtoWarps.get("Ruins_Of_Alph_Kabuto_Item_Room_Links")
        inputROM.seek(warpLocations[standardLink.get("RUINS_OF_ALPH_KABUTO_ITEM_ROOM_TO_RUINS_OF_ALPH_KABUTO_WORD_ROOM_1_LINK").MEMORY_ORIGIN]
                      + standardLink.get("RUINS_OF_ALPH_KABUTO_ITEM_ROOM_TO_RUINS_OF_ALPH_KABUTO_WORD_ROOM_1_LINK").OFFSET)
        inputROM.write(WarpInstruction.getInstruction(inputLink.LINK.value))
        inputROM.read(2)
        inputROM.write(WarpInstruction.getInstruction(inputLink.LINK.value))
        print("Done Fixing Kabuto Double")


    if inputLink.OWN == johtoWarps.get("Ruins_Of_Alph_Aerodactyl_Chamber_Links").get("RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_8_LINK").OWN:
        print("Fixing Aero Chamber Double!")
        standardLink = johtoWarps.get("Ruins_Of_Alph_Aerodactyl_Item_Room_Links")
        inputROM.seek(warpLocations[standardLink.get("RUINS_OF_ALPH_AERODACTYL_ITEM_ROOM_TO_RUINS_OF_ALPH_AERODACTYL_WORD_ROOM_1_LINK").MEMORY_ORIGIN]
                      + standardLink.get("RUINS_OF_ALPH_AERODACTYL_ITEM_ROOM_TO_RUINS_OF_ALPH_AERODACTYL_WORD_ROOM_1_LINK").OFFSET)
        inputROM.write(WarpInstruction.getInstruction(inputLink.LINK.value))
        inputROM.read(2)
        inputROM.write(WarpInstruction.getInstruction(inputLink.LINK.value))
        print("Done Fixing Aero Double")


    if inputLink.OWN == johtoWarps.get("Ruins_Of_Alph_Omanyte_Chamber_Links").get("RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_6_LINK").OWN:
        print("Fixing Omanyte Chamber Double!")
        standardLink = johtoWarps.get("Ruins_Of_Alph_Omanyte_Item_Room_Links")
        inputROM.seek(warpLocations[standardLink.get("RUINS_OF_ALPH_OMANYTE_ITEM_ROOM_TO_RUINS_OF_ALPH_OMANYTE_WORD_ROOM_1_LINK").MEMORY_ORIGIN]
                      + standardLink.get("RUINS_OF_ALPH_OMANYTE_ITEM_ROOM_TO_RUINS_OF_ALPH_OMANYTE_WORD_ROOM_1_LINK").OFFSET)
        inputROM.write(WarpInstruction.getInstruction(inputLink.LINK.value))
        inputROM.read(2)
        inputROM.write(WarpInstruction.getInstruction(inputLink.LINK.value))
        print("Done Fixing Omanyte Double")


    if inputLink.OWN == johtoWarps.get("Tin_Tower_1F_Links").get("TIN_TOWER_1F_TO_ECRUTEAK_CITY_LINK").OWN:
        print("Fixing Rear Stairs of Tin Tower 1F")
        standardLink = johtoWarps.get("Tin_Tower_1F_Links")
        inputROM.seek(warpLocations[standardLink.get("TIN_TOWER_1F_TO_ECRUTEAK_CITY_LINK").MEMORY_ORIGIN] + 10)
        inputROM.write(WarpInstruction.getInstruction(inputLink.LINK.value))
        print("Done fixing Rear Stairs for Tin Tower")


def reassignWarp(inputROM, link, memLocation, locationOfWarpScript, bytesToFind):
    inputROM.seek(memLocation - 2)
    y_coord = inputROM.read(1)
    x_coord = inputROM.read(1)
    dest_map = WarpInstruction.getInstruction(link.OWN.value)[1::]
    inputROM.seek(locationOfWarpScript)
    script = inputROM.read(150)
    dynamicOffset = script.find(bytesToFind)
    inputROM.seek(locationOfWarpScript + dynamicOffset)
    inputROM.seek(locationOfWarpScript + dynamicOffset)
    inputROM.write(dest_map)
    inputROM.write(x_coord)
    inputROM.write(y_coord)
    inputROM.seek(locationOfWarpScript + dynamicOffset)

def directConnectRed(inputROM, warpLocations, johtoWarps, kantoWarps):

    link = johtoWarps.get("Victory_Road_Gate_Links").get("VICTORY_ROAD_GATE_TO_ROUTE_28_2_LINK")
    inputROM.seek(warpLocations[link.MEMORY_ORIGIN] + link.OFFSET)
    inputROM.write(WarpInstruction.getInstruction(link.LINK.value))
    if link.DUAL_WIDTH is True:
        inputROM.read(2)
        inputROM.write(WarpInstruction.getInstruction(link.LINK.value))

    link = kantoWarps.get("Silver_Cave_Room_3_Links").get("SILVER_CAVE_ROOM_3_TO_SILVER_CAVE_ROOM_2_2_LINK")
    inputROM.seek(warpLocations[link.MEMORY_ORIGIN] + link.OFFSET)
    inputROM.write(WarpInstruction.getInstruction(link.LINK.value))
    if link.DUAL_WIDTH is True:
        inputROM.read(2)
        inputROM.write(WarpInstruction.getInstruction(link.LINK.value))

def randomizeROM(inputROM, settings, customPath):

    startTime = time.time()

    print("Randomizing Warps..")
    randomizedNodes = randomizeWarpsNew(settings[2],settings[9])

    rom = inputROM.read()
    lookupDict = AutomaticWarpLocator.getLookupDict()
    warpLocations = dict()
    for key in lookupDict.keys():

        foundLocation = rom.find(lookupDict[key])
        warpLocations[key] = foundLocation + 5
    scriptLocations = buildMemoryLocationsFromSym(settings[0], customPath)


    # for key in warpLocations.keys():
    #     print(key, " is at ",hex(warpLocations.get(key)))
    johtoWarps = buildJohtoWarpLinks()
    kantoWarps = buildKantoWarpLinks()

    print("Writing New Warps to ROM...")
    for node in randomizedNodes:
        for link in node[1].LINKS:
            memLocation = warpLocations[link.MEMORY_ORIGIN] + link.OFFSET
            inputROM.seek(memLocation)
            inputROM.write(WarpInstruction.getInstruction(link.LINK.value))
            if link.DUAL_WIDTH is True:
                inputROM.read(2)
                inputROM.write(WarpInstruction.getInstruction(link.LINK.value))

            checkForDoubles(link, inputROM, warpLocations, johtoWarps)

            #TODO investigate these with the changed speedchoice
            if link.LINK == johtoWarps.get("Ecruteak_Gym_Links").get("ECRUTEAK_GYM_TO_ECRUTEAK_CITY_LINK").OWN:
                print("REASSIGNING ECRUTEAK KICKOUT WARP")
                reassignWarp(inputROM, link, memLocation, scriptLocations["EcruteakGymClosed"], b'\x04\t\x06\x1b')
            if link.LINK == johtoWarps.get("Slowpoke_Well_B1F_Links").get("SLOWPOKE_WELL_B1F_TO_AZALEA_TOWN_LINK").OWN:
                print("REASSIGNING SLOWPOKE WELL WARP")
                reassignWarp(inputROM, link, memLocation, scriptLocations["TrainerGruntM1.Script"], b'\x08\x04\x03\x03')

    directConnectRed(inputROM, warpLocations, johtoWarps, kantoWarps)

    randomizeTime = time.time() - startTime
    print("Time to randomize warps and write to ROM:", randomizeTime,"seconds")

    writeWarpRandoNonOptionalChanges(inputROM, warpLocations, scriptLocations, settings)

    if settings[1]:
        enableLegendaries(inputROM, warpLocations, scriptLocations,settings)

    if settings[3]:
        disableDarkMode(inputROM, warpLocations)

    if settings[4]:
        doMapChanges(inputROM, warpLocations, scriptLocations)

    if settings[5]:
        catchEmAllBoi(inputROM, warpLocations,scriptLocations)

    if settings[6]:
        presolveAlphRuins(inputROM, warpLocations, scriptLocations)

    if settings[7]:
        removeRivalInMoon(inputROM, warpLocations, scriptLocations)

    if settings[8]:
        changeGoldenrodRockets(inputROM, warpLocations, scriptLocations)

    #Starter levels will always be final script
    if settings[-1]:
        print("\tMaking starters lv100 for testing")
        inputROM.seek(scriptLocations["CyndaquilPokeBallScript"])
        inputROM.write(bytes.fromhex(getHex(98)))
        inputROM.seek(scriptLocations["TotodilePokeBallScript"])
        inputROM.write(bytes.fromhex(getHex(98)))
        inputROM.seek(scriptLocations["ChikoritaPokeBallScript"])
        inputROM.write(bytes.fromhex(getHex(98)))

    #For testing custom scripts/warps
    # inputROM.seek(warpLocations["CherrygroveCity"])
    # inputROM.write(bytes.fromhex(getHex(1)))
    # inputROM.write(bytes.fromhex(getHex(3)))
    # inputROM.write(bytes.fromhex(getHex(30)))

    inputROM.close()

    return randomizedNodes

def removeRivalInMoon(inputROM, warpLocations, scriptLocations):
    print("Removing Mt.Moon Rival Fight")
    inputROM.seek(scriptLocations["InitializeEventsScript"] + 213)
    inputROM.write(bytes.fromhex(getHex(164)))
    inputROM.write(bytes.fromhex(getHex(7)))

    inputROM.seek(scriptLocations["MountMoon_MapScripts"] + 1)
    inputROM.write(bytes.fromhex(getHex(141)))

    inputROM.seek(warpLocations["MountMoon"] + 52)  # Rival mt moon
    inputROM.write(bytes.fromhex(getHex(9)))
    inputROM.write(bytes.fromhex(getHex(7)))

def writeWarpRandoNonOptionalChanges(inputROM, warpLocations, scriptLocations, settings):

    inputROM.seek(scriptLocations["No_Biking"])
    inputROM.write(bytes.fromhex(getHex(8)))
    inputROM.seek(scriptLocations["BikeFunction"])
    inputROM.write(bytes.fromhex(getHex(0)))

    #Makes the Goldenrod B1F basement door always open so you aren't blocked
    inputROM.seek(scriptLocations["GoldenrodB1FDoorUnlock"])
    inputROM.write(bytes.fromhex(getHex(9)))
    inputROM.write(bytes.fromhex(getHex(7)))

    #Makes slowpoke guard walk left/right so you aren't blocked
    inputROM.seek(warpLocations["AzaleaTown"] + 113)
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(1)))

    # print("Mahogany: ", hex(warpLocations["MahoganyTown"]))
    inputROM.seek(warpLocations["MahoganyTown"] + 25)
    inputROM.write(bytes.fromhex(getHex(7)))
    inputROM.read(7)
    inputROM.write(bytes.fromhex(getHex(7)))
    inputROM.read(30)
    inputROM.write(bytes.fromhex(getHex(17)))

    # print("Rt32: ", hex(warpLocations["Route32"]))
    inputROM.seek(warpLocations["Route32"] + 21)
    inputROM.write(bytes.fromhex(getHex(11)))

    print("\tDisabling E4 Walking")
    inputROM.seek(scriptLocations["KogasRoom_EnterMovement"])
    inputROM.write(bytes.fromhex(getHex(71)))
    inputROM.seek(scriptLocations["KarensRoom_EnterMovement"])
    inputROM.write(bytes.fromhex(getHex(71)))
    inputROM.seek(scriptLocations["WillsRoom_EnterMovement"])
    inputROM.write(bytes.fromhex(getHex(71)))
    inputROM.seek(scriptLocations["BrunosRoom_EnterMovement"])
    inputROM.write(bytes.fromhex(getHex(71)))
    inputROM.seek(scriptLocations["LancesRoom_EnterMovement"])
    inputROM.write(bytes.fromhex(getHex(71)))

    print("\tOpening All E4 Doors")
    inputROM.seek(scriptLocations["KogasDoorLocksBehindYou"])
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek((scriptLocations["KarensDoorLocksBehindYou"]))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek((scriptLocations["WillsDoorLocksBehindYou"]))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek((scriptLocations["BrunosDoorLocksBehindYou"]))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek(scriptLocations["LancesDoorLocksBehindYou"])
    inputROM.read(1)
    inputROM.write(bytes.fromhex(getHex(49)))

    inputROM.seek(scriptLocations["KogasRoomDoors"])
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek((scriptLocations["KarensRoomDoors"]))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek((scriptLocations["WillsRoomDoors"]))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek((scriptLocations["BrunosRoomDoors"]))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek(scriptLocations["LancesRoomDoors"])
    inputROM.read(1)
    inputROM.write(bytes.fromhex(getHex(49)))

    print("\tFixing Champions Room Tile Collision")
    inputROM.seek(scriptLocations["TilesetChampionsRoomColl"])
    inputROM.write(bytes.fromhex(getHex(112)))
    inputROM.write(bytes.fromhex(getHex(112)))

    print("\tUnlocking Basement without Keycard")
    inputROM.seek(scriptLocations['LockBasementDoor'])
    inputROM.write(bytes.fromhex(getHex(46)))

    print("\tMaking Director Always Appear in Underground Warehouse")
    inputROM.seek(warpLocations['GoldenrodUndergroundWarehouse'] + 66)
    inputROM.write(bytes.fromhex(getHex(255)))
    inputROM.write(bytes.fromhex(getHex(255)))
    print(hex(scriptLocations["DirectorKeycard"]))
    inputROM.seek(scriptLocations["DirectorKeycard"])
    inputROM.write(bytes.fromhex(getHex(0)))

    # Remove Right Guard from Victory Road Gate
    print("\tFixing Victory Road Gate")
    if "Pokemon - Crystal Speedchoice" in settings[0]:
        print("Detected Speedchoice offset of 91")
        inputROM.seek(warpLocations["VictoryRoadGate"] + 86)
    else:
        inputROM.seek(warpLocations["VictoryRoadGate"] + 90)
        print("Going to offset of 95")
    inputROM.write(bytes.fromhex(getHex(26)))
    inputROM.write(bytes.fromhex(getHex(0)))

    print("\t Removing Rocks from Above")
    inputROM.seek(scriptLocations["InitializeEventsScript"])
    inputROM.write(bytes.fromhex(getHex(9)))
    inputROM.read(2)
    inputROM.write(bytes.fromhex(getHex(10)))
    inputROM.read(2)
    inputROM.write(bytes.fromhex(getHex(11)))
    inputROM.read(2)
    inputROM.write(bytes.fromhex(getHex(12)))

    print("\t Making lower alph usable")
    inputROM.seek(scriptLocations["RuinsOfAlphOutside_Blocks"])
    inputROM.write(bytes.fromhex(getHex(90)))
    inputROM.read(8)
    inputROM.write(bytes.fromhex(getHex(90)))

    print("\t Making Victory Road Usable")
    inputROM.seek(scriptLocations["VictoryRoad_Blocks"])
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.read(6)
    inputROM.write(bytes.fromhex(getHex(2)))

def changeGoldenrodRockets(inputROM, warpLocations, scriptLocations):
    print("Moving Goldenrod Rockets", hex(warpLocations["GoldenrodCity"]))
    inputROM.seek(warpLocations["GoldenrodCity"] + 229)
    inputROM.write(bytes.fromhex(getHex(7)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(17)))
    inputROM.read(9)
    inputROM.write(bytes.fromhex(getHex(21)))
    inputROM.write(bytes.fromhex(getHex(33)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(70)))

    inputROM.read(11)
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(16)))

    inputROM.read(10)
    inputROM.write(bytes.fromhex(getHex(24)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(66)))

    inputROM.read(9)
    inputROM.write(bytes.fromhex(getHex(31)))
    inputROM.write(bytes.fromhex(getHex(37)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(67)))

    inputROM.read(9)
    inputROM.write(bytes.fromhex(getHex(14)))
    inputROM.write(bytes.fromhex(getHex(32)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(34)))

    inputROM.read(9)
    inputROM.write(bytes.fromhex(getHex(16)))
    inputROM.write(bytes.fromhex(getHex(24)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(51)))


def AddressToIntValues(address):
    bank_size = 0x4000
    value = (address % bank_size) + bank_size
    bytes_return = value.to_bytes(2, byteorder='little')
    return bytes_return


def enableLegendaries(inputROM, warpLocations, scriptLocations, settings):
    print("\tEnabling Always Catchable Setting")

    inputROM.seek(warpLocations["WhirlIslandLugiaChamber"] + 7)
    inputROM.write(bytes.fromhex(getHex(15)))
    inputROM.seek(scriptLocations["LugiaToggle"])
    inputROM.write(bytes.fromhex(getHex(18)))
    #Change ho-oh, different in each version
    if "1.1" in settings[0]:
        print("Doing Vanilla Ho-OH")
        inputROM.seek(scriptLocations["HoOhToggle"])
        inputROM.write(bytes.fromhex(getHex(62)))
    elif "Speedchoice" in settings[0]:
        inputROM.seek(scriptLocations["HoOhToggle"])
        appearAddress = scriptLocations["HoOhAddress"]
        bytes_result = AddressToIntValues(appearAddress)
        # Convert appear address to bytes from the label it jumps to, and use this!
        inputROM.write(bytes_result)
        inputROM.seek(scriptLocations["HoOhToggleE4"])
        inputROM.write(bytes_result)
    print("Done Enabling Legendaries")


def presolveAlphRuins(inputROM, warpLocations, scriptLocations):
    print("Fixing the Ruins of Alph FLoors")
    print("Fixing Aero")
    inputROM.seek(scriptLocations["RuinsOfAlphAerodactylChamber_MapScripts.FloorClosed"])
    inputROM.write(bytes.fromhex(getHex(24)))
    inputROM.read(3)
    inputROM.write(bytes.fromhex(getHex(25)))
    print("Fixing HoOh")
    inputROM.seek(scriptLocations["RuinsOfAlphHoOhChamber_MapScripts.FloorClosed"])
    inputROM.write(bytes.fromhex(getHex(24)))
    inputROM.read(3)
    inputROM.write(bytes.fromhex(getHex(25)))
    print("Fixing Omanyte")
    inputROM.seek(scriptLocations["RuinsOfAlphOmanyteChamber_MapScripts.FloorClosed"])
    inputROM.write(bytes.fromhex(getHex(24)))
    inputROM.read(3)
    inputROM.write(bytes.fromhex(getHex(25)))
    print("Fixing Kabuto")
    inputROM.seek(scriptLocations["RuinsOfAlphKabutoChamber_MapScripts.FloorClosed"])
    inputROM.write(bytes.fromhex(getHex(24)))
    inputROM.read(3)
    inputROM.write(bytes.fromhex(getHex(25)))

def doMapChanges(inputROM, warpLocations, scriptLocations):
    print("\t Vermillion Map Block Changes")
    inputROM.seek(scriptLocations["VermilionCity_Blocks"])
    inputROM.write(bytes.fromhex(getHex(97)))

    print("\t Mortar Map Block Changes")
    inputROM.seek(scriptLocations["MountMortar2FInside_Blocks"])
    inputROM.write(bytes.fromhex(getHex(2)))

    print("\t Blackthorn Map Block Changes")
    inputROM.seek(scriptLocations["BlackthornCity_Blocks"])
    inputROM.write(bytes.fromhex(getHex(111)))  # 6F
    inputROM.write(bytes.fromhex(getHex(114)))  # 72
    inputROM.write(bytes.fromhex(getHex(109)))
    inputROM.write(bytes.fromhex(getHex(113)))
    inputROM.write(bytes.fromhex(getHex(111)))  # 6F
    inputROM.write(bytes.fromhex(getHex(114)))  # 6C
    inputROM.read(14)
    inputROM.write(bytes.fromhex(getHex(105)))
    inputROM.read(4)
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(71)))  # 47
    inputROM.read(11)
    inputROM.write(bytes.fromhex(getHex(109)))  # 6D
    inputROM.write(bytes.fromhex(getHex(105)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.read(14)
    inputROM.write(bytes.fromhex(getHex(113)))
    inputROM.write(bytes.fromhex(getHex(105)))
    inputROM.write(bytes.fromhex(getHex(2)))  # 69
    inputROM.read(17)
    inputROM.write(bytes.fromhex(getHex(113)))
    inputROM.write(bytes.fromhex(getHex(105)))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.read(17)
    inputROM.write(bytes.fromhex(getHex(113)))  # 71
    inputROM.write(bytes.fromhex(getHex(105)))
    inputROM.write(bytes.fromhex(getHex(2)))  # 71
    inputROM.read(17)
    inputROM.write(bytes.fromhex(getHex(113)))  # 71
    inputROM.write(bytes.fromhex(getHex(105)))
    inputROM.write(bytes.fromhex(getHex(2)))  # 71
    inputROM.read(17)
    inputROM.write(bytes.fromhex(getHex(113)))  # 71
    inputROM.read(28)
    inputROM.write(bytes.fromhex(getHex(75)))  # 71
    inputROM.read(39)
    inputROM.write(bytes.fromhex(getHex(90)))  # 71
    inputROM.read(16)
    inputROM.write(bytes.fromhex(getHex(90)))  # 71
    inputROM.read(2)
    inputROM.write(bytes.fromhex(getHex(90)))  # 71
    inputROM.seek(warpLocations["BlackthornCity"] + 56)
    inputROM.write(bytes.fromhex(getHex(23)))

def catchEmAllBoi(inputROM, warpLocations, scriptLocations):
    print("\tMaking Aides Give Pokeballs")
    inputROM.seek(scriptLocations["AideScript_GivePotion"])
    inputROM.write(bytes.fromhex(getHex(5)))
    inputROM.write(bytes.fromhex(getHex(5)))

def disableDarkMode(inputROM, warpLocations):
    print("Removing Flash Requirement in Dark Caves")
    # print(hex(warpLocations["DungeonsMapGroup"] +587)) #write 12, read 8, 9 times then read 35, then write, read 8, write, then read 72, write, read 8 , write
    inputROM.seek(warpLocations["DungeonsMapGroup"] + 586)
    for i in range(9):
        inputROM.write(bytes.fromhex(getHex(18)))
        inputROM.read(8)
    inputROM.read(27)
    inputROM.write(bytes.fromhex(getHex(18)))
    inputROM.read(8)
    inputROM.write(bytes.fromhex(getHex(18)))
    inputROM.read(71)
    inputROM.write(bytes.fromhex(getHex(18)))
    inputROM.read(8)
    inputROM.write(bytes.fromhex(getHex(18)))