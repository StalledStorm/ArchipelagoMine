from ..Connection import Connection
from ..Requirement import PONRRequirement
from ..VariableConnection import VariableConnection
from ..Requirements import *
from ..FusionLocation import FusionLocation

from ..regions.MainDeck import SectorHubElevator2Top
from ..regions.Sector1 import Sector1TubeRight
from ..regions.Sector2 import *
from ..regions.Sector4 import Sector4TubeLeft

Sector2Hub.connections = [
    VariableConnection(SectorHubElevator2Top, []),
    Connection(Sector2TubeLeft, [HasScrewAttack]),
    Connection(Sector2TubeRight, [HasScrewAttack]),
    Connection(Sector2LeftSide, [
        PONRRequirement(["Morph Ball"], [CanDestroyBombBlocks])
    ], one_way=True),
    Connection(Sector2ZazabiZoneUpper, [CanBombOrPowerBomb]),
    Connection(Sector2NettoriZone, [
        CanPowerBombAndJumpHigh,
        Requirement(["Morph Ball", "Power Bomb Data"], [CanDoSimpleWallJump])
    ])
]

Sector2TubeLeft.connections = [
    VariableConnection(Sector1TubeRight, [])
]

Sector2TubeRight.connections = [
    VariableConnection(Sector4TubeLeft, [])
]

Sector2LeftSide.connections = [
    Connection(Sector2Hub, [
        Requirement(["Morph Ball", "Hi-Jump"], [CanDestroyBombBlocks]),
        CanBombRequirement([], [CanPowerBomb, HasScrewAttack]),
        #Loop around through Cathedral
        CanBombRequirement([], [HasSpaceJump, CanDoSimpleWallJumpWithHiJump])
    ]),
    Connection(Sector2ZazabiZone, [CanBombOrPowerBomb], one_way=True)
]

Sector2ZazabiZone.connections = [
    Connection(Sector2LeftSide, [
        #Loop around through Cathedral
        CanBombOrPowerBombRequirement(["Space Jump"], []),
        CanBombOrPowerBombRequirement(["Screw Attack"], [HasSpaceJump, CanDoSimpleWallJumpWithHiJump])
    ]),
    Connection(Sector2NettoriZone, [HasSpaceJump]),
    Connection(Sector2ZazabiZoneUpper, [HasSpaceJump, CanDoSimpleWallJumpWithHiJump])
]

Sector2ZazabiZoneUpper.connections = [
    Connection(Sector2ZazabiZone, [
        PONRRequirement(["Nothing"], []),
    ], one_way=True)
]

Sector2Hub.locations = [
    FusionLocation("Sector 2 (TRO) -- Crumble City -- Lower Item", False, [
        CanScrewAttackAndSpaceJump
    ]),
    FusionLocation("Sector 2 (TRO) -- Crumble City -- Upper Item", False, [
        CanScrewAttackAndSpaceJump
    ]),
    FusionLocation("Sector 2 (TRO) -- Data Courtyard", False, [CanBombOrPowerBomb]),
    FusionLocation("Sector 2 (TRO) -- Data Room", True, [
        Requirement(["Level 1 Keycard"], [])
    ]),
    FusionLocation("Sector 2 (TRO) -- Kago Room", False, [
        CanJumpHigh, HasScrewAttack, CanFreezeEnemies, CanDoBeginnerShinespark
    ]),
    FusionLocation("Sector 2 (TRO) -- Level 1 Security Room", True, [
        PONRRequirement(["Nothing"], []),
        Requirement([], [HasSpaceJump]),
        Requirement(["Level 1 Keycard"], []),
    ]),
    FusionLocation("Sector 2 (TRO) -- Lobby Cache", False, [
        Requirement(["Level 1 Keycard"], [CanBombOrPowerBomb])
    ]),
]

Sector2LeftSide.locations = [
    FusionLocation("Sector 2 (TRO) -- Zoro Zig-Zag", False, [
        Requirement(["Morph Ball"], [CanActivatePillar, CanJumpHigh])
    ])
]

Sector2ZazabiZone.locations = [
    FusionLocation("Sector 2 (TRO) -- Cultivation Station", False, [
        CanBombOrPowerBombRequirement([], [CanJumpHigh, CanFreezeEnemies])
    ]),
    FusionLocation("Sector 2 (TRO) -- Oasis", False, [CanJumpHigh]),
    FusionLocation("Sector 2 (TRO) -- Oasis Storage", False, [
        CanPowerBomb,
        Requirement(["Hi-Jump"], [CanBomb]),
        Requirement(["Morph Ball", "Screw Attack"], [CanJumpHighUnderwater])
    ]),
    FusionLocation("Sector 2 (TRO) -- Ripper Tower -- Lower Item", False, [
        Requirement(["Morph Ball"], [CanFreezeEnemies])
    ]),
    FusionLocation("Sector 2 (TRO) -- Ripper Tower -- Upper Item", False, [
        PONRRequirement(["Morph Ball"], [CanFreezeEnemies]),
        CanDestroyBombBlocksRequirement(["Morph Ball"], [CanFreezeEnemies])
    ]),
    FusionLocation("Sector 2 (TRO) -- Zazabi Arena", True, [
        PONRRequirement([], [CanFightBoss]),
        CanJumpHighRequirement([], [CanFightBoss]),
    ]),
    FusionLocation("Sector 2 (TRO) -- Zazabi Arena Access", False, []),
    FusionLocation("Sector 2 (TRO) -- Zazabi Speedway -- Lower Item", False, [
        Requirement(["Space Jump", "Speed Booster", "Screw Attack"], [CanFightBoss])
    ]),
    FusionLocation("Sector 2 (TRO) -- Zazabi Speedway -- Upper Item", False, [
        Requirement(["Space Jump", "Speed Booster", "Screw Attack"], [CanFightBoss])
    ])
]

Sector2ZazabiZoneUpper.locations = [
    FusionLocation("Sector 2 (TRO) -- Dessgeega Dorm", False, [
        PONRRequirement(["Morph Ball"], [CanDestroyBombBlocks]),
        CanBombOrPowerBomb
    ])
]

Sector2NettoriZone.locations = [
    FusionLocation("Sector 2 (TRO) -- Nettori Arena", True, [
        CanFightMidgameBoss,
        CanFightBossOnAdvanced
    ]),
    FusionLocation("Sector 2 (TRO) -- Overgrown Cache", False, [HasMorph]),
    FusionLocation("Sector 2 (TRO) -- Puyo Palace", False, [
        PONRRequirement(["Nothing"], []),
        Requirement([], [CanJumpHigh, CanDoSimpleWallJump])
    ])
]
