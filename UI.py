import hashlib
import os
import random
import shutil
import sys
import tkinter as tk
import traceback
from enum import Enum
from tkinter import filedialog
from idlelib.tooltip import Hovertip

import randomizeROM

def displayMainWindow():

    mainWindow.geometry("800x460")
    mainWindow.title("Pokemon Crystal Warp Randomizer v1.2.0 by iFatRain")
    mainWindow.configure(bg= UI_Colors.Lavender_Web.value)
    mainWindow.protocol("WM_DELETE_WINDOW", lambda:[mainWindow.destroy(), quit()])

    baseOptions_Label       = tk.Label(mainWindow,
                                         text="Pick base version:",
                                         bg=UI_Colors.Lavender_Web.value,
                                         font=("Comic Sans MS", 12, ""))

    baseOptions_Vanilla     = tk.Radiobutton(mainWindow,
                                               text="Vanilla",
                                               font=("Comic Sans MS", 12, ""),
                                               bg=UI_Colors.Lavender_Web.value,
                                               activebackground=UI_Colors.Lavender_Web.value,
                                               variable=baseROM, value=1)

    baseOptions_Speedchoice7p2 = tk.Radiobutton(mainWindow,
                                               text="SC 7.2",
                                               font=("Comic Sans MS", 12, ""),
                                               bg=UI_Colors.Lavender_Web.value,
                                               activebackground=UI_Colors.Lavender_Web.value,
                                               variable=baseROM,
                                               value=2)

    baseOptions_Speedchoice7p3 = tk.Radiobutton(mainWindow,
                                             text="SC 7.31",
                                             font=("Comic Sans MS", 12, ""),
                                             bg=UI_Colors.Lavender_Web.value,
                                             activebackground=UI_Colors.Lavender_Web.value,
                                             variable=baseROM,
                                             value=3)


    tk.Label(mainWindow,
             text="Pokémon Crystal Warp Randomizer",
             font=("Comic Sans MS", 20, "bold"),
             bg=UI_Colors.Lavender_Web.value,
             fg="black").place(x=170, y=0)

    tk.Label(mainWindow,
             text="Pokémon Crystal",
             font=("Comic Sans MS", 22, "italic bold"),
             bg=UI_Colors.Lavender_Web.value,
             fg=UI_Colors.Blue_Sapphire.value).place(x=150, y=0)

    tk.Label(mainWindow,
             text="by iFatRain",
             font=("Comic Sans MS", 10, ""),
             bg=UI_Colors.Lavender_Web.value,
             fg="black").place(x=550, y=40)

    tk.Label(mainWindow,
             text="Special Thanks to 3nt0n & Adysons",
             font=("Comic Sans MS", 8, ""),
             bg=UI_Colors.Lavender_Web.value,
             fg="black").place(x=580, y=420)

    #
    #   Seed button and text/input
    #

    tk.Label(mainWindow,
             text="(Seed number is optional)",
             font=("Comic Sans MS",10, ""),
             bg=UI_Colors.Lavender_Web.value).place(x=570, y=150)

    tk.Label(mainWindow,
             text="Seed:",
             font=("Comic Sans MS", 15, ""),
             bg=UI_Colors.Lavender_Web.value).place(x=460, y=175)

    tk.Entry(mainWindow,
             textvariable=seedString,
             font=("Comic Sans MS", 15, ""),
             bg="white").place(x=530, y=175)

    #
    #   Randomize Button
    #

    tk.Button(mainWindow,
              text="Randomize",
              font=("Comic Sans MS", 16, "bold"),
              bg=UI_Colors.Han_Blue.value,
              fg=UI_Colors.Minion_Yellow.value,
              command= lambda: randomize(loadedROMPath.get())).place(x=650, y=70)

    #
    #   LOAD ROM BUTTON AND TEXT
    #
    tk.Button(mainWindow,
              text="Load ROM",
              font=("Comic Sans MS", 13, "bold"),
              bg=UI_Colors.Han_Blue.value,
              fg=UI_Colors.Minion_Yellow.value,
              command=lambda:[loadAndDetermineROM(), displayBaseOptions(baseOptions_Vanilla,baseOptions_Speedchoice7p2,
                  baseOptions_Speedchoice7p3,baseOptions_Label)]).place(x=40, y=70)

    tk.Label(mainWindow,
             textvariable=loadedROMName,
             font=("Comic Sans MS", 13, "bold"),
             bg=UI_Colors.Lavender_Web.value,
             fg="black").place(x=160, y=75)

    legendarySetting = tk.Checkbutton(mainWindow,
                   variable=legendaryAvailability,
                   text=" Lugia/Ho-Oh Always Catchable",
                   bg=UI_Colors.Lavender_Web.value,
                   font=("Comic Sans MS", 12, ""),
                   activebackground=UI_Colors.Lavender_Web.value)
    legendarySetting.place(x=30, y= 140)
    Hovertip(legendarySetting,"Enables Both Legendary Birds without the Key-Item \nAlso Moves Lugia to Shorline",500)

    splitSetting = tk.Checkbutton(mainWindow,
                   variable=regionSplit,
                   text=" Combined Regions",
                   bg=UI_Colors.Lavender_Web.value,
                   font=("Comic Sans MS", 12, ""),
                   activebackground=UI_Colors.Lavender_Web.value)
    splitSetting.place(x=30, y=170)
    Hovertip(splitSetting,"Enables Warps between both Regions\n  ->If unchecked all warps will be to same region",500)

    litCavesSetting = tk.Checkbutton(mainWindow,
                   variable=litDarkCaves,
                   text=" Lit Dark Caves",
                   bg=UI_Colors.Lavender_Web.value,
                   font=("Comic Sans MS", 12, ""),
                   activebackground=UI_Colors.Lavender_Web.value)
    litCavesSetting.place(x=30, y=200)
    Hovertip(litCavesSetting,"Removes the need to use Flash to see in Dark Caves",500)

    mapChangeSetting = tk.Checkbutton(mainWindow,
                   variable=mapChanges,
                   text=" Softlock Prevention Map Changes",
                   bg=UI_Colors.Lavender_Web.value,
                   font=("Comic Sans MS", 12, ""),
                   activebackground=UI_Colors.Lavender_Web.value)
    mapChangeSetting.place(x=30, y=230)
    Hovertip(mapChangeSetting,"Modifies to map to help prevent softlocks:\nBlackthorn behind Gym is majorly overhauled.\n" +
             "Also removes a ledge in Mt.Mortar and a pylon near Snorlax.",500)

    pokeballSetting = tk.Checkbutton(mainWindow,
                   variable=aidePokeball,
                   text=" Aide Gives Pokeballs at Start",
                   bg=UI_Colors.Lavender_Web.value,
                   font=("Comic Sans MS", 12, ""),
                   activebackground=UI_Colors.Lavender_Web.value)
    pokeballSetting.place(x=30, y=260)
    Hovertip(pokeballSetting,"After getting your Pokemon the aide will give\n5 Pokeballs instead of a potion",500)

    puzzleSetting = tk.Checkbutton(mainWindow,
                   variable=ruinPuzzles,
                   text=" Presolved Ruins Puzzles",
                   bg=UI_Colors.Lavender_Web.value,
                   font=("Comic Sans MS", 12, ""),
                   activebackground=UI_Colors.Lavender_Web.value)
    puzzleSetting.place(x=30, y=290)
    Hovertip(puzzleSetting,"Removes the need to solve the Alph Ruin Puzzles\nDropdowns will become opened",500)

    rivalFightSetting = tk.Checkbutton(mainWindow,
                                  variable=rivalFightSkip,
                                  text=" Remove Mt.Moon Rival Fight",
                                  bg=UI_Colors.Lavender_Web.value,
                                  font=("Comic Sans MS", 12, ""),
                                  activebackground=UI_Colors.Lavender_Web.value)
    rivalFightSetting.place(x=30, y=320)
    Hovertip(rivalFightSetting, "Removes the rival fight from Mt.Moon", 500)

    goldenrodTakeoverSetting = tk.Checkbutton(mainWindow,
                                  variable=easyTakeover,
                                  text=" Goldenrod Takeover Rockets Wander",
                                  bg=UI_Colors.Lavender_Web.value,
                                  font=("Comic Sans MS", 12, ""),
                                  activebackground=UI_Colors.Lavender_Web.value)
    goldenrodTakeoverSetting.place(x=30, y=350)
    Hovertip(goldenrodTakeoverSetting, "Rocket Grunts no longer block entrances during Goldenrod Takeover\nInstead they are placed throughout and will roam the city", 500)

    levelSetting = tk.Checkbutton(mainWindow,
                                  variable=starterLevel,
                                  text=" Lvl 98 Starters for Testing",
                                  bg=UI_Colors.Lavender_Web.value,
                                  font=("Comic Sans MS", 12, ""),
                                  activebackground=UI_Colors.Lavender_Web.value)
    levelSetting.place(x=30, y=380)
    Hovertip(levelSetting, "Makes the 3 starters lv98\nThis setting is intended for TESTING ONLY", 500)

    mainWindow.mainloop()

def displaySeedInfoWindow(seed):

    seedInfoWindow = tk.Tk()
    seedInfoWindow.geometry("500x150")
    seedInfoWindow.title("Pokemon Crystal Warp Randomizer v1.2.0 by iFatRain")
    seedInfoWindow.configure(bg=UI_Colors.Lavender_Web.value)
    seedInfoWindow.protocol("WM_DELETE_WINDOW", lambda: [mainWindow.destroy(), seedInfoWindow.destroy(), quit()])

    tk.Label(seedInfoWindow,
             text="Pokemon Crystal Warp Randomizer",
             font=("Comic Sans MS", 20, "bold"),
             bg=UI_Colors.Lavender_Web.value).place(x=20, y=0)

    tk.Label(seedInfoWindow,
             text="by iFatRain",
             font=("Comic Sans MS", 10, ""),
             bg=UI_Colors.Lavender_Web.value).place(x=400, y=40)

    tk.Label(seedInfoWindow,
             text="Seed:",
             font=("", 15, ""),
             bg=UI_Colors.Lavender_Web.value).place(x=20, y=85)

    seedDisplay = tk.Text(seedInfoWindow,
                          font=("Comic Sans MS", 15, ""),
                          height=1,
                          width=23,
                          bd=0,
                          bg=UI_Colors.Lavender_Web.value)
    seedDisplay.place(x=90,y=85)
    seedDisplay.insert(tk.END,seed)
    seedDisplay.configure(state="disabled")

    tk.Button(seedInfoWindow,
              text="Close",
              bg="grey",
              font=("Comic Sans MS", 16, "bold"),
              command=lambda:[seedInfoWindow.destroy(),mainWindow.destroy()]).place(x=400, y=70)

    seedInfoWindow.mainloop()

def displayBaseOptions(vanilla, speedchoice7p2,speedchoice7p3,label):
    if not supportedROM.get():
        label.place(x=160, y=110)
        vanilla.place(x=300,y=110)
        speedchoice7p2.place(x=380,y=110)
        speedchoice7p3.place(x=460, y=110)

    else:
        label.place_forget()
        vanilla.place_forget()
        speedchoice7p2.place_forget()
        speedchoice7p3.place_forget()

def determineROM(rom_md5):
    # vanillaROM_MD5 = "301899b8087289a6436b0a241fbbb474"
    # 7.2 confirmed = "79369a19272472ae254b5b6abc32e9cd"
    print(rom_md5)
    match rom_md5:
        case "301899b8087289a6436b0a241fbbb474":
            loadedROMName.set("Pokemon - Crystal Version 1.1")
            supportedROM.set(True)
        case "79369a19272472ae254b5b6abc32e9cd":
            loadedROMName.set("Pokemon - Crystal Speedchoice Version 7.2")
            supportedROM.set(True)
        case "acb7fc79e249271129082f73bb4bd2ba":
            loadedROMName.set("Pokemon - Crystal Speedchoice Version 7.31")
            supportedROM.set(True)
        # case "958e6f4e49b6fc693099377dcff6b12f":
        #     loadedROMName.set("Pokemon - Crystal Speedchoice Version BETA")
        #     supportedROM.set(True)
        case _:
            loadedROMName.set("Unsupported ROM!")
            supportedROM.set(False)
    return rom_md5

def loadAndDetermineROM():

    originalROM = filedialog.askopenfilename()
    loadedROMPath.set(originalROM)
    determineROM(str(hashlib.md5(open(originalROM, 'rb').read()).hexdigest()))

def sortingFunc(input):
    return str(input).split(".")[1]

def assignSeed():
    if seedString.get() == "":
        seedString.set(str(random.randint(-sys.maxsize, sys.maxsize)))
    random.seed(seedString.get())

def randomize(originalROM):
    #Checks if an supported ROM was loaded, if not checks for Base Option Selection
    if not supportedROM.get():
        if baseROM.get() == 0:
            return
        elif baseROM.get() == 1:
            loadedROMName.set("Pokemon - Crystal Version 1.1")
        elif baseROM.get() == 2:
            loadedROMName.set("Pokemon - Crystal Speedchoice Version 7.2")
        elif baseROM.get() == 3:
            loadedROMName.set("Pokemon - Crystal Speedchoice Version 7.31")

    assignSeed()

    # Creates a setting Array that we can pass into the other functions to do different things based on settings
    settings = [loadedROMName.get(), legendaryAvailability.get(), regionSplit.get(), litDarkCaves.get(), mapChanges.get(),
                aidePokeball.get(), ruinPuzzles.get(), rivalFightSkip.get(), easyTakeover.get(), starterLevel.get()]

    # Remove the main window while we try the rando
    mainWindow.withdraw()

    # Create the output file for new rom.
    # Starts of as a duplicate of the original then we randomize it.
    newROM = ""
    while newROM == "" or newROM == originalROM:
       newROM = filedialog.asksaveasfilename(defaultextension=".gbc")
    shutil.copy(originalROM, newROM)

    # Try to randomize, catch failures to avoid a hung process
    try:
        with open(file=newROM, mode='r+b') as ROM:
            randomizedNodeList = randomizeROM.randomizeROM(ROM, settings)
    except:
        # TODO Add a Fatal Error Screen
        print("Randomizer failed")
        traceback.print_exc()
        displaySeedInfoWindow("Randomizer Failed!!")
        # Below shouldn't ever really be triggered because windows are closed before this
        # ...but adding for extra safety ;)
        try:
            mainWindow.destroy()
            quit()
        except:
            quit()
    print("\nSettings were:", settings[::])
    print("Seed was:", seedString.get())

    # Randomizer Success - create output log in same place as the output rom, and display the seed window
    createOutputLog(randomizedNodeList, settings, os.path.join(os.path.dirname(os.path.abspath(newROM)),newROM.removesuffix(".gbc") + "_spoiler_log.txt"))
    displaySeedInfoWindow(seedString.get())

def createOutputLog(nodeList, settings, outputPath):
    allLinks = []
    for node in nodeList:
        for link in node.value.LINKS:
            allLinks.append(link)

    allLinks.sort(key=sortingFunc)
    with open(outputPath, "w") as spoilerLog:
        spoilerLog.write("Randomizer version: v1.2.0\n")
        spoilerLog.write("Seed: " +  seedString.get() + "\n\n")
        spoilerLog.write("Version and settings chosen: ")
        for value in settings:
            spoilerLog.write('['+str(value)+']')
        spoilerLog.write("\n\n")
        currentMap = str(link.value.OWN).split(".")[1].split("_TO_")[0]
        for link in allLinks:
            if link.value.OUTPUT_TO_LOG == False:
                # print(str(link.value.OWN).split(".")[1].split("_TO_")[0])
                if str(link.value.OWN).split(".")[1].split("_TO_")[0] != currentMap:
                    currentMap = str(link.value.OWN).split(".")[1].split("_TO_")[0]
                    spoilerLog.write("\n\n\nWarps for " + str(currentMap + "\n"))
                spoilerLog.write("\n\t\t" + str(link.value.OWN).split(".")[1].ljust(75, ".") + str(link.value.LINK).split(".")[1])
                link.value.OUTPUT_TO_LOG = True
        spoilerLog.close()

def main():
    displayMainWindow()


class UI_Colors(Enum):

    Blue_Sapphire = "#115D79"
    French_Violet = "#8300C0"
    Old_Gold = "#CBB400"
    Lavender_Web = "#EDEDFF"
    Quicksilver = "#99A2A1"
    Minion_Yellow = "#FADE3E"
    Han_Blue = "#4F6BC9"


# Sets up Global UI variables
mainWindow = tk.Tk()
seedString = tk.StringVar()

# Randomizer Settings
legendaryAvailability = tk.IntVar()
regionSplit = tk.IntVar()
litDarkCaves = tk.IntVar()
mapChanges = tk.IntVar()
aidePokeball = tk.IntVar()
ruinPuzzles = tk.IntVar()
rivalFightSkip = tk.IntVar()
easyTakeover = tk.IntVar()

starterLevel = tk.IntVar()

# ROM Variables
baseROM = tk.IntVar()
loadedROMName = tk.StringVar()
loadedROMName.set("No ROM Loaded!")
loadedROMPath = tk.StringVar()
supportedROM = tk.BooleanVar()
supportedROM.set(False)


