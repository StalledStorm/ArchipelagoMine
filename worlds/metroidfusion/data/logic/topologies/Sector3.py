from ..Connection import Connection
from ..Requirement import PONRRequirement
from ..VariableConnection import VariableConnection
from ..Requirements import *
from ..FusionLocation import FusionLocation

from ..regions.MainDeck import SectorHubElevator3Top
from ..regions.Sector1 import Sector1TubeLeft
from ..regions.Sector3 import *
from ..regions.Sector5 import Sector5TubeRight

Sector3Hub.connections = [
    VariableConnection(SectorHubElevator3Top, []),
     Connection(Sector3FieryStorageRight, [
        PONRRequirement(["Varia Suit"], [CanDoBeginnerShinespark])
    ], one_way=True),
    Connection(Sector3SecurityZone, [HasSpeedBooster]),
    Connection(Sector3MainShaft, [
        PONRRequirement(["Speed Booster"], [
            HasMorph,
            CanDefeatStabilizerOrToughEnemy,
            CanDoBeginnerShinespark,
            HasWaveBeam
        ]),
        Requirement(["Speed Booster", "Morph Ball"], [CanDestroyBombBlocks])
    ], one_way=True),
    Connection(Sector3BOXZone, [
        Requirement(["Level 2 Keycard"], [CanDefeatMediumGeron])
    ]),
    Connection(Sector3LowerAttic, [
        Requirement(["Screw Attack", "Morph Ball"], [HasSpaceJump, CanDoBeginnerShinespark])
    ])
]

Sector3TubeLeft.connections = [
    VariableConnection(Sector5TubeRight, []),
    Connection(Sector3FieryStorageLeft, [
        Requirement(["Screw Attack"], [CanJumpHigh, CanDoSimpleWallJump])
    ])
]

Sector3TubeRight.connections = [
    VariableConnection(Sector1TubeLeft, []),
    Connection(Sector3UpperAttic, [
        PONRRequirement([], [HasScrewAttack])
    ], one_way=True)
]

Sector3FieryStorageRight.connections = [
    Connection(Sector3FieryStorageLeft, [CanDestroyBombBlocks]),
    Connection(Sector3Hub, [
        Requirement(["Varia Suit"], [
            CanBeatToughEnemy,
            CanLavaDive,
            CanScrewAttackAndSpaceJump
        ]),
        CanDoBeginnerShinesparkRequirement(["Varia Suit"], [CanDestroyBombBlocks])
    ])
]

Sector3FieryStorageLeft.connections = [
    Connection(Sector3TubeLeft, [
        PONRRequirement([], [HasScrewAttack])
    ], one_way=True)
]

Sector3MainShaft.connections = [
    Connection(Sector3Hub, [
        PONRRequirement(["Morph Ball"], [CanDestroyBombBlocks]),
        Requirement(["Morph Ball", "Speed Booster"], [CanDestroyBombBlocks]),
        CanDefeatMediumGeronRequirement(["Morph Ball", "Level 2 Keycard"], [CanDestroyBombBlocks])
    ], one_way=True),
    Connection(Sector3BoilerZone, [Requirement(["Level 2 Keycard"], [HasVaria])]),
    Connection(Sector3BobZone, [
        Requirement(["Morph Ball", "Hi-Jump"], [HasScrewAttack])
    ], one_way=True),
    Connection(Sector3SovaProcessing, [
        CanDestroyBombBlocksRequirement(
            ["Level 2 Keycard", "Varia Suit"],
            [
                HasSpaceJump,
                HasWaveBeam,
                CanBeatToughEnemyRequirement([], [CanDoBeginnerShinespark]),
                CanFreezeEnemiesRequirement(["Hi-Jump"], [])
            ], level_2_e_tanks
        )
    ])
]

Sector3BobZone.connections = [
    Connection(Sector3BOXZone, [
        Requirement(["Level 2 Keycard"], [CanBallJumpAndBomb]),
        Requirement(["Level 2 Keycard", "Wave Beam"], [CanBallJump])
    ]),
    Connection(Sector3Hub, [
        PONRRequirement(["Morph Ball"], [CanDestroyBombBlocks]),
    ], one_way=True),
    Connection(Sector3MainShaft, [CanBombOrPowerBomb])
]

Sector3BOXZone.connections = [
    Connection(Sector3BobZone, [
        PONRRequirement(["Level 2 Keycard"], [HasMorph]),
        CanDefeatMediumGeronRequirement(["Level 2 Keycard"], [HasMorph])
    ], one_way=True),
    Connection(Sector3MainShaft, [
        PONRRequirement(["Level 2 Keycard"] [HasMorph]),
        CanDefeatMediumGeronRequirement(["Level 2 Keycard", "Morph Ball"], [CanDestroyBombBlocks])
    ], one_way=True),
    Connection(Sector3UpperAttic, [
        PONRRequirement([], [HasSpaceJump], level_2_e_tanks)
    ], one_way=True)
]

Sector3LowerAttic.connections = [
    Connection(Sector3Hub, [
        Requirement(["Morph Ball"] [CanDestroyBombBlocks])
    ], one_way=True),
    Connection(Sector3UpperAttic, [
        CanBombOrPowerBombRequirement([], [HasSpaceJump, CanDoAdvancedWallJumpWithHiJump]),
        #future trick CanBombOrPowerBombRequirement(["Hi-Jump"], [CanFreezeEnemies]),
        #future trick CanBombOrPowerBombRequirement([], [CanDoSimpleWallJumpAndFreezeEnemies])
    ]),
    #overzealous plans Connection(Sector3MidAttic, [
        #CanDestroyBombBlocksRequirement([], [CanJumpHigh, CanActivatePillar])
    #])
]

Sector3UpperAttic.connections = [
    Connection(Sector3BOXZone, [
        CanFightBossRequirement([], [CanJumpHigh, CanDoSimpleWallJump], level_2_e_tanks)
    ]),
    Connection(Sector3TubeRight, [
        Requirement(["Screw Attack"], [CanJumpHigh, CanDoBeginnerShinespark])
    ]),
    Connection(Sector3LowerAttic, [
        PONRRequirement(["Morph Ball"], [CanDestroyBombBlocks]),
        PONRRequirement(["Speed Booster"], [CanDestroyBombBlocks])
    ], one_way=True),
    #overzealous plans Connection(Sector3MidAttic, [
        #PONRRequirement(["Speed Booster"], [CanDestroyBombBlocks])
    #])
]

Sector3SovaProcessing.connections = [
    Connection(Sector3UpperAttic, [
        Requirement(["Screw Attack", "Speed Booster"], [CanLavaDive])
    ], one_way=True)
]

Sector3FieryStorageRight.locations = [
    FusionLocation("Sector 3 (PYR) -- Fiery Storage -- Lower Item", False, []),
]

Sector3FieryStorageLeft.locations = [
    FusionLocation("Sector 3 (PYR) -- Fiery Storage -- Upper Item", False, [
        CanDestroyBombBlocksRequirement(["Speed Booster"], [
            CanActivatePillar,
            HasSpaceJump,
            CanDoAdvancedShinesparkRequirement([], [CanDoAdvancedWallJump])
        ])
    ])
]

Sector3TubeLeft.locations = [
    FusionLocation("Sector 3 (PYR) -- Glass Tube to Sector 5 (ARC)", False, [
        Requirement(["Hi-Jump"], [CanBomb]),
        CanPowerBomb,
        HasScrewAttack
    ])
]

Sector3SecurityZone.locations = [
    FusionLocation("Sector 3 (PYR) -- Level 2 Security Room", True, [
        HasKeycard2,
        PONRRequirement(["Speed Booster"], [CanBallJumpAndBomb])
    ]),
    FusionLocation("Sector 3 (PYR) -- Security Access", False, [
        CanBeatToughEnemyRequirement([], [CanJumpHigh, CanDoSimpleWallJump]),
        CanDoAdvancedShinesparkRequirement([], [])
    ])
]

Sector3MainShaft.locations = [
    FusionLocation("Sector 3 (PYR) -- Namihe's Lair", False, [
        CanPowerBombAndJumpHigh,
        PONRRequirement(["Morph Ball", "Power Bomb"], [CanDoAdvancedShinespark])
    ]),
    FusionLocation("Sector 3 (PYR) -- Processing Access", False, [
        Requirement(["Level 2 Keycard"], [])
    ]),
]

Sector3BoilerZone.locations = [
    FusionLocation("Sector 3 (PYR) -- Lava Maze", False, [
        CanPowerBombRequirement([], [CanLavaDive])
    ]),
    FusionLocation("Sector 3 (PYR) -- Main Boiler Control Room -- Boiler", True, [
        Requirement(["Missile Data"], [HasSpaceJump]),
        CanFreezeEnemiesRequirement(["Missile Data"], [HasHiJump, CanDoSimpleWallJump])
    ]),
    FusionLocation("Sector 3 (PYR) -- Main Boiler Control Room -- Core X", True, [
        Requirement(["Missile Data"], [HasSpaceJump]),
        CanFreezeEnemiesRequirement(["Missile Data"], [HasHiJump, CanDoSimpleWallJump])
    ]),
]

Sector3BobZone.locations = [
    FusionLocation("Sector 3 (PYR) -- Bob's Abode", False, []),
]

Sector3BOXZone.locations = [
    FusionLocation("Sector 3 (PYR) -- Data Room", True, [
        CanFightBossRequirement(["Level 2 Keycard"], [CanJumpHigh, CanDoSimpleWallJump], level_2_e_tanks)
    ]),
    FusionLocation("Sector 3 (PYR) -- Geron's Treasure", False, [CanDefeatMediumGeron])
]

Sector3LowerAttic.locations = [
    FusionLocation("Sector 3 (PYR) -- Alcove -- Lower Item", False, [
        #overzealous plans if in MidAttic: CanDestroyBombBlocks,
        CanDestroyBombBlocksRequirement([], [CanActivatePillar, CanJumpHigh])
    ]),
    FusionLocation("Sector 3 (PYR) -- Alcove -- Upper Item", False, [
        Requirement([], [CanPowerBomb])
    ]),
]

Sector3UpperAttic.locations = [
    FusionLocation("Sector 3 (PYR) -- Deserted Runway", False, [HasSpeedBooster]),
]

Sector3SovaProcessing.locations = [
    FusionLocation("Sector 3 (PYR) -- Sova Processing -- Left Item", False, [
        CanBallJumpRequirement([], [HasSpaceJump, CanFreezeEnemies])
    ]),
    FusionLocation("Sector 3 (PYR) -- Sova Processing -- Right Item", False, [
        Requirement(["Morph Ball"], [HasSpaceJump, CanFreezeEnemies])
    ]),
    FusionLocation("Sector 3 (PYR) -- Garbage Chute -- Lower Item", False, [
        Requirement(["Screw Attack", "Speed Booster"], [CanLavaDive])
    ]),
    FusionLocation("Sector 3 (PYR) -- Garbage Chute -- Upper Item", False, [
        Requirement(["Screw Attack", "Speed Booster"], [CanLavaDive])
    ])
]
