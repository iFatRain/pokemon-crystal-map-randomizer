# Pokémon Crystal 



This is a map randomizer for Pokemon Crystal.

Currently supported ROMs:
- Pokemon Crystal (Vanilla)
- Pokemon Crystal Speedchoice ver 7.2
- Pokemon Crystal Speedchoice ver 7.31

NOTE ON UNSUPPORTED VERSIONS:
The warp randomization *should* work with any base version that has not already had it's warp's modified. HOWEVER script support can only be assured for these 3 versions. UPR randomization of these 3 versions *should* still work 100% but will show as "Unsupported" within the application. When this happens just select the base version used prior to UPR randomization when the options appear. UPR versioning *should* work exactly the same as the base versions but since it is technically a modified ROM I can't promise that.

<a download="iFat's Crystal Randomizer.zip" href="https://github.com/iFatRain/pokemon-crystal-map-randomizer/blob/main/iFat's%20Crystal%20Randomizer.zip">
    Download the randomizer here
</a>

Using the randomizer is as simple as running the program, and selecting your source ROM within the program. The program should be in the same directory as the syms folder. ie Randomizers/syms and Randomizers/program.exe

To use with UPR or KIR:
Apply UPR to Vanilla, Speedchoice 7.2/7.31 and then select that ROM as the input rom for the map randomizer. When loaded it will display "Unsupported ROM" and give you a list of options. Select which Base ROM you used to create the UPR randomization.

To use KIR: Use the appropriate version of KIR AFTER you have already randomized the warps. KIR support for map rando is still untested and experimental.

---
<a href="https://sekii.gitlab.io/pokemon-tracker/">
    Thanks Sekii for the tracker here!
</a>

## More details on the map randomizer

### Settings explained

- Lugia/Ho-Oh Always Catchable - No Silver/Rainbow Wing is needed for them to appear and no HM Surf is needed to interact with Lugia

- Combined Regions - Randomizes both Johto and Kanto warps (if turned off, Kanto warps are only accessable after either getting 8 badges and using the victory gate or beating Lance and using the ship)

- Lit Dark Caves - Dark places are lit up  (makes HM Flash unnecessary)

- Softlock Prevention Map Changes - Makes 2 small map changes (Mt Mortar, Vermilion) and a major change to Blackthorn to help prevent potential softlocks, detailed below.

- Aide Gives Pokeballs at Start - Get 5 pokeballs at the start instead of the potion (turn off if you also use a full Item Randomizer) 

- Presolved Ruins Puzzles - Ruins of Alphs puzzles don't need to be solved to open the hole

- (Temporary Setting) Lv 98 Testing Starters - Make the starting Pokemon lvl 98 to aid in testing seeds while in development.


### Changes Made to the game

**Map changes:**

* Ruins of Alph bottom - ledges removed
* Mt mortar - ledge removed (softlock prevention)
* Vermilion - barrier next to Snorlax removed to prevent being trapped (softlock prevention)
* Blackthorn City - Walkable path to Dragons Den entrance to prevent getting stuck after walking off old man (softlock prevention)

**Script changes:**

* Ice path - rocks gone from the top, rocks already set at bottom
* Basement open without basement key!
* The director always gives you the key card when talking to him 
* Right guard in victory road gate removed


### Vanilla/Unused Warps

Some warps are kept vanilla or are not fully randomized. Most of them could have been randomized, but in most cases we decided that it makes more sense (and more fun) to keep them vanilla.

**Vanilla**:

- All of New Bark Town - Bugs happen if you leave the town and fight battles without picking up a pokemon.
- Goldenrod Day Care South Exit - We just like it more that way - makes it easier to visit your pets :)
- Goldenrod Radio Tower Interior - The rocket section would be much more complicated and might even be impossible in rare cases, so we decided to just keep those places vanilla.
- Goldenrod Basement Puzzle Room connection to Director Room - see above
- Mahogany Team Rocket HQ Interior - see above
- Victory Road Interior - There is an item that is unaccessible if we randomize it, so the cave itself is vanilla. 

- Important rooms on the SS Aqua to finish the ship quest - Guarantees that there is a way to travel between Johto and Kanto (mainly needed if 'Combined Regions' is not set)
- Players Room on SS Aqua - Makes travel using the ship possible

- Magnet Train connection - prevents forced one-ways; Pass is also very late game so for example the Goldenrod train would never be useful
- Olivine port and Vermilion port - makes it easier to travel between Johto and Kanto 
- All of Mt. Silver - There isn't much to randomize, also enables the usual 16 Badge enforcement for game completion


**Unused**:

- Tin Tower F1->F2 - this leads to the same warp as the entrance and is therefore useless. This warp would otherwise be too late game to be useful
- Alph ruins treasure rooms - Those warps link to the same warps as the holes when solving puzzles



### General Randomization Logic 

Goal is to be able to reach any place in the game without the use of HMs. Also softlocking shouldn't be possible. There are some one-ways, but they should never cause actual problems. If two warps are not traversable in both directions, meaning you'd need to hop a ledge or something and couldnt return to the source warp, then they are NOT considered to be together in the seed checking logic.

**Randomization steps:**

All maps are split into following:

- Major City Nodes: Major Cities that are all connected to each other
- Hub Nodes: Larger nodes like caves with 3 or more warps but aren't cities
- Corridors: places with only 2 warps (Think Gate houses)
- Dead-ends: places with 1 warp, assuming that the player has no HMs. (Think house interiors, or areas that can only be left via ledges or surf) 

1. The randomizer connects all Major Nodes to one connected graph to ensure that they can all be reached (eg. Pallet town - Viridian City - Pewter City - Mt Moon left entrance count as one major node).

2. Then Hub Nodes (eg. alph ruins, mt mortar interior) are put between the connection of the major places. These two steps gives us all of the possible overworld/hub warps to place dead-ends onto.

3. First important dead-ends (item or pokemon containing) and non-important dead-ends that are accessible via HMs are linked to the remaining unused warps (Meaning they're not imporant but you can reach them from other warps if you use HM's). If there are still unused warps, non-important dead-ends that aren't reachable are linked to those (Unimportant house interiors for example)

4. (In theory, if we still had open warps, we would just link them with each other. In practise, we always have enough dead-ends link them to, depending on the settings)

5. At the end we randomly put the corrdiors between the links to extend the routings.


**Locks and Unlocks:**

There are some places that are locked by story progression. A seed checker ensures that it is possible to obtain all badges and HM's and therefore reach all places (otherwise lavender radio could be behind snorlax for example). 

**Progression Notes**
A note on order of certain events: 
- You MUST talk to Kurt in his house before doing the Slowpoke Well or the rocket will remain blocking the well entrance.
- Fighting Rival in Goldenrod Underground before Burned Tower will make his sprite disappear from burned tower. You can still trigger the fight cutscene.
- Goldenrod Takeover triggers at 7 badges, so do your best to explore any node that may become locked by triggering 7 badges first. Radio Tower is enforced to not be in Goldenrod and the major city connections are enforced to not be blocked off in Goldenrod.
- In Goldenrod Radio Tower, even if you get keycard early, you must start the rocket takeover to properly clear/fight the Rocket Boss at radio tower.


### Known Bugs

Currently no known bugs :) Please post them or DM iFatRain#7210 on discord if you find them.


---
Map randomizer created by IFatRain.
 
Special Thanks to Adyson and 3nt0n! Thanks to Sekii for the tracker

Testers: Adyson, 3nt0n, Snowbear, Choatix, Pokemonfan1937, PulseEffects, iFatRain



*readme.md written by 3nton, revisions by iFatRain*

