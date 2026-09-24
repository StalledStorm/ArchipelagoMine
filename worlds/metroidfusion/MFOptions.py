from dataclasses import dataclass

from Options import Toggle, Range, Choice, PerGameCommonOptions, DefaultOnToggle, StartInventoryPool, OptionGroup, \
    ItemSet, DeathLink, Removed


# Main Options

class GameMode(Choice):
    """Determines starting location and accessibility.
    Vanilla starts you in the Docking Bay with no items.
    Open Sector Hub starts you in the Sector Hub with one E-Tank and one random item. All sector elevators will be open.
    Custom will apply the settings in the Custom Game Mode section."""
    display_name = "Game Mode"
    option_vanilla = 0
    option_open_sector_hub = 1
    option_custom = 2
    default = 0

class InfantMetroidsInPool(Range):
    """How many Infant Metroids will be in the item pool."""
    display_name = "Infant Metroids in Pool"
    range_start = 1
    range_end = 20
    default = 5

class InfantMetroidsRequired(Range):
    """How many Infant Metroids will be required to beat the game.
    If set to more than the number in the pool, will instead become however many are present."""
    display_name = "Infant Metroids Required"
    range_start = 1
    range_end = 20
    default = 5

class InfantMetroidLocations(Choice):
    """Where Infant Metroids can be located.
    Anywhere allows them to be anywhere in the multiworld.
    Bosses Encouraged increases the chances of them being located on local boss locations.
    Only Bosses means Infant Metroids can only be on your boss locations. Will limit the number of Infant Metroids
    in the pool. if greater than the number of bosses."""
    display_name = "Infant Metroid Locations"
    option_anywhere = 0
    option_bosses_encouraged = 1
    option_only_bosses = 2
    default = 0

# Logic Options

class EarlyProgression(Choice):
    """Determines if an early progression item guaranteed in one of your first locations.
    Normal restricts the starting item pool to Morph Ball and Missiles.
    Advanced expands the pool to Screw Attack.
    If Shinespark Tricks are set to Advanced, adds Speed Booster as well
    Option is in testing and may increase generation failures."""
    display_name = "Early Progression"
    option_none = 0
    option_normal = 1
    option_advanced = 2
    default = 1

class PointOfNoReturnsInLogic(DefaultOnToggle):
    """Should Point of No Return locations be in logic.
    If disabled, you will never be required to enter an area without the items to exit out."""
    display_name = "Point of No Returns in Logic"

class SectorTubeShuffle(Toggle):
    """If enabled, shuffles the tube connections between sectors.
    Does not affect the non-glass tube connections."""
    display_name = "Sector Tube Shuffle"

class ElevatorShuffle(Choice):
    """If enabled, shuffles the various elevator connections.
     Sectors will shuffle the six sector elevators in the Sector Hub.
     All will include all elevator connections in the game.
     Note that if enabled, logical energy tank requirements will be relaxed."""
    display_name = "Elevator Shuffle"
    option_none = 0
    option_sectors = 1
    option_all = 2
    default = 0

# Trick Options

class CombatDifficulty(Choice):
    """What level of combat tools are logically expected to defeat bosses and enemies while navigating.
    A higher difficulty will expect less combat tools to be available and to include fewer Energy Tanks than normal."""
    display_name = "Combat Difficulty"
    option_vanilla = 0
    option_beginner = 1
    option_intermediate = 2
    option_advanced = 3
    option_expert = 4
    option_master = 5
    default = 0

class KnowledgeDifficulty(Choice):
    """Knowledge of interactions that aren't explained by a vanilla playthrough.
    A higher difficulty will expect knowing details in increasing obscurity."""
    display_name = "Knowledge Difficulty"
    option_vanilla = 0
    option_beginner = 1
    option_intermediate = 2
    option_advanced = 3
    option_expert = 4
    default = 0

class DamageBoostTrickDifficulty(Choice):
    """A damage boost is the act of intentionally taking damage to prevent taking a larger amount of damage, or to
    induce desirable knockback to use in travel.
    A higher difficulty represents a greater risk of taking more damage than necessary to achieve results."""
    display_name = "Damage Boost Trick Difficulty"
    option_none = 0
    option_beginner = 1
    option_intermediate = 2
    option_advanced = 3
    option_expert = 4
    option_master = 5
    default = 0

class DamageRunTrickDifficulty(Choice):
    """Traversing damaging environments without the Varia Suit, excluding damage from enemies.
    A higher difficulty will expect less extra Energy Tanks to perform."""
    display_name = "Damage Run Trick Difficulty"
    option_none = 0
    option_beginner = 1
    option_intermediate = 2
    option_advanced = 3
    option_expert = 4
    option_master = 5
    default = 0

class FrozenEnemiesTrickDifficulty(Choice):
    """Freezing an enemy to use as a platform in getting elsewhere.
    A higher difficulty will expect more precise positioning or a risk to self."""
    display_name = "Frozen Enemies Trick Difficulty"
    option_vanilla = 0
    option_beginner = 1
    option_intermediate = 2
    option_advanced = 3
    option_expert = 4
    option_master = 5
    default = 0

class JumpBombJumpTrickDifficulty(Choice):
    """The act of placing a bomb at the peak of a jump to use in getting more vertical reach.
    A higher difficulty will require more precision.
    The beginner level is unavailable due to the difficulty of this trick."""
    display_name = "Jump Bomb Jump Trick Difficulty"
    option_none = 0
    # option_beginner = 1
    option_intermediate = 2
    option_advanced = 3
    option_expert = 4
    option_master = 5
    default = 0

class JumpExtendTrickDifficulty(Choice):
    """Abusing midair state transitions to slow your falling speed.
    A higher difficulty will require more precision."""
    display_name = "Jump Extend Trick Difficulty"
    option_none = 0
    option_beginner = 1
    option_intermediate = 2
    option_advanced = 3
    option_expert = 4
    option_master = 5
    default = 0

class MidairMorphTrickDifficulty(Choice):
    """The act of entering Morph Ball in midair to enter a tunnel.
    A higher difficulty will require more precision."""
    display_name = "Midair Morph Trick Difficulty"
    option_none = 0
    option_beginner = 1
    option_intermediate = 2
    option_advanced = 3
    option_expert = 4
    default = 0

class ShinesparkTrickDifficulty(Choice):
    """Using the stored charges from Speed Booster to traverse the station in unorthodox ways.
    Note that this does not exclude locations that require shinesparking in vanilla to collect.
    Use the ShinesparkLocations location group for that."""
    display_name = "Shinespark Trick Difficulty"
    option_vanilla = 0
    option_beginner = 1
    option_intermediate = 2
    option_advanced = 3
    option_expert = 4
    option_master = 5
    default = 0

class UnderwaterWallJumpTrickDifficulty(Choice):
    """Wall jumping underwater without Gravity Suit can be used to climb higher.
    A higher difficulty will require climbing a greater height."""
    display_name = "Underwater Wall Jump Trick Difficulty"
    option_vanilla = 0
    option_beginner = 1
    option_intermediate = 2
    option_advanced = 3
    option_expert = 4
    option_master = 5
    default = 0

class WallJumpTrickDifficulty(Choice):
    """Your ability to kick off walls to climb higher in areas that won't expect you to do so.
    A higher difficulty will expect a wider range of ingenuity or higher risk."""
    display_name = "Wall Jump Trick Difficulty"
    option_vanilla = 0
    option_beginner = 1
    option_intermediate = 2
    option_advanced = 3
    option_expert = 4
    option_master = 5
    default = 0

# Custom Game Mode options

class StartingLocation(Choice):
    """Your starting location.
    This is a Custom Game Mode option and will only be applied if GameMode is set to Custom."""
    display_name = "Starting Location"
    option_docking_bay = 0
    option_operations_deck = 1
    option_sector_hub = 2
    option_concourse_save_station = 3
    default = 0

class StartingMajorUpgrades(Range):
    """How many major upgrades you begin with.
    Note that depending on your StartingLocation and EarlyProgression settings, you may receive more than specified here
    in order to successfully generate the game. Upgrades are taken from the general item pool and will be replaced
    by a random filler item.
    These will be applied in addition to your start_inventory and start_inventory_from_pool items.
    These will be sent by the client once you're connected.
    This is a Custom Game Mode option and will only be applied if GameMode is set to Custom."""
    display_name = "Starting Major Upgrades"
    range_start = 0
    range_end = 22
    default = 0

class StartingEnergyTanks(Range):
    """How many Energy Tanks you begin with.
    This will be overridden by the number specified in start_inventory and start_inventory_from_pool, if applicable.
    Energy tanks are taken from the general item pool and will be replaced by a random filler item.
    These will be sent by the client once you're connected.
    This is a Custom Game Mode option and will only be applied if GameMode is set to Custom."""
    display_name = "Starting Energy Tanks"
    range_start = 0
    range_end = 20
    default = 0

class FillerItems(ItemSet):
    """Which Items are used as filler when Items are removed from the pool
    Whenever an item is removed from the pool by start_inventory_from_pool, StartingMajorUpgrades, StartingEnergyTanks,
    or for other reasons, it will be replaced with a random item from this list.
    This is a Custom Game Mode option and will only be applied if GameMode is set to Custom."""
    display_name = "Filler Items"
    default = ["Missile Tank", "Power Bomb Tank"]

class OpenSectorElevators(Toggle):
    """Determines if the sector elevators in the Sector Hub are locked by their vanilla keycard requirements.
    This is a Custom Game Mode option and will only be applied if GameMode is set to Custom."""
    display_name = "Open Sector Elevators"

class SectorNavigationRoomHintLocks(Toggle):
    """Determines if the Navigation Rooms at the start of each sector have their hints locked by keycard requirements.
    If set, the keycard required for the hint will be one level higher than the level needed to access the sector
    in vanilla. Has no effect if EnableHints is disabled.
    This is a Custom Game Mode option and will only be applied if GameMode is set to Custom."""
    display_name = "Sector Navigation Room Hint Locks"

# Minor Options

class PaletteRandomization(Toggle):
    """Randomize the ingame palettes."""
    display_name = "Palette Randomization"

class AlternateHealthHudLayout(Toggle):
    """Enables an alternative HUD for health."""
    display_name = "Alternate Health HUD Layout"

class EnableHints(DefaultOnToggle):
    """Enable ingame hints at Navigation Stations."""
    display_name = "Enable Hints"

class RevealHiddenBlocks(DefaultOnToggle):
    """Enables whether destructible blocks are revealed from the start."""
    display_name = "Reveal Hidden Blocks"

class FastDoorTransitions(DefaultOnToggle):
    """Enables fast door transitions between rooms."""
    display_name = "Fast Door Transitions"

class InstantMorph(DefaultOnToggle):
    """Enables instant morphing, using the 'SELECT' button."""
    display_name = "Instant Morph"

class SecondaryWeaponToggle(Toggle):
    """Sets the missile launcher to be toggled on and off, instead of needing to be held."""
    display_name = "Secondary Weapon Toggle"

class NerfGeronWeaknesses(Toggle):
    """Makes Gerons only weak to their 'intended' values."""
    display_name = "Nerf Geron Weaknesses"

class MusicRando(Choice):
    """Changes how music is shuffled.
    Vanilla: Does not shuffle any songs.
    Type: Shuffles songs within the same category. This ensures that you won't hear boss music while exploring,
    or an item jingle as the escape sequence. Jingles are not shuffled. Certain songs, such as the Credits song,
    are excluded from shuffling.
    Full: Will shuffle all songs with each other. Jingles are not shuffled. Certain songs, such as the
    Credits song, are excluded from shuffling."""
    display_name = "Music Rando"
    option_vanilla = 0
    option_type = 1
    option_full = 2
    default = 0

class MajorJingles(Toggle):
    """Replace all major item jingles with the minor jingle instead. Select 'true' to disable major item jingles."""
    display_name = "Major Jingles"

class MissileDataAmmo(Range):
    """The amount of missiles provided by a Missile Data item."""
    display_name = "Missile Data Ammo"
    range_start = 5
    range_end = 100
    default = 10

class PowerBombDataAmmo(Range):
    """The amount of power bombs provided by a Power Bomb Data item."""
    display_name = "Power Bomb Data Ammo"
    range_start = 5
    range_end = 100
    default = 10

class MissileTankAmmo(Range):
    """The amount of missiles provided by a Missile Tank item."""
    display_name = "Missile Tank Ammo"
    range_start = 0
    range_end = 100
    default = 5

class PowerBombTankAmmo(Range):
    """The amount of power bombs provided by a Power Bomb Tank item."""
    display_name = "Power Bomb Tank Ammo"
    range_start = 0
    range_end = 100
    default = 2

@dataclass
class MetroidFusionOptions(PerGameCommonOptions):
    GameMode: GameMode
    InfantMetroidsInPool: InfantMetroidsInPool
    InfantMetroidsRequired: InfantMetroidsRequired
    InfantMetroidLocations: InfantMetroidLocations

    EarlyProgression: EarlyProgression
    SectorTubeShuffle: SectorTubeShuffle
    ElevatorShuffle: ElevatorShuffle
    PointOfNoReturnsInLogic: PointOfNoReturnsInLogic

    ShinesparkTrickDifficulty: ShinesparkTrickDifficulty
    WallJumpTrickDifficulty: WallJumpTrickDifficulty
    CombatDifficulty: CombatDifficulty
    KnowledgeDifficulty: KnowledgeDifficulty
    DamageBoostTrickDifficulty: DamageBoostTrickDifficulty
    DamageRunTrickDifficulty: DamageRunTrickDifficulty
    FrozenEnemiesTrickDifficulty: FrozenEnemiesTrickDifficulty
    JumpBombJumpTrickDifficulty: JumpBombJumpTrickDifficulty
    JumpExtendTrickDifficulty: JumpExtendTrickDifficulty
    MidairMorphTrickDifficulty: MidairMorphTrickDifficulty
    UnderwaterWallJumpTrickDifficulty: UnderwaterWallJumpTrickDifficulty

    StartingLocation: StartingLocation
    StartingMajorUpgrades: StartingMajorUpgrades
    StartingEnergyTanks: StartingEnergyTanks
    FillerItems: FillerItems
    OpenSectorElevators: OpenSectorElevators
    SectorNavigationRoomHintLocks: SectorNavigationRoomHintLocks

    PaletteRandomization: PaletteRandomization
    AlternateHealthHudLayout: AlternateHealthHudLayout
    EnableHints: EnableHints
    InstantMorph: InstantMorph
    SecondaryWeaponToggle: SecondaryWeaponToggle
    NerfGeronWeaknesses: NerfGeronWeaknesses
    MusicRando: MusicRando
    MajorJingles: MajorJingles
    RevealHiddenBlocks: RevealHiddenBlocks
    FastDoorTransitions: FastDoorTransitions
    MissileDataAmmo: MissileDataAmmo
    MissileTankAmmo: MissileTankAmmo
    PowerBombDataAmmo: PowerBombDataAmmo
    PowerBombTankAmmo: PowerBombTankAmmo

    start_inventory_from_pool: StartInventoryPool
    death_link: DeathLink

metroid_fusion_option_groups = [
    OptionGroup("Main Options", [
        GameMode,
        InfantMetroidsInPool,
        InfantMetroidsRequired,
        InfantMetroidLocations
    ]),
    OptionGroup("Logic Options", [
        EarlyProgression,
        SectorTubeShuffle,
        ElevatorShuffle,
        PointOfNoReturnsInLogic
    ]),
    OptionGroup("Trick Options", [
        ShinesparkTrickDifficulty,
        WallJumpTrickDifficulty,
        CombatDifficulty,
        KnowledgeDifficulty,
        DamageBoostTrickDifficulty,
        DamageRunTrickDifficulty,
        FrozenEnemiesTrickDifficulty,
        JumpExtendTrickDifficulty,
        JumpBombJumpTrickDifficulty,
        MidairMorphTrickDifficulty,
        UnderwaterWallJumpTrickDifficulty
    ]),
    OptionGroup("Custom Game Mode Options", [
        StartingLocation,
        StartingMajorUpgrades,
        StartingEnergyTanks,
        FillerItems,
        OpenSectorElevators,
        SectorNavigationRoomHintLocks
    ]),
    OptionGroup("Minor Options", [
        PaletteRandomization,
        AlternateHealthHudLayout,
        EnableHints,
        RevealHiddenBlocks,
        FastDoorTransitions,
        InstantMorph,
        SecondaryWeaponToggle,
        NerfGeronWeaknesses,
        MusicRando,
        MajorJingles,
        MissileDataAmmo,
        MissileTankAmmo,
        PowerBombDataAmmo,
        PowerBombTankAmmo,
    ])
]