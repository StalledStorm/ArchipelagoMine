from dataclasses import dataclass

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from FusionTrick import Trick
from rule_builder.rules import (True_, False_, And, Or, Rule, Has, HasAll, HasAllCounts, HasAny,
                                HasAnyCount, HasFromList, HasFromListUnique, HasGroup, HasGroupUnique,
                                CanReachLocation, CanReachRegion, CanReachEntrance)

@dataclass
class CanGoal(Rule["MetroidFusionWorld"], game="Metroid Fusion"):

    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        options = world.options
        min_req = (HasAllCounts({
                        "Infant Metroid": options.InfantMetroidsRequired.value,
                        "Energy Tank": 3
                    }) & HasAll("Charge Beam", "Missile Data")
                    & CanReachRegion("Operations Room"))
        advanced_goal = (HasAll("Plasma Beam", "Varia Suit")
                         & Has("Energy Tank", 6))
        beginner_goal = (HasAll("Wide Beam", "Super Missile")
                         & Has("Energy Tank", 10))

        match options.CombatDifficulty.value:
            case 2:
                return min_req.resolve(world)
            case 1:
                return (min_req & advanced_goal).resolve(world)
            case _:
                return (min_req & advanced_goal & beginner_goal).resolve(world)

@dataclass
class TrickEnabled(Rule["MetroidFusionWorld"], game="Metroid Fusion"):
    trick: Trick
    """The trick type and difficulty to match against"""

    def _instantiate(self, world: "MetroidFusionWorld") -> Rule.Resolved:
        if self.trick.can_perform_trick(world.options):
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