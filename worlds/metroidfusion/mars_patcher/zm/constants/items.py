from enum import IntEnum, auto


class MajorSource(IntEnum):
    LONG_BEAM = 0
    CHARGE_BEAM = auto()
    ICE_BEAM = auto()
    WAVE_BEAM = auto()
    PLASMA_BEAM = auto()
    BOMBS = auto()
    VARIA_SUIT = auto()
    GRAVITY_SUIT = auto()
    MORPH_BALL = auto()
    SPEED_BOOSTER = auto()
    HI_JUMP = auto()
    SCREW_ATTACK = auto()
    SPACE_JUMP = auto()
    POWER_GRIP = auto()
    FULLY_POWERED = auto()
    ZIPLINES = auto()


class ItemType(IntEnum):
    UNDEFINED = -1
    NONE = 0
    ENERGY_TANK = auto()
    MISSILE_TANK = auto()
    SUPER_MISSILE_TANK = auto()
    POWER_BOMB_TANK = auto()
    LONG_BEAM = auto()
    CHARGE_BEAM = auto()
    ICE_BEAM = auto()
    WAVE_BEAM = auto()
    PLASMA_BEAM = auto()
    BOMBS = auto()
    VARIA_SUIT = auto()
    GRAVITY_SUIT = auto()
    MORPH_BALL = auto()
    SPEED_BOOSTER = auto()
    HI_JUMP = auto()
    SCREW_ATTACK = auto()
    SPACE_JUMP = auto()
    POWER_GRIP = auto()
    FULLY_POWERED = auto()
    ZIPLINES = auto()
    ICE_TRAP = auto()


class ItemSprite(IntEnum):
    DEFAULT = auto()
    EMPTY = auto()
    ENERGY_TANK = auto()
    MISSILE_TANK = auto()
    SUPER_MISSILE_TANK = auto()
    POWER_BOMB_TANK = auto()
    LONG_BEAM = auto()
    CHARGE_BEAM = auto()
    ICE_BEAM = auto()
    WAVE_BEAM = auto()
    PLASMA_BEAM = auto()
    BOMBS = auto()
    VARIA_SUIT = auto()
    GRAVITY_SUIT = auto()
    MORPH_BALL = auto()
    SPEED_BOOSTER = auto()
    HI_JUMP = auto()
    SCREW_ATTACK = auto()
    SPACE_JUMP = auto()
    POWER_GRIP = auto()
    FULLY_POWERED = auto()
    ZIPLINES = auto()
    ANONYMOUS = auto()
    SHINY_MISSILE_TANK = auto()
    SHINY_POWER_BOMB_TANK = auto()


class ItemJingle(IntEnum):
    DEFAULT = 0
    MINOR = auto()
    MAJOR = auto()
    UNKNOWN = auto()
    FULLY_POWERED = auto()


class HintLocation(IntEnum):
    NONE = -1
    LONG_BEAM = 0
    BOMBS = auto()
    ICE_BEAM = auto()
    SPEED_BOOSTER = auto()
    HI_JUMP = auto()
    VARIA_SUIT = auto()
    WAVE_BEAM = auto()
    SCREW_ATTACK = auto()


BEAM_BOMB_FLAGS = {
    "LONG_BEAM": 1 << 0,
    "ICE_BEAM": 1 << 1,
    "WAVE_BEAM": 1 << 2,
    "PLASMA_BEAM": 1 << 3,
    "CHARGE_BEAM": 1 << 4,
    "BOMBS": 1 << 7,
}

SUIT_MISC_FLAGS = {
    "HI_JUMP": 1 << 0,
    "SPEED_BOOSTER": 1 << 1,
    "SPACE_JUMP": 1 << 2,
    "SCREW_ATTACK": 1 << 3,
    "VARIA_SUIT": 1 << 4,
    "GRAVITY_SUIT": 1 << 5,
    "MORPH_BALL": 1 << 6,
    "POWER_GRIP": 1 << 7,
}
