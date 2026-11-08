import pkgutil
from ..constants import game_data as gd
from .auto_generated_types import MarsschemamfEnvironmentaldamage
from .constants.reserved_space import ReservedPointersMF
from .data import get_relative_data_path
from ..patching import BpsDecoder, IpsDecoder
from ..rom import Rom


def _get_patch_path(rom: Rom, subfolder: str, filename: str) -> str:
    dir = f"{rom.game.name}_{rom.region.name}".lower()
    return get_relative_data_path(__file__, "patches", dir, subfolder, filename)


def _internal_apply_ips_patch(rom: Rom, patch_name: str, subfolder: str) -> None:
    path = _get_patch_path(rom, subfolder, patch_name)
    patch = pkgutil.get_data(__name__, path)
    IpsDecoder().apply_patch(patch, rom.data)


def apply_patch_in_data_path(rom: Rom, patch_name: str) -> None:
    _internal_apply_ips_patch(rom, patch_name, "")


def apply_patch_in_asm_path(rom: Rom, patch_name: str) -> None:
    _internal_apply_ips_patch(rom, patch_name, "asm")


def apply_base_patch(rom: Rom) -> None:
    path = _get_patch_path(rom, "asm", "m4rs.bps")
    patch = pkgutil.get_data(__name__, path)
    rom.data = BpsDecoder().apply_patch(patch, rom.data)


def disable_demos(rom: Rom) -> None:
    # b 0x8087460
    rom.write_16(0x87436, 0xE013)


def skip_door_transitions(rom: Rom) -> None:
    rom.write_32(0x69500, 0x3000BDE)
    rom.write_8(0x694E2, 0xC)


def stereo_default(rom: Rom) -> None:
    rom.write_8(rom.read_ptr(ReservedPointersMF.DEFAULT_STEREO_FLAG_POINTER_ADDR.value), 1)


def disable_sounds(rom: Rom, start: int, end: int, exclude: set[int] = set()) -> None:
    sound_data_addr = gd.sound_data_entries(rom)
    for idx in range(start, end):
        if idx not in exclude:
            addr = sound_data_addr + idx * 8
            rom.write_8(rom.read_ptr(addr), 0)


def disable_music(rom: Rom) -> None:
    # Exclude jingles
    exclude = {
        16,  # Major obtained
        17,  # Loading save
        20,  # Minor obtained
        59,  # Event
    }
    disable_sounds(rom, 0, 100, exclude)


def disable_sound_effects(rom: Rom) -> None:
    disable_sounds(rom, 100, gd.sound_count(rom))


def change_missile_limit(rom: Rom, limit: int) -> None:
    rom.write_8(rom.read_ptr(ReservedPointersMF.MISSILE_LIMIT_ADDR.value), limit)


def apply_unexplored_map(rom: Rom) -> None:
    apply_patch_in_asm_path(rom, "unhidden_map.ips")


def apply_nerf_gerons(rom: Rom) -> None:
    apply_patch_in_asm_path(rom, "nerf_geron_weakness.ips")


def apply_alternative_health_layout(rom: Rom) -> None:
    rom.write_8(rom.read_ptr(ReservedPointersMF.USE_ALTERNATIVE_HUD_DISPLAY.value), 1)


def apply_environmental_damage(rom: Rom, damage_dict: MarsschemamfEnvironmentaldamage) -> None:
    base_address = rom.read_ptr(ReservedPointersMF.ENVIRONMENTAL_HAZARD_DAMAGE_ADDR.value)
    damage = [
        damage_dict["Lava"],
        damage_dict["Acid"],
        damage_dict["Heat"],
        # ASM currently has Subzero and Cold mislabelled. https://github.com/MetroidAdvRandomizerSystem/mars-fusion-asm/issues/374
        damage_dict["Cold"],
        damage_dict["Subzero"],
    ]
    for offset, damage_amount in enumerate(damage):
        rom.write_8(base_address + offset, damage_amount)


def apply_reveal_hidden_tiles(rom: Rom) -> None:
    rom.write_8(rom.read_ptr(ReservedPointersMF.REVEAL_HIDDEN_TILES_ADDR.value), 1)


def apply_reveal_unexplored_doors(rom: Rom) -> None:
    apply_patch_in_asm_path(rom, "unhidden_map_doors.ips")


def apply_instant_unmorph_patch(rom: Rom) -> None:
    rom.write_8(rom.read_ptr(ReservedPointersMF.INSTANT_MORPH_FLAG_POINTER_ADDR.value), 1)
