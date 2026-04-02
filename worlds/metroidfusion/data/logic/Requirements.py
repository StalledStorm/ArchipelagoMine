from typing import TYPE_CHECKING

from .Requirement import Requirement, PONRRequirement
if TYPE_CHECKING:
    from ... import MetroidFusionOptions

level_1_e_tanks = 3
level_2_e_tanks = 5
level_3_e_tanks = 7
level_4_e_tanks = 10

#region Individual Item Requirements
#Morph Ball Items
class HasMorph(Requirement):
    def __init__(self,
                 name = "Has Morph Ball",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Morph Ball"}
        elif items_needed is not None:
            items_needed.add("Morph Ball")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasBombData(Requirement):
    def __init__(self,
                 name = "Has Bomb Data",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Bomb Data"}
        elif items_needed is not None:
            items_needed.add("Bomb Data")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasPowerBombData(Requirement):
    def __init__(self,
                 name = "Has Power Bomb Data",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Power Bomb Data"}
        elif items_needed is not None:
            items_needed.add("Power Bomb Data")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

#Suit Items
class HasVaria(Requirement):
    def __init__(self,
                 name = "Has Varia Suit",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Varia Suit"}
        elif items_needed is not None:
            items_needed.add("Varia Suit")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasGravity(Requirement):
    def __init__(self,
                 name = "Has Gravity Suit",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Gravity Suit"}
        elif items_needed is not None:
            items_needed.add("Gravity Suit")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

#Mobility Items
# Reserved for when Wall Jump Boots enter the fray
class HasWallJump(Requirement):
    def __init__(self,
                 name = "Has Wall Jump",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Wall Jump Boots"}
        elif items_needed is not None:
            items_needed.add("Wall Jump Boots")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasHiJump(Requirement):
    def __init__(self,
                 name = "Has Hi-Jump",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Hi-Jump"}
        elif items_needed is not None:
            items_needed.add("Hi-Jump")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasSpaceJump(Requirement):
    def __init__(self,
                 name = "Has Space Jump",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Space Jump"}
        elif items_needed is not None:
            items_needed.add("Space Jump")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasSpeedBooster(Requirement):
    def __init__(self,
                 name = "Has Speed Booster",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Speed Booster"}
        elif items_needed is not None:
            items_needed.add("Speed Booster")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasScrewAttack(Requirement):
    def __init__(self,
                 name = "Has Screw Attack",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Screw Attack"}
        elif items_needed is not None:
            items_needed.add("Screw Attack")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

#Missile Items
class HasMissile(Requirement):
    def __init__(self,
                 name = "Has Missile Data",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Missile Data"}
        elif items_needed is not None:
            items_needed.add("Missile Data")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasSuperMissile(Requirement):
    def __init__(self,
                 name = "Has Super Missile",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Super Missile"}
        elif items_needed is not None:
            items_needed.add("Super Missile")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasIceMissile(Requirement):
    def __init__(self,
                 name = "Has Ice Missile",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Ice Missile"}
        elif items_needed is not None:
            items_needed.add("Ice Missile")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasDiffusionMissile(Requirement):
    def __init__(self,
                 name = "Has Diffusion Missile",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Diffusion Missile"}
        elif items_needed is not None:
            items_needed.add("Diffusion Missile")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

#Beam Items
class HasChargeBeam(Requirement):
    def __init__(self,
                 name = "Has Charge Beam",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Charge Beam"}
        elif items_needed is not None:
            items_needed.add("Charge Beam")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasWideBeam(Requirement):
    def __init__(self,
                 name = "Has Wide Beam",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Wide Beam"}
        elif items_needed is not None:
            items_needed.add("Wide Beam")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasPlasmaBeam(Requirement):
    def __init__(self,
                 name = "Has Plasma Beam",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Plasma Beam"}
        elif items_needed is not None:
            items_needed.add("Plasma Beam")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasWaveBeam(Requirement):
    def __init__(self,
                 name = "Has Wave Beam",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Wave Beam"}
        elif items_needed is not None:
            items_needed.add("Wave Beam")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasIceBeam(Requirement):
    def __init__(self,
                 name = "Has Ice Beam",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Ice Beam"}
        elif items_needed is not None:
            items_needed.add("Ice Beam")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

#Keycard Items
class HasKeycard1(Requirement):
    def __init__(self,
                 name = "Has Level 1 Keycard",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Level 1 Keycard"}
        elif items_needed is not None:
            items_needed.add("Level 1 Keycard")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasKeycard2(Requirement):
    def __init__(self,
                 name = "Has Level 2 Keycard",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Level 2 Keycard"}
        elif items_needed is not None:
            items_needed.add("Level 2 Keycard")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasKeycard3(Requirement):
    def __init__(self,
                 name = "Has Level 3 Keycard",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Level 3 Keycard"}
        elif items_needed is not None:
            items_needed.add("Level 3 Keycard")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

class HasKeycard4(Requirement):
    def __init__(self,
                 name = "Has Level 4 Keycard",
                 *requirements, **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', None)
        if items_needed is None:
            items_needed = {"Level 4 Keycard"}
        elif items_needed is not None:
            items_needed.add("Level 4 Keycard")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)
#endregion

#region Combined Item Requirements
class CanBomb(HasMorph, HasBombData):
    def __init__(self,
                 name = "Can Bomb",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanPowerBomb(HasMorph, HasPowerBombData):
    def __init__(self,
                 name = "Can Power Bomb",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanBallJump(HasMorph):
    def __init__(self,
                 name = "Can Ball Jump",
                 *requirements, **kwargs):
        requirements += ([HasBombData(), HasHiJump()],)
        super().__init__(name, *requirements, **kwargs)

class CanJumpHigh(Requirement):
    def __init__(self,
                 name = "Can Jump High",
                 *requirements, **kwargs):
        requirements +=  ([HasHiJump(), HasSpaceJump()],)
        super().__init__(name, *requirements, **kwargs)

class CanLavaDive(HasVaria, HasGravity):
    def __init__(self,
                 name = "Can Lava Dive",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanJumpHighUnderwater(HasGravity):
    def __init__(self,
                 name = "Can Jump High Underwater",
                 *requirements, **kwargs):
        requirements +=  ([CanJumpHigh()],)
        super().__init__(name, *requirements, **kwargs)

class CanSpeedBoosterUnderwater(HasGravity, HasSpeedBooster):
    def __init__(self,
                 name = "Can Speed Booster Underwater",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanScrewAttackUnderwater(HasGravity, HasScrewAttack):
    def __init__(self,
                 name = "Can Screw Attack Underwater",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanUseSuperMissile(HasMissile, HasSuperMissile):
    def __init__(self,
                 name = "Can Use Super Missile",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanUseIceMissile(HasMissile, HasIceMissile):
    def __init__(self,
                 name = "Can Use Ice Missile",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanUseDiffusionMissile(HasMissile, HasDiffusionMissile):
    def __init__(self,
                 name = "Can Use Diffusion Missile",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanUseOneMissileUpgrade(HasMissile):
    def __init__(self,
                 name = "Can Use One Missile Upgrade",
                 *requirements, **kwargs):
        requirements +=  ([CanUseSuperMissile(), CanUseIceMissile(), CanUseDiffusionMissile()],)
        super().__init__(name, *requirements, **kwargs)


class CanUseTwoMissileUpgrades(HasMissile):
    def __init__(self,
                 name = "Can Use Two Missile Upgrades",
                 *requirements, **kwargs):
        requirements += ([
            Requirement("Can Use Super Missile and Ice Missile",
                        items_needed={"Super Missile", "Ice Missile"}
            ),
            Requirement("Can Use Ice Missile and Diffusion Missile",
                        items_needed={"Ice Missile", "Diffusion Missile"}
            ),
            Requirement("Can Use Super Missile and Diffusion Missile",
                        items_needed={"Super Missile", "Diffusion Missile"}
            )
        ],)
        super().__init__(name, *requirements, **kwargs)

class CanUseAllMissileUpgrades(HasMissile, HasSuperMissile, HasIceMissile, HasDiffusionMissile):
    def __init__(self,
                 name = "Can Use All Missiles",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanFreezeEnemies(Requirement):
    def __init__(self,
                 name = "Can Freeze Enemies",
                 *requirements, **kwargs):
        requirements += ([HasIceBeam(), CanUseIceMissile(), CanUseDiffusionMissile()],)
        super().__init__(name, *requirements, **kwargs)

class CanActivatePillar(Requirement):
    def __init__(self,
                 name = "Can Activate Pillar",
                 *requirements, **kwargs):
        requirements += ([CanBomb(), CanPowerBomb(), HasWaveBeam()],)
        super().__init__(name, *requirements, **kwargs)

class CanDestroyBombBlocks(Requirement):
    def __init__(self,
                 name = "Can Destroy Bomb Blocks",
                 *requirements, **kwargs):
        requirements += ([CanBomb(), CanPowerBomb(), HasScrewAttack()],)
        super().__init__(name, *requirements, **kwargs)

class CanDestroyBombBlocksUnderwater(HasGravity, CanDestroyBombBlocks):
    def __init__(self,
                 name = "Can Destroy Bomb Blocks Underwater",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanChargedWaveShot(HasChargeBeam, HasWaveBeam):
    def __init__(self,
                 name = "Can Shoot Charged Wave Beam",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanUseOneBeamUpgrade(Requirement):
    def __init__(self,
                 name = "Can Use One Beam Upgrade",
                 *requirements, **kwargs):
        requirements += ([
            HasChargeBeam(),
            HasWideBeam(),
            HasPlasmaBeam(),
            HasWaveBeam(),
            HasIceBeam()
        ],)
        super().__init__(name, *requirements, **kwargs)

class CanUseTwoBeamUpgrades(Requirement):
    def __init__(self,
                 name = "Can Use Two Beam Upgrades",
                 *requirements, **kwargs):
        requirements += ([
            Requirement("Charge Wide", items_needed={"Charge Beam", "Wide Beam"}),
            Requirement("Charge Plasma", items_needed={"Charge Beam", "Plasma Beam"}),
            Requirement("Charge Wave", items_needed={"Charge Beam", "Wave Beam"}),
            Requirement("Charge Ice", items_needed={"Charge Beam", "Ice Beam"}),
            Requirement("Wide Plasma", items_needed={"Wide Beam", "Plasma Beam"}),
            Requirement("Wide Wave", items_needed={"Wide Beam", "Wave Beam"}),
            Requirement("Wide Ice", items_needed={"Wide Beam", "Ice Beam"}),
            Requirement("Plasma Wave", items_needed={"Plasma Beam", "Wave Beam"}),
            Requirement("Plasma Ice", items_needed={"Plasma Beam", "Ice Beam"}),
            Requirement("Wave Ice", items_needed={"Wave Beam", "Ice Beam"})
        ],)
        super().__init__(name, *requirements, **kwargs)

class CanUseThreeBeamUpgrades(Requirement):
    def __init__(self,
                 name = "Can Use Three Beam Upgrades",
                 *requirements, **kwargs):
        requirements += ([
            Requirement("Charge Wide Plasma", items_needed={"Charge Beam", "Wide Beam", "Plasma Beam"}),
            Requirement("Charge Wide Wave", items_needed={"Charge Beam", "Wide Beam", "Wave Beam"}),
            Requirement("Charge Wide Ice", items_needed={"Charge Beam", "Wide Beam", "Ice Beam"}),
            Requirement("Charge Plasma Wave", items_needed={"Charge Beam", "Plasma Beam", "Wave Beam"}),
            Requirement("Charge Plasma Ice", items_needed={"Charge Beam", "Plasma Beam", "Ice Beam"}),
            Requirement("Charge Wave Ice", items_needed={"Charge Beam", "Wave Beam", "Ice Beam"}),
            Requirement("Wide Plasma Wave", items_needed={"Wide Beam", "Plasma Beam", "Wave Beam"}),
            Requirement("Wide Plasma Ice", items_needed={"Wide Beam", "Plasma Beam", "Ice Beam"}),
            Requirement("Wide Wave Ice", items_needed={"Wide Beam", "Wave Beam", "Ice Beam"}),
            Requirement("Plasma Wave Ice", items_needed={"Plasma Beam", "Wave Beam", "Ice Beam"})
        ],)
        super().__init__(name, *requirements, **kwargs)

class CanUseFourBeamUpgrades(Requirement):
    def __init__(self,
                 name = "Can Use Four Beam Upgrades",
                 *requirements, **kwargs):
        requirements += ([
            Requirement("Charge Wide Plasma Wave",
                        items_needed={"Charge Beam", "Wide Beam", "Plasma Beam", "Wave Beam"}),
            Requirement("Charge Wide Plasma Ice",
                        items_needed={"Charge Beam", "Wide Beam", "Plasma Beam", "Ice Beam"}),
            Requirement("Charge Wide Wave Ice",
                        items_needed={"Charge Beam", "Wide Beam", "Wave Beam", "Ice Beam"}),
            Requirement("Charge Plasma Wave Ice",
                        items_needed={"Charge Beam", "Plasma Beam", "Wave Beam", "Ice Beam"}),
            Requirement("Wide Plasma Wave Ice",
                        items_needed={"Wide Beam", "Plasma Beam", "Wave Beam", "Ice Beam"}),
        ],)
        super().__init__(name, *requirements, **kwargs)

class CanUseAllBeamUpgrades(HasChargeBeam, HasWideBeam, HasPlasmaBeam, HasWaveBeam, HasIceBeam):
    def __init__(self,
                 name = "Can Use All Beam Upgrades",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanDoSimpleWallJump(Requirement):
    name = "Can Do Simple Wall Jump"
    items_needed = ["Wall Jump Boots"]

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= options.WallJumpTrickDifficulty.option_beginner

class CanDoSimpleWallJumpWithHiJump(Requirement):
    name = "Can Do Simple Wall Jump with Hi-Jump"
    items_needed = ["Hi-Jump"]

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= options.WallJumpTrickDifficulty.option_beginner

class CanDoSimpleWallJumpWithScrewAttack(Requirement):
    name = "Can Do Simple Wall Jump with Screw Attack"
    items_needed = ["Screw Attack"]

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= options.WallJumpTrickDifficulty.option_beginner

class CanDoSimpleWallJumpWithHiJumpAndScrewAttack(Requirement):
    name = "Can Do Simple Wall Jump with Hi-Jump and Screw Attack"
    items_needed = ["Hi-Jump", "Screw Attack"]

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= options.WallJumpTrickDifficulty.option_beginner

class CanDoSimpleWallJumpAndFreezeEnemies(Requirement):
    name = "Can Do Simple Wall Jump and Freeze Enemies"
    other_requirements = [CanFreezeEnemies]

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= options.WallJumpTrickDifficulty.option_beginner

class CanDoAdvancedWallJump(Requirement):
    name = "Can Do Advanced Wall Jump"
    items_needed = ["Wall Jump Boots"]

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= options.WallJumpTrickDifficulty.option_advanced

class CanDoAdvancedWallJumpWithHiJump(Requirement):
    name = "Can Do Advanced Wall Jump with Hi-Jump"
    items_needed = ["Hi-Jump"]

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= options.WallJumpTrickDifficulty.option_advanced

class CanDoAdvancedWallJumpWithScrewAttack(Requirement):
    name = "Can Do Advanced Wall Jump with Screw Attack"
    items_needed = ["Screw Attack"]

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= options.WallJumpTrickDifficulty.option_advanced

class CanDoAdvancedCombat(Requirement):
    name = "Can Do Advanced Combat"
    items_needed = ["Nothing"]

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_advanced

class CanDoExpertCombat(Requirement):
    name = "Can Do Expert Combat"
    items_needed = ["Nothing"]

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_expert

class CanFightBossOnAdvanced(Requirement):
    name = "Can Fight Boss on Advanced"
    items_needed = ["Missile Data", "Charge Beam"]
    energy_tanks_needed = level_1_e_tanks

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_advanced

class CanFightLategameBossOnAdvanced(Requirement):
    name = "Can Fight Lategame Boss on Advanced"
    items_needed = ["Missile Data", "Charge Beam", "Super Missile"]
    energy_tanks_needed = level_2_e_tanks

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_advanced

class CanFightBossOnExpert(Requirement):
    name = "Can Fight Boss on Expert"
    items_needed = ["Missile Data", "Charge Beam"]

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_expert

class SectorHubLevel1KeycardRequirement(Requirement):
    name = "Sector Hub Level 1 Keycard Requirement"
    items_needed = ["Level 1 Keycard"]
    energy_tanks_needed = level_1_e_tanks

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions"):
        if options.GameMode == options.GameMode.option_custom:
            return not options.OpenSectorElevators
        else:
            return options.GameMode == options.GameMode.option_vanilla


class SectorHubLevel2KeycardRequirement(Requirement):
    name = "Sector Hub Level 2 Keycard Requirement"
    items_needed = ["Level 2 Keycard"]
    energy_tanks_needed = level_2_e_tanks

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions"):
        if options.GameMode == options.GameMode.option_custom:
            return not options.OpenSectorElevators
        else:
            return options.GameMode == options.GameMode.option_vanilla


# endregion

#region Keycard Requirements
class HasKeycard1(Requirement):
    name = "Has Keycard 1"
    energy_tanks_needed = level_1_e_tanks
    items_needed = ["Level 1 Keycard"]

class HasKeycard2(Requirement):
    name = "Has Keycard 2"
    energy_tanks_needed = level_2_e_tanks
    items_needed = ["Level 2 Keycard"]

class HasKeycard1And2(Requirement):
    name = "Has Keycard 1 and 2"
    energy_tanks_needed = level_2_e_tanks
    items_needed = ["Level 1 Keycard", "Level 2 Keycard"]

class HasKeycard3(Requirement):
    name = "Has Keycard 3"
    energy_tanks_needed = level_3_e_tanks
    items_needed = ["Level 3 Keycard"]

class HasKeycard4(Requirement):
    name = "Has Keycard 4"
    energy_tanks_needed = level_4_e_tanks
    items_needed = ["Level 4 Keycard"]

class Level1KeycardRequirement(Requirement):
    name = "Level 1 Keycard Requirement"
    def __init__(self, items_needed, other_requirements, energy_tanks_needed=3):
        super().__init__(items_needed, other_requirements, energy_tanks_needed)
        self.items_needed.append("Level 1 Keycard")

class Level2KeycardRequirement(Requirement):
    name = "Level 2 Keycard Requirement"
    def __init__(self, items_needed, other_requirements, energy_tanks_needed=5):
        super().__init__(items_needed, other_requirements, energy_tanks_needed)
        self.items_needed.append("Level 2 Keycard")

class Level1And2KeycardRequirement(Requirement):
    name = "Level 1 and 2 Keycard Requirement"
    def __init__(self, items_needed, other_requirements, energy_tanks_needed=5):
        super().__init__(items_needed, other_requirements, energy_tanks_needed)
        self.items_needed.append("Level 1 Keycard")
        self.items_needed.append("Level 2 Keycard")

class Level3KeycardRequirement(Requirement):
    name = "Level 3 Keycard Requirement"
    def __init__(self, items_needed, other_requirements, energy_tanks_needed=7):
        super().__init__(items_needed, other_requirements, energy_tanks_needed)
        self.items_needed.append("Level 3 Keycard")

class Level4KeycardRequirement(Requirement):
    name = "Level 4 Keycard Requirement"
    def __init__(self, items_needed, other_requirements, energy_tanks_needed=10):
        super().__init__(items_needed, other_requirements, energy_tanks_needed)
        self.items_needed.append("Level 4 Keycard")
#endregion

#region Enemy Requirements
class CanDamageSmallGeron(HasMissile):
    def __init__(self,
                 name = "Can Damage Small Geron",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanDamageMediumGeron(CanUseSuperMissile):
    def __init__(self,
                 name = "Can Damage Medium Geron",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanDamageLargeGeron(CanPowerBomb):
    def __init__(self,
                 name = "Can Damage Large Geron",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanDamageStabilizer(Requirement):
    def __init__(self,
                 name = "Can Damage Stabilizer",
                 *requirements, **kwargs):
        requirements += ([HasMissile(), HasChargeBeam()],)
        super().__init__(name, *requirements, **kwargs)

class CanDamageAnyGeron(Requirement):
    def __init__(self,
                 name = "Can Damage Any Geron",
                 *requirements, **kwargs):
        requirements += ([CanPowerBomb(), HasScrewAttack()],)
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions"):
        return not options.NerfGeronWeaknesses

class CanDamageToughEnemy(Requirement):
    def __init__(self,
                 name = "Can Damage Tough Enemy",
                 *requirements, **kwargs):
        requirements += ([HasMissile(), HasChargeBeam()],)
        super().__init__(name, *requirements, **kwargs)

class CanDamageToughEnemyThroughWalls(Requirement):
    def __init__(self,
                 name = "Can Damage Tough Enemy Through Walls",
                 *requirements, **kwargs):
        requirements += ([CanChargedWaveShot(), CanPowerBomb()],)
        super().__init__(name, *requirements, **kwargs)

#endregion

#region Boss Requirements
class CanDamageCoreX(HasMissile):
    def __init__(self,
                 name = "Can Damage Core X",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanFightEarlyGameBoss(CanDamageCoreX):
    def __init__(self,
                 name = "Can Fight Early Game Boss",
                 *requirements, **kwargs):
        kwargs['energy_tanks_needed'] = max(kwargs.pop('energy_tanks_needed', 0), level_1_e_tanks)
        super().__init__(name, *requirements, **kwargs)

class CanFightMidGameBoss(CanFightEarlyGameBoss, CanUseSuperMissile, HasChargeBeam):
    def __init__(self,
                 name = "Can Fight Mid Game Boss",
                 *requirements, **kwargs):
        kwargs['energy_tanks_needed'] = max(kwargs.pop('energy_tanks_needed', 0), level_2_e_tanks)
        super().__init__(name, *requirements, **kwargs)

class CanFightLateGameBoss(CanFightMidGameBoss, HasPlasmaBeam, HasSpaceJump):
    def __init__(self,
                 name = "Can Fight Late Game Boss",
                 *requirements, **kwargs):
        kwargs['energy_tanks_needed'] = max(kwargs.pop('energy_tanks_needed', 0), level_3_e_tanks)
        super().__init__(name, *requirements, **kwargs)

#endregion

#region Trick Options Requirements

class CanDoBeginnerShinespark(HasSpeedBooster):
    def __init__(self,
                 name = "Can Do Beginner Shinespark",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.ShinesparkTrickDifficulty >= 1#options.ShinesparkTrickDifficulty.option_beginner

class CanDoAdvancedShinespark(HasSpeedBooster):
    def __init__(self,
                 name = "Can Do Advanced Shinespark",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.ShinesparkTrickDifficulty >= 2#options.ShinesparkTrickDifficulty.option_advanced

class CanDoSimpleWallJump(HasWallJump):
    def __init__(self,
                 name = "Can Do Simple Wall Jump",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= 1#options.WallJumpTrickDifficulty.option_beginner

class CanDoAdvancedWallJump(HasWallJump):
    def __init__(self,
                 name = "Can Do Advanced Wall Jump",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= 2#options.WallJumpTrickDifficulty.option_advanced

class CanDoAdvancedCombat(Requirement):
    def __init__(self,
                 name = "Can Do Advanced Combat",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= 1#options.CombatDifficulty.option_advanced

class CanDoExpertCombat(Requirement):
    def __init__(self,
                 name = "Can Do Expert Combat",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= 2#options.CombatDifficulty.option_expert

class CanFightMidGameBossOnAdvanced(CanFightEarlyGameBoss, HasChargeBeam):
    def __init__(self,
                 name = "Can Fight Mid Game Boss On Advanced",
                 *requirements, **kwargs):
        kwargs['energy_tanks_needed'] = max(kwargs.pop('energy_tanks_needed', 0), level_1_e_tanks)
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= 1#options.CombatDifficulty.option_advanced

class CanFightLateGameBossOnAdvanced(CanFightMidGameBoss):
    def __init__(self,
                 name = "Can Fight Late Game Boss on Advanced",
                 *requirements, **kwargs):
        kwargs['energy_tanks_needed'] = max(kwargs.pop('energy_tanks_needed', 0), level_2_e_tanks)
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= 1#options.CombatDifficulty.option_advanced

class CanFightBossOnExpert(CanDamageCoreX, HasChargeBeam):
    def __init__(self,
                 name = "Can Fight Boss on Expert",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= 2#options.CombatDifficulty.option_expert

class SectorHubLevel1KeycardRequirement(HasKeycard1):
    def __init__(self,
                 name = "Sector Hub Level 1 Keycard Requirement",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions"):
        if options.GameMode == options.GameMode.option_custom:
            return not options.OpenSectorElevators
        else:
            return options.GameMode == 0#options.GameMode.option_vanilla


class SectorHubLevel1And2KeycardRequirement(HasKeycard1, HasKeycard2):
    def __init__(self,
                 name = "Sector Hub Level 1 and 2 Keycard Requirement",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions"):
        if options.GameMode == options.GameMode.option_custom:
            return not options.OpenSectorElevators
        else:
            return options.GameMode == 0#options.GameMode.option_vanilla

# endregion

#region Prefab Requirements

class CanCollectCrumbleCity(Requirement):
    def __init__(self,
                 name = "Can Collect Crumble City",
                 *requirements, **kwargs):
        requirements += ([
            Requirement("Can Collect Crumble City Item",
                        [
                            HasScrewAttack("Break into Crumble City and Collect Item",
                                           [
                                               HasSpaceJump("Fly"),
                                               # Awaiting trick option evaluation. This is masochistic to perform.
                                               # [CanDoExpertCrumbleJank()]
                                           ]
                                           # MARS changes the door type to a Level 0 Security Door.
                                           #    This is the original door requirement.
                                           # , [HasKeycard4()]
                                           )
                        ])
        ],)
        super().__init__(name, *requirements, **kwargs)

class CanObtainRipperTower(Requirement):
    def __init__(self,
                 name = "Can Obtain Ripper Tower",
                 *requirements, **kwargs):
        requirements += ([
            Requirement("Can Obtain Ripper Tower Item",
                        [CanFreezeEnemies()],
                        items_needed={"Morph Ball"})
        ],)
        super().__init__(name, *requirements, **kwargs)

class PONREnterBobsTunnelFromAbove(PONRRequirement, HasMorph, HasKeycard2):
    def __init__(self,
                 name = "Can Enter Bob's Tunnel From Above",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)

class CanFightBOX(CanDamageToughEnemy):
    def __init__(self,
                 name = "Can Fight BOX",
                 *requirements, **kwargs):
        requirements += ([CanJumpHigh(), CanDoSimpleWallJump()],)
        kwargs['energy_tanks_needed'] = max(kwargs.pop('energy_tanks_needed', 0), level_2_e_tanks)
        super().__init__(name, *requirements, **kwargs)

class CanClimbSector3Attic(Requirement):
    def __init__(self,
                 name = "Can Climb Sector 3 Attic",
                 *requirements, **kwargs):
        requirements += ([
                             CanDestroyBombBlocks()
                         ], [
            HasHiJump("Wall Jump Good",
                      [CanDoAdvancedWallJump()]),
            HasSpaceJump("Fly through Bomb Blocks",
                         items_needed={"Screw Attack"}),
            CanActivatePillar(),
            CanFreezeEnemies("Step on Sidehopper",
                             [
                                 CanBomb("Bomb without killing your platform",
                                         items_needed={"Hi-Jump"}),
                                 HasScrewAttack("Needed a stool")
                             ], [CanDoSimpleWallJump()])
        ],)
        super().__init__(name, *requirements, **kwargs)

class CanDoBoiler(CanDamageCoreX):
    def __init__(self,
                 name = "Can Do Boiler",
                 *requirements, **kwargs):
        requirements += ([
            # Required to get to the Boiler Control Room
            # Main blocker is Pyrochamber Access
            HasSpaceJump("Fly"),
            CanFreezeEnemies("Freeze Funes",
                             [
                                 CanDoSimpleWallJump(),
                                 HasHiJump()
                             ])
        ],)
        kwargs['energy_tanks_needed'] = max(kwargs.pop('energy_tanks_needed', 0), level_2_e_tanks)
        super().__init__(name, *requirements, **kwargs)

class CanGetSovaProcessingItem(HasMorph):
    def __init__(self,
                 name = "Can Get Sova Processing Item",
                 *requirements, **kwargs):
        requirements += ([HasSpaceJump(), CanFreezeEnemies()],)
        super().__init__(name, *requirements, **kwargs)

class CanActivatePumpControl(Requirement):
    def __init__(self,
                 name = "Can Activate Pump Control",
                 *requirements, **kwargs):
        requirements += ([
            HasKeycard1("Enter Pump Control",
                        [
                            # Getting to the Terminal
                            HasSpeedBooster("Break through Speed Booster Blocks"),
                            HasGravity("Use Drain Pipe below Pump Control Terminal",
                                       [
                                           # Get in and out of Item Nook
                                           CanBallJump()
                                       ], [
                                           # Climb Up Drain Pipe
                                           HasSpaceJump(),
                                           CanDoSimpleWallJump(None,
                                                               items_needed={"Hi-Jump"})
                                       ], energy_tanks_needed=level_2_e_tanks,)
                        ], [
                            # Leaving
                            CanBallJump("Use Tunnel"),
                            # Shinespark will risk softlocking
                            CanDoAdvancedShinespark("Charge Shinespark and Use Terminal")
                        ], energy_tanks_needed=level_1_e_tanks),
        ],)
        super().__init__(name, *requirements, **kwargs)

class CanDoScizerSanctuary(Requirement):
    def __init__(self,
                 name = "Can Do Scizer Sanctuary",
                 *requirements, **kwargs):
        requirements += ([
            CanDamageToughEnemy("Kill the Golden Crabs and Unlock Door",
                                [
                                    # Kill the caged crabs
                                    HasWaveBeam(),
                                    CanPowerBomb(),
                                    CanDoAdvancedCombat("Use Flare from Charge Beam",
                                                        items_needed={"Charge Beam"})
                                ], [
                                    # Kill the gold crabs
                                    CanChargedWaveShot(),
                                    HasMissile("Open Tunnel",
                                               [
                                                   CanDoAdvancedCombat("Thread the Needle"),
                                                   HasMorph("Enter Tunnel into Golden Crab Enclosure")
                                               ])
                                ])
        ],)
        super().__init__(name, *requirements, **kwargs)

class CanEnterReservoirVault(Requirement):
    def __init__(self,
                 name = "Can Enter Reservoir Vault",
                 *requirements, **kwargs):
        requirements += ([
            HasMorph("Break Bomb Block Chain and Enter Tunnel",
                     [
                         # Break Bomb Block Chain
                         CanBomb(),
                         CanPowerBomb()
                     ], [
                         # Enter Tunnel
                         CanBallJump(),
                         #future CanDoAdvancedMidairMorph()
                     ])
        ],)
        super().__init__(name, *requirements, **kwargs)


class CanCrossSector4DrainPipeTunnel(Requirement):
    def __init__(self,
                 name = "Can Cross Sector 4 Drain Pipe Tunnel",
                 *requirements, **kwargs):
        requirements += ([
            HasMorph(None,
                     [
                         # Freeze the Powamp
                         CanUseDiffusionMissile(),
                         HasIceBeam(None, items_needed={"Wave Beam"})
                     ], [
                         CanActivatePumpControl(),
                         Requirement("Damage Run through Electrified Water",
                                     energy_tanks_needed=level_2_e_tanks)
                     ])
        ],)
        super().__init__(name, *requirements, **kwargs)

class CanGetToTrainingAerie(Requirement):
    def __init__(self,
                 name = "Can Get to Training Aerie",
                 *requirements, **kwargs):
        requirements += ([
            HasSpaceJump(),
            CanFreezeEnemies(),
            CanDoBeginnerShinespark(None, [
                HasKeycard3()
            ], [
                CanDoAdvancedWallJump()
            ])
        ],)
        super().__init__(name, *requirements, **kwargs)

class CanFightNightmare(Requirement):
    def __init__(self,
                 name = "Can Fight Nightmare",
                 *requirements, **kwargs):
        requirements += ([
            # Nightmare Fight Requirements
            CanFightLateGameBoss(),
            CanFightLateGameBossOnAdvanced(),
            CanFightBossOnExpert()
        ], [
            # Can leave Nightmare Arena?
            CanSpeedBoosterUnderwater(),
            HasGravity("PONR - Enter Nightmare Arena with Gravity Suit",
                       [PONRRequirement()]),
            HasSpeedBooster("PONR - Enter Nightmare Arena with Speed Booster",
                            [PONRRequirement()]),
            PONRRequirement("PONR - Enter Nightmare Arena")
        ])
        super().__init__(name, *requirements, **kwargs)

class CanFightVariaCoreX(CanDamageCoreX, HasChargeBeam):
    def __init__(self,
                 name = "Can Fight Varia Core X",
                 *requirements, **kwargs):
        kwargs['energy_tanks_needed'] = max(kwargs.pop('energy_tanks_needed', 0), level_2_e_tanks)
        super().__init__(name, *requirements, **kwargs)

class CanEnterSpaceboostAlley(CanPowerBomb, HasScrewAttack, HasKeycard4, HasSpeedBooster):
    def __init__(self,
                 name = "Can Enter Spaceboost Alley",
                 *requirements, **kwargs):
        super().__init__(name, *requirements, **kwargs)
