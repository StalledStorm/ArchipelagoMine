from ..Connection import Connection
from ..Requirement import PONRRequirement
from ..VariableConnection import VariableConnection
from ..Requirements import *
from ..FusionLocation import FusionLocation

from ..regions.MainDeck import SectorHubElevator1Top
from ..regions.Sector1 import *
from ..regions.Sector2 import Sector2TubeLeft
from ..regions.Sector3 import Sector3TubeRight
from ..regions.Sector6 import Sector6RestrictedZoneElevatorToTourian

Sector1Hub.connections = [
    VariableConnection(SectorHubElevator1Top, []),
    Connection(Sector1Antechamber, [
        Requirement(["Screw Attack", "Level 2 Keycard"], [HasSpaceJump, CanDoAdvancedWallJumpWithHiJump])
    ]),
    Connection(Sector1TubeLeft, [
        Requirement(["Morph Ball", "Screw Attack", "Level 1 Keycard"], [])
    ]),
    Connection(Sector1FirstStabilizerZone, [
        CanDefeatSmallGeron,
        Requirement(["Level 1 Keycard", "Level 2 Keycard"], [CanLavaDive]),
        CanDoAdvancedShinespark
    ]),
]

Sector1Antechamber.connections = [
    Connection(Sector1Hub, [
        Requirement(["Level 2 Keycard"], [HasScrewAttack])
    ], one_way=True),
    Connection(Sector1TubeRight, [HasMorph], one_way=True)
]

Sector1TubeRight.connections = [
    Connection(Sector1Antechamber, [CanBallJump]),
    VariableConnection(Sector2TubeLeft, [])
]

Sector1TubeLeft.connections = [
    VariableConnection(Sector3TubeRight, [])
]

Sector1FirstStabilizerZone.connections = [
    Connection(Sector1SecondStabilizerZone, [CanDefeatStabilizerOrToughEnemy]),
    Connection(Sector1AfterChargeCoreZone, [HasWaveBeam]),
]

Sector1SecondStabilizerZone.connections = [
    Connection(Sector1ThirdStabilizerZone, [CanDefeatStabilizerOrToughEnemy]),
    Connection(Sector1TourianExit, [
        CanBallJumpRequirement(["Wave Beam", "Ice Beam"], [CanScrewAttackAndSpaceJump]),
        CanBallJumpRequirement(["Wave Beam", "Missile Data", "Diffusion Missile"], [CanScrewAttackAndSpaceJump]),
        PONRRequirement(["Missile Data", "Diffusion Missile", "ScrewAttack", "Space Jump"], [CanBallJump])
    ], one_way=True)
]

Sector1ThirdStabilizerZone.connections = [
    Connection(Sector1ChargeCoreZone, [
        PONRRequirement(["Morph Ball"], [CanDefeatThirdStabilizer]),
        Requirement(["Morph Ball", "Missile Data"],[])
    ], one_way=True),
]

Sector1ChargeCoreZone.connections = [
    Connection(Sector1AfterChargeCoreZone, [HasMissile])
]

Sector1AfterChargeCoreZone.connections = [
    Connection(Sector1FirstStabilizerZone, [], one_way=True)
]

Sector1TourianExit.connections = [
    Connection(Sector1SecondStabilizerZone, [
        CanBallJumpRequirement(["Wave Beam", "Ice Beam"], [CanScrewAttackAndSpaceJump]),
        CanBallJumpRequirement(["Wave Beam", "Missile Data", "Diffusion Missile"], [CanScrewAttackAndSpaceJump]),
        PONRRequirement(["Morph Ball", "Wave Beam"], [CanScrewAttackAndSpaceJump])
    ], one_way=True),
    Connection(Sector1TourianHub, [
        PONRRequirement(
            ["Missile Data", "Morph Ball", "Screw Attack"],
            [HasSpaceJump, CanDoSimpleWallJump],
            level_4_e_tanks)
    ], one_way=True)
]

Sector1TourianHub.connections = [
    Connection(Sector1TourianExit, [
        Requirement(
            ["Missile Data", "Morph Ball", "Screw Attack", "Wave Beam"],
            [HasSpaceJump, CanDoAdvancedWallJump],
            level_4_e_tanks)
    ]),
    Connection(Sector1TourianHubElevatorTop, [
        Requirement(["Screw Attack"], [HasSpaceJump, CanDoSimpleWallJump])
    ])
]

Sector1TourianHubElevatorTop.connections = [
    VariableConnection(Sector6RestrictedZoneElevatorToTourian, []),
    Connection(Sector1TourianHub, [PONRRequirement(["Nothing"], [], level_4_e_tanks)], one_way=True)
]

Sector1Antechamber.locations = [
    FusionLocation("Sector 1 (SRX) -- Antechamber", False, [])
]

Sector1FirstStabilizerZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Atmospheric Stabilizer Northeast", False, [
        PONRRequirement(["Nothing"], []),
        Requirement([], [CanDefeatStabilizer, CanDoAdvancedShinespark])
    ]),
    FusionLocation("Sector 1 (SRX) -- Hornoad Hole", False, [HasMorph]),
    FusionLocation("Sector 1 (SRX) -- Wall Jump Tutorial", False, [
        CanBallJumpRequirement([], [HasSpaceJump, CanDoSimpleWallJump])
    ])
]

Sector1SecondStabilizerZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Lava Lake -- Lower Item", False, [
        Requirement(["Morph Ball"], [CanLavaDive])
    ]),
    FusionLocation("Sector 1 (SRX) -- Lava Lake -- Upper Left Item", False, [
        HasSpaceJump,
        CanDoBeginnerShinespark
    ]),
    FusionLocation("Sector 1 (SRX) -- Lava Lake -- Upper Right Item", False, []),
]

Sector1ThirdStabilizerZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Stabilizer Storage", False, [CanDefeatThirdStabilizer])
]

Sector1ChargeCoreZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Charge Core Arena -- Core X", True, [
        CanFightBeginnerBoss
    ]),
    FusionLocation("Sector 1 (SRX) -- Charge Core Arena -- Upper Item", False, [
        PONRRequirement(["Speed Booster"],[]),
        Requirement(["Speed Booster"], [HasMissile])
    ]),
    FusionLocation("Sector 1 (SRX) -- Watering Hole", False, [
        CanBallJumpRequirement(["Gravity Suit", "Speed Booster"], [
            Requirement(["Plasma Beam"], []),
            HasChargeBeam,
            HasScrewAttack,
            CanDoBeginnerShinesparkRequirement(["Wide Beam"], []),
            CanDoBeginnerShinesparkRequirement([], [HasWaveBeam, HasMissile, CanPowerBomb]),
            CanDoAdvancedShinespark
        ])
    ])
]

Sector1AfterChargeCoreZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Crab Rave", False, [
        Requirement(["Morph Ball", "Missile Data"], [])
    ])
]

Sector1TourianHub.locations = [
    FusionLocation("Sector 1 (SRX) -- Animorphs Cache", False, [
        PONRRequirement([], [CanReachAnimorphs]),
        CanReachAnimorphsRequirement([], [HasSpaceJump, CanDoSimpleWallJumpWithHiJump]),
    ]),
    FusionLocation("Sector 1 (SRX) -- Ridley Arena", True, [
        Requirement(["Morph Ball", "Bomb Data", "Wave Beam"], [CanFightLateGameBoss]),
        Requirement(["Morph Ball", "Power Bomb Data"], [CanFightLateGameBoss]),
        Requirement(["Morph Ball", "Bomb Data", "Wave Beam", "Plasma Beam", "Space Jump"], [CanFightLategameBossOnAdvanced]),
        Requirement(["Morph Ball", "Power Bomb Data", "Plasma Beam", "Space Jump"], [CanFightLategameBossOnAdvanced]),
        Requirement(["Morph Ball", "Bomb Data", "Wave Beam", "Space Jump"], [CanFightBossOnExpert]),
        Requirement(["Morph Ball", "Power Bomb Data", "Space Jump"], [CanFightBossOnExpert]),
        PONRRequirement(["Morph Ball", "Bomb Data", "Wave Beam"], [CanFightBossOnExpertRequirement([], [CanDoAdvancedWallJump])]),
        PONRRequirement(["Morph Ball", "Power Bomb Data"], [CanFightBossOnExpertRequirement([], [CanDoAdvancedWallJump])])
    ]),
    FusionLocation("Sector 1 (SRX) -- Ripper Maze", False, [
        PONRRequirement(["Missile Data", "Diffusion Missile", "Screw Attack", "Morph Ball"], [HasSpaceJump, CanDoSimpleWallJump]),
        CanBallJumpRequirement(["Missile Data", "Diffusion Missile", "Screw Attack"], [HasSpaceJump, CanDoSimpleWallJump])
    ])
]
