from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....MFOptions import MetroidFusionOptions


class TrickDifficulty(Enum):
    """
    * VANILLA ``0`` - Intended developer routes to pick up every item in an unmodified game
    * BEGINNER ``1`` - Tricks beginning to step outside the boundaries of the intended game mechanics
    * INTERMEDIATE ``2`` - Tricks commonly used in randomization and most speedruns
    * ADVANCED ``3`` - Tricks for experienced players continuing to think outside the box
    * EXPERT ``4`` - Tricks performed by seasoned game veterans or competing speedrunners
    * MASTER ``5`` - The upper echelon of speedrunning technical maneuvers
    * THEORETICAL ``6`` - Reserved for any tricks yet to be performed by humans at full game speed
    """
    VANILLA = 0
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    EXPERT = 4
    MASTER = 5
    THEORETICAL = 6


class TrickType(Enum):
    UNDEFINED = -1
    GENERIC_MOVEMENT = 0
    KNOWLEDGE = 1
    COMBAT = 2
    WALL_JUMP = 3
    FROZEN_ENEMIES = 4
    SHINESPARK = 5
    MIDAIR_MORPH = 6
    DAMAGE_RUN = 7
    UNDERWATER_WALL_JUMP = 8
    JUMP_BOMB_JUMP = 9
    JUMP_EXTEND = 10
    DAMAGE_BOOST = 11


class Trick:
    def __init__(self,
                 trick_type: TrickType,
                 difficulty: TrickDifficulty):
        self.trick_type = trick_type
        self.difficulty = difficulty

    def __str__(self):
        return (self.difficulty.name
                + " "
                + self.trick_type.name).replace("_", " ").title()

    def can_perform_trick(self, options: "MetroidFusionOptions") -> bool:
        match self.trick_type:
            case TrickType.GENERIC_MOVEMENT:
                return options.MovementTrickDifficulty.value > self.difficulty.value
            case TrickType.KNOWLEDGE:
                return options.KnowledgeDifficulty.value > self.difficulty.value
            case TrickType.COMBAT:
                return options.CombatDifficulty.value > self.difficulty.value
            case TrickType.WALL_JUMP:
                return options.WallJumpTrickDifficulty.value > self.difficulty.value
            case TrickType.FROZEN_ENEMIES:
                return options.FrozenEnemiesTrickDifficulty.value > self.difficulty.value
            case TrickType.SHINESPARK:
                return options.ShinesparkTrickDifficulty.value > self.difficulty.value
            case TrickType.MIDAIR_MORPH:
                return options.MidairMorphTrickDifficulty.value > self.difficulty.value
            case TrickType.DAMAGE_RUN:
                return options.DamageRunTrickDifficulty.value > self.difficulty.value
            case TrickType.UNDERWATER_WALL_JUMP:
                return options.UnderwaterWallJumpTrickDifficulty.value > self.difficulty.value
            case TrickType.JUMP_BOMB_JUMP:
                return options.JumpBombJumpTrickDifficulty.value > self.difficulty.value
            case TrickType.JUMP_EXTEND:
                return options.JumpExtendTrickDifficulty.value > self.difficulty.value
            case TrickType.DAMAGE_BOOST:
                return options.DamageBoostTrickDifficulty.value > self.difficulty.value
            case _:
                return False