from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....MFOptions import MetroidFusionOptions

class EnergyAmmoUtil:

    @staticmethod
    def damage_to_ammo_calc(hp: int, damage_per_instance: int) -> int:
        return -int(-(hp / damage_per_instance) // 1)

    @staticmethod
    def ammo_modified_by_options(ammo: int, options: "MetroidFusionOptions") -> int:
        match options.CombatDifficulty.value:
            case 0:
                return -int(-(ammo * 1.5) // 1)
            case 1 | 2:
                return -int(-(ammo * 1.25) // 1)
            case 3 | 4:
                return -int(-(ammo * 1.1) // 1)
            case _:
                return ammo * 1

    @staticmethod
    def energy_value_to_tanks(energy: int) -> int:
        return EnergyAmmoUtil.damage_to_ammo_calc(energy, 100)