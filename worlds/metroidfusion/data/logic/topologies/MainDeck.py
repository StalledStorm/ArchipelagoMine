from ..Connection import Connection
from ..FusionLocation import FusionLocation
from ..VariableConnection import VariableConnection

from ..regions.MainDeck import *
from ..regions.Sector1 import Sector1EntranceElevatorBottom, TourianElevatorTop
from ..regions.Sector2 import Sector2EntranceElevatorBottom, OvergrownEntranceTunnel
from ..regions.Sector3 import Sector3EntranceElevatorBottom
from ..regions.Sector4 import Sector4EntranceElevatorBottom
from ..regions.Sector5 import Sector5EntranceElevatorBottom
from ..regions.Sector6 import Sector6EntranceElevatorBottom, AuthorizationCheckpointTunnel

from ..rules.FusionRule import *
from ..rules.FusionTrick import TrickType, TrickDifficulty
from ..FusionEnemy import Enemy
from rule_builder.rules import (True_, False_, And, Or, Has, HasAll, HasAllCounts, HasAny,
                                HasAnyCount, HasFromList, HasFromListUnique, HasGroup, HasGroupUnique,
                                CanReachLocation, CanReachRegion, CanReachEntrance)


# Elevator and Tube Connections
MainElevatorTop.connections = [
    VariableConnection(SectorHubElevatorBottom, True_),
    Connection(MainElevatorCache, True_),
    Connection(MainElevatorAccess, True_)
]

SectorHubElevatorBottom.connections = [
    VariableConnection(MainElevatorTop, True_),
    Connection(SectorHubElevator1Top, Or(
        OpenSectorHubElevators(),
        True_()
    )),
    Connection(SectorHubElevator2Top, Or(
        OpenSectorHubElevators(),
        True_()
    )),
]

SectorHubElevator1Top.connections = [
    VariableConnection(Sector1EntranceElevatorBottom, True_),
    Connection(SectorHubElevatorBottom, Or(
        OpenSectorHubElevators(),
        True_()
    )),
    Connection(SectorHubElevator3Top, Or(
        OpenSectorHubElevators(),
        Has("Level 1 Keycard")
    ))
]

SectorHubElevator3Top.connections = [
    VariableConnection(Sector3EntranceElevatorBottom, True_),
    Connection(SectorHubElevator1Top, Or(
        OpenSectorHubElevators(),
        Has("Level 1 Keycard")
    )),
    Connection(SectorHubElevator5Top, Or(
        OpenSectorHubElevators(),
        Has("Level 2 Keycard")
    ))
]

SectorHubElevator5Top.connections = [
    VariableConnection(Sector5EntranceElevatorBottom, True_),
    Connection(SectorHubElevator3Top, Or(
        OpenSectorHubElevators(),
        Has("Level 2 Keycard")
    ))
]

SectorHubElevator2Top.connections = [
    VariableConnection(Sector2EntranceElevatorBottom, True_),
    Connection(SectorHubElevatorBottom, Or(
        OpenSectorHubElevators(),
        True_()
    )),
    Connection(SectorHubElevator4Top, Or(
        OpenSectorHubElevators(),
        Has("Level 1 Keycard")
    )),
]

SectorHubElevator4Top.connections = [
    VariableConnection(Sector4EntranceElevatorBottom, True_),
    Connection(SectorHubElevator2Top, Or(
        OpenSectorHubElevators(),
        Has("Level 1 Keycard")
    )),
    Connection(SectorHubElevator6Top, Or(
        OpenSectorHubElevators(),
        Has("Level 2 Keycard")
    ))
]

SectorHubElevator6Top.connections = [
    VariableConnection(Sector6EntranceElevatorBottom, True_),
    Connection(SectorHubElevator4Top, Or(
        OpenSectorHubElevators(),
        Has("Level 2 Keycard")
    )),
]

HabitationDeckElevatorBottom.connections = [
    VariableConnection(HabitationDeckElevatorTop, True_),
    Connection(CentralNexus, Has("Level 2 Keycard"))
]

HabitationDeckElevatorTop.connections = [
    VariableConnection(HabitationDeckElevatorBottom, True_),
    Connection(HabitationDeckSave, True_),
    Connection(HabitationDeckEntrance, Has("Level 2 Keycard"))
]

OperationsDeckElevatorBottom.connections = [
    VariableConnection(OperationsDeckElevatorTop, True_),
    Connection(CrewQuartersWest, True_)
]

OperationsDeckElevatorTop.connections = [
    VariableConnection(OperationsDeckElevatorBottom, True_),
    Connection(OperationsDeck, True_)
]

# Not a tube, but connects to another sector
SiloTunnelLeft.connections = [
    Connection(OvergrownEntranceTunnel, True_),
    Connection(SiloTunnelRight, Or(
        CanDestroyBombBlocks(tunnel=True),
        IsLocationCollected("Sector 2 (TRO) -- Nettori Arena")
    ))
]

# Not a tube, but connects to another sector
RestrictedBackDoor.connections = [
    Connection(AuthorizationCheckpointTunnel, And(
        HasAll("Screw Attack", "Morph Ball"),
        Or(
            Has("Space Jump"),
            And(
                Has("Wall Jump Boots"),
                TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
            )
        )
    )),
    Connection(RestrictedSave, Has("Level 4 Keycard"))
]

RestrictedElevatorBottom.connections = [
    VariableConnection(TourianElevatorTop, True_),
    Connection(RestrictedNavigation, Has("Level 4 Keycard"))
]


# Region Connections
DockingBayHangar.connections = [
    Connection(DockingBayAccess, True_)
]

DockingBayAccess.connections = [
    Connection(DockingBayHangar, True_),
    Connection(DockingBayClimb, True_)
]

DockingBayClimb.connections = [
    Connection(DockingBayAccess, True_),
    Connection(SiloEntryTop, Or(
        Has("Level 4 Keycard"),
        CanPowerBomb()
    )),
    Connection(StationEntrance, True_)
]

StationEntrance.connections = [
    Connection(DockingBayClimb, True_),
    Connection(CentralNexus, True_),
    Connection(GenesisSpeedway, Or(
        CanPowerBomb(),
        And(
            # Video demonstration: https://www.youtube.com/watch?v=QpbgjolExgE
            TricksEnabled({(TrickType.SHINESPARK.value, TrickDifficulty.ADVANCED.value)}),
            Has("Speed Booster")
        )
    ))
]

GenesisSpeedway.connections = [
    Connection(StationEntrance, Or(
        CanPowerBomb(),
        Has("Speed Booster")
    ))
]

CentralNexus.connections = [
    Connection(NexusNavigation, True_),
    Connection(HornoadHallway, True_),
    Connection(HabitationDeckElevatorBottom, Has("Level 2 Keycard")),
    Connection(NexusStorage, And(
        CanDamageLargeGeron(),
        Has("Level 2 Keycard")
    )),
    Connection(DarkStairwellSecretTunnel, And(
        CanDestroyBombBlocks(),
        Has("Morph Ball"),
        TricksEnabled({(TrickType.KNOWLEDGE.value, TrickDifficulty.BEGINNER.value)})
    ))
]

NexusStorage.connections = [
    Connection(CentralNexus, Has("Level 2 Keycard"))
]

NexusNavigation.connections = [
    Connection(CentralNexus, True_),
    Connection(DarkStairwell, True_)
]

DarkStairwellSecretTunnel.connections = [
    Connection(CentralNexus, And(
        HasAll("Screw Attack", "Morph Ball"),
        CanDestroyBombBlocks(tunnel=True),
        Or(
            CanBallJump(),
            TricksEnabled({(TrickType.MIDAIR_MORPH.value, TrickDifficulty.ADVANCED.value)})
        )
    )),
    Connection(DarkStairwell, And(
        HasAll("Screw Attack", "Morph Ball"),
        Or(
            CanBallJump(),
            TricksEnabled({(TrickType.MIDAIR_MORPH.value, TrickDifficulty.ADVANCED.value)})
        )
    ))
]

DarkStairwell.connections = [
    Connection(NexusNavigation, True_),
    Connection(DarkStairwellSecretTunnel, TricksEnabled({(TrickType.KNOWLEDGE.value, TrickDifficulty.BEGINNER.value)})),
    Connection(CubbyHole, Has("Morph Ball")),
    Connection(QuarantineJunction, True_),
    Connection(SubZeroContainment, Has("Level 3 Keycard")),
]

CubbyHole.connections = [
    Connection(DarkStairwell, Has("Morph Ball"))
]

SubZeroContainment.connections = [
    Connection(DarkStairwell, Has("Level 3 Keycard"))
]

QuarantineJunction.connections = [
    Connection(DarkStairwell, True_),
    Connection(QuarantineBay, True_),
    Connection(MainElevatorAccess, Or(
        Has("Morph Ball"),
        And(
            # Video demonstration: https://www.youtube.com/watch?v=QcD2-t9UDrg
            Has("Speed Booster"),
            TricksEnabled({(TrickType.SHINESPARK.value, TrickDifficulty.INTERMEDIATE.value)})
        )
    ))
]

MainElevatorAccess.connections = [
    Connection(QuarantineJunction, HasAny("Morph Ball", "Speed Booster")),
    Connection(MainElevatorTop, True_)
]

MainElevatorCache.connections = [
    Connection(MainElevatorTop, True_)
]

HornoadHallway.connections = [
    Connection(CentralNexus, True_),
    Connection(ConcourseSave, True_)
]

ConcourseSave.connections = [
    Connection(HornoadHallway, True_),
    Connection(Concourse, True_)
]

Concourse.connections = [
    Connection(ConcourseSave, True_),
    Connection(ConcourseRecharge, True_),
    Connection(ConcourseVentilation, Has("Morph Ball")),
    Connection(CrewQuartersNavigation, True_)
]

ConcourseVentilation.connections = [
    Connection(Concourse, Has("Morph Ball")),
    Connection(LowerArachnusArena, And(
        Has("Morph Ball"),
        Or(
            CanJumpHigh(),
            And(
                Has("Wall Jump Boots"),
                TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
            )
        )
    ))
]

CrewQuartersNavigation.connections = [
    Connection(Concourse, True_),
    Connection(CrewQuartersWest, True_)
]

CrewQuartersWest.connections = [
    Connection(OperationsDeckElevatorBottom, True_),
    Connection(OperationsVentilationWalkwayLeft, True_),
]

OperationsVentilationWalkwayLeft.connections = [
    Connection(CrewQuartersWest, True_),
    Connection(OperationsVentilationWalkwayRight, Or(
        CanDamageSmallGeron(),
        And(
            # Video demonstration: https://www.youtube.com/watch?v=dWJXG-nGo6A
            HasAll("Speed Booster", "Wall Jump Boots"),
            TricksEnabled({
                (TrickType.SHINESPARK.value, TrickDifficulty.MASTER.value),
                (TrickType.WALL_JUMP.value, TrickDifficulty.ADVANCED.value),
                # Added due to requiring as little wasted movement as possible to maintain the shinespark
                (TrickType.GENERIC_MOVEMENT.value, TrickDifficulty.ADVANCED.value)
            })
        )
    ))
]

OperationsVentilationWalkwayRight.connections = [
    Connection(OperationsVentilationWalkwayLeft, CanDamageSmallGeron()),
    Connection(CrewQuartersEast, True_),
]

CrewQuartersEast.connections = [
    Connection(OperationsVentilationWalkwayRight, True_),
    Connection(CrewQuartersSave, True_),
    Connection(OperationsVentilationBottom, True_),
    Connection(UpperArachnusArena, CanClearEnemy(enemy=Enemy.GADORA))
]

CrewQuartersSave.connections = [
    Connection(CrewQuartersEast, True_)
]

OperationsDeck.connections = [
    Connection(OperationsDeckElevatorTop, True_),
    Connection(OperationsRoom, CanGoal()),
    Connection(OperationsDeckNavigation, True_),
    Connection(OperationsDeckRecharge, True_),
    Connection(OperationsVentilationTop, Has("Missile Data"))
]

OperationsDeckRecharge.connections = [
    Connection(OperationsDeck, True_),
    Connection(OperationsDeckSave, True_)
]

OperationsDeckSave.connections = [
    Connection(OperationsDeckRecharge, True_)
]

OperationsDeckNavigation.connections = [
    Connection(OperationsDeck, True_),
    Connection(OperationsDeckData, True_)
]

OperationsRoom.connections = [
    Connection(OperationsDeck, True_)
]

OperationsVentilationTop.connections = [
    Connection(OperationsDeck, True_),
    Connection(OperationsVentilationBottom, Has("Missile Data"))
]

OperationsVentilationBottom.connections = [
    Connection(CrewQuartersEast, True_),
    Connection(OperationsVentilationStorage, True_)
]

OperationsVentilationStorage.connections = [
    Connection(OperationsVentilationBottom, True_)
]

ArachnusArena.connections = [
    Connection(LowerArachnusArena, Has("Morph Ball"))
]

UpperArachnusArena.connections = [
    Connection(Attic, Has("Missile Data")),
    Connection(LowerArachnusArena, Has("Screw Attack")),
    Connection(ArachnusArena, Or(
        Has("Morph Ball"),
        CanPONR()
    )),
    Connection(CrewQuartersEast, IsLocationCollected("Main Deck -- Arachnus Arena -- Core X"))
]

LowerArachnusArena.connections = [
    Connection(UpperArachnusArena, And(
        Has("Screw Attack"),
        Or(
            CanJumpHigh(),
            And(
                Has("Wall Jump Boots"),
                TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
            ),
            # Video demonstration: https://youtu.be/ycp5oCd5-9I
            TricksEnabled({(TrickType.GENERIC_MOVEMENT.value, TrickDifficulty.EXPERT.value)})
        )
    )),
    Connection(ConcourseVentilation, Has("Morph Ball")),
    Connection(ArachnusArena, Has("Morph Ball"))
]

SiloEntryTop.connections = [
    Connection(DockingBayClimb, Or(
        CanPowerBomb(),
        And(
            Has("Level 4 Keycard"),
            Or(
                CanJumpHigh(),
                And(
                    Has("Wall Jump Boots"),
                    TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
                )
            )
        )
    )),
    Connection(SiloEntryBottom, Has("Morph Ball"))
]

SiloEntryBottom.connections = [
    Connection(SiloEntryTop, Has("Morph Ball")),
    Connection(CentralReactorCoreTop, True_)
]

CentralReactorCoreTop.connections = [
    Connection(SiloEntryBottom, True_),
    Connection(SiloCatwalkLeft, True_),
    Connection(SiloTunnelRight, And(
        HasAll("Space Jump", "Morph Ball"),
    )),
    Connection(CentralReactorCoreBottom, Or(
        CanJumpHigh(),
        And(
            Has("Wall Jump Boots"),
            TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
        ),
        CanPONR()
    ))
]

SiloTunnelRight.connections = [
    Connection(CentralReactorCoreTop, Or(
        CanDestroyBombBlocks(tunnel=True),
        IsLocationCollected("Sector 2 (TRO) -- Nettori Arena")
    ))
]

CentralReactorCoreBottom.connections = [
    Connection(CentralReactorCoreTop, Or(
        CanJumpHigh(),
        And(
            Has("Wall Jump Boots"),
            TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
        ),
        And(
            # Video demonstration: https://www.youtube.com/watch?v=x7CqxW4JyJ4
            Has("Speed Booster"),
            TricksEnabled({(TrickType.SHINESPARK.value, TrickDifficulty.BEGINNER.value)}),
            CanClearEnemy(enemy=Enemy.KIHUNTER_GROUND, enemy_count=3)
        )
    )),
    Connection(SiloSave, True_),
    Connection(SiloCheckpoint, True_),
    Connection(SiloTunnelRight, And(
        # Video demonstration: https://www.youtube.com/watch?v=vVG5YNwzGjw
        HasAll("Speed Booster", "Morph Ball"),
        Or(
            And(
                Has("Hi-Jump"),
                TricksEnabled({(TrickType.SHINESPARK.value, TrickDifficulty.EXPERT.value)})
            ),
            TricksEnabled({(TrickType.SHINESPARK.value, TrickDifficulty.MASTER.value)})
        ),
        Or(
            IsLocationCollected("Sector 2 (TRO) -- Nettori Arena"),
            CanBallJump(),
            TricksEnabled({
                (TrickType.MIDAIR_MORPH.value, TrickDifficulty.ADVANCED.value),
                # Jump, shoot vine block below, then grab ledge
                (TrickType.GENERIC_MOVEMENT.value, TrickDifficulty.INTERMEDIATE.value)
            }),
        ),
        Or(
            # Easy retry to open the shutter backward, or take the long loop through Yakuza's Arena
            Has("Wave Beam"),
            TricksEnabled({(TrickType.SHINESPARK.value, TrickDifficulty.MASTER.value)})
        )
    ))
]

SiloSave.connections = [
    Connection(CentralReactorCoreBottom, True_)
]

SiloCatwalkLeft.connections = [
    Connection(CentralReactorCoreTop, True_),
    Connection(SiloCatwalkRight, Or(
        Has("Space Jump"),
        TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.INTERMEDIATE.value)}),
        And(
            Has("Energy Tank", 2),
            TricksEnabled({(TrickType.DAMAGE_BOOST.value, TrickDifficulty.BEGINNER.value)})
        ),
        CanClearEnemy(enemy=Enemy.ZEBESIAN_GROUND, enemy_count=2)
    ))
]

SiloCatwalkRight.connections = [
    Connection(SiloCatwalkLeft, Or(
        Has("Space Jump"),
        TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.INTERMEDIATE.value)}),
        And(
            Has("Energy Tank", 2),
            TricksEnabled({(TrickType.DAMAGE_BOOST.value, TrickDifficulty.BEGINNER.value)})
        ),
        CanClearEnemy(enemy=Enemy.ZEBESIAN_GROUND, enemy_count=2)
    )),
    Connection(SiloScaffoldingTop, True_)
]

SiloScaffoldingTop.connections = [
    Connection(SiloCatwalkRight, True_),
    Connection(SiloScaffoldingBottom, And(
        Or(
            CanJumpHigh(),
            And(
                Has("Wall Jump Boots"),
                TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.ADVANCED.value)})
            ),
            CanPONR()
        ),
        Or(
            TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.EXPERT.value)}),
            And(
                Has("Energy Tank", 4),
                TricksEnabled({(TrickType.DAMAGE_BOOST.value, TrickDifficulty.INTERMEDIATE.value)})
            ),
            CanClearEnemy(enemy=Enemy.ZEBESIAN_GROUND, enemy_count=3)
        )
    ))
]

SiloScaffoldingBottom.connections = [
    Connection(SiloScaffoldingTop, And(
        Or(
            CanJumpHigh(),
            And(
                Has("Wall Jump Boots"),
                TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.ADVANCED.value)})
            )
        ),
        Or(
            TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.EXPERT.value)}),
            And(
                Has("Energy Tank", 4),
                TricksEnabled({(TrickType.DAMAGE_BOOST.value, TrickDifficulty.INTERMEDIATE.value)})
            ),
            CanClearEnemy(enemy=Enemy.ZEBESIAN_GROUND, enemy_count=3)
        )
    )),
    Connection(YakuzaArenaTop, And(
        Has("Morph Ball"),
        CanClearEnemy(enemy=Enemy.GADORA),
        Or(
            Has("Wave Beam"),
            CanDo15MissileDamage(),
            CanBomb(),
            CanPowerBomb()
        )
    ))
]

YakuzaArenaTop.connections = [
    Connection(AuxiliaryPowerStation, And(
        Has("Space Jump"),
        Or(
            IsLocationCollected("Main Deck -- Yakuza Arena"),
            TricksEnabled({(TrickType.KNOWLEDGE.value, TrickDifficulty.BEGINNER.value)})
        )
    )),
    Connection(YakuzaArenaBottom, Or(
        Has("Space Jump"),
        CanPONR()
    ))
]

YakuzaArenaBottom.connections = [
    Connection(YakuzaArenaTop, Has("Space Jump"))
]

AuxiliaryPowerStation.connections = [
    Connection(YakuzaArenaTop, True_),
    Connection(AuxiliaryNavigation, True_)
]

AuxiliaryNavigation.connections = [
    Connection(AuxiliaryNavigation, True_),
    Connection(SiloCheckpoint, True_)
]

SiloCheckpoint.connections = [
    Connection(CentralReactorCoreBottom, True_),
    Connection(AuxiliaryNavigation, Has("Wave Beam"))
]

RestrictedSave.connections = [
    Connection(RestrictedBackDoor, Has("Level 4 Keycard")),
    Connection(RestrictedCorridor, Has("Level 4 Keycard"))
]

RestrictedCorridor.connections = [
    Connection(RestrictedSave, Has("Level 4 Keycard")),
    Connection(RestrictedAirlockBottom, Has("Level 4 Keycard"))
]

RestrictedAirlockBottom.connections = [
    Connection(RestrictedCorridor, Has("Level 4 Keycard")),
    Connection(RestrictedAirlockTop, Has("Speed Booster"))
]

RestrictedAirlockTop.connections = [
    Connection(RestrictedNavigation, Has("Level 4 Keycard"))
]

RestrictedNavigation.connections = [
    Connection(RestrictedAirlockTop, Has("Level 4 Keycard")),
    Connection(RestrictedElevatorBottom, Has("Level 4 Keycard"))
]

HabitationDeckSave.connections = [
    Connection(HabitationDeckElevatorTop, True_)
]

HabitationDeckEntrance.connections = [
    Connection(HabitationDeckElevatorTop, Has("Level 2 Keycard")),
    Connection(HabitationDeckBottomRight, Has("Level 2 Keycard")),
    Connection(HabitationDeckMiddle, And(
        Has("Level 2 Keycard"),
        Or(
            Has("Space Jump"),
            And(
                Has("Hi-Jump"),
                Or(
                    CanFreezeEnemies(),
                    And(
                        # Video demonstration: https://youtu.be/C56BsRG_eKY
                        CanClearEnemy(enemy=Enemy.FUNE),
                        Has("Wall Jump Boots"),
                        TricksEnabled({
                            (TrickType.JUMP_EXTEND.value, TrickDifficulty.ADVANCED.value),
                            (TrickType.WALL_JUMP.value, TrickDifficulty.ADVANCED.value)
                        })
                    )
                )
            ),
            And(
                # Video demonstration: https://youtu.be/o-DdSO4E3-M
                CanFreezeEnemies(),
                Has("Wall Jump Boots"),
                TricksEnabled({
                    (TrickType.FROZEN_ENEMIES.value, TrickDifficulty.BEGINNER.value),
                    (TrickType.WALL_JUMP.value, TrickDifficulty.INTERMEDIATE.value)
                })
            ),
        )
    )),
    Connection(HabitationDeckTopRight, And(
        Has("Level 2 Keycard"),
        CanReachRegion(HabitationDeckMiddle.name),
        Or(
            CanFreezeEnemies(),
            Has("Space Jump")
        )
    ))
]

HabitationDeckTopRight.connections = [
    Connection(HabitationDeckEntrance, Has("Level 2 Keycard")),
    Connection(HabitationDeckMiddle, True_),
    Connection(HabitationDeckTopLeft, IsLocationCollected("Main Deck -- Habitation Deck -- Animals"))
]

HabitationDeckMiddle.connections = [
    Connection(HabitationDeckEntrance, Has("Level 2 Keycard")),
    Connection(HabitationDeckBottomRight, True_),
    Connection(HabitationDeckBottomMiddle, True_),
    Connection(HabitationDeckBottomLeft, Has("Speed Booster"))
]

HabitationDeckBottomRight.connections = [
    Connection(HabitationDeckEntrance, Has("Level 2 Keycard")),
    Connection(HabitationDeckBottomMiddle, Has("Wave Beam"))
]

HabitationDeckBottomMiddle.connections = [
    Connection(HabitationDeckBottomRight, True_),
    Connection(HabitationDeckBottomLeft, Has("Wave Beam"))
]

HabitationDeckBottomLeft.connections = [
    Connection(HabitationDeckBottomMiddle, True_),
    Connection(HabitationVentilation, True_),
]

HabitationVentilation.connections = [
    Connection(HabitationDeckBottomLeft, True_),
    Connection(HabitationDeckTopLeft, Or(
        Has("Space Jump"),
        CanFreezeEnemies()
    ))
]

HabitationDeckTopLeft.connections = [
    Connection(HabitationVentilation, True_),
    Connection(HabitationDeckTopRight, IsLocationCollected("Main Deck -- Habitation Deck -- Animals"))
]

# Item Locations
ArachnusArena.locations = [
    FusionLocation("Main Deck -- Arachnus Arena -- Core X", True, And(
        CanClearEnemy(enemy=Enemy.ARACHNUS),
        CanClearEnemy(enemy=Enemy.CORE_X_MORPH)
    ))
]

Attic.locations = [
    FusionLocation("Main Deck -- Attic", False, True_)
]

AuxiliaryPowerStation.locations = [
    FusionLocation("Main Deck -- Auxiliary Power Station", True, True_)
]

CubbyHole.locations = [
    FusionLocation("Main Deck -- Cubby Hole", False, True_)
]

GenesisSpeedway.locations = [
    FusionLocation("Main Deck -- Genesis Speedway", False, And(
        CanPowerBomb(),
        CanBallJump()
    ))
]

HabitationDeckTopLeft.locations = [
    FusionLocation("Main Deck -- Habitation Deck -- Animals", True, True_)
]

HabitationDeckBottomMiddle.locations = [
    FusionLocation("Main Deck -- Habitation Deck -- Lower Item", False, True_)
]

MainElevatorCache.locations = [
    FusionLocation("Main Deck -- Main Elevator Cache", False, Has("Speed Booster"))
]

NexusStorage.locations = [
    FusionLocation("Main Deck -- Nexus Storage", False, And(
        CanBallJump(),
        Or(
            CanDestroyBombBlocks(tunnel=True),
            TricksEnabled({(TrickType.GENERIC_MOVEMENT.value, TrickDifficulty.BEGINNER.value)}),
            CanPONR()
        )
    ))
]

OperationsDeckData.locations = [
    FusionLocation("Main Deck -- Operations Deck Data Room", True, True_)
]

OperationsVentilationBottom.locations = [
    FusionLocation("Main Deck -- Operations Ventilation", False, True_)
]

OperationsVentilationStorage.locations = [
    FusionLocation("Main Deck -- Operations Ventilation Storage", False, True_)
]

QuarantineBay.locations = [
    FusionLocation("Main Deck -- Quarantine Bay", False, CanClearEnemy(enemy=Enemy.HORNOAD_QUARANTINE_BAY))
]

RestrictedAirlockBottom.locations = [
    FusionLocation("Main Deck -- Restricted Airlock", False, Has("Speed Booster"))
]

SiloCatwalkRight.locations = [
    FusionLocation("Main Deck -- Silo Catwalk", False, True_)
]

SiloScaffoldingBottom.locations = [
    FusionLocation("Main Deck -- Silo Scaffolding", False, Has("Morph Ball"))
]

StationEntrance.locations = [
    FusionLocation("Main Deck -- Station Entrance", False, CanPowerBomb())
]

SubZeroContainment.locations = [
    FusionLocation("Main Deck -- Sub-Zero Containment", False, Or(
        Has("Varia Suit"),
        And(
            TricksEnabled({(TrickType.DAMAGE_RUN.value, TrickDifficulty.INTERMEDIATE.value)}),
            Has("Energy Tank")
        )
    ))
]

UpperArachnusArena.locations = [
    FusionLocation("Main Deck -- Arachnus Arena -- Upper Item", False, True_)
]
YakuzaArenaBottom.locations = [
    FusionLocation("Main Deck -- Yakuza Arena", True, And(
        CanClearEnemy(enemy=Enemy.YAKUZA),
        CanClearEnemy(enemy=Enemy.CORE_X_SPACE),
        Or(
            TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.MASTER.value)}),
            And(
                Has("Energy Tank", 5),
                HasAll("Charge Beam", "Wide Beam", "Super Missile", "Morph Ball")
            ),
            And(
                Has("Energy Tank", 4),
                TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.BEGINNER.value)}),
                HasAll("Charge Beam", "Wide Beam", "Ice Missile", "Morph Ball")
            ),
            And(
                Has("Energy Tank", 3),
                TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.INTERMEDIATE.value)}),
                HasAll("Charge Beam", "Diffusion Missile")
            ),
            And(
                Has("Energy Tank", 2),
                TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.ADVANCED.value)}),
                Has("Charge Beam")
            ),
            And(
                Has("Energy Tank"),
                TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.EXPERT.value)})
            )
        )
    ))
]
