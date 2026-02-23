from ..Connection import Connection
from ..Requirement import PONRRequirement
from ..VariableConnection import VariableConnection
from ..Requirements import *
from ..FusionLocation import FusionLocation

from ..regions.MainDeck import SectorHubElevator6Top
from ..regions.Sector1 import Sector1TourianHubElevatorTop
from ..regions.Sector4 import Sector4TubeRight
from ..regions.Sector5 import Sector5TubeLeft
from ..regions.Sector6 import *


Sector6Hub.connections = [
    VariableConnection(SectorHubElevator6Top, []),
    Connection(Sector6Crossroads, [CanDefeatMediumGeron, CanDoBeginnerShinespark]),
    Connection(Sector6TubeLeft, [
        PONRRequirement([], [HasScrewAttack])
    ], one_way=True)
]

Sector6TubeLeft.connections = [
    VariableConnection(Sector4TubeRight, []),
    Connection(Sector6Hub, [
        HasScrewAttackRequirement([], [CanJumpHigh, CanDoSimpleWallJump, CanDoBeginnerShinespark])
    ])
]

Sector6TubeRight.connections = [
    VariableConnection(Sector5TubeLeft, []),
    Connection(Sector6Crossroads, [HasScrewAttack])
]

Sector6Crossroads.connections = [
    Connection(Sector6BeforeXBOXZone, [
        Requirement(["Varia Suit", "Level 4 Keycard"], [CanPowerBomb])
    ]),
    Connection(Sector6Catacombs, [
        PONRRequirement([], [HasSpeedBooster]),
        CanFightBossRequirement(["Speed Booster", "Level 2 Keycard", "Varia Suit"], [CanBombOrPowerBomb])
    ], one_way=True),
    Connection(Sector6AfterVariaCoreXZone, [
        PONRRequirement(["Morph Ball"], [HasScrewAttack]),
        Requirement(["Morph Ball", "Varia Suit"], [HasScrewAttack]),
        CanFightBossRequirement(["Level 2 Keycard", "Morph Ball", "Power Bomb Data", "Screw Attack"], [HasSpaceJump, CanDoAdvancedWallJump])
    ], one_way=True)
]

Sector6Catacombs.connections = [
    Connection(Sector6Crossroads, [
        CanDoBeginnerShinesparkRequirement(["Hi-Jump"], [HasSpaceJump], level_1_e_tanks),
        CanDoAdvancedShinesparkRequirement([], [], level_1_e_tanks)
    ]),
    Connection(Sector6BeforeVariaCoreXZone, [
        PONRRequirement([], [CanBombOrPowerBomb]),
        CanFightBossRequirement(["Level 2 Keycard", "Varia Suit"], [CanBombOrPowerBomb])
    ], one_way=True)
]

Sector6BeforeXBOXZone.connections = [
    Connection(Sector6XBOXZone, [
        PONRRequirement(["Nothing"], [], level_4_e_tanks),
        HasScrewAttackRequirement([], [HasSpaceJump, CanDoSimpleWallJump], level_4_e_tanks),
        CanFreezeEnemiesRequirement(["Hi-Jump"], [HasScrewAttack], level_4_e_tanks)
    ], one_way=True)
]

Sector6XBOXZone.connections = [
    Connection(Sector6AfterXBOXZone, [
        CanFightLateGameBoss,
        CanFightLategameBossOnAdvanced,
        CanFightBossOnExpert
    ])
]

Sector6AfterXBOXZone.connections = [
    Connection(Sector6BeforeXBOXZone, [
        HasScrewAttackRequirement([], [HasSpaceJump, CanDoSimpleWallJump]),
        CanFreezeEnemiesRequirement(["Hi-Jump"], [HasScrewAttack])
    ], one_way=True),
    Connection(Sector6XBOXSave, [
        PONRRequirement(["Nothing"], []),
        Requirement([], [HasSpaceJump, CanFreezeEnemies, CanDoSimpleWallJumpWithHiJump, CanDoAdvancedWallJump], level_4_e_tanks),
        CanDoBeginnerShinesparkRequirement([], [CanDoSimpleWallJumpWithScrewAttack], level_4_e_tanks)
    ], one_way=True)
]

Sector6XBOXSave.connections = [
    Connection(Sector6XBOXZone, [
        Requirement([], [HasSpaceJump, CanFreezeEnemies, CanDoSimpleWallJumpWithHiJump, CanDoAdvancedWallJump], level_4_e_tanks),
        CanDoBeginnerShinesparkRequirement([], [CanDoSimpleWallJumpWithScrewAttack], level_4_e_tanks)
    ], one_way=True),
    Connection(Sector6RestrictedZone, [
        PONRRequirement([], [HasWaveBeam])
    ], one_way=True)
]

Sector6RestrictedZone.connections = [
    Connection(Sector6XBOXSave, [
        HasScrewAttackRequirement(["Wave Beam"], [HasSpaceJump, CanDoSimpleWallJump])
    ]),
    Connection(Sector6RestrictedZoneElevatorToTourian, [HasSpeedBooster], one_way=True)
    #One day, elevator shuffle PONR pathing logic. One day.
]

Sector6RestrictedZoneElevatorToTourian.connections = [
    VariableConnection(Sector1TourianHubElevatorTop, [HasKeycard4])
]

Sector6BeforeVariaCoreXZone.connections = [
    Connection(Sector6Catacombs, [
        CanPowerBombRequirement([], [HasSpaceJump, CanDoAdvancedWallJump])
    ]),
    Connection(Sector6VariaCoreXZone, [
        Requirement(["Level 2 Keycard"], [CanFightBoss])
    ])
]

Sector6VariaCoreXZone.connections = [
    Connection(Sector6CavernsSave, [CanFightBoss])
]

Sector6AfterVariaCoreXZone.connections = [
    Connection(Sector6Crossroads, [
        PONRRequirement([], [HasMorph]),
        HasVariaRequirement(["Morph Ball"], [HasScrewAttack]),
        CanFightBossRequirement(["Speed Booster", "Level 2 Keycard", "Varia Suit"], [CanBombOrPowerBomb])
    ], one_way=True),
    Connection(Sector6VariaCoreXZone, [
        PONRRequirement([], [CanFightBoss]),
        CanFightBossRequirement(["Level 2 Keycard", "Morph Ball", "Power Bomb Data", "Screw Attack"], [HasSpaceJump, CanDoAdvancedWallJump]),
    ], one_way=True)
]

Sector6CavernsSave.connections = [
    Connection(Sector6AfterVariaCoreXZone, [HasVaria])
]

Sector6Hub.locations = [
    FusionLocation("Sector 6 (NOC) -- Entrance Lobby", False, [
        CanBallJumpRequirement([], [CanDestroyBombBlocks, CanDoBeginnerShinespark])
    ])
]

Sector6Crossroads.locations = [
    FusionLocation("Sector 6 (NOC) -- Missile Mimic Lodge", False, [
        HasVariaRequirement([], [CanBombOrPowerBomb])
    ]),
    FusionLocation("Sector 6 (NOC) -- Pillar Highway", False, [
        HasVariaRequirement(["Screw Attack", "Speed Booster"], [CanBomb, HasWaveBeam])
    ]),
    FusionLocation("Sector 6 (NOC) -- Vault", False, [CanBallJumpAndBomb])
]

Sector6Catacombs.locations = [
    FusionLocation("Sector 6 (NOC) -- Catacombs", False, [])
]

Sector6BeforeXBOXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Spaceboost Alley -- Lower Item", False, [
        Requirement(["Level 4 Keycard", "Space Jump", "Screw Attack"], [HasSpeedBooster])
    ]),
    FusionLocation("Sector 6 (NOC) -- Spaceboost Alley -- Upper Item", False, [
        Requirement(["Level 4 Keycard", "Screw Attack"], [HasSpeedBooster])
    ])
]

Sector6XBOXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- X-B.O.X. Arena", True, [
        CanFightLateGameBoss,
        CanFightLategameBossOnAdvanced,
        CanFightBossOnExpert
    ])
]

Sector6AfterXBOXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- X-B.O.X. Garage -- Lower Item", False, [HasWaveBeam]),
    FusionLocation("Sector 6 (NOC) -- X-B.O.X. Garage -- Upper Item", False, [
        CanFreezeEnemiesRequirement(["Morph Ball", "Bomb Data", "Screw Attack"], [HasSpaceJump, CanDoSimpleWallJump]),
    ])
]

Sector6RestrictedZone.locations = [
    FusionLocation("Main Deck -- Restricted Airlock", False, [HasSpeedBooster])
]

Sector6BeforeVariaCoreXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Zozoro Wine Cellar", False, [
        CanBombOrPowerBombRequirement([], [CanJumpHigh, CanFreezeEnemies])
    ])
]

Sector6VariaCoreXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Varia Core-X Arena", True, [CanFightBoss])
]

Sector6AfterVariaCoreXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Twin Caverns West -- Lower Item", False, [
        Requirement(["Morph Ball"], [CanJumpHigh])
    ]),
    FusionLocation("Sector 6 (NOC) -- Twin Caverns West -- Upper Item", False, [])
]
