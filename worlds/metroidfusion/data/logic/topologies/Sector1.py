from ..Connection import Connection
from ..VariableConnection import VariableConnection
from ..FusionLocation import FusionLocation
from ..FusionRegion import connection_to

from ..regions.MainDeck import SectorHubElevator1Top, RestrictedElevatorBottom
from ..regions.Sector1 import *
from ..regions.Sector2 import Sector2TubeLeft
from ..regions.Sector3 import Sector3TubeRight

from ..rules.FusionRule import *
from ..rules.FusionTrick import TrickType, TrickDifficulty
from ..FusionEnemy import Enemy
from rule_builder.rules import (True_, False_, And, Or, Has, HasAll, HasAllCounts, HasAny,
                                HasAnyCount, HasFromList, HasFromListUnique, HasGroup, HasGroupUnique,
                                CanReachLocation, CanReachRegion, CanReachEntrance)


# Elevator and Tube Connections
Sector1EntranceElevatorBottom.connections = [
    VariableConnection(SectorHubElevator1Top, True_),
    Connection(EntranceNavigation, True_)
]

TourianElevatorTop.connections = [
    VariableConnection(RestrictedElevatorBottom, True_),
    Connection(RipperMazeLeft, True_)
]

Sector1TubeLeft.connections = [
    VariableConnection(Sector3TubeRight, True_),
    Connection(LavaLakeAnnex, HasAll("Screw Attack", "Morph Ball"))
]

Sector1TubeRight.connections = [
    VariableConnection(Sector2TubeLeft, True_),
    Connection(AntechamberTop, CanBallJump())
]

# Region Connections

EntranceNavigation.connections = [
    Connection(Sector1EntranceElevatorBottom, True_),
    Connection(EntranceSave, True_)
]

EntranceSave.connections = [
    Connection(EntranceNavigation, True_),
    Connection(EntranceRecharge, True_)
]

EntranceRecharge.connections = [
    Connection(EntranceSave, True_),
    Connection(EntranceLobby, True_)
]

EntranceLobby.connections = [
    Connection(EntranceRecharge, True_),
    Connection(AntechamberBottom, Has("Level 2 Keycard")),
    Connection(LavaLakeAnnex, Has("Level 1 Keycard")),
    Connection(YamebaCorridor, True_)
]

AntechamberBottom.connections = [
    Connection(EntranceLobby, Has("Level 2 Keycard")),
    Connection(AntechamberTop, And(
        Has("Screw Attack"),
        CanJumpHigh()
    ))
]

AntechamberTop.connections = [
    Connection(AntechamberBottom, And(
        Has("Screw Attack"),
        Or(
            CanJumpHigh(),
            CanPONR()
        )
    )),
    Connection(Sector1TubeRight, Has("Morph Ball"))
]

LavaLakeAnnex.connections = [
    Connection(EntranceLobby, Has("Level 1 Keycard")),
    Connection(Sector1TubeLeft, HasAll("Screw Attack", "Morph Ball")),
    Connection(LavaLake, And(
        Has("Level 2 Keycard"),
        Or(
            CanLavaDive(),
            And(
                Has("Energy Tank"),
                HasAny("Varia Suit", "Gravity Suit"),
                TricksEnabled({(TrickType.DAMAGE_RUN.value, TrickDifficulty.BEGINNER.value)})
            ),
            And(
                # Video demonstration: https://youtu.be/jfuH3Epvxh8
                #              Part 2: https://youtu.be/RF2_8Y0PaVQ
                Has("Energy Tank", 2),
                TricksEnabled({(TrickType.DAMAGE_RUN.value, TrickDifficulty.INTERMEDIATE.value)}),
            )
        )
    ))
]

LavaLake.connections = [
    Connection(LavaLakeAnnex, And(
        Has("Level 2 Keycard"),
        Or(
            CanLavaDive(),
            And(
                Has("Energy Tank"),
                HasAny("Varia Suit", "Gravity Suit"),
                TricksEnabled({(TrickType.DAMAGE_RUN.value, TrickDifficulty.BEGINNER.value)})
            ),
            And(
                # Video demonstration: https://youtu.be/VFbTQoMI0uA
                #              Part 2: https://youtu.be/pu2I2jaMrjI
                Has("Energy Tank", 2),
                TricksEnabled({(TrickType.DAMAGE_RUN.value, TrickDifficulty.INTERMEDIATE.value)})
            )
        )
    )),
    Connection(ZebesianZig, True_)
]

YamebaCorridor.connections = [
    Connection(EntranceLobby, Or(
        CanDamageSmallGeron(),
        And(
            # Charge spark in Moto Motorway. Maintain into Atmospheric Stabilizer Northeast,
            # and carry through Atmospheric Stabilizer Northwest.
            # Video demonstration: https://youtu.be/aq0PQxbFJQk
            IsLocationCollected("Sector 1 (SRX) -- Atmospheric Stabilizer Northeast"),
            CanDamageSmallGeron(speed_booster_override=True),
            TricksEnabled({
                (TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value),
                (TrickType.SHINESPARK.value, TrickDifficulty.MASTER.value)
            }),
            Or(
                And(
                    TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.ADVANCED.value)}),
                    HasAny("Plasma Beam", "Charge Beam")
                ),
                And(
                    TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.INTERMEDIATE.value)}),
                    HasAny("Wave Beam", "Wide Beam")
                )
            )
        )
    )),
    Connection(AtmosphericStabilizerNorthwest, Or(
        CanDamageSmallGeron(),
        And(
            CanDamageSmallGeron(speed_booster_override=True),
            TricksEnabled({(TrickType.KNOWLEDGE.value, TrickDifficulty.BEGINNER.value)})
        )
    ))
]

AtmosphericStabilizerNorthwest.connections = [
    Connection(YamebaCorridor, Or(
        CanDamageStabilizer(),
        And(
            # Charge spark in Moto Motorway. Maintain into Atmospheric Stabilizer Northeast,
            # and carry through Atmospheric Stabilizer Northwest.
            # Video demonstration: https://youtu.be/aq0PQxbFJQk
            IsLocationCollected("Sector 1 (SRX) -- Atmospheric Stabilizer Northeast"),
            CanDamageStabilizer(speed_booster_override=True),
            TricksEnabled({
                (TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value),
                (TrickType.SHINESPARK.value, TrickDifficulty.MASTER.value)
            }),
            Or(
                And(
                    TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.ADVANCED.value)}),
                    HasAny("Plasma Beam", "Charge Beam")
                ),
                And(
                    TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.INTERMEDIATE.value)}),
                    HasAny("Wave Beam", "Wide Beam")
                )
            )
        )
    )),
    Connection(HornoadHole, Or(
        CanDamageStabilizer(),
        And(
            # Can Destroy via Shinespark
            CanDamageStabilizer(speed_booster_override=True),
            TricksEnabled({
                (TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value),
                (TrickType.SHINESPARK.value, TrickDifficulty.ADVANCED.value)
            })
        )
    ))
]

HornoadHole.connections = [
    Connection(AtmosphericStabilizerNorthwest, Or(
        CanDamageStabilizer(),
        And(
            # Charge spark in Moto Motorway. Maintain into Atmospheric Stabilizer Northeast,
            # and carry through Atmospheric Stabilizer Northwest.
            # Video demonstration: https://youtu.be/aq0PQxbFJQk
            IsLocationCollected("Sector 1 (SRX) -- Atmospheric Stabilizer Northeast"),
            CanDamageStabilizer(speed_booster_override=True),
            TricksEnabled({
                (TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value),
                (TrickType.SHINESPARK.value, TrickDifficulty.MASTER.value)
            }),
            Or(
                And(
                    TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.ADVANCED.value)}),
                    HasAny("Plasma Beam", "Charge Beam")
                ),
                And(
                    TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.INTERMEDIATE.value)}),
                    HasAny("Wave Beam", "Wide Beam")
                )
            )
        )
    )),
    Connection(TwinJunctionsWest, True_)
]

TwinJunctionsWest.connections = [
    Connection(HornoadHole, True_),
    Connection(TwinJunctionsEast, True_),
    Connection(MotoMotorway, True_),
    Connection(AtmosphericStabilizerNortheast, Or(
        connection_to(AtmosphericStabilizerNortheast, TwinJunctionsWest),
        CanPONR()
    ))
]

AtmosphericStabilizerNortheast.connections = [
    Connection(TwinJunctionsWest, Or(
        CanDamageStabilizer(),
        And(
            # Video demonstration: https://youtu.be/I9YH_s989sQ
            CanDamageStabilizer(speed_booster_override=True),
            TricksEnabled({
                (TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value),
                (TrickType.SHINESPARK.value, TrickDifficulty.EXPERT.value)
            }),
        )
    ))
]

MotoMotorway.connections = [
    Connection(TwinJunctionsWest, True_),
    Connection(ZebesianZig, True_)
]

ZebesianZig.connections = [
    Connection(LavaLake, True_),
    Connection(SciserPuddle, Or(
        CanClearEnemy(enemy=Enemy.ZEBESIAN_WALL, enemy_count=8),
        CanFreezeEnemies(8),
        # Pacifist
        # Video demonstration: https://youtu.be/u40B3GpSIsA
        TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.INTERMEDIATE.value)}),
    ))
]

SciserPuddle.connections = [
    Connection(ZebesianZig, True_),
    Connection(AtmosphericStabilizerSouthwest, True_)
]

AtmosphericStabilizerSouthwest.connections = [
    Connection(SciserPuddle, Or(
        CanDamageStabilizer(),
        And(
            CanDamageStabilizer(speed_booster_override=True),
            TricksEnabled({
                (TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value),
                (TrickType.SHINESPARK.value, TrickDifficulty.ADVANCED.value)
            }),
            # Check if you can pass through and clear Atmospheric Stabilizer Northwest
            CanReachRegion(ZebesianZag.name)
        )
    )),
    Connection(MotoManor, CanDamageStabilizer())
]

MotoManor.connections = [
    Connection(AtmosphericStabilizerSouthwest, True_),
    Connection(TourianTrapdoorTop, True_)
]

TourianTrapdoorTop.connections = [
    Connection(MotoManor, True_),
    Connection(TourianTrapdoorBottom, And(
        Has("Screw Attack"),
        Or(
            CanPONR(),
            connection_to(TourianTrapdoorBottom, TourianTrapdoorTop)
        )
    )),
    Connection(AtmosphericStabilizerSoutheast, True_)
]

AtmosphericStabilizerSoutheast.connections = [
    Connection(TourianTrapdoorTop, CanLeaveStabilizerSoutheast()),
    Connection(StabilizerStorage, CanLeaveStabilizerSoutheast()),
    Connection(ZebesianZag, CanLeaveStabilizerSoutheast())
]

StabilizerStorage.connections = [
    Connection(AtmosphericStabilizerSoutheast, True_)
]

ZebesianZag.connections = [
    Connection(AtmosphericStabilizerSoutheast, True_),
    Connection(TwinJunctionsEastShutter, Or(
        HasAny("Charge Beam", "Missile Data"),
        CanFreezeEnemies(5),
        CanPowerBomb(),
        And(
            Has("Screw Attack"),
            Or(
                Has("Space Jump"),
                # Requires spin cancel to prevent destroying the platforms.
                # Video demonstration: https://youtu.be/rsQZgb4xF6Y
                TricksEnabled({(TrickType.GENERIC_MOVEMENT.value, TrickDifficulty.BEGINNER.value)})
            )
        ),
        # Pacifist
        # Video demonstration: https://youtu.be/Lh9D7Ye3rw8
        TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.INTERMEDIATE.value)}),
        And(
            # Video demonstration: https://youtu.be/_PmmHN9YvKw
            Has("Speed Booster"),
            # Set to require a trick to not confuse trickless players
            TricksEnabled({(TrickType.SHINESPARK.value, TrickDifficulty.BEGINNER.value)})
        ),
        And(
            # Video demonstration: https://youtu.be/cqHI8tNmNVw
            HasEnergy(170),
            TricksEnabled({
                (TrickType.DAMAGE_BOOST.value, TrickDifficulty.INTERMEDIATE.value),
                (TrickType.GENERIC_MOVEMENT.value, TrickDifficulty.BEGINNER.value)
            })
        )
    ))
]

TwinJunctionsEastShutter.connections = [
    Connection(ZebesianZag, Has("Wave Beam")),
    Connection(SciserPlayground, True_)
]

SciserPlayground.connections = [
    Connection(TwinJunctionsEastShutter, True_),
    Connection(ChargeCoreLowerAccess, Has("Morph Ball"))
]

ChargeCoreLowerAccess.connections = [
    Connection(HornoadHousing, Or(
        Has("Morph Ball"),
        CanDestroyBombBlocks()
    )),
    Connection(WateringHole, Or(
        CanDestroyBombBlocks(),
        And(
            Has("Speed Booster"),
            TricksEnabled({(TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value)})
        )
    )),
    Connection(ChargeCoreArena, CanClearEnemy(enemy=Enemy.GADORA))
]

WateringHole.connections = [
    Connection(ChargeCoreLowerAccess, True_)
]

HornoadHousing.connections = [
    Connection(ChargeCoreLowerAccess, True_),
    Connection(CentralSave, True_)
]

CentralSave.connections = [
    Connection(HornoadHousing, True_)
]

ChargeCoreArena.connections = [
    Connection(ChargeCoreLowerAccess, IsLocationCollected("Sector 1 (SRX) -- Charge Core Arena -- Core X")),
    Connection(ChargeCoreUpperAccess, IsLocationCollected("Sector 1 (SRX) -- Charge Core Arena -- Core X"))
]

ChargeCoreUpperAccess.connections = [
    Connection(ChargeCoreArena, True_),
    Connection(AtmosphericStabilizerCentral, True_),
    Connection(CrabRave, HasAll("Morph Ball", "Missile Data"))
]

AtmosphericStabilizerCentral.connections = [
    Connection(ChargeCoreUpperAccess, Or(
        And(
            # Vanilla
            CanDamageStabilizer(),
            Has("Morph Ball")
        ),
        And(
            # Charge Beam flare only
            # Video demonstration: https://youtu.be/EYzjWUclb_0
            Has("Charge Beam"),
            TricksEnabled({(TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value)})
        ),
        And(
            # Damage boost into the Geron to get past the shielding
            # Video demonstration: https://youtu.be/Mp9YwFW3dLM
            HasAny("Charge Beam", "Missile Data"),
            TricksEnabled({
                (TrickType.DAMAGE_BOOST.value, TrickDifficulty.INTERMEDIATE.value),
                (TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value)
            })
        ),
        And(
            # Shinespark kill from Twin Junction East
            # Video demonstration: https://youtu.be/2biI4SB_wAs
            HasAll("Speed Booster", "Wave Beam"),
            TricksEnabled({
                (TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value),
                (TrickType.SHINESPARK.value, TrickDifficulty.INTERMEDIATE.value)
            })
        )
    )),
    Connection(TwinJunctionsWestShutter, Or(
        And(
            # Vanilla
            CanDamageStabilizer(),
            Has("Morph Ball")
        ),
        And(
            # Charge Beam flare only
            # Video demonstration: https://youtu.be/EYzjWUclb_0
            Has("Charge Beam"),
            TricksEnabled({(TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value)})
        ),
        And(
            # Damage boost into the Geron to get past the shielding
            # Video demonstration: https://youtu.be/Mp9YwFW3dLM
            HasAny("Charge Beam", "Missile Data"),
            TricksEnabled({
                (TrickType.DAMAGE_BOOST.value, TrickDifficulty.INTERMEDIATE.value),
                (TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value)
            })
        )
    ))
]

TwinJunctionsWestShutter.connections = [
    Connection(AtmosphericStabilizerCentral, Has("Wave Beam")),
    Connection(TwinJunctionsEast, True_)
]

TwinJunctionsEast.connections = [
    Connection(TwinJunctionsWestShutter, True_),
    Connection(TwinJunctionsWest, True_),
    Connection(TwinJunctionsSave, True_)
]

TwinJunctionsSave.connections = [
    Connection(TwinJunctionsEast, True_),
    Connection(WallJumpTutorial, Or(
        CanBallJump(),
        And(
            Has("Morph Ball"),
            TricksEnabled({(TrickType.MIDAIR_MORPH.value, TrickDifficulty.BEGINNER.value)})
        )
    ))
]

WallJumpTutorial.connections = [
    Connection(TwinJunctionsSave, Has("Morph Ball"))
]

TourianTrapdoorBottom.connections = [
    Connection(TourianTrapdoorTop, And(
        Has("Screw Attack"),
        Or(
            Has("Space Jump"),
            And(
                CanFreezeEnemies(4, 10, 20),
                Or(
                    And(
                        # No Jump Upgrades climb with Wall Jump
                        # Video demonstration: https://youtu.be/rpQG_ZFJ2Wg
                        Has("Wall Jump Boots"),
                        TricksEnabled({
                            (TrickType.FROZEN_ENEMIES.value, TrickDifficulty.MASTER.value),
                            (TrickType.WALL_JUMP.value, TrickDifficulty.INTERMEDIATE.value)
                        }),
                    ),
                    And(
                        Has("Hi-Jump"),
                        Or(
                            And(
                                # Hi-Jump + Wall Jump climb
                                # Video demonstration: https://youtu.be/Hfmrj3rurOY
                                Has("Wall Jump Boots"),
                                TricksEnabled({
                                    (TrickType.FROZEN_ENEMIES.value, TrickDifficulty.INTERMEDIATE.value),
                                    (TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)
                                })
                            ),
                            # No Wall Jump with Hi-Jump
                            # Video demonstration: https://youtu.be/T_aded4xYeU
                            TricksEnabled({(TrickType.FROZEN_ENEMIES.value, TrickDifficulty.ADVANCED.value)})
                        )
                    )
                )
            )
        )
    )),
    Connection(RipperSauna, True_)
]

RipperSauna.connections = [
    Connection(TourianTrapdoorBottom, And(
        HasAll("Morph Ball", "Screw Attack", "Wave Beam"),
        Or(
            Has("Space Jump"),
            And(
                # Video demonstration: https://youtu.be/BPF8pppB7po
                HasEnergy(130),
                TricksEnabled({(TrickType.DAMAGE_RUN.value, TrickDifficulty.INTERMEDIATE.value)})
            ),
            And(
                # Video demonstration: https://youtu.be/rjzsSJlkeKw
                CanFreezeEnemies(5),
                TricksEnabled({(TrickType.FROZEN_ENEMIES.value, TrickDifficulty.ADVANCED.value)})
            )
        )
    )),
    Connection(TourianTower, And(
        HasAll("Morph Ball", "Screw Attack"),
        Or(
            CanBallJump(),
            TricksEnabled({(TrickType.MIDAIR_MORPH.value, TrickDifficulty.INTERMEDIATE.value)})
        ),
        Or(
            Has("Space Jump"),
            And(
                # Video demonstration: https://youtu.be/BPF8pppB7po
                HasEnergy(90),
                TricksEnabled({(TrickType.DAMAGE_RUN.value, TrickDifficulty.INTERMEDIATE.value)})
            ),
            And(
                # Video demonstration: https://youtu.be/rjzsSJlkeKw
                CanFreezeEnemies(5),
                TricksEnabled({(TrickType.FROZEN_ENEMIES.value, TrickDifficulty.ADVANCED.value)})
            )
        ),
        Or(
            Has("Wave Beam"),
            CanPONR()
        )
    ))
]

TourianTower.connections = [
    Connection(RipperSauna, HasAll("Morph Ball", "Screw Attack")),
    Connection(TourianCheckpoint, And(
        HasAll("Morph Ball", "Screw Attack"),
        Or(
            Has("Space Jump"),
            And(
                Has("Wall Jump Boots"),
                TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
            )
        )
    ))
]

TourianCheckpoint.connections = [
    Connection(TourianTower, Has("Wave Beam")),
    Connection(TourianEasternHubCheckpoint, Or(
        Has("Wave Beam"),
        CanPONR()
    ))
]

TourianEasternHubCheckpoint.connections = [
    Connection(TourianCheckpoint, True_),
    Connection(TourianEasternHubLadder, And(
        HasAll("Missile Data", "Morph Ball"),
        HasMissileAmmo(3)
    )),
    Connection(TourianEasternHub, And(
        HasAll("Missile Data", "Morph Ball"),
        HasMissileAmmo(3)
    ))
]

TourianEasternHubLadder.connections = [
    Connection(TourianEasternHubCheckpoint, And(
        HasAll("Missile Data", "Morph Ball"),
        HasMissileAmmo(3)
    )),
    Connection(GoldPirateCrossing, CanDestroyBombBlocks(chain=True)),
    Connection(TourianEasternHub, True_)
]

GoldPirateCrossing.connections = [
    Connection(TourianEasternHubLadder, CanDestroyBombBlocks(chain=True)),
    Connection(TourianWesternHub, And(
        CanDestroyBombBlocks(chain=True),
        Or(
            Has("Wave Beam"),
            And(
                CanPowerBomb(),
                HasPowerBombAmmo(2)
            )
        ),
        CanClearEnemy(enemy=Enemy.ZEBESIAN_GOLD, enemy_count=2)
    ))
]

TourianWesternHub.connections = [
    Connection(GoldPirateCrossing, Or(
        Has("Space Jump"),
        And(
            Has("Wall Jump Boots"),
            TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
        )
    )),
    Connection(TourianSaveWest, True_),
    Connection(GenesisHabitation, True_),
    Connection(NeoRidleyArenaAccess, True_)
]

TourianSaveWest.connections = [
    Connection(TourianWesternHub, True_)
]

GenesisHabitation.connections = [
    Connection(TourianWesternHub, True_)
]

NeoRidleyArenaAccess.connections = [
    Connection(TourianWesternHub, Or(
        Has("Screw Attack"),
        CanFreezeEnemies(6),
        TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.ADVANCED.value)}),
        And(
            HasEnergy(150),
            TricksEnabled({(TrickType.DAMAGE_BOOST.value, TrickDifficulty.BEGINNER.value)})
        )
    )),
    Connection(NeoRidleyArena, And(
        CanClearEnemy(enemy=Enemy.GADORA),
        Or(
            Has("Screw Attack"),
            CanFreezeEnemies(6),
            TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.ADVANCED.value)}),
            And(
                HasEnergy(150),
                TricksEnabled({(TrickType.DAMAGE_BOOST.value, TrickDifficulty.BEGINNER.value)})
            )
        )
    ))
]

NeoRidleyArena.connections = [
    Connection(NeoRidleyArenaAccess, And(
        IsLocationCollected("Sector 1 (SRX) -- Neo-Ridley Arena"),
        Or(
            Has("Space Jump"),
            And(
                # Woe be the man who enables max tricks
                # Video demonstration: https://youtu.be/3rfQghnP54o
                CanBomb(),
                Has("Wall Jump Boots"),
                TricksEnabled({
                    (TrickType.WALL_JUMP.value, TrickDifficulty.MASTER.value),
                    (TrickType.JUMP_EXTEND.value, TrickDifficulty.MASTER.value),
                    (TrickType.JUMP_BOMB_JUMP.value, TrickDifficulty.MASTER.value)
                })
            )
        )
    ))
]

TourianEasternHub.connections = [
    Connection(TourianSaveEast, True_),
    Connection(YamebaPool, True_),
    Connection(Animorphs, Or(
        CanJumpHigh(),
        CanPONR()
    )),
    Connection(TourianEasternHubLadder, Or(
        Has("Space Jump"),
        And(
            Has("Wall Jump Boots"),
            TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.INTERMEDIATE.value)})
        ),
        And(
            HasAll("Hi-Jump", "Wall Jump Boots"),
            TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
        )
    ))
]

TourianSaveEast.connections = [
    Connection(TourianEasternHub, True_)
]

Animorphs.connections = [
    Connection(TourianEasternHub, Or(
        Has("Space Jump"),
        And(
            HasAll("Hi-Jump", "Wall Jump Boots"),
            TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
        )
    )),
    Connection(AnimorphsCache, And(
        Or(
            # Kill the snail
            And(
                Has("Charge Beam"),
                Or(
                    Has("Wave Beam"),
                    # Charge flare on corner
                    # Video demonstration: https://youtu.be/6Stz6EU-Zrc
                    TricksEnabled({(TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value)})
                )
            ),
            And(
                CanPowerBomb(),
                HasPowerBombAmmo(2)
            )
        ),
        CanClearEnemy(enemy=Enemy.GERUBUS),
        CanClearEnemy(enemy=Enemy.ZEBESIAN_GOLD)
    ))
]

AnimorphsCache.connections = [
    Connection(Animorphs, True_)
]

YamebaPool.connections = [
    Connection(TourianEasternHub, True_),
    Connection(RipperMazeRight, True_)
]

RipperMazeRight.connections = [
    Connection(YamebaPool, True_),
    Connection(RipperMazeLeft, And(
        Or(
            # Pass Rippers
            HasAny("Morph Ball", "Screw Attack"),
            And(
                # Glitch through frozen Ripper
                # Video demonstration: https://youtu.be/6TSAshOOI-Q
                CanFreezeEnemies(2),
                TricksEnabled({(TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value)})
            ),
            And(
                HasEnergy(50),
                TricksEnabled({(TrickType.DAMAGE_BOOST.value, TrickDifficulty.BEGINNER.value)})
            ),
            # Dodge
            # Video demonstration: https://youtu.be/pmg_d94lKUQ
            TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.INTERMEDIATE.value)})
        ),
        Or(
            # Pass Gerubus
            CanClearEnemy(enemy=Enemy.GERUBUS, enemy_count=2),
            And(
                # Dodge
                # Video demonstration: https://youtu.be/mpN1LGf4lmU
                Has("Morph Ball"),
                TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.BEGINNER.value)})
            ),
            And(
                HasEnergy(101),
                TricksEnabled({(TrickType.DAMAGE_BOOST.value, TrickDifficulty.BEGINNER.value)})
            )
        ),
        Or(
            # Pass triple Rippers
            And(
                Has("Screw Attack"),
                Or(
                    Has("Space Jump"),
                    And(
                        Has("Wall Jump Boots"),
                        TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
                    )
                )
            ),
            And(
                # Video demonstration: https://youtu.be/1-vVlBiw0og
                CanFreezeEnemies(3),
                Or(
                    Has("Space Jump"),
                    And(
                        Has("Wall Jump Boots"),
                        TricksEnabled({
                            (TrickType.WALL_JUMP.value, TrickDifficulty.INTERMEDIATE.value),
                            (TrickType.FROZEN_ENEMIES.value, TrickDifficulty.INTERMEDIATE.value)
                        })
                    )
                )
            ),
            And(
                # Damage Boost
                # Video demonstration: https://youtu.be/uyPIOm9rYyQ
                HasEnergy(101),
                TricksEnabled({(TrickType.DAMAGE_BOOST.value, TrickDifficulty.INTERMEDIATE.value)}),
                Or(
                    Has("Space Jump"),
                    And(
                        HasAll("Hi-Jump", "Wall Jump Boots"),
                        TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.INTERMEDIATE.value)})
                    )
                )
            ),
            And(
                # Damage Boost, Wall Jump only
                # Video demonstration: https://youtu.be/twrTcGHR8SM
                HasEnergy(201),
                Has("Wall Jump Boots"),
                TricksEnabled({
                    (TrickType.WALL_JUMP.value, TrickDifficulty.ADVANCED.value),
                    (TrickType.DAMAGE_BOOST.value, TrickDifficulty.ADVANCED.value)
                })
            ),
            And(
                # Space Jump No-Hit
                # Video demonstration: https://youtu.be/M2fDkXlM8LU
                Has("Space Jump"),
                TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.EXPERT.value)})
            )
        )
    ))
]

RipperMazeLeft.connections = [
    Connection(TourianElevatorTop, True_),
    Connection(RipperMazeRight, And(
        Or(
            CanJumpHigh(),
            And(
                Has("Wall Jump Boots"),
                TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
            )
        ),
        Or(
            # Pass triple Rippers
            Has("Screw Attack"),
            CanFreezeEnemies(3),
            # Video demonstration: https://youtu.be/66mAKLiF8z4
            TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.ADVANCED.value)}),
            And(
                HasEnergy(50),
                TricksEnabled({(TrickType.DAMAGE_BOOST.value, TrickDifficulty.BEGINNER.value)})
            )
        ),
        Or(
            # Pass Gerubus
            CanClearEnemy(enemy=Enemy.GERUBUS),
            And(
                # Dodge
                # Video demonstration: https://youtu.be/mpN1LGf4lmU
                Has("Morph Ball"),
                TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.BEGINNER.value)})
            ),
            And(
                HasEnergy(101),
                TricksEnabled({(TrickType.DAMAGE_BOOST.value, TrickDifficulty.BEGINNER.value)})
            )
        ),
        Or(
            # Pass Rippers
            HasAny("Morph Ball", "Screw Attack"),
            And(
                # Glitch through frozen Ripper
                # Video demonstration: https://youtu.be/6TSAshOOI-Q
                CanFreezeEnemies(2),
                TricksEnabled({(TrickType.KNOWLEDGE.value, TrickDifficulty.INTERMEDIATE.value)})
            ),
            And(
                HasEnergy(50),
                TricksEnabled({(TrickType.DAMAGE_BOOST.value, TrickDifficulty.BEGINNER.value)})
            ),
            # Dodge
            # Video demonstration: https://youtu.be/X-rHiHQ7Sxw
            TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.INTERMEDIATE.value)})
        )
    )),
]



# Item Locations
CrabRave.locations = [
    FusionLocation("Sector 1 (SRX) -- Crab Rave", False, True_)
]

AntechamberTop.locations = [
    FusionLocation("Sector 1 (SRX) -- Antechamber", False, True_)
]

ChargeCoreArena.locations = [
    FusionLocation("Sector 1 (SRX) -- Charge Core Arena -- Core X", True,
                   CanClearEnemy(enemy=Enemy.CORE_X_CHARGE)),
    FusionLocation("Sector 1 (SRX) -- Charge Core Arena -- Upper Item", False, And(
        Has("Speed Booster"),
        Or(
            And(
                # Trickless
                # Video demonstration: https://youtu.be/Z6_miH4qoQY
                Has("Hi-Jump"),
                IsLocationCollected("Sector 1 (SRX) -- Charge Core Arena -- Core X"),
            ),
            # Video demonstration: https://youtu.be/Fo8-jjuPdik
            TricksEnabled({(TrickType.SHINESPARK.value, TrickDifficulty.ADVANCED.value)}),
            And(
                # Video demonstration: https://youtu.be/q7HKdMt4v3g
                Has("Hi-Jump"),
                TricksEnabled({(TrickType.SHINESPARK.value, TrickDifficulty.INTERMEDIATE.value)})
            )
        )
    ))
]

WateringHole.locations = [
    FusionLocation("Sector 1 (SRX) -- Watering Hole", False, And(
        Has("Speed Booster"),
        CanBallJump(),
        Or(
            Has("Gravity Suit"),
            And(
                # The 7-frame Window
                # Video demonstration: https://youtu.be/7CrmoeqlIUk
                Has("Charge Beam"),
                TricksEnabled({(TrickType.SHINESPARK.value, TrickDifficulty.MASTER.value)})
            )
        ),
        Or(
            HasAny("Charge Beam", "Missile Data", "Plasma Beam"),
            And(
                Has("Wide Beam"),
                HasAny("Ice Beam", "Wave Beam")
            ),
            CanScrewAttackUnderwater(),
            # Maintain spark until Sciser is dead
            # Video demonstration: https://youtu.be/QnQD7K9hcB8
            TricksEnabled({(TrickType.SHINESPARK.value, TrickDifficulty.ADVANCED.value)})
        )
    ))
]

AtmosphericStabilizerNortheast.locations = [
    FusionLocation("Sector 1 (SRX) -- Atmospheric Stabilizer Northeast", False, True_)
]

HornoadHole.locations = [
    FusionLocation("Sector 1 (SRX) -- Hornoad Hole", False, Has("Morph Ball"))
]

WallJumpTutorial.locations = [
    FusionLocation("Sector 1 (SRX) -- Wall Jump Tutorial", False, True_)
]

StabilizerStorage.locations = [
    FusionLocation("Sector 1 (SRX) -- Stabilizer Storage", False, True_)
]

LavaLake.locations = [
    FusionLocation("Sector 1 (SRX) -- Lava Lake -- Lower Item", False, And(
        Has("Morph Ball"),
        Or(
            CanLavaDive(),
            And(
                # Suitless
                # Video demonstration: https://youtu.be/GUfsbWoRpzA
                HasEnergy(150),
                TricksEnabled({(TrickType.DAMAGE_RUN.value, TrickDifficulty.INTERMEDIATE.value)})
            ),
            And(
                # Varia
                Has("Varia Suit"),
                HasEnergy(55),
                TricksEnabled({(TrickType.DAMAGE_RUN.value, TrickDifficulty.BEGINNER.value)})
            ),
            And(
                # Gravity
                Has("Gravity Suit"),
                HasEnergy(80),
                TricksEnabled({(TrickType.DAMAGE_RUN.value, TrickDifficulty.BEGINNER.value)})
            )
        )
    )),
    FusionLocation("Sector 1 (SRX) -- Lava Lake -- Upper Left Item", False, Or(
        Has("Space Jump"),
        And(
            Has("Speed Booster"),
            TricksEnabled({(TrickType.SHINESPARK.value, TrickDifficulty.BEGINNER.value)})
        )
    )),
    FusionLocation("Sector 1 (SRX) -- Lava Lake -- Upper Right Item", False, True_),
]

AnimorphsCache.locations = [
    FusionLocation("Sector 1 (SRX) -- Animorphs Cache", False, True_),
]

NeoRidleyArena.locations = [
    FusionLocation("Sector 1 (SRX) -- Neo-Ridley Arena", True, And(
        CanClearEnemy(enemy=Enemy.CORE_X_SCREW),
        Or(
            # Diddle the Riddle
            And(
                # Space Jump Cheese
                HasAll("Space Jump", "Charge Beam"),
                TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.MASTER.value)})
            ),
            # Missiles Only
            CanDo45MissileDamage(100),
            CanDo40MissileDamage(113),
            CanDo35MissileDamage(129),
            CanDo30MissileDamage(150),
            CanDo25MissileDamage(180),
            CanDo20MissileDamage(225),
            CanDo15MissileDamage(300),
            HasMissileAmmo(450),
            And(
                # Beams only
                Has("Charge Beam"),
                Or(
                    And(
                        # All Beam
                        HasAll("Ice Beam", "Plasma Beam", "Wave Beam", "Wide Beam"),
                        HasEnergy(161)
                    ),
                    And(
                        # Vanilla Beam damage
                        HasAll("Plasma Beam", "Wide Beam"),
                        HasAny("Ice Beam", "Wave Beam"),
                        Or(
                            HasEnergy(551),
                            TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.EXPERT.value)})
                        )
                    ),
                    And(
                        # Plasma & Wide only
                        HasAll("Plasma Beam", "Wide Beam"),
                        HasEnergy(751),
                        TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.INTERMEDIATE.value)})
                    ),
                    And(
                        # Plasma Only or All but
                        HasEnergy(2051),
                        TricksEnabled({(TrickType.COMBAT.value, TrickDifficulty.EXPERT.value)}),
                        Or(
                            Has("Plasma Beam"),
                            HasAll("Ice Beam", "Wave Beam", "Wide Beam"),
                        )
                    )
                )
            )
        )
    ))
]

RipperMazeLeft.locations = [
    FusionLocation("Sector 1 (SRX) -- Ripper Maze", False, And(
        Has("Morph Ball"),
        Or(
            CanJumpHigh(),
            And(
                Has("Wall Jump Boots"),
                TricksEnabled({(TrickType.WALL_JUMP.value, TrickDifficulty.BEGINNER.value)})
            )
        ),
        Or(
            CanDo15MissileDamage(),
            And(
                TricksEnabled({(TrickType.KNOWLEDGE.value, TrickDifficulty.ADVANCED.value)}),
                HasMissileAmmo(3),
                Or(
                    Has("Space Jump"),
                    # Video demonstration: https://youtu.be/8tUjNmvbRDE
                    TricksEnabled({(TrickType.GENERIC_MOVEMENT.value, TrickDifficulty.INTERMEDIATE.value)}),
                    And(
                        CanFreezeEnemies(3),
                        TricksEnabled({(TrickType.FROZEN_ENEMIES.value, TrickDifficulty.BEGINNER.value)})
                    )
                )
            )
        ),
        Or(
            CanBallJump(),
            And(
                TricksEnabled({(TrickType.MIDAIR_MORPH.value, TrickDifficulty.BEGINNER.value)}),
                CanPONR()
            )
        )
    ))
]
