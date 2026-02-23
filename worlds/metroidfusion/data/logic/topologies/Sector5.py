from ..Connection import Connection
from ..Requirement import PONRRequirement
from ..VariableConnection import VariableConnection
from ..Requirements import *
from ..FusionLocation import FusionLocation

from ..regions.MainDeck import SectorHubElevator5Top
from ..regions.Sector3 import Sector3TubeLeft
from ..regions.Sector4 import Sector4UpperWaterZone
from ..regions.Sector5 import *
from ..regions.Sector6 import Sector6TubeRight

Sector5Hub.connections = [
    VariableConnection(SectorHubElevator5Top, []),
    Connection(Sector5MagicBox, [
        Requirement(["Level 3 Keycard"], [])
    ]),
    Connection(Sector5TopLeftBigRoom, [
        Requirement(["Level 3 Keycard"], [CanJumpHigh, CanDoAdvancedWallJump]),
        Requirement(["Morph Ball"], [HasMissile])
    ]),
    Connection(Sector5FrozenHub, [
        Requirement(["Varia Suit"], [HasKeycard3])
    ])
]

Sector5TubeLeft.connections = [
    VariableConnection(Sector6TubeRight, []),
    Connection(Sector5MagicBox, [HasScrewAttack])
]

Sector5TubeRight.connections = [
    VariableConnection(Sector3TubeLeft, []),
    Connection(Sector5BeforeNightmareHub, [], one_way=True)
]

Sector5TopLeftBigRoom.connections = [
    Connection(Sector5FrozenHub, [HasVaria], one_way=True)
]

Sector5FrozenHub.connections = [
    Connection(Sector5DataRoom, [
        PONRRequirement(["Level 3 Keycard"], [HasVaria]),
        HasKeycard3Requirement([], [HasVaria])
    ], one_way=True),
    Connection(Sector5BeforeNightmareHub, [
        Requirement(["Level 3 Keycard"], [HasVaria])
    ]),
    Connection(Sector5SecurityZone, [
        PONRRequirement(["Speed Booster", "Varia Suit"], [CanBombOrPowerBomb], level_3_e_tanks),
        HasSpaceJumpRequirement(["Speed Booster", "Varia Suit"], [CanBombOrPowerBomb], level_3_e_tanks),
        #Requirement(["Varia Suit", "Level 3 Keycard"], [CanDoExpertShinespark]),
        Requirement(["Varia Suit", "Level 3 Keycard"], [HasWaveBeam])
    ], one_way=True),
    Connection(Sector5TopLeftBigRoom, [
        Requirement(["Varia Suit"], [CanJumpHigh, CanDoAdvancedWallJump])
    ])
]

Sector5SecurityZone.connections = [
    Connection(Sector5DataRoom, [
        HasSpaceJumpRequirement(["Varia Suit"], [HasKeycard3]),
        CanDoAdvancedWallJumpWithHiJumpRequirement(["Varia Suit", "Level 3 Keycard"], [CanFreezeEnemies], level_3_e_tanks)
        #ReverseIceLOLRequirement
    ]),
    Connection(Sector5FrozenHub, [
        Requirement(["Level 3 Keycard", "Varia Suit"], []),
        Requirement(["Space Jump", "Varia Suit"], [CanBombOrPowerBomb]),
        Requirement(["Space Jump", "Speed Booster", "Morph Ball", "Level 3 Keycard", "Varia Suit"], [CanFreezeEnemies])
    ], one_way=True)
]

Sector5DataRoom.connections = [
    Connection(Sector5FrozenHub, [
        Requirement(["Level 3 Keycard"], [HasWaveBeam])
    ]),
    Connection(Sector5SecurityZone, [HasKeycard3], one_way=True)
]

Sector5BeforeNightmareHub.connections = [
    Connection(Sector5TubeRight, [CanJumpHigh, CanDoSimpleWallJump]),
    Connection(Sector5NightmareHub, [
        PONRRequirement([], [CanBeatToughEnemy], level_3_e_tanks),
        CanDrainAQARequirement(["Level 4 Keycard", "Gravity Suit", "Speed Booster"], [CanBeatToughEnemy], level_3_e_tanks)
        #Hoping to one day have means to check paths to loop through 4 and get back
    ], one_way=True)
]

Sector5NightmareHub.connections = [
    Connection(Sector5BeforeNightmareHub, [
        Requirement(["Gravity Suit", "Screw Attack"], [
            HasSpaceJump,
            CanDoBeginnerShinesparkRequirement([], [CanDoAdvancedWallJump])
        ], level_3_e_tanks)
    ]),
    Connection(Sector5NightmareZoneArena, [CanSpeedBoosterUnderwater], one_way=True),
    Connection(Sector4UpperWaterZone, [CanSpeedBoosterUnderwater]),
    Connection(Sector5NightmareZoneUpper, [
        CanJumpHighRequirement([], [CanBeatToughEnemy, CanPowerBomb, CanScrewAttackUnderwater], level_3_e_tanks),
        CanDoBeginnerShinesparkRequirement(["Gravity Suit"], [CanDefeatStabilizerOrToughEnemy], level_3_e_tanks)
    ])
]

Sector5NightmareZoneUpper.connections = [
    Connection(Sector5NightmareHub, [
        PONRRequirement([], [CanBeatToughEnemy, CanPowerBomb, CanScrewAttackUnderwater], level_3_e_tanks)
    ], one_way=True),
    Connection(Sector5NightmareZoneArena, [
        PONRRequirement([], [
            CanBeatToughEnemyRequirement([], [HasSpaceJump, CanDoSimpleWallJump])
        ])
    ], one_way=True)
]

Sector5NightmareZoneArena.connections = [
    Connection(Sector5NightmareHub, [
        CanSpeedBoosterUnderwaterRequirement([], [
            CanJumpHighRequirement([], [CanFightLateGameBoss, CanFightLategameBossOnAdvanced, CanFightBossOnExpert])
        ])
    ])
]

Sector5Hub.locations = [
    FusionLocation("Sector 5 (ARC) -- Gerubus Gully", False, [
        PONRRequirement(["Morph Ball", "Level 3 Keycard"], [HasScrewAttack, CanDoBeginnerShinespark]),
        Requirement(["Level 3 Keycard"], [CanPowerBomb]),
        CanBombRequirement(["Level 3 Keycard"], [HasScrewAttack, HasHiJump, CanDoBeginnerShinespark])
    ]),
]

Sector5MagicBox.locations = [
    FusionLocation("Sector 5 (ARC) -- Magic Box", False, [])
]

Sector5TopLeftBigRoom.locations = [
    FusionLocation("Sector 5 (ARC) -- Training Aerie -- Left Item", False, [
        Requirement(["Speed Booster"], [
            HasSpaceJump,
            CanFreezeEnemies,
            CanDoBeginnerShinesparkRequirement(["Level 3 Keycard"], [CanDoAdvancedWallJump])
        ])
    ]),
    FusionLocation("Sector 5 (ARC) -- Training Aerie -- Right Item", False, [
        HasSpaceJump,
        CanFreezeEnemies,
        CanDoBeginnerShinesparkRequirement(["Level 3 Keycard"], [CanDoAdvancedWallJump])
    ])
]

Sector5FrozenHub.locations = [
    FusionLocation("Sector 5 (ARC) -- Ripper Road", False, [
        CanFreezeEnemiesRequirement(["Varia Suit"], [
            CanPowerBombRequirement([], [CanBallJump]),
            CanBombRequirement([], [HasScrewAttack])
        ])
    ])
]

Sector5BeforeNightmareHub.locations = [
    FusionLocation("Sector 5 (ARC) -- Crow's Nest", False, [
        PONRRequirement(["Morph Ball"], [
            CanDoBeginnerShinesparkRequirement([], [
                CanBeatToughEnemyRequirement([], [CanJumpHigh, CanDoSimpleWallJump], level_3_e_tanks)
            ])
        ]),
        Requirement(["Morph Ball", "Power Bomb Data"], [CanJumpHigh, CanDoAdvancedWallJump]),
        Requirement(["Morph Ball", "Screw Attack"], [CanJumpHigh, CanDoAdvancedWallJump]),
        CanDoBeginnerShinesparkRequirement(["Morph Ball", "Bomb Data"], [
            CanBeatToughEnemyRequirement([], [CanJumpHigh, CanDoSimpleWallJump], level_3_e_tanks)
        ])
    ])
]

Sector5DataRoom.locations = [
    FusionLocation("Sector 5 (ARC) -- Data Room", True, [])
]

Sector5SecurityZone.locations = [
    FusionLocation("Sector 5 (ARC) -- E-Tank Mimic Den", False, [
        PONRRequirement(["Morph Ball", "Power Bomb Data", "Level 3 Keycard", "Varia Suit"], [CanFreezeEnemies, HasSpaceJump]),
        PONRRequirement(["Morph Ball", "Screw Attack", "Level 3 Keycard", "Varia Suit"], [CanFreezeEnemies, HasSpaceJump]),
        CanBallJumpAndBombRequirement(["Level 3 Keycard", "Varia Suit"], [CanFreezeEnemies, HasSpaceJump])
    ]),
    FusionLocation("Sector 5 (ARC) -- Level 3 Security Room", True, [HasVaria]),
    FusionLocation("Sector 5 (ARC) -- Ripper's Treasure", False, [
        CanPowerBombRequirement(["Varia Suit"], [
            HasSpaceJump,
            CanFreezeEnemiesRequirement([], [HasHiJump, CanDoSimpleWallJump])
        ])
    ]),
    FusionLocation("Sector 5 (ARC) -- Security Shaft East", False, [
        Requirement(["Varia Suit"], [CanPowerBomb])
    ]),
    FusionLocation("Sector 5 (ARC) -- Transmutation Trial", False, [
        CanBallJumpRequirement(["Level 3 Keycard", "Varia Suit"], [HasSpaceJump, CanFreezeEnemies])
    ])
]

Sector5NightmareHub.locations = [
    FusionLocation("Sector 5 (ARC) -- Flooded Airlock to Sector 4 (AQA)", False, [
        CanSpeedBoosterUnderwater
    ]),
    FusionLocation("Sector 5 (ARC) -- Mini-Fridge", False, [
        Requirement(["Morph Ball", "Missile Data", "Varia Suit", "Gravity Suit"], [
            CanFreezeEnemies,
            HasSpaceJump,
            CanDoBeginnerShinespark
        ], level_3_e_tanks)
    ])
]

Sector5NightmareZoneUpper.locations = [
    FusionLocation("Sector 5 (ARC) -- Nightmare Hub", False, [
        Requirement(["Power Bomb Data"], [CanBallJump])
    ]),
    FusionLocation("Sector 5 (ARC) -- Ruined Break Room", False, [CanPowerBomb]),
    FusionLocation("Sector 5 (ARC) -- Nightmare Nook", False, [
        PONRRequirement([], [
            CanBeatToughEnemyRequirement([], [
                CanBallJumpAndBombRequirement([], [HasSpaceJump, CanDoSimpleWallJump])
            ])
        ]),
        CanBallJumpAndBombRequirement(["Gravity Suit", "Speed Booster"], [
            CanJumpHighRequirement([], [
                HasSpaceJumpRequirement([], [CanFightLateGameBoss, CanFightLategameBossOnAdvanced, CanFightBossOnExpert]),
                CanDoSimpleWallJumpRequirement([], [CanFightLateGameBoss, CanFightLategameBossOnAdvanced, CanFightBossOnExpert])
            ])
        ])
    ])
]

Sector5NightmareZoneArena.locations = [
    FusionLocation("Sector 5 (ARC) -- Nightmare Arena", True, [
        CanJumpHighRequirement([], [CanFightLateGameBoss, CanFightLategameBossOnAdvanced, CanFightBossOnExpert])
    ])
]
