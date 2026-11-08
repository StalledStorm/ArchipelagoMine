from ...rom import Rom
from .reserved_space import ReservedPointersZM


def tileset_tilemap_sizes_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.TILESET_TILEMAP_SIZES_PTR.value)


def chozo_statue_targets_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.CHOZO_STATUE_TARGETS_PTR.value)


def intro_cutscene_data_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.INTRO_CUTSCENE_DATA_PTR.value)


def starting_info_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.STARTING_INFO_PTR.value)


def major_locations_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.MAJOR_LOCATIONS_PTR.value)


def minor_locations_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.MINOR_LOCATIONS_PTR.value)


def difficulty_options_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.DIFFICULTY_OPTIONS_PTR.value)


def metroid_sprite_stats_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.METROID_SPRITE_STATS_PTR.value)


def black_pirates_require_plasma_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.BLACK_PIRATES_REQUIRE_PLASMA_PTR.value)


def skip_door_transitions_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.SKIP_DOOR_TRANSITIONS_PTR.value)


def ball_launcher_without_bombs_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.BALL_LAUNCHER_WITHOUT_BOMBS_PTR.value)


def disable_midair_bomb_jump_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.DISABLE_MIDAIR_BOMB_JUMP_PTR.value)


def disable_walljump_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.DISABLE_WALLJUMP_PTR.value)


def remove_cutscenes_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.REMOVE_CUTSCENES_PTR.value)


def skip_suitless_sequence_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.SKIP_SUITLESS_SEQUENCE_PTR.value)


def tank_increase_amounts_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.TANK_INCREASE_AMOUNTS_PTR.value)


def title_text_lines_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.TITLE_TEXT_LINES_PTR.value)


def statues_cutscene_palette_addr(rom: Rom) -> int:
    return rom.read_ptr(ReservedPointersZM.STATUES_CUTSCENE_PALETTE_PTR.value)
