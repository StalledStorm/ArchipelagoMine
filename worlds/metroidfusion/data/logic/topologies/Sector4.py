from ..Connection import Connection
from ..Requirement import PONRRequirement
from ..VariableConnection import VariableConnection
from ..Requirements import *
from ..FusionLocation import FusionLocation

from ..regions.MainDeck import SectorHubElevator4Top
from ..regions.Sector2 import Sector2TubeRight
from ..regions.Sector4 import *
from ..regions.Sector5 import Sector5NightmareHub
from ..regions.Sector6 import Sector6TubeLeft

Sector4Hub.connections = [
    VariableConnection(SectorHubElevator4Top, []),
    Connection(Sector4UpperZone, [
        PONRRequirement([], [CanBombOrPowerBomb], level_1_e_tanks),
        CanDrainAQARequirement(["Speed Booster"], [CanBombOrPowerBomb], level_1_e_tanks),
        CanPowerBombRequirement(["Space Jump"], [], level_1_e_tanks)
    ], one_way=True),
    Connection(Sector4DataZone, [
        CanDrainAQARequirement(["Missile Data", "Diffusion Missile"], [HasMorph]),
        CanDrainAQARequirement(["Ice Beam", "Wave Beam"], [HasMorph])
    ]),
    Connection(Sector4RightWaterZone, [
        CanDrainAQARequirement(["Morph Ball", "Missile Data", "Diffusion Missile", "Gravity Suit"], [HasSpeedBooster, HasScrewAttack]),
        CanDrainAQARequirement(["Morph Ball", "Ice Beam", "Wave Beam", "Gravity Suit"], [HasSpeedBooster, HasScrewAttack])
    ]),
    Connection(Sector4RightWaterZoneSave, [
        CanDrainAQARequirement(["Missile Data", "Diffusion Missile", "Gravity Suit"], [CanBomb]),
        CanDrainAQARequirement(["Ice Beam", "Wave Beam", "Gravity Suit"], [CanBomb]),
        CanDrainAQARequirement(["Missile Data", "Diffusion Missile", "Hi-Jump"], [HasMorph]),
        CanDrainAQARequirement(["Ice Beam", "Wave Beam", "Hi-Jump"], [HasMorph])
    ]),
]


Sector4TubeRight.connections = [
    VariableConnection(Sector6TubeLeft, [HasScrewAttack]),
    Connection(Sector4RightDataZone, [
        PONRRequirement(["Morph Ball"], [HasMissile]),
        Requirement(["Missile Data"], [CanBallJump])
    ], one_way=True),
]

Sector4TubeLeft.connections = [
    VariableConnection(Sector2TubeRight, []),
    Connection(Sector4RightWaterZone, [
        Requirement(["Gravity Suit", "Screw Attack"], [HasSpaceJump, CanDoSimpleWallJump])
    ])
]

Sector4UpperZone.connections = [
    Connection(Sector4Hub, [
        PONRRequirement(["Speed Booster"], [CanDrainAQA]),
        CanDrainAQARequirement(["Speed Booster"], [CanBombOrPowerBomb]),
        Requirement(["Space Jump"], [CanPowerBomb])
    ], one_way=True),
    Connection(Sector4BeforePumpControlZone, [
        PONRRequirement([], [CanBombOrPowerBomb]),
        CanBombOrPowerBombRequirement([], [CanJumpHigh, CanDoSimpleWallJump]),
        CanDrainAQARequirement([], [CanJumpHigh, CanDoBeginnerShinespark])
    ], one_way=True),
    Connection(Sector4ReservoirVault, [HasSpaceJump, CanDoSimpleWallJump])
]

Sector4BeforePumpControlZone.connections = [
    Connection(Sector4PumpControl, [
        Level1KeycardRequirement([], [HasSpeedBooster])
    ], one_way=True),
    Connection(Sector4UpperWaterZone, [
        CanDrainAQARequirement(["Gravity Suit"], [HasKeycard4])
    ], one_way=True),
    Connection(Sector4SerrisZone, [
        PONRRequirement(["Hi-Jump"], [CanBombOrPowerBomb]),
        PONRRequirement(["Morph Ball", "Bomb Data", "Gravity Suit"], []),
        Requirement(["Hi-Jump", "Speed Booster"], [CanBombOrPowerBomb]),
        Requirement(["Morph Ball", "Bomb Data", "Gravity Suit"], [HasSpeedBooster, CanDoSimpleWallJump])
    ], one_way=True),
    Connection(Sector4UpperZone, [
        PONRRequirement(["Morph Ball", "Speed Booster"], [CanDrainAQA]),
        CanBombOrPowerBombRequirement([], [CanJumpHigh, CanDoSimpleWallJump]),
        CanDrainAQARequirement([], [CanJumpHigh, CanDoBeginnerShinespark])
    ], one_way=True)
]

Sector4SerrisZone.connections = [
    Connection(Sector4BeforePumpControlZone, [
        CanBallJumpAndBombRequirement(["Gravity Suit"], [CanDoSimpleWallJump, HasSpaceJump])
    ]),
    Connection(Sector4ReservoirVault, [HasSpeedBooster], one_way=True)
]

Sector4ReservoirVault.connections = [
    Connection(Sector4UpperZone, [], one_way=True)
]

Sector4PumpControl.connections = [
    Connection(Sector4BeforePumpControlZone, [
        Requirement(["Level 1 Keycard"], [CanBallJump, CanDoBeginnerShinespark])
    ], one_way=True)
]

Sector4UpperWaterZone.connections = [
    Connection(Sector4BeforePumpControlZone, [
        CanDrainAQARequirement(["Level 4 Keycard"], [HasHiJump, HasGravity])
    ]),
    Connection(Sector5NightmareHub, [
        Requirement(["Gravity Suit", "Speed Booster"], [CanJumpHigh], level_3_e_tanks)
    ], one_way=True),
    Connection(Sector4CargoHold, [CanScrewAttackUnderwater]),
    Connection(Sector4UpperSecurityZone, [
        PONRRequirement([], [CanSpeedBoosterUnderwater], level_4_e_tanks),
        CanBallJumpAndBombRequirement(["Speed Booster", "Gravity Suit", "Level 4 Keycard"], [
            CanFightMidgameBossRequirement(["Wave Beam", "Ice Beam"], [HasSpaceJump, CanDoSimpleWallJump]),
            CanFightMidgameBossRequirement(["Missile Data", "Diffusion Missile"], [HasSpaceJump, CanDoSimpleWallJump])
        ], level_4_e_tanks),
        Requirement(["Speed Booster", "Morph Ball"], [CanScrewAttackUnderwater], level_4_e_tanks)
    ], one_way=True)
]

Sector4CargoHold.connections= [
    Connection(Sector4UpperSecurityZone, [
        Requirement(["Gravity Suit"], [CanBomb], level_4_e_tanks),
        Requirement(["Morph Ball"], [HasHiJump], level_4_e_tanks)
    ])
]

Sector4UpperSecurityZone.connections= [
    Connection(Sector4CargoHold, [
        PONRRequirement([], [HasMorph])
    ], one_way=True),
    Connection(Sector4SecurityZone, [
        PONRRequirement(["Nothing"], [])
    ], one_way=True)
]

Sector4SecurityZone.connections = [
    Connection(Sector4RightWaterZoneSave, [
        CanFightMidgameBossRequirement(["Morph Ball", "Gravity Suit", "Level 4 Keycard"], [
            HasSpaceJump, CanDoSimpleWallJump, CanDoAdvancedShinespark
        ], level_4_e_tanks),
        CanScrewAttackUnderwaterRequirement(["Morph Ball", "Level 4 Keycard"], [
            HasSpaceJump, CanDoSimpleWallJump, CanDoAdvancedShinespark
        ], level_4_e_tanks)
    ]),
    Connection(Sector4LowerSecurityZone, [
        PONRRequirement([], [HasKeycard4]),
        PONRRequirement(["Missile Data", "Morph Ball"], [
            HasGravityRequirement([], [CanBomb, HasScrewAttack]),
            HasHiJumpRequirement([], [CanBomb]),
            CanPowerBomb
        ])
    ], one_way=True),
    Connection(Sector4UpperSecurityZone, [
        Requirement(["Gravity Suit"], [HasSpaceJump]),
        CanDoAdvancedShinesparkRequirement(["Level 4 Keycard", "Gravity Suit"], [HasScrewAttack, CanPowerBomb]),
        CanDoAdvancedShinesparkRequirement(["Level 4 Keycard", "Gravity Suit", "Missile Data"], [CanBomb])
    ]),
    #Connection(Sector4UpperWaterZone, [
        #CanDoExpertShinesparkRequirement(
            #["Space Jump", "Gravity Suit", "Hi-Jump", "Level 4 Keycard"],
            #[CanPowerBomb], level_4_energy_tanks)
    #])
]

Sector4LowerSecurityZone.connections = [
    Connection(Sector4SecurityRoom, [
        PONRRequirement(["Level 4 Keycard"], []),
        PONRRequirement(["Morph Ball"], [
            CanPowerBomb,
            CanBeatToughEnemyRequirement([], [CanScrewAttackUnderwater, CanBomb])
        ])
    ], one_way=True),
    Connection(Sector4SecurityZone, [
        Level4KeyCardRequirement(["Gravity Suit"], [HasSpaceJump, CanDoSimpleWallJump]),
        CanPowerBombRequirement(["Gravity Suit", "Missile Data"], [HasSpaceJump, CanDoSimpleWallJump]),
        CanScrewAttackUnderwaterRequirement(["Missile Data", "Morph Ball"], [HasSpaceJump, CanDoSimpleWallJump])
    ])
]

Sector4SecurityRoom.connections = [
    Connection(Sector4LowerSecurityZone, [
        Level4KeycardRequirement(["Gravity Suit"], [HasSpaceJump, CanDoSimpleWallJump])
    ])
]

Sector4RightWaterZone.connections = [
    Connection(Sector4RightDataZone, [
        PONRRequirement(["Gravity Suit", "Morph Ball", "Missile Data"], [CanFreezeEnemies, HasSpaceJump]),
        CanDiffusionMissileRequirement(["Morph Ball"], [HasGravity])
    ], one_way=True),
    Connection(Sector4TubeLeft, [
        PONRRequirement(["Screw Attack"], [HasGravity])
    ], one_way=True),
    Connection(Sector4RightWaterZoneSave, [
        HasGravityRequirement([], [HasScrewAttack]),
        PONRRequirement(["Gravity Suit"], [CanDoBeginnerShinespark])
    ], one_way=True)
]

Sector4RightWaterZoneSave.connections = [
    Connection(Sector4SecurityZone, [
        PONRRequirement(["Morph Ball", "Level 4 Keycard"], [CanFightMidgameBoss, CanScrewAttackUnderwater], level_4_e_tanks)
    ], one_way=True),
    Connection(Sector4RightWaterZone, [
        PONRRequirement(["Morph Ball", "Hi-Jump", "Gravity Suit", "Speed Booster"], [CanFreezeEnemies]),
        PONRRequirement(["Morph Ball", "Bomb Data", "Gravity Suit", "Speed Booster"], [CanFreezeEnemies]),
        HasGravityRequirement([], [HasScrewAttack])
    ], one_way=True)
]

Sector4DataZone.connections = [
    Connection(Sector4RightDataZone, [
        Level4KeycardRequirement([], [CanBombOrPowerBomb])
    ])
]

Sector4RightDataZone.connections = [
    Connection(Sector4TubeRight, [CanBallJumpRequirement([], [CanDiffusionMissile])]),
    Connection(Sector4RightWaterZone, [
        PONRRequirement(["Morph Ball"], [CanDiffusionMissile]),
        HasGravityRequirement(["Morph Ball"], [CanDiffusionMissile])
    ], one_way=True)
]

Sector4Hub.locations = [
    FusionLocation("Sector 4 (AQA) -- Drain Pipe", False, [
        CanDrainAQARequirement(["Morph Ball"], [CanDefeatMediumGeron, HasWaveBeam])
    ]),
    FusionLocation("Sector 4 (AQA) -- Reservoir East", False, [
        CanDrainAQARequirement([], [CanPowerBomb])
    ])
]

Sector4PumpControl.locations = [
    FusionLocation("Sector 4 (AQA) -- Pump Control Unit", False, [
        PONRRequirement(["Morph Ball"], [CanDrainAQA]),
        CanDrainAQARequirement([], [CanBallJump])
    ])
]

Sector4BeforePumpControlZone.locations =[
    FusionLocation("Sector 4 (AQA) -- C-Cache", False, [
        Requirement(["Morph Ball"], [CanDestroyBombBlocks]),
        Requirement(["Level 1 Keycard", "Morph Ball"], [CanDoBeginnerShinespark])
    ])
]

Sector4UpperZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Broken Bridge", False, [HasMorph]),
    FusionLocation("Sector 4 (AQA) -- Waterway", False, [
        CanDrainAQARequirement(["Speed Booster"], [HasMorph])
    ])
]

Sector4ReservoirVault.locations = [
    FusionLocation("Sector 4 (AQA) -- Reservoir Vault -- Lower Item", False, [
        Requirement(["Missile Data"], [CanBallJumpAndBomb])
    ]),
    FusionLocation("Sector 4 (AQA) -- Reservoir Vault -- Upper Item", False, [
        CanBallJumpAndBomb
    ])
]

Sector4SerrisZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Serris Arena", True, [
        Requirement(["Hi-Jump"], [CanFightBoss]),
        Requirement(["Space Jump"], [CanFightBoss])
    ])
]

Sector4CargoHold.locations = [
    FusionLocation("Sector 4 (AQA) -- Cargo Hold to Sector 5 (ARC)", False, [])
]

Sector4UpperSecurityZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Yard Firing Range", False, [])
]

Sector4SecurityZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Cheddar Bay", False, [
        HasMissileRequirement(["Gravity Suit", "Morph Ball"], [CanBomb, HasScrewAttack]),
        HasMissileRequirement([], [CanPowerBomb]),
        HasGravityRequirement(["Level 4 Keycard", "Morph Ball"], [HasScrewAttack, CanPowerBomb])
    ]),
    FusionLocation("Sector 4 (AQA) -- Aquarium Pirate Tank", False, [
        PONRRequirement([], [CanPowerBomb]),
        CanPowerBombRequirement(["Gravity Suit"], [HasSpaceJump, CanFreezeEnemies])
    ])
]

Sector4LowerSecurityZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Sanctuary Cache", False, [
        CanBombRequirement(["Gravity Suit", "Wave Beam"], [CanBeatToughEnemy]),
        CanBombRequirement(["Gravity Suit", "Power Bomb Data"], [HasMissile]),
        CanBombOrPowerBombRequirement(["Hi-Jump", "Wave Beam"], [CanBeatToughEnemy]),
        CanPowerBombRequirement(["Hi-Jump"], [HasMissile])
    ])
]

Sector4SecurityRoom.locations = [
    FusionLocation("Sector 4 (AQA) -- Level 4 Security Room", True, [])
]

Sector4RightWaterZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Aquarium Kago Storage -- Left Item", False, [
        CanSpeedBoosterUnderwater,
        CanScrewAttackUnderwater
    ]),
    FusionLocation("Sector 4 (AQA) -- Aquarium Kago Storage -- Right Item", False, [
        CanSpeedBoosterUnderwater
    ])
]

Sector4DataZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Data Room", True, [
        CanDrainAQARequirement([], [HasKeycard4])
    ])
]
