import time

from logic import AutomaticWarpLocator
from logic.MemoryAddressReader import buildMemoryLocationsFromSym
from logic.NewRandomizerLogic import randomizationStep1, randomizationStep2, randomizationStep3, randomizationStep4, \
    checkSeedCompletability, randomizationStep5
from class_definitions import WarpInstruction, getHex

def randomizeWarps():
    completableSeed = False
    fullyCompletable = False
    while fullyCompletable is False:
        print("Randomizing..")
        print("Doing Step 1")
        randomizedNodes = randomizationStep1()
        print("Doing Step 2")
        randomizedNodes = randomizationStep2(randomizedNodes)
        print("Doing Step 3")
        randomizedNodes = randomizationStep3(randomizedNodes)
        print("Doing Step 4")
        randomizedNodes = randomizationStep4(randomizedNodes)
        print("Doing Step 5")
        randomizedNodes = randomizationStep5(randomizedNodes)
        print("Checking the seed....")
        completableSeed, fullyCompletable = checkSeedCompletability(randomizedNodes)

    return randomizedNodes


def randomizeROM(inputROM, settings):

    startTime = time.time()
    randomizedNodes = randomizeWarps()

    rom = inputROM.read()
    scriptLocations = buildMemoryLocationsFromSym(settings[1])
    lookupDict = AutomaticWarpLocator.getLookupDict()
    warpLocations = dict()
    for key in lookupDict.keys():

        foundLocation = rom.find(lookupDict[key])
        # print(key, "was found at", hex(foundLocation + 5))
        warpLocations[key] = foundLocation + 5



    # for node in randomizedNodes:
    #     for link in node.value.LINKS:
    #         # print(link.value.MODIFIED)

    print("Writing random warps to rom...")
    for node in randomizedNodes:
        # print("Writing Node: ", node)
        for link in node.value.LINKS:
            memLocation = warpLocations[link.value.MEMORY_ORIGIN] + link.value.OFFSET
            inputROM.seek(memLocation)
            inputROM.write(WarpInstruction.getInstruction(link.value.LINK.value))
            if link.value.DUAL_WIDTH is True:
                inputROM.read(2)
                inputROM.write(WarpInstruction.getInstruction(link.value.LINK.value))
    randomizeTime = time.time() - startTime


    # for values in scriptLocations:
    #     print(values)
    # Make Lugia and Ho-oh always accessable
    print(settings[0])
    print(settings[1])
    if settings[0] == 1:
        print("EASY LEGENDARIES DETECTED")
        print("WhirlIslandLugiaChamber is at", hex(warpLocations["WhirlIslandLugiaChamber"]))
        memToSeekTo = (warpLocations["WhirlIslandLugiaChamber"] + 7)
        print("Seeking to:", hex(memToSeekTo))
        inputROM.seek(memToSeekTo) #0x0018C546Vanilla Lugia Location
        inputROM.write(bytes.fromhex(getHex(15)))
        print("Wrote lugia loction, changing the item")
        inputROM.seek(scriptLocations["LugiaToggle"]) # 0x0018C510Vanilla Lugia Script
        inputROM.write(bytes.fromhex(getHex(18)))


        print("changing ho oh item")
        print("HoOh Toggle is at ", hex(scriptLocations["HoOhToggle"])) #00077256 is speedchoice
        inputROM.seek(scriptLocations["HoOhToggle"]) #0x0007723C is vanilla
        # if settings[1] == "Pokemon - Crystal Version 1.1":
        #     inputROM.write(bytes.fromhex(getHex(62)))
        # else:
        inputROM.write(bytes.fromhex(getHex(88)))

    print("Disabling E4 Walking")
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


    print("Fixing E4 Doors")
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

    print("Fixing the tile collision")
    inputROM.seek(scriptLocations["TilesetChampionsRoomColl"])
    inputROM.write(bytes.fromhex(getHex(112)))


    print("Writing Aides Give Potion for Pokeballs")
    inputROM.seek(scriptLocations["AideScript_GivePotion"])
    inputROM.write(bytes.fromhex(getHex(5)))
    inputROM.write(bytes.fromhex(getHex(5)))

    #Always unlocks the underground switch room door to make underground a hub
    inputROM.seek(scriptLocations['LockBasementDoor'])
    inputROM.write(bytes.fromhex(getHex(46)))

    #This will make the director always in underground warehouse
    inputROM.seek(warpLocations['GoldenrodUndergroundWarehouse'] + 66)
    inputROM.write(bytes.fromhex(getHex(255)))
    inputROM.write(bytes.fromhex(getHex(255)))

    print("Making starters lv100 for testing")
    inputROM.seek(scriptLocations["CyndaquilPokeBallScript"])
    inputROM.write(bytes.fromhex(getHex(100)))
    inputROM.seek(scriptLocations["TotodilePokeBallScript"])
    inputROM.write(bytes.fromhex(getHex(100)))
    inputROM.seek(scriptLocations["ChikoritaPokeBallScript"])
    inputROM.write(bytes.fromhex(getHex(100)))

    inputROM.close
    print("Time to randomize links: ", randomizeTime)
    return randomizedNodes

