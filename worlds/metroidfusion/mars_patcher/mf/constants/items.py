from enum import IntEnum, auto
from typing import Any, Final


class MajorSource(IntEnum):
    MAIN_DECK_DATA = 0
    ARACHNUS = auto()
    CHARGE_CORE_X = auto()
    LEVEL_1 = auto()
    TRO_DATA = auto()
    ZAZABI = auto()
    SERRIS = auto()
    LEVEL_2 = auto()
    PYR_DATA = auto()
    MEGA_X = auto()
    LEVEL_3 = auto()
    ARC_DATA_1 = auto()
    WIDE_CORE_X = auto()
    ARC_DATA_2 = auto()
    YAKUZA = auto()
    NETTORI = auto()
    NIGHTMARE = auto()
    LEVEL_4 = auto()
    AQA_DATA = auto()
    WAVE_CORE_X = auto()
    RIDLEY = auto()
    BOILER = auto()
    ANIMALS = auto()
    AUXILIARYPOWER = auto()


class ItemType(IntEnum):
    UNDEFINED = -1
    NONE = 0
    LEVEL_0 = auto()
    MISSILES = auto()
    MORPH_BALL = auto()
    CHARGE_BEAM = auto()
    LEVEL_1 = auto()
    BOMBS = auto()
    HI_JUMP = auto()
    SPEED_BOOSTER = auto()
    LEVEL_2 = auto()
    SUPER_MISSILES = auto()
    VARIA_SUIT = auto()
    LEVEL_3 = auto()
    ICE_MISSILES = auto()
    WIDE_BEAM = auto()
    POWER_BOMBS = auto()
    SPACE_JUMP = auto()
    PLASMA_BEAM = auto()
    GRAVITY_SUIT = auto()
    LEVEL_4 = auto()
    DIFFUSION_MISSILES = auto()
    WAVE_BEAM = auto()
    SCREW_ATTACK = auto()
    ICE_BEAM = auto()
    MISSILE_TANK = auto()
    ENERGY_TANK = auto()
    POWER_BOMB_TANK = auto()
    ICE_TRAP = auto()
    INFANT_METROID = auto()

    def __le__(self, other: Any) -> bool:
        if isinstance(other, ItemType):
            return self.value <= other.value
        return NotImplemented


class ItemSprite(IntEnum):
    UNCHANGED = -1
    EMPTY = 0
    LEVEL_0 = auto()
    MISSILES = auto()
    MORPH_BALL = auto()
    CHARGE_BEAM = auto()
    LEVEL_1 = auto()
    BOMBS = auto()
    HI_JUMP = auto()
    SPEED_BOOSTER = auto()
    LEVEL_2 = auto()
    SUPER_MISSILES = auto()
    VARIA_SUIT = auto()
    LEVEL_3 = auto()
    ICE_MISSILES = auto()
    WIDE_BEAM = auto()
    POWER_BOMBS = auto()
    SPACE_JUMP = auto()
    PLASMA_BEAM = auto()
    GRAVITY_SUIT = auto()
    LEVEL_4 = auto()
    DIFFUSION_MISSILES = auto()
    WAVE_BEAM = auto()
    SCREW_ATTACK = auto()
    ICE_BEAM = auto()
    MISSILE_TANK = auto()
    ENERGY_TANK = auto()
    POWER_BOMB_TANK = auto()
    ANONYMOUS = auto()
    SHINY_MISSILE_TANK = auto()
    SHINY_POWER_BOMB_TANK = auto()
    INFANT_METROID = auto()
    SAMUS_HEAD = auto()
    WALLJUMP_BOOTS = auto()
    RANDOVANIA = auto()
    ARCHIPELAGO_COLOR = auto()
    ARCHIPELAGO_MONOCHROME = auto()


KEY_MAJOR_LOCS: Final = "MajorLocations"
KEY_MINOR_LOCS: Final = "MinorLocations"
KEY_AREA: Final = "Area"
KEY_ROOM: Final = "Room"
KEY_SOURCE: Final = "Source"
KEY_BLOCK_X: Final = "BlockX"
KEY_BLOCK_Y: Final = "BlockY"
KEY_HIDDEN: Final = "Hidden"
KEY_ORIGINAL: Final = "Original"
KEY_ITEM: Final = "Item"
KEY_ITEM_SPRITE: Final = "ItemSprite"
KEY_ITEM_MESSAGES: Final = "ItemMessages"
KEY_ITEM_JINGLE: Final = "Jingle"


class ItemJingle(IntEnum):
    MINOR = 0
    MAJOR = auto()


JINGLE_ENUMS = {"Minor": ItemJingle.MINOR, "Major": ItemJingle.MAJOR}

SOURCE_ENUMS = {
    "MainDeckData": MajorSource.MAIN_DECK_DATA,
    "Arachnus": MajorSource.ARACHNUS,
    "ChargeCoreX": MajorSource.CHARGE_CORE_X,
    "Level1": MajorSource.LEVEL_1,
    "TroData": MajorSource.TRO_DATA,
    "Zazabi": MajorSource.ZAZABI,
    "Serris": MajorSource.SERRIS,
    "Level2": MajorSource.LEVEL_2,
    "PyrData": MajorSource.PYR_DATA,
    "MegaX": MajorSource.MEGA_X,
    "Level3": MajorSource.LEVEL_3,
    "ArcData1": MajorSource.ARC_DATA_1,
    "WideCoreX": MajorSource.WIDE_CORE_X,
    "ArcData2": MajorSource.ARC_DATA_2,
    "Yakuza": MajorSource.YAKUZA,
    "Nettori": MajorSource.NETTORI,
    "Nightmare": MajorSource.NIGHTMARE,
    "Level4": MajorSource.LEVEL_4,
    "AqaData": MajorSource.AQA_DATA,
    "WaveCoreX": MajorSource.WAVE_CORE_X,
    "Ridley": MajorSource.RIDLEY,
    "Boiler": MajorSource.BOILER,
    "Animals": MajorSource.ANIMALS,
    "AuxiliaryPower": MajorSource.AUXILIARYPOWER,
}

ITEM_ENUMS = {
    "Undefined": ItemType.UNDEFINED,
    "None": ItemType.NONE,
    "Level0": ItemType.LEVEL_0,
    "Missiles": ItemType.MISSILES,
    "MorphBall": ItemType.MORPH_BALL,
    "ChargeBeam": ItemType.CHARGE_BEAM,
    "Level1": ItemType.LEVEL_1,
    "Bombs": ItemType.BOMBS,
    "HiJump": ItemType.HI_JUMP,
    "SpeedBooster": ItemType.SPEED_BOOSTER,
    "Level2": ItemType.LEVEL_2,
    "SuperMissiles": ItemType.SUPER_MISSILES,
    "VariaSuit": ItemType.VARIA_SUIT,
    "Level3": ItemType.LEVEL_3,
    "IceMissiles": ItemType.ICE_MISSILES,
    "WideBeam": ItemType.WIDE_BEAM,
    "PowerBombs": ItemType.POWER_BOMBS,
    "SpaceJump": ItemType.SPACE_JUMP,
    "PlasmaBeam": ItemType.PLASMA_BEAM,
    "GravitySuit": ItemType.GRAVITY_SUIT,
    "Level4": ItemType.LEVEL_4,
    "DiffusionMissiles": ItemType.DIFFUSION_MISSILES,
    "WaveBeam": ItemType.WAVE_BEAM,
    "ScrewAttack": ItemType.SCREW_ATTACK,
    "IceBeam": ItemType.ICE_BEAM,
    "MissileTank": ItemType.MISSILE_TANK,
    "EnergyTank": ItemType.ENERGY_TANK,
    "PowerBombTank": ItemType.POWER_BOMB_TANK,
    "IceTrap": ItemType.ICE_TRAP,
    "InfantMetroid": ItemType.INFANT_METROID,
}

ITEM_SPRITE_ENUMS = {
    "Empty": ItemSprite.EMPTY,
    "Level0": ItemSprite.LEVEL_0,
    "Missiles": ItemSprite.MISSILES,
    "MorphBall": ItemSprite.MORPH_BALL,
    "ChargeBeam": ItemSprite.CHARGE_BEAM,
    "Level1": ItemSprite.LEVEL_1,
    "Bombs": ItemSprite.BOMBS,
    "HiJump": ItemSprite.HI_JUMP,
    "SpeedBooster": ItemSprite.SPEED_BOOSTER,
    "Level2": ItemSprite.LEVEL_2,
    "SuperMissiles": ItemSprite.SUPER_MISSILES,
    "VariaSuit": ItemSprite.VARIA_SUIT,
    "Level3": ItemSprite.LEVEL_3,
    "IceMissiles": ItemSprite.ICE_MISSILES,
    "WideBeam": ItemSprite.WIDE_BEAM,
    "PowerBombs": ItemSprite.POWER_BOMBS,
    "SpaceJump": ItemSprite.SPACE_JUMP,
    "PlasmaBeam": ItemSprite.PLASMA_BEAM,
    "GravitySuit": ItemSprite.GRAVITY_SUIT,
    "Level4": ItemSprite.LEVEL_4,
    "DiffusionMissiles": ItemSprite.DIFFUSION_MISSILES,
    "WaveBeam": ItemSprite.WAVE_BEAM,
    "ScrewAttack": ItemSprite.SCREW_ATTACK,
    "IceBeam": ItemSprite.ICE_BEAM,
    "MissileTank": ItemSprite.MISSILE_TANK,
    "EnergyTank": ItemSprite.ENERGY_TANK,
    "PowerBombTank": ItemSprite.POWER_BOMB_TANK,
    "Anonymous": ItemSprite.ANONYMOUS,
    "ShinyMissileTank": ItemSprite.SHINY_MISSILE_TANK,
    "ShinyPowerBombTank": ItemSprite.SHINY_POWER_BOMB_TANK,
    "InfantMetroid": ItemSprite.INFANT_METROID,
    "SamusHead": ItemSprite.SAMUS_HEAD,
    "WalljumpBoots": ItemSprite.WALLJUMP_BOOTS,
    "Randovania": ItemSprite.RANDOVANIA,
    "ArchipelagoColor": ItemSprite.ARCHIPELAGO_COLOR,
    "ArchipelagoMonochrome": ItemSprite.ARCHIPELAGO_MONOCHROME,
}


# TODO: Consider creating "game_enums.py"
BEAM_FLAGS = {"ChargeBeam": 1, "WideBeam": 2, "PlasmaBeam": 4, "WaveBeam": 8, "IceBeam": 0x10}
MISSILE_BOMB_FLAGS = {
    "Missiles": 1,
    "SuperMissiles": 2,
    "IceMissiles": 4,
    "DiffusionMissiles": 8,
    "Bombs": 0x10,
    "PowerBombs": 0x20,
}
SUIT_MISC_FLAGS = {
    "HiJump": 1,
    "SpeedBooster": 2,
    "SpaceJump": 4,
    "ScrewAttack": 8,
    "VariaSuit": 0x10,
    "GravitySuit": 0x20,
    "MorphBall": 0x40,
    "SaxSuit": 0x80,
}
