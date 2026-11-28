# Metroid Fusion Tricks List

These tricks have been largely compiled by the [Randovania team](https://github.com/randovania/randovania/tree/main/randovania/games/fusion/logic_database), with edits and adjustments as necessary to facilitate 
Archipelago's systems. If you find that a difficulty level needs adjusting, we welcome any feedback.

It is planned to have a video demonstration for most, if not all, of the tricks listed in this document. If you would 
like to submit a video, it must meet the following:
- Publicly viewable on YouTube or similar video hosting site via a link
  - Videos only uploaded to Discord will not be accepted
- Primarily contains only in-game footage and in-game audio
  - Stream-friendly layouts are acceptable
  - Audio must not distract from the trick being performed
- Optionally shows live input feedback, such as an input overlay, that does not affect viewing the trick being 
  performed

## Available Trick Types
### Combat
Your skill in navigating the game's combat scenarios. Higher difficulties expect less weaponry upgrades, navigation 
tools, and energy to be available, and may expect a higher level of precision with what tools are in your possession.
### Movement
A generic catch-all for any maneuver that isn't otherwise classified by other tricks. Higher difficulties
 require more precision.
### Knowledge
How much you know about game interactions that aren't intentionally shown or expected in a vanilla game playthrough.
 Higher difficulties expect knowing details in increasing obscurity.
### Damage Boost
The act of intentionally taking damage to use the invincibility period to avoid more detrimental sources of harm, or to
 induce desirable levels of knockback to reach an area. Higher difficulties require more precision or less
 available energy to perform.
### Damage Run
Traversing damaging environments without protection items, not normally including enemy interaction. Higher difficulties
 require less available energy, and may be accompanied by a Movement trick.
### Frozen Enemies
Freezing an enemy to use them as a stepping stone. Higher difficulties require more precise positioning of the frozen 
enemy.
### Midair Morph
As the name implies, the act of entering Morph Ball in midair to enter a tunnel that normally expects a Bomb Jump or
 the use of Jumpball via Hi-Jump. Higher difficulties require more precision.
### Shinespark Tricks
You can store a Speed Booster charge by crouching at speed to use later to launch yourself horizontally or upwards. 
This stored charge is referred to as a Shinespark. Higher difficulties expect more unorthodox uses and may require more 
precision.
### Wall Jump
You can kick off of walls back and forth to climb higher. Not possessing the item "Wall Jump Boots" may lock this 
feature. Higher difficulties expect more precise use.
### Underwater Wall Jump (UWJ)
The use of a Wall Jump underwater without Gravity Suit can be performed in quick succession against the same wall
repeatedly to climb higher. Higher difficulties expect climbing more vertical distance.
### Jump Bomb Jump (JBJ)
The act of placing a bomb at the peak of a jump to use in getting more vertical reach. Higher difficulties require more
 precision. The beginner difficulty is not available due to the skill floor required to perform this trick.
### Jump Extend
Rapidly switching between different midair states to slow falling speed. Higher difficulties require more
 precision.

## Available Trick Difficulties
### None
This trick will not be expected in logic.
### Vanilla
This will expect what is required of you to complete an unmodified copy of the game in the original developer's intended
methods.
### Beginner
This is the entry point for learning the use of a trick and how it works.
### Intermediate
You have practiced a trick enough to begin stretching your known boundaries of its use.
### Advanced
You have learned enough about a trick to begin learning the absolute limits about its applicable uses.
### Expert
You have innate knowledge of a trick and can use it in most situations that require it.
### Master
You are reaching the edge of what is physically possible for a trick and can potentially find a new use of the trick.
### Theoretical
This is reserved for tricks meeting the following criteria:
- Potentially able to be performed within the limits of game mechanics
- Does not have documented proof a human has performed the trick at normal game speed
- May have been only performed in a Tool-Assisted Speedrun setting

## Tricks List
This list is sorted in this order:
- Sector
- Room name (alphabetically)
- Connection destination (alphabetically)
- Associated tricks' difficulty levels (ascending) or event flags

It is recommended to use the Find feature ( [CTRL]+[F] ) with the Room name due to the size of this list.

Note that only tricks above Vanilla difficulty are listed to reduce clutter
### Any
- Removing a Geron of ANY type
  - YAML `NerfGeronWeaknesses: false`
    - Destroy with Screw Attack or Power Bomb
      - Knowledge - Beginner

### Main Deck
#### Arachnus Arena
- Destination: `Main Deck -- Crew Quarters East`
  - If location `Main Deck -- Arachnus Arena` is collected, the entry door is unlocked.
    - From the upper room section, exit is free.
    - From the lower room section, with Wall Jump and without Hi-Jump or Space Jump
      - Wall Jump - Beginner
    - From the lower room section, without any Jump upgrades
      - Movement - Expert
      - [Video Demonstration](https://youtu.be/ycp5oCd5-9I)
- Location: `Main Deck -- Arachnus Arena`
  - Hitless Fight
    - Combat - Beginner
#### Central Nexus
- Destination: `Main Deck -- Dark Stairwell`
  - Knowledge - Beginner
#### Central Reactor Core
- Destination: `Main Deck -- Central Reactor Core`
  - You're in the lower section by the Save Station and are climbing the room without Hi-Jump or Space Jump.
    - Wall Jump - Beginner
  - You're in the lower section by the Save Station and are climbing the room with Speed Booster.
    - Shinespark - Beginner
    - [Video Demonstration](https://youtu.be/x7CqxW4JyJ4)
- Destination: `Main Deck -- Silo Tunnel`
  - [Video Demonstration](https://youtu.be/vVG5YNwzGjw)
  - You're getting to the tunnel using Speed Booster and without Space Jump
    - With Hi-Jump
      - Shinespark - Advanced
    - Without Hi-Jump
      - Shinespark - Master
    - Location `Sector 2 (TRO) -- Nettori Arena` isn't collected
      - You're in the vine blocks around the tunnel entry
      - Movement - Intermediate OR Midair Morph - Advanced
    - For retry attempts without Wave Beam, you need to take the long loop through `Main Deck -- Silo Scaffolding`
      - Shinespark - Master
#### Concourse Ventilation
- Destination: `Main Deck -- Arachnus Arena`
  - You're entering Arachnus' Arena from the intended exit.
  - Wall Jump - Beginner
#### Dark Stairwell
- Destination: `Main Deck -- Central Nexus` or `Main Deck -- Dark Stairwell`
  - You're in the secret cubby that contains Screw Attack blocks
  - Midair Morph - Advanced
- Destination: `Main Deck -- Dark Stairwell`
  - You're in the main room getting to the secret cubby
  - Knowledge - Beginner
#### Habitation Deck Entrance
- Destination: `Main Deck -- Habitation Deck` through middle door
  - Via Frozen Fune without Hi-Jump
    - Frozen Enemies - Beginner
    - Wall Jump - Intermediate
    - [Video Demonstration](https://youtu.be/o-DdSO4E3-M)
  - Via Wall Jump into Jump Extend without Fune
    - Jump Extend - Advanced
    - Wall Jump - Advanced
    - [Video Demonstration](https://youtu.be/C56BsRG_eKY)
#### Nexus Storage
- Location: `Main Deck -- Nexus Storage`
  - Leaving back out the tunnel entrance
    - [Video demonstration](https://youtu.be/7T5fVhUYQ4g)
    - Movement - Beginner
    - Without Hi-Jump or Space Jump
      - Wall Jump - Beginner
#### Operations Ventilation
- Destination: `Main Deck -- Crew Quarters East`
  - Speed Booster starts in `Main Deck -- Station Entrance`
  - Wall Jump - Advanced
  - Movement - Advanced
  - Shinespark - Master
  - [Video Demonstration](https://youtu.be/dWJXG-nGo6A)
#### Quarantine Junction
- Destination: `Main Deck -- Main Elevator Access`
  - Speed Booster starts at `Main Deck -- Station Entrance`
  - Shinespark - Intermediate
  - [Video Demonstration](https://youtu.be/QcD2-t9UDrg)
#### Restricted Back Door
- Destination: `Sector 6 (NOC) -- Authorization Checkpoint`
  - Disable Screw Attack just after the wall jump to ledge grab on a Screw Attack block to reach the tunnel
    - Wall Jump - Beginner
#### Silo Catwalk
- Destination: `Main Deck -- Central Reactor Core` or `Main Deck -- Silo Scaffolding`
  - Pretend the Pirates don't exist
    - Damage Boost - Beginner
  - Pacifist and Hitless
    - Combat - Intermediate
#### Silo Entry
- Destination: `Main Deck -- Docking Bay Climb`
  - When using the Level 4 Security Door without Hi-Jump or Space Jump
  - Wall Jump - Beginner
#### Silo Scaffolding
- Destination: `Main Deck -- Yakuza Arena`
  - Pretend the Pirates don't exist
    - Damage Boost - Intermediate
  - Pacifist Pirates
    - Combat - Expert
- To item, then Destination: `Main Deck -- Silo Catwalk`
  - Pretend the Pirates don't exist
    - Damage Boost - Intermediate
  - Climb without Hi-Jump or Space Jump
    - Wall Jump - Advanced
  - Pacifist Pirates
    - Combat - Expert
#### Silo Tunnel
- Destination: `Sector 2 (TRO) -- Overgrown Entrance` or `Main Deck -- Central Reactor Core`
  - If location `Sector 2 (TRO) -- Nettori Arena` is collected, the tunnel is free to travel through without bombs.
#### Station Entrance
- Destination: `Main Deck -- Genesis Speedway`
  - Shinespark - Advanced
#### Sub-Zero Containment
- Location: `Main Deck -- Sub-Zero Containment`
  - Suitless
    - Damage Run - Intermediate
#### Yakuza Arena
- Destination: `Main Deck -- Auxiliary Power Station`
  - Skip the fight with Space Jump
    - Knowledge - Beginner
- Location: `Main Deck -- Yakuza Arena`
  - 4 E-Tanks, Ice Missiles, Charge Beam, Wide Beam, and Morph Ball
    - Combat - Beginner
  - 3 E-Tanks, Diffusion Missiles and Charge Beam
    - Combat - Intermediate
  - 2 E-Tanks, Base Missiles and Charge Beam
    - Combat - Advanced
  - 1 E-Tank, Base Missiles only
    - Combat - Expert
  - No E-Tanks, Base Missiles only
    - Combat - Master

### Sector 1
#### Atmospheric Stabilizer Northeast
- Destination: `Sector 1 (SRX) -- Twin Junctions West`
  - Start charging Speed Booster in Twin Junctions West. Destroy the Stabilizer Parasite with it.
    - [Video demonstration](https://youtu.be/I9YH_s989sQ)
    - Knowledge - Intermediate
    - Shinespark - Expert
#### Atmospheric Stabilizer Northwest
- Destination: `Sector 1 (SRX) -- Hornoad Hole`
  - Start charging Speed Booster in either Yameba Corridor or Entrance Lobby. Destroy the Stabilizer Parasite with it.
    - Knowledge - Intermediate
    - Shinespark - Advanced
- Destination: `Sector 1 (SRX) -- Yameba Corridor`
  - Tricks required are the same as: Yameba Corridor → Entrance Lobby
#### Atmospheric Stabilizer Southeast
- Destination: Any Exit Door
  - YAML `NerfGeronWeaknesses: false`, with Screw Attack and Wall Jump without Space Jump
    - Wall Jump - Beginner
    - Knowledge - Beginner
  - Using a Shinespark
    - Knowledge - Intermediate
    - With Hi-Jump
      - Shinespark - Advanced
    - With Wall Jump
      - Wall Jump - Advanced
      - Shinespark - Advanced
      - [Video demonstration](https://youtu.be/SrshBBv-MCw)
    - Without Hi-Jump or Wall Jump
      - Shinespark - Expert
      - [Video demonstration](https://youtu.be/WsY4pSmBAyo)
#### Atmospheric Stabilizer Southwest
- Destination: `Sector 1 (SRX) -- Sciser Puddle`
  - Start charging Speed Booster in either Atmospheric Stabilizer SE or Zebesian Zag. Destroy the Stabilizer Parasite 
    with it.
    - Knowledge - Intermediate
    - Shinespark - Advanced
#### Hornoad Hole
- Destination: `Sector 1 (SRX) -- Atmospheric Stabilizer Northwest`
  - Tricks required are the same as: Yameba Corridor → Entrance Lobby
#### Lava Lake
- Destination: `Sector 1 (SRX) -- Lava Lake Annex`
  - Single Suit, 1 E-Tank
    - Damage Run - Beginner
  - No Suits, 2 E-Tanks
    - Damage Run - Intermediate
    - [Part 1 Video, Getting to the door](https://youtu.be/VFbTQoMI0uA)
    - [Part 2 Video, Leaving the lava](https://youtu.be/pu2I2jaMrjI)
#### Lava Lake Annex
- Destination: `Sector 1 (SRX) -- Lava Lake`
  - Single Suit, 1 E-tank
    - Damage Run - Beginner
  - No Suits, 2 E-Tanks
    - Damage Run - Intermediate
    - [Part 1 Video, Getting to the door](https://youtu.be/jfuH3Epvxh8)
    - [Part 2 Video, Leaving the lava](https://youtu.be/RF2_8Y0PaVQ)
#### Tourian Trapdoor
- Destination: `Sector 1 (SRX) -- Moto Manor` or `Sector 1 (SRX) -- Atmospheric Stabilizer Southeast`
  - Climb from the bottom of the room
    - Hi-Jump and Wall Jump
      - [Video demonstration](https://youtu.be/Hfmrj3rurOY)
      - Wall Jump - Beginner
      - Frozen Enemies - Intermediate
    - Hi-Jump only
      - [Video demonstration](https://youtu.be/T_aded4xYeU)
      - Frozen Enemies - Advanced
    - Wall Jump only
      - [Video demonstration](https://youtu.be/rpQG_ZFJ2Wg)
      - Wall Jump - Intermediate
      - Frozen Enemies - Master
#### Yameba Corridor
- Destination: `Sector 1 (SRX) -- Atmospheric Stabilizer Northwest`
  - Ram the Geron with Speed Booster
    - Knowledge - Beginner
- Destination: `Sector 1 (SRX) -- Entrance Lobby`
  - YAML `NerfGeronWeaknesses: false`
    - Destroy Stabilizer Parasite with Screw Attack or Power Bomb
      - Knowledge - Beginner
  - Charge Shinespark in Moto Motorway. Maintain into Atmospheric Stabilizer NE and carry through Atmospheric Stabilizer
    NW. Demonstration uses significant amounts of pause buffering.
    - [Video demonstration](https://youtu.be/aq0PQxbFJQk)
    - Knowledge - Intermediate
    - Shinespark - Master
    - Wave Beam OR Wide Beam
      - Combat - Intermediate
    - Charge Beam OR Plasma Beam
      - Combat - Advanced
#### Zebesian Zag
- Destination: `Sector 1 (SRX) -- Twin Junctions East`
  - Screw Attack only, requiring cancelling a spin
    - Movement - Beginner
    - [Video demonstration](https://youtu.be/rsQZgb4xF6Y)
  - Pacifist Hitless
    - Combat - Intermediate
    - [Video demonstration](https://youtu.be/Lh9D7Ye3rw8)
  - Skip the room with a Shinespark
    - Shinespark - Beginner
    - [Video demonstration](https://youtu.be/_PmmHN9YvKw)
  - Damage Boost through them with at least 1 E-Tank
    - Movement - Beginner 
    - Damage Boost - Intermediate
    - [Video demonstration](https://youtu.be/cqHI8tNmNVw)
#### Zebesian Zig
- Destination: `Sector 1 (SRX) -- Sciser Puddle`
  - Pacifist Descent
    - [Video Demonstration](https://youtu.be/u40B3GpSIsA)
    - Combat - Intermediate

### Sector 2

### Sector 3

### Sector 4

### Sector 5

### Sector 6