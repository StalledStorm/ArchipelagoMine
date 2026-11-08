from ..rom import Rom
from ..room_entry import RoomEntry
from .auto_generated_types import MarsschemazmTankIncrements
from .constants.game_data import (
    chozo_statue_targets_addr,
    major_locations_addr,
    minor_locations_addr,
    tank_increase_amounts_addr,
)
from .locations import HintLocation, LocationSettings


class ItemPatcher:
    """Class for writing item assignments to a ROM."""

    def __init__(self, rom: Rom, settings: LocationSettings):
        self.rom = rom
        self.settings = settings

    def write_items(self) -> None:
        rom = self.rom
        hint_targets_addr = chozo_statue_targets_addr(rom)

        # Handle minor locations
        # Locations need to be written in order so that binary search works
        minor_locs = sorted(self.settings.minor_locs, key=lambda x: x.key)
        minor_loc_addr = minor_locations_addr(rom)
        for min_loc in minor_locs:
            # TODO: Update tileset and get BG1 value
            bg1_val = 0x4A  # Use power bomb tank block for now
            # Overwrite BG1 if not hidden
            if not min_loc.hidden:
                room = RoomEntry(rom, min_loc.area, min_loc.room)
                with room.load_bg1() as bg1:
                    bg1.set_block_value(min_loc.block_x, min_loc.block_y, bg1_val)

            # See struct MinorLocation in include/structs/randomizer.h
            rom.write_32(minor_loc_addr, min_loc.key)
            rom.write_16(minor_loc_addr + 4, bg1_val)
            rom.write_8(minor_loc_addr + 6, min_loc.new_item.value)
            rom.write_8(minor_loc_addr + 7, min_loc.item_jingle.value)
            # TODO: Handle custom messages
            rom.write_32(minor_loc_addr + 8, 0)
            rom.write_8(minor_loc_addr + 0xC, min_loc.hint_value)
            minor_loc_addr += 0x10

            if min_loc.hinted_by != HintLocation.NONE:
                room = RoomEntry(rom, min_loc.area, min_loc.room)
                map_x, map_y = room.map_coords_at_block(min_loc.block_x, min_loc.block_y)
                target_addr = hint_targets_addr + (min_loc.hinted_by.value * 0xC)
                rom.write_8(target_addr + 6, min_loc.area)
                rom.write_8(target_addr + 7, map_x)
                rom.write_8(target_addr + 8, map_y)

        # Handle major locations
        major_locs_addr = major_locations_addr(rom)
        for maj_loc in self.settings.major_locs:
            addr = major_locs_addr + (maj_loc.major_src.value * 8)
            rom.write_8(addr, maj_loc.new_item.value)
            rom.write_8(addr + 1, maj_loc.item_jingle.value)
            rom.write_8(addr + 2, maj_loc.hint_value)
            # TODO: Handle custom messages
            rom.write_32(addr + 4, 0)

            if maj_loc.hinted_by != HintLocation.NONE:
                target_addr = hint_targets_addr + (maj_loc.hinted_by.value * 0xC)
                rom.write_8(target_addr + 6, maj_loc.area)
                rom.write_8(target_addr + 7, maj_loc.map_x)
                rom.write_8(target_addr + 8, maj_loc.map_y)


def set_tank_increments(rom: Rom, data: MarsschemazmTankIncrements) -> None:
    addr = tank_increase_amounts_addr(rom)
    rom.write_16(addr, data["energy_tank"])
    rom.write_16(addr + 2, data["missile_tank"])
    rom.write_8(addr + 4, data["super_missile_tank"])
    rom.write_8(addr + 5, data["power_bomb_tank"])
