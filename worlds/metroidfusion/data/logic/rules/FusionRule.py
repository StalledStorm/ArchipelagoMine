from dataclasses import dataclass
from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from FusionTrick import Trick
from rule_builder.rules import (True_, False_, And, Or, Rule, Has, HasAll, HasAllCounts, HasAny,
                                HasAnyCount, HasFromList, HasFromListUnique, HasGroup, HasGroupUnique,
                                CanReachLocation, CanReachRegion, CanReachEntrance)
from ..FusionEnemy import Enemy, Immunity

import EnergyAmmoUtil

if TYPE_CHECKING:
    from ....MFOptions import MetroidFusionOptions
    from ....__init__ import MetroidFusionWorld


@dataclass
class CanGoal(Rule["MetroidFusionWorld"], game="Metroid Fusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        options = world.options
        min_req = And(
            HasAllCounts({
                "Infant Metroid": options.InfantMetroidsRequired.value,
                "Energy Tank": 3,
                "Charge Beam": 1,
                "Missile Data": 1
            }),
            CanReachRegion("Main Deck - Operations Room"),
            CanReachRegion("Main Deck - Operations Deck"),
            CanReachRegion("Main Deck - Docking Bay Hangar")
        )
        advanced_goal = And(
            HasAll("Plasma Beam", "Varia Suit"),
            Has("Energy Tank", 6)
        )
        beginner_goal = And(
            HasAll("Wide Beam", "Super Missile"),
            Has("Energy Tank", 10)
        )

        match options.CombatDifficulty.value:
            case 2 | 3 | 4 | 5 | 6:
                return min_req.resolve(world)
            case 1:
                return (min_req & advanced_goal).resolve(world)
            case _:
                return (min_req & advanced_goal & beginner_goal).resolve(world)

@dataclass
class TrickEnabled(Rule["MetroidFusionWorld"], game="Metroid Fusion"):
    trick_type: int
    difficulty: int
    """The trick type and difficulty to match against"""

    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        if Trick.can_perform_trick(world.options, self.trick_type, self.difficulty):
            return True_.resolve(world)
        else:
            return False_.resolve(world)

@dataclass
class CanPONR(Rule["MetroidFusionWorld"], game="Metroid Fusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        if world.options.PointOfNoReturnsInLogic.value:
            return True_.resolve(world)
        else:
            return False_.resolve(world)

@dataclass
class OpenSectorHubElevators(Rule["MetroidFusionWorld"], game="Metroid Fusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        if any([world.options.GameMode.value == 1,
                world.options.GameMode.value == 2 and world.options.OpenSectorElevators.value]):
            return True_.resolve(world)
        return False_.resolve(world)

@dataclass
class IsLocationCollected(Rule["MetroidFusionWorld"], game="Metroid Fusion"):
    location_name: str

    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return self.Resolved(player=world.player, location_name=self.location_name)

    class Resolved(Rule.Resolved):
        location_name: str

        def _evaluate(self, state: CollectionState) -> bool:
            return state.multiworld.get_location(self.location_name, self.player) in state.locations_checked

@dataclass
class CanBomb(Rule["MetroidFusionWorld"], game="Metroid Fusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Morph Ball", "Bomb Data").resolve(world)

@dataclass
class CanPowerBomb(Rule["MetroidFusionWorld"], game="Metroid Fusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Morph Ball", "Power Bomb Data").resolve(world)

@dataclass
class CanBallJump(Rule["MetroidFusionWorld"], game="Metroid Fusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return And(Has("Morph Ball"), HasAny("Bomb Data", "Hi-Jump")).resolve(world)

@dataclass
class CanJumpHigh(Rule["MetroidFusionWorld"], game="Metroid Fusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAny("Hi-Jump", "Space Jump").resolve(world)

@dataclass
class CanLavaDive(Rule["MetroidFusionWorld"], game="Metroid Fusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Varia Suit", "Gravity Suit").resolve(world)

@dataclass
class CanJumpHighUnderwater(Rule["MetroidFusionWorld"], game="Metroid Fusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return And(CanJumpHigh(), Has("Gravity Suit")).resolve(world)

@dataclass
class CanSpeedBoosterUnderwater(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Gravity Suit", "Speed Booster").resolve(world)

@dataclass
class CanScrewAttackUnderwater(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Gravity Suit", "Screw Attack").resolve(world)

@dataclass
class CanDo15MissileDamage(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Missile Data", "Diffusion Missile").resolve(world)

@dataclass
class CanDo20MissileDamage(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Missile Data", "Ice Missile").resolve(world)

@dataclass
class CanDo25MissileDamage(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Missile Data", "Ice Missile", "Diffusion Missile").resolve(world)

@dataclass
class CanDo30MissileDamage(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Missile Data", "Super Missile").resolve(world)

@dataclass
class CanDo35MissileDamage(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Missile Data", "Super Missile", "Diffusion Missile").resolve(world)

@dataclass
class CanDo40MissileDamage(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Missile Data", "Super Missile", "Ice Missile").resolve(world)

@dataclass
class CanDo45MissileDamage(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Missile Data", "Super Missile", "Ice Missile", "Diffusion Missile").resolve(world)

@dataclass
class CanFreezeEnemies(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return Or(Has("Ice Beam"), CanDo20MissileDamage(), CanDo15MissileDamage()).resolve(world)

@dataclass
class CanActivatePillar(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return Or(Has("Wave Beam"), CanBomb(), CanPowerBomb()).resolve(world)

@dataclass
class CanDestroyBombBlocks(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    chain: bool = False
    """Bomb blocks are part of a chain"""
    tunnel: bool = False
    """Bomb blocks are only accessible via tunnel"""

    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        if self.chain or self.tunnel:
            return Or(CanBomb(), CanPowerBomb()).resolve(world)
        return Or(Has("Screw Attack"), CanBomb(), CanPowerBomb()).resolve(world)

@dataclass
class CanDestroyBombBlocksUnderwater(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return And(Has("Gravity Suit"), CanDestroyBombBlocks()).resolve(world)

@dataclass
class CanChargedWave(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return HasAll("Charge Beam", "Wave Beam").resolve(world)

@dataclass
class CanClearEnemy(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    enemy: Enemy | None = None
    """Enemy whose HP will be reduced to zero"""
    enemy_count: int = 1
    """Enemy quantity whose HP needs to be zero. Multiple of ``enemy_hp``"""
    speed_booster_override: bool = False
    """Toggle when room space allows for charging a speed boost to deal damage."""

    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return self.Resolved(world.options,
                             enemy=self.enemy,
                             enemy_count=self.enemy_count,
                             player=world.player)

    class Resolved(Rule.Resolved):
        options: "MetroidFusionOptions"
        enemy: Enemy | None = None
        enemy_count: int = 1
        speed_booster_override: bool = False

        def _evaluate(self, state: CollectionState) -> bool:
            # Pre-eval check
            missile_ammo_req = 0
            pb_ammo_req = 0
            if self.enemy is None:
                missile_ammo_req = self.enemy_count
                pb_ammo_req = self.enemy_count

            # Setup
            missile_damage = 10
            if state.has("Super Missile", self.player):
                missile_damage += 20
            if state.has("Ice Missile", self.player):
                missile_damage += 10
            if state.has("Diffusion Missile", self.player):
                missile_damage += 5
            total_missiles = 0
            if state.has("Missile Data", self.player):
                total_missiles += (self.options.MissileDataAmmo.value +
                                   state.count("Missile Tank", self.player) * self.options.MissileTankAmmo.value)
            total_pbs = 0
            if state.has("Power Bomb Data", self.player):
                total_pbs += (self.options.PowerBombDataAmmo.value +
                              state.count("Power Bomb Tank", self.player) * self.options.PowerBombTankAmmo.value)

            # Calculate how much ammo is needed
            if self.enemy:
                missile_ammo_req = EnergyAmmoUtil.damage_to_ammo_calc(self.enemy.hp, missile_damage)
                pb_ammo_req = EnergyAmmoUtil.damage_to_ammo_calc(self.enemy.hp, 50)
                missile_ammo_req *= self.enemy_count

            missile_ammo_req = EnergyAmmoUtil.ammo_modified_by_options(missile_ammo_req, self.options)
            pb_ammo_req = EnergyAmmoUtil.ammo_modified_by_options(pb_ammo_req, self.options)

            # Do checks
            if (self.enemy in {Enemy.GERON, Enemy.GERON_SUPER, Enemy.GERON_POWER}
                and self.options.NerfGeronWeaknesses.value):
                match self.enemy:
                    case Enemy.GERON:
                        return total_missiles >= missile_ammo_req and state.has("Missile Data", self.player)
                    case Enemy.GERON_SUPER:
                        return (total_missiles >= missile_ammo_req
                                and state.has_all(["Missile Data", "Super Missile"], self.player))
                    case Enemy.GERON_POWER:
                        return (total_pbs >= pb_ammo_req
                                and state.has_all(["Morph Ball", "Power Bomb Data"], self.player))
            elif self.enemy.can_be_damaged_by(Immunity.MISSILE, state.prog_items[self.player]):
                return total_missiles >= missile_ammo_req
            elif self.enemy.can_be_damaged_by(Immunity.PB, state.prog_items[self.player]):
                return total_pbs >= pb_ammo_req
            else:
                return self.enemy.can_be_damaged(state.prog_items[self.player],
                                                 speed_booster_override=self.speed_booster_override)

@dataclass
class CanDamageSmallGeron(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        if world.options.NerfGeronWeaknesses.value:
            return CanClearEnemy(enemy=Enemy.GERON).resolve(world)
        return Or(CanClearEnemy(enemy=Enemy.GERON), Has("Screw Attack")).resolve(world)

@dataclass
class CanDamageMediumGeron(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        if world.options.NerfGeronWeaknesses.value:
            return And(CanClearEnemy(enemy=Enemy.GERON_SUPER), Has("Super Missile")).resolve(world)
        return Or(
            And(CanClearEnemy(enemy=Enemy.GERON_SUPER), Has("Super Missile")),
            Has("Screw Attack")
        ).resolve(world)

@dataclass
class CanDamageLargeGeron(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        if world.options.NerfGeronWeaknesses.value:
            return CanPowerBomb().resolve(world)
        return Or(CanPowerBomb(), Has("Screw Attack")).resolve(world)

@dataclass
class CanDamageStabilizer(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        if world.options.NerfGeronWeaknesses.value:
            return Or(CanClearEnemy(enemy=Enemy.ATMOSPHERIC_STABILIZER_PARASITE), Has("Charge Beam")).resolve(world)
        return Or(
            CanClearEnemy(enemy=Enemy.ATMOSPHERIC_STABILIZER_PARASITE),
            HasAny("Charge Beam", "Screw Attack")
        ).resolve(world)

@dataclass
class HasMissileAmmo(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    ammo: int

    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return self.Resolved(world.options, ammo=self.ammo, player=world.player)

    class Resolved(Rule.Resolved):
        options: "MetroidFusionOptions"
        ammo: int = 0

        def _evaluate(self, state: CollectionState) -> bool:
            if not state.has("Missile Data", self.player):
                return False
            ammo = EnergyAmmoUtil.ammo_modified_by_options(self.ammo, self.options)
            ammo -= self.options.MissileDataAmmo.value
            ammo -= (self.options.MissileTankAmmo.value * state.count("Missile Tank", self.player))
            return ammo >= 0

@dataclass
class HasPowerBombAmmo(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    ammo: int

    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return self.Resolved(world.options, ammo=self.ammo, player=world.player)

    class Resolved(Rule.Resolved):
        options: "MetroidFusionOptions"
        ammo: int = 0

        def _evaluate(self, state: CollectionState) -> bool:
            if not state.has("Power Bomb Data", self.player):
                return False
            ammo = EnergyAmmoUtil.ammo_modified_by_options(self.ammo, self.options)
            ammo -= self.options.PowerBombDataAmmo.value
            ammo -= (self.options.PowerBombTankAmmo.value * state.count("Power Bomb Tank", self.player))
            return ammo >= 0

@dataclass
class HasEnergy(Rule["MetroidFusionWorld"], game="MetroidFusion"):
    energy: int

    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        return Has("Energy Tank", EnergyAmmoUtil.energy_value_to_tanks(self.energy)).resolve(world)