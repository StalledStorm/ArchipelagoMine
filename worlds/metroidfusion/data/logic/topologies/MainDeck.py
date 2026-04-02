from ..Connection import Connection
from ..FusionLocation import FusionLocation
from ..regions.MainDeck import *
from ..regions.Sector1 import Sector1Hub
from ..regions.Sector2 import Sector2Hub, Sector2NettoriZone
from ..regions.Sector3 import Sector3Hub
from ..regions.Sector4 import Sector4Hub
from ..regions.Sector5 import Sector5Hub
from ..regions.Sector6 import Sector6Hub
from ..Requirement import Requirement, PONRRequirement
from ..Requirements import *
from ..VariableConnection import VariableConnection

# Region Connections
AuxiliaryReactor.connections = [
    Connection(ReactorZone, [], one_way=True),
    Connection(YakuzaZone, [
        PONRRequirement()
    ], one_way=True)
]

HabitationDeckElevatorBottom.connections = [
    VariableConnection(HabitationDeckElevatorTop, [])
]

HabitationDeckElevatorTop.connections = [
    VariableConnection(HabitationDeckElevatorBottom, []),
    Connection(HabitationDeck, [
        HasKeycard2("Open Door with Level 2 Keycard")
    ])
]

MainDeckHub.connections = [
    Connection(OperationsDeckElevatorBottom, []),
    Connection(VentilationZone, [
        CanDamageSmallGeron("Kill Lower Vent Geron"),
        CanDamageAnyGeron("Kill Lower Vent Geron with NerfGeronWeakness Disabled")
    ]),
    Connection(LowerArachnusArena, [
        HasMorph("Can Enter and Leave Arachnus Fight Arena")
    ]),
    Connection(UpperArachnusArena, [
        HasMorph("Use Hidden Screw Attack Tunnel", [
            CanJumpHigh(),
            CanDoSimpleWallJump()
        ], [
            HasScrewAttack()
        ])
    ]),
    Connection(HabitationDeckElevatorBottom, [
        HasKeycard2("Open Elevator Door with Level 2 Keycard")
    ]),
    Connection(SectorHubElevatorTop, [
        HasMorph("Use Morph Tunnel"),
        CanDoAdvancedShinespark("Can Shinespark to Sector Hub Elevator")
    ]),
    Connection(ReactorZone, [
        HasMorph("Can Enter Reactor Zone", [
            HasKeycard4("Open Door to Reactor Zone with Level 4 Keycard"),
            CanPowerBomb("Can Blow Up Wall to Reactor Zone")
        ], energy_tanks_needed=level_2_e_tanks)
    ]),
    Connection(NexusStorage, [
        HasKeycard2("Can Enter Nexus Storage", [
            CanDamageLargeGeron(),
            CanDamageAnyGeron()
        ])
    ])
]

OperationsDeckElevatorBottom.connections = [
    VariableConnection(OperationsDeckElevatorTop, [])
]

OperationsDeckElevatorTop.connections = [
    VariableConnection(OperationsDeckElevatorBottom, []),
    Connection(OperationsDeck, [])
]

OperationsDeck.connections = [
    Connection(VentilationZone, [
        HasMissile("Can Break Ventilation Cap")
    ], one_way=True)
]

ReactorZone.connections = [
    Connection(YakuzaZone, [
        HasMorph("Can Access Yakuza - Vanilla Route", [
            CanDamageToughEnemy("Can Kill Kihunter, Pirate, and Eyedoor")
        ], [
            CanBomb("Destroy Block with Bomb"),
            CanPowerBomb("Destroy Block with Power Bomb"),
            HasWaveBeam("Destroy Block with Wave Beam")
        ], [
            HasSpaceJump("Can Enter and Fly out of Yakuza's Arena"),
            PONRRequirement("PONR - Can Enter Yakuza'a Arena")
        ]),
    ], one_way=True),
    Connection(AuxiliaryReactor, [
        HasWaveBeam("Can Open Auxiliary Gate Backwards")
    ]),
    Connection(Sector2NettoriZone, [
        HasSpaceJump("Can Get to Sector 2 Backdoor", [
            CanDamageToughEnemy("Can Kill Kihunter")
        ], [
            CanBomb("Traverse Tunnel with Bomb"),
            CanPowerBomb("Traverse Tunnel with Power Bomb")
        ])
    ], one_way=True)
]

SectorHubElevatorTop.connections = [
    Connection(MainDeckHub, [
        PONRRequirement("PONR - Enter Main Deck Hub with Speed Booster - Trickless", [
            HasSpeedBooster()
        ])
    ], one_way=True),
    VariableConnection(SectorHubElevatorBottom, [])
]

SectorHubElevatorBottom.connections = [
    VariableConnection(SectorHubElevatorTop, []),
    Connection(SectorHubElevator1Top, []),
    Connection(SectorHubElevator2Top, []),
]

SectorHubElevator1Top.connections = [
    VariableConnection(Sector1Hub, []),
    Connection(SectorHubElevator3Top, [SectorHubLevel1KeycardRequirement]),
]

SectorHubElevator2Top.connections = [
    VariableConnection(Sector2Hub, []),
    Connection(SectorHubElevator4Top, [SectorHubLevel1KeycardRequirement]),
]

SectorHubElevator3Top.connections = [
    VariableConnection(Sector3Hub, []),
    Connection(SectorHubElevator5Top, [SectorHubLevel2KeycardRequirement]),
]

SectorHubElevator4Top.connections = [
    VariableConnection(Sector4Hub, []),
    Connection(SectorHubElevator6Top, [SectorHubLevel2KeycardRequirement])
]

SectorHubElevator5Top.connections = [
    VariableConnection(Sector5Hub, [])
]

SectorHubElevator6Top.connections = [
    VariableConnection(Sector6Hub, [])
]

UpperArachnusArena.connections = [
    Connection(LowerArachnusArena, [
        PONRRequirement("PONR - Vanilla Route"),
        HasMorph("Vanilla Route")
    ], one_way=True),
    Connection(MainDeckHub, [
        HasScrewAttack("Use Screw Attack Tunnel, then exit left", [
            HasMorph()
        ])
    ], one_way=True)
]

VentilationZone.connections = [
    Connection(UpperArachnusArena, [
        CanDamageToughEnemy("Enter Arachnus Arena through Eyedoor", [
            HasMorph("Can Leave Arachnus Arena"),
            PONRRequirement("PONR - Can Enter Arachnus Fight")
        ])
    ], one_way=True)
]

YakuzaZone.connections = [
    Connection(AuxiliaryReactor, [
        HasSpaceJump("Leave Yakuza Arena")
    ])
]

# Item Locations
AuxiliaryReactor.locations = [
    FusionLocation("Main Deck -- Auxiliary Power Station", True, [])
]

HabitationDeck.locations = [
    FusionLocation("Main Deck -- Habitation Deck -- Animals", True, [
        HasKeycard2("Enter Habitation Deck", [
            HasSpaceJump("Vanilla Route to Animals Terminal with Space Jump", [
                HasSpeedBooster()
            ]),
            CanFreezeEnemies("Vanilla Route to Animals Terminal without Space Jump", [
                HasHiJump(),
                CanDoAdvancedWallJump()
            ], [
                HasSpeedBooster()
            ]),
            CanFreezeEnemies("Go Backwards through Gates on Lower Floor", [
                CanJumpHigh(),
                CanDoSimpleWallJump()
            ], [
                HasWaveBeam()
            ]),
        ])
    ]),
    FusionLocation("Main Deck -- Habitation Deck -- Lower Item", False, [
        HasKeycard2("Enter Habitation Deck", [
            HasSpaceJump("Vanilla Route to Animals with Space Jump"),
            HasWaveBeam("Go Backwards through Gates on Lower Floor"),
            CanFreezeEnemies("Vanilla Route to Animals without Space Jump", [
                HasHiJump(),
                CanDoAdvancedWallJump()
            ])
        ])
    ])
]

LowerArachnusArena.locations = [
    FusionLocation("Main Deck -- Arachnus Arena -- Core X", True, [
        CanDamageCoreX()
    ])
]

MainDeckHub.locations = [
    FusionLocation("Main Deck -- Cubby Hole", False, [
        HasMorph()
    ]),
    FusionLocation("Main Deck -- Genesis Speedway", False, [
        CanPowerBomb("Can Enter Genesis Speedway Tunnel", [
            CanBallJump()
        ])
    ]),
    FusionLocation("Main Deck -- Quarantine Bay", False, []),
    FusionLocation("Main Deck -- Station Entrance", False, [
        CanPowerBomb("Blow Up the Floor")
    ]),
    FusionLocation("Main Deck -- Sub-Zero Containment", False, [
        HasKeycard3("Open Door with Level 3 Keycard", [
            HasVaria()
        ])
    ])
]

NexusStorage.locations = [
    FusionLocation("Main Deck -- Nexus Storage", False, [
        CanBallJump("Can Access Nexus Storage Item", [
            PONRRequirement("PONR - Collect Nexus Storage Item",
                            hard_items_needed={"Hi-Jump"}),
            CanBomb(),
            CanPowerBomb()
        ])
    ])
]

OperationsDeck.locations = [
    FusionLocation("Main Deck -- Operations Deck Data Room", True, [])
]

ReactorZone.locations = [
    FusionLocation("Main Deck -- Silo Catwalk", False, [
        CanDamageToughEnemy("Kill Pirates")
    ]),
    FusionLocation("Main Deck -- Silo Scaffolding", False, [
        HasMorph("Grab Silo Scaffolding Item", [
            PONRRequirement("PONR - Silo Scaffolding"),
            CanJumpHigh(),
            CanDoAdvancedWallJump()
        ], [
            CanDamageToughEnemy("Kill Pirates"),
            CanDoExpertCombat("Avoid Pirates")
        ])
    ])
]

SectorHubElevatorTop.locations = [
    FusionLocation("Main Deck -- Main Elevator Cache", False, [
        HasSpeedBooster()
    ])
]

UpperArachnusArena.locations = [
    FusionLocation("Main Deck -- Arachnus Arena -- Upper Item", False, []),
    FusionLocation("Main Deck -- Attic", False, [
        HasMissile("Blast Open the Ceiling")
    ]),
]

VentilationZone.locations = [
    FusionLocation("Main Deck -- Operations Ventilation", False, []),
    FusionLocation("Main Deck -- Operations Ventilation Storage", False, [])
]

YakuzaZone.locations = [
    FusionLocation("Main Deck -- Yakuza Arena", True, [
        CanFightMidGameBoss(),
        CanFightMidGameBossOnAdvanced()
    ])
]
