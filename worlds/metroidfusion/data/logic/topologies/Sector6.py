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
    Connection(Sector6Crossroads, [CanDamageMediumGeron, CanDamageAnyGeron, HasScrewAttack]),
    Connection(Sector6Crossroads, [CanDoBeginnerShinespark], one_way=True),
    Connection(Sector6TubeLeft, [
        PONRRequirement("PONR - Enter Sector 6 West Tube", [
            HasScrewAttack()
        ])
    ], one_way=True)
]

Sector6TubeLeft.connections = [
    VariableConnection(Sector4TubeRight, []),
    Connection(Sector6Hub, [
        HasScrewAttack("Leave Sector 6 West Tube", [
            CanJumpHigh(),
            CanDoSimpleWallJump(),
            CanDoBeginnerShinespark()
        ])
    ])
]

Sector6TubeRight.connections = [
    VariableConnection(Sector5TubeLeft, []),
    Connection(Sector6Crossroads, [
        HasScrewAttack()
    ])
]

Sector6Crossroads.connections = [
    Connection(Sector6BeforeXBOXZone, [
        CanPowerBomb("Approach X-B.O.X. Arena", [
            HasVaria()
        ], [
            HasKeycard4()
        ], [
            # Return from X-B.O.X. Arena?
            HasSpaceJump(),
            CanDoSimpleWallJump(),
            CanFreezeEnemies()
        ])
    ]),
    Connection(Sector6Catacombs, [
        HasSpeedBooster("Nocturnal Playground <-> Catacombs", [
            CanDoAdvancedShinespark(),
            CanDoBeginnerShinespark(None, [
                HasHiJump()
            ]),
            PONRRequirement("PONR - Nocturnal Playground -> Catacombs")
        ]),
    ]),
    Connection(Sector6AfterVariaCoreXZone, [
        HasMorph("Nocturnal Playground <-> Post-Varia Core X Zone", [
            HasScrewAttack()
        ], [
            HasVaria(),
            PONRRequirement("PONR - Nocturnal Playground -> Post-Varia Core X Zone")
        ])
    ])
]

Sector6Catacombs.connections = [
    Connection(Sector6Crossroads, [
        CanDoBeginnerShinespark([], [
            HasHiJump(),
            HasSpaceJump()
        ]),
        CanDoAdvancedShinespark([], [])
    ]),
    Connection(Sector6BeforeVariaCoreXZone, [
        Requirement("Catacombs -> Pre-Varia Core X Zone", [
            CanBomb(),
            CanPowerBomb()
        ], [
            HasKeycard2("Can pass through Sector 6 Data", [
                HasVaria()
            ]),
            PONRRequirement("PONR - Catacombs -> Pre-Varia Core X Zone")
        ])
    ], one_way=True)
]

Sector6BeforeXBOXZone.connections = [
    Connection(Sector6XBOXZone, [
        Requirement("Enter X-B.O.X. Arena", [
            HasScrewAttack("Ascend X-B.O.X. Garage", [
                CanJumpHigh()
            ]),
            HasWaveBeam("Exit to Restricted Zone"),
            PONRRequirement("PONR - Enter X-B.O.X. Arena")
        ], energy_tanks_needed=level_4_e_tanks)
    ], one_way=True)
]

Sector6XBOXZone.connections = [
    Connection(Sector6AfterXBOXZone, [
        CanFightLateGameBoss(),
        CanFightLateGameBossOnAdvanced(),
        CanFightBossOnExpert()
    ])
]

Sector6AfterXBOXZone.connections = [
    Connection(Sector6BeforeXBOXZone, [
        HasScrewAttack("Ascend X-B.O.X. Garage", [
            CanJumpHigh()
        ]),
    ], one_way=True),
    Connection(Sector6XBOXSave, [
        Requirement("Go to X-B.O.X. Save Station", [
            HasSpaceJump(),
            CanFreezeEnemies(),
            CanDoSimpleWallJump(None, [
                HasHiJump()
            ]),
            CanDoAdvancedWallJump(),
            # CanDoBeginnerShinespark(None, [
            #     HasKeycard4()
            # ], [
            #     #future CanDoJumpExtend()
            # ])
            PONRRequirement("PONR - X-B.O.X. Save Station")
        ], energy_tanks_needed=level_4_e_tanks)
    ], one_way=True)
]

Sector6XBOXSave.connections = [
    Connection(Sector6XBOXZone, [
        Requirement("Ascend from X-B.O.X. Save Station", [
            HasSpaceJump(),
            CanFreezeEnemies(),
            CanDoSimpleWallJump(None, [
                HasHiJump()
            ]),
            CanDoAdvancedWallJump(),
            # CanDoBeginnerShinespark(None, [
            #     HasKeycard4()
            # ], [
            #     #future CanDoJumpExtend()
            # ])
        ], energy_tanks_needed=level_4_e_tanks)
    ], one_way=True),
    Connection(Sector6RestrictedZone, [
        HasWaveBeam("Exit to Restricted Zone", [
            HasScrewAttack(None, [
                HasSpaceJump()
            ]),
            HasSpeedBooster(),
            PONRRequirement("PONR - Exit to Restricted Zone")
        ], [
            HasKeycard4()
        ]),
    ], one_way=True)
]

Sector6RestrictedZone.connections = [
    Connection(Sector6XBOXSave, [
        HasScrewAttack("Leave Restricted Zone to Sector 6", [
            HasSpaceJump()
        ], [
            HasMorph()
        ], [
            HasWaveBeam(),
            PONRRequirement("PONR - Leave Restricted Zone to Sector 6")
        ], [
            HasKeycard4()
        ])
    ]),
    Connection(Sector6RestrictedZoneElevatorToTourian, [
        HasSpeedBooster(None, [
            HasKeycard4()
        ]),
    ], one_way=True)
    #One day, elevator shuffle PONR pathing logic. One day.
]

Sector6RestrictedZoneElevatorToTourian.connections = [
    VariableConnection(Sector1TourianHubElevatorTop, [
        HasKeycard4()
    ])
]

Sector6BeforeVariaCoreXZone.connections = [
    Connection(Sector6Catacombs, [
        CanPowerBomb("Backwards Travel Pre-Varia Core X", [
            HasSpaceJump(),
            CanDoSimpleWallJump(None, [
                HasHiJump()
            ]),
            CanDoAdvancedWallJump()
        ]),
    ]),
    Connection(Sector6VariaCoreXZone, [
        HasKeycard2("Enter Varia Core X Arena", [
            CanFightVariaCoreX()
        ])
    ])
]

Sector6VariaCoreXZone.connections = [
    Connection(Sector6CavernsSave, [
        CanFightVariaCoreX()
    ])
]

Sector6AfterVariaCoreXZone.connections = [
    Connection(Sector6Crossroads, [
        HasVaria("Twin Caverns -> Crossroads", [
            HasMorph()
        ])
    ], one_way=True),
    Connection(Sector6VariaCoreXZone, [
        CanFightVariaCoreX()
    ], one_way=True)
]

Sector6CavernsSave.connections = [
    Connection(Sector6AfterVariaCoreXZone, [
        HasVaria()
    ])
]

Sector6Hub.locations = [
    FusionLocation("Sector 6 (NOC) -- Entrance Lobby", False, [
        Requirement("Enter Tunnel to Entrance Lobby Nook", [
            HasMorph(),
            CanBallJump("Skill Issue")
        ], [
            CanDestroyBombBlocks(),
            CanDoBeginnerShinespark()
        ])
    ])
]

Sector6Crossroads.locations = [
    FusionLocation("Sector 6 (NOC) -- Missile Mimic Lodge", False, [
        HasVaria("Nocturnal Shaft <-> Missile Mimic Lodge Item", [
            CanBomb(),
            CanPowerBomb()
        ], [
            # Deal with Mimic
            HasMissile(),
            CanDoAdvancedCombat()
        ])
    ]),
    FusionLocation("Sector 6 (NOC) -- Pillar Highway", False, [
        HasVaria("Nocturnal Shaft <-> Pillar Highway", [
            HasSpeedBooster()
        ], [
            CanBomb(),
            HasWaveBeam()
        ], [
            HasScrewAttack()
        ])
    ]),
    FusionLocation("Sector 6 (NOC) -- Vault", False, [
        CanBomb(),
        CanPowerBomb()
    ])
]

Sector6Catacombs.locations = [
    FusionLocation("Sector 6 (NOC) -- Catacombs", False, [])
]

Sector6BeforeXBOXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Spaceboost Alley -- Lower Item", False, [
        CanEnterSpaceboostAlley("Can Grab Spaceboost Alley Lower Item", [
            HasSpaceJump()
        ])
    ]),
    FusionLocation("Sector 6 (NOC) -- Spaceboost Alley -- Upper Item", False, [
        CanEnterSpaceboostAlley("Can Grab Spaceboost Alley Upper Item")
    ])
]

Sector6XBOXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- X-B.O.X. Arena", True, [
        CanFightLateGameBoss(),
        CanFightLateGameBossOnAdvanced(),
        CanFightBossOnExpert()
    ])
]

Sector6AfterXBOXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- X-B.O.X. Garage -- Lower Item", False, [
        HasWaveBeam()
    ]),
    FusionLocation("Sector 6 (NOC) -- X-B.O.X. Garage -- Upper Item", False, [
        HasScrewAttack("Can Grab X-B.O.X. Garage Upper Item", [
            CanJumpHigh()
        ], [
            CanBallJump()
        ], [
            CanBomb(),
            CanPowerBomb()
        ], [
            CanUseDiffusionMissile(),
            HasIceBeam(None, [  # NEEDS TESTING TO CONFIRM THIS IS POSSIBLE
                HasWaveBeam()
            ])
        ])
    ])
]

Sector6RestrictedZone.locations = [
    FusionLocation("Main Deck -- Restricted Airlock", False, [
        HasSpeedBooster()
    ])
]

Sector6BeforeVariaCoreXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Zozoro Wine Cellar", False, [
        Requirement("Can Obtain Zozoro Wine Cellar Item", [
            CanBomb(),
            CanPowerBomb()
        ], [
            CanJumpHigh(),
            CanFreezeEnemies(),
            #future CanDoAdvancedJumpBombJump()
        ])
    ])
]

Sector6VariaCoreXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Varia Core-X Arena", True, [
        CanFightVariaCoreX()
    ])
]

Sector6AfterVariaCoreXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Twin Caverns West -- Lower Item", False, [
        HasMorph("Can Obtain Twin Caverns West Lower Item", [
            CanJumpHigh(),
            Requirement("Jump Good")
        ])
    ]),
    FusionLocation("Sector 6 (NOC) -- Twin Caverns West -- Upper Item", False, [])
]
