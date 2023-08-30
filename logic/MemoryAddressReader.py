import os, sys


def buildMemoryLocationsFromSym(detectedROMName, custom_path=None):
    memoryMapWarps = dict()
    memoryMapScripts = dict()

    sym_path = None
    is_syms = os.path.isdir("syms")
    if not is_syms:
        sym_path = "logic"
    else:
        sym_path = "."


    if detectedROMName == "Pokemon - Crystal Version 1.1":
        file = os.path.join(sym_path,"syms\\vanilla.sym")
    elif detectedROMName == "Pokemon - Crystal Speedchoice Version 7.2":
        print("\nLoading Speedchoice 7.2 Scripts...")
        # file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "crystal-speedchoice7.2.sym")
        file = os.path.join(sym_path,"syms\\crystal-speedchoice7.2.sym")
    elif detectedROMName == "Pokemon - Crystal Speedchoice Version 7.31":
        print("\nLoading Speedchoice 7.31 Scripts...")
        # file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "crystal-speedchoice7.31.sym")
        file = os.path.join(sym_path,"syms\\crystal-speedchoice7.31.sym")
    elif detectedROMName == "Pokemon - Crystal Speedchoice Version 8":
        print("\nLoading Speedchoice 8 Scripts...")
        file = os.path.join(sym_path,"syms\\crystal-speedchoice8.sym")
    elif detectedROMName == "Custom" and custom_path is not None:
        file = custom_path

    with open(file, "r") as memLoc:

        for line in memLoc.read().splitlines():
            # if "_MapEvents" in line:
            #     memInfo = line.split(" ")[0]
            #     mapName = line.split(" ")[1].split("_MapEvents")[0]
            #     bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
            #
            #     print("{} warp mem is at {}".format(mapName, hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000)))
            #
            #     memoryMapWarps[mapName] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000

            if "GoldenrodUndergroundWarehouseDirectorScript" in line:
                if line.split(" ")[1] == "GoldenrodUndergroundWarehouseDirectorScript":
                    memInfo = line.split(" ")[0]
                    bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                    memoryMapScripts["DirectorKeycard"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 11
                    print("DIRECTORS BADGE CHECK IS AT ",hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 11))

            if "GoldenrodDeptStoreB1F_MapScripts.ClearBoxes" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["GoldenrodB1FDoorUnlock"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 +1
                print("GoldenrodB1F DoorUnlock is at ", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 1))

            if "MapScripts.Lugia" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["LugiaToggle"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 12
                #print("LugiaToggle is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 12))

            if "WhirlIslandLugiaChamber_MapScripts.Appear" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["LugiaAddress"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 0 #Start of line

            if "sRoomDoors" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1].split(".")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 8
                #print(line.split(" ")[1].split(".")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 8))

            if "sRoom_EnterMovement" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000))
            # 14 offset for lance
            if "DoorLocksBehindYou" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1].split(".")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 13
                #print(line.split(" ")[1].split(".")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 13)) #technically its at 14 but we go back 1 to move which tile is changed

            if "LockBasementDoor" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1].split(".")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3
                #print(line.split(" ")[1].split(".")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "TilesetChampionsRoomColl" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 0xC6
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 0xC6))

            if "AideScript_GivePotion" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                byteOffset = 6
                if detectedROMName == "Pokemon - Crystal Speedchoice Version 8":
                    byteOffset += 3 # Speedchoice 7.4 added additional bytes for re-obtaining the item

                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + byteOffset
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 6))

            if "CyndaquilPokeBallScript" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49))

            if "TotodilePokeBallScript" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49))

            if "ChikoritaPokeBallScript" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49))

            if "Pokemon - Crystal Speedchoice" in detectedROMName:
                if "MapScripts.NoE4Check" in line:
                    memInfo = line.split(" ")[0]
                    bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                    #Address of NoE4CheckLabel
                    memoryMapScripts["NoE4Address"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 0
                    #Location of NoAppear (Rainbow Wing check)
                    memoryMapScripts["HoOhToggleE4"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 12
            if "MapScripts.HoOh" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                #Location of NoAppear (E4 Check)
                memoryMapScripts["HoOhToggle"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 12

            if "TinTowerRoof_MapScripts.Appear" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["HoOhAddress"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 0 #Start of line

            if "InitializeEventsScript" in line and "InitializeEventsScriptStdScript" not in line and "SkipDirector" not in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                if "Pokemon - Crystal Speedchoice" in detectedROMName:
                    memoryMapScripts["InitializeEventsScript"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 76
                    print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 76))
                else:
                    memoryMapScripts["InitializeEventsScript"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 73
                    print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 73))

            if "BlackthornCity_Blocks" in line and "Beta" not in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["BlackthornCity_Blocks"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "MountMortar2FInside_Blocks" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["MountMortar2FInside_Blocks"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 65

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 65))

            if "VermilionCity_Blocks" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["VermilionCity_Blocks"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 95

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 95))

            if "RuinsOfAlphOutside_Blocks" in line and "Beta" not in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["RuinsOfAlphOutside_Blocks"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 153

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 153))

            if "VictoryRoad_Blocks" in line and "Beta" not in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["VictoryRoad_Blocks"] = (int(bank, 16) * 0x4000) + int(address,16) - 0x4000 + 144

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 144))


            if "RuinsOfAlphKabutoChamber_MapScripts.FloorClosed" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["RuinsOfAlphKabutoChamber_MapScripts.FloorClosed"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "RuinsOfAlphHoOhChamber_MapScripts.FloorClosed" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["RuinsOfAlphHoOhChamber_MapScripts.FloorClosed"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "RuinsOfAlphOmanyteChamber_MapScripts.FloorClosed" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["RuinsOfAlphOmanyteChamber_MapScripts.FloorClosed"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "RuinsOfAlphAerodactylChamber_MapScripts.FloorClosed" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["RuinsOfAlphAerodactylChamber_MapScripts.FloorClosed"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "EcruteakGymClosed" in line and "EcruteakGymClosedText" not in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["EcruteakGymClosed"] = (int(bank,16) * 0x4000) + int(address, 16) - 0x4000

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000))

            if "TrainerGruntM1.Script" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["TrainerGruntM1.Script"] = (int(bank,16) * 0x4000) + int(address, 16) - 0x4000

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000))


            if "MountMoon_MapScripts" in line and "." not in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["MountMoon_MapScripts"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000))

            if "DragonsDenB1F_MapEvents" in line and "." not in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["DragonsDenB1F_MapEvents"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000))

            #Bike Anywhere Scripts
            if ".no_biking" in line: #Write a 8, original is 1
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["No_Biking"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 4

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 4))

            if "BikeFunction.CheckEnvironment" in line: #Write 0 original is 9
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["BikeFunction"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 17

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 17))

        memLoc.close() #memoryMapWarps,
    return memoryMapScripts