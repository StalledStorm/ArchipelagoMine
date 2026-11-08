from mars_patcher.mf.constants.sprites import SpriteIdMF

MF_TILESET_ALT_PAL_ROWS = {
    0x46F134: 0xD,  # 08
    0x4CCCC0: 0xD,  # 09, 40
    0x407E9C: 0xB,  # 0B, 1E
    0x498808: 0xA,  # 0E
    0x46E6F4: 0xD,  # 12
    0x46DCB4: 0xD,  # 13
    0x406B5C: 0xD,  # 19
    0x46E2F4: 0xD,  # 1B
    0x4CC5C0: 0xD,  # 1F
    0x4CC780: 0xD,  # 20
    0x4F21F8: 0xD,  # 21
    0x4F23B8: 0xD,  # 22
    0x4F27B8: 0xC,  # 28
    0x498AC8: 0xB,  # 29
    0x4F2A58: 0xC,  # 2A
    0x5352F0: 0xC,  # 2B, 2F
    0x510868: 0xD,  # 30
    0x510A28: 0xD,  # 31
    0x5355D0: 0xD,  # 34
    0x46E4B4: 0xC,  # 38
    0x46E8B4: 0xD,  # 3D
    0x54D53C: 0xB,  # 3E
    0x40719C: 0xC,  # 43
    0x46E134: 0xC,  # 46
    0x4060DC: 0xD,  # 48
    0x46EF74: 0xD,  # 54
    0x535950: 0xC,  # 56
    0x407CDC: 0xD,  # 57
    0x498648: 0xD,  # 58
    0x535B10: 0xD,  # 5B
    0x4078DC: 0xD,  # 5E
}


# Animated palettes not included here are used for multiple tileset palettes
TILESET_ANIM_PALS = {
    0x40769C: 0x01,  # Navigation room
    0x407A9C: 0x02,  # Save room
    0x406F5C: 0x03,  # Recharge room
    0x405E9C: 0x04,  # Data room
    # 0x05 Docking bay
    0x46EA74: 0x07,  # Operations deck
    # 0x08 Main elevator top/bottom
    0x46BCD4: 0x09,  # Sector 1 elevator
    0x46BF94: 0x0A,  # Sector 2 elevator
    0x46C254: 0x0B,  # Sector 3 elevator
    0x46C514: 0x0C,  # Sector 4 elevator
    0x46C7D4: 0x0D,  # Sector 5 elevator
    0x46CA94: 0x0E,  # Sector 6 elevator
    0x4F27B8: 0x0F,  # Sector 3 glowing BG3
    0x4F2A58: 0x10,  # Meltdown alarm
    0x498AC8: 0x11,  # Stabilizer rooms
    0x54D0DC: 0x12,  # Sector 6 glowing BG3
    0x406D1C: 0x13,  # Security room
    # 0x14 Electrified water
    0x46DE74: 0x15,  # Near quarantine bay
    0x4F2578: 0x16,  # Boiler control room
    0x4F1D38: 0x17,  # Main boiler
    0x46ECB4: 0x18,  # Operations deck (SA-X fight)
    0x4F1F98: 0x19,  # Main boiler
    0x46E4B4: 0x1A,  # Auxiliary power
    0x46B814: 0x1B,  # Reactor silo
    # 0x1C Restricted lab alarm
    0x46AF14: 0x1D,  # Operations room
    0x40719C: 0x1E,  # Sector 2 flashing panels 1
    0x40741C: 0x1F,  # Sector 2 flashing panels 2
    0x46D554: 0x20,  # Restricted lab
}


EXCLUDED_ENEMIES_MF = {
    SpriteIdMF.SAX_ELEVATOR,
    SpriteIdMF.AREA_BANNER,
    SpriteIdMF.MESSAGE_BANNER,
    SpriteIdMF.SAX_TRO_1,
    SpriteIdMF.SAX_NOC,
    SpriteIdMF.SAX_ARC,
    SpriteIdMF.SAX_LAB,
    SpriteIdMF.SAX_BOSS,
    SpriteIdMF.SAX_MONSTER,
    SpriteIdMF.SAX_OMEGA,
    SpriteIdMF.SAX_TRO_2,
}


ENEMY_GROUPS_MF = {
    "Zebesian": [
        SpriteIdMF.ZEBESIAN_WALL,
        SpriteIdMF.ZEBESIAN_GROUND,
        SpriteIdMF.GOLD_ZEBESIAN,
        SpriteIdMF.ZEBESIAN_AQUA,
        SpriteIdMF.ZEBESIAN_PRE_AQUA,
    ],
    "Zeela": [SpriteIdMF.ZEELA, SpriteIdMF.RED_ZEELA],
    "Sciser": [SpriteIdMF.SCISER, SpriteIdMF.GOLD_SCISER],
    "BeamCoreX": [
        SpriteIdMF.CHARGE_BEAM_CORE_X,
        SpriteIdMF.WIDE_BEAM_CORE_X,
        SpriteIdMF.PLASMA_BEAM_CORE_X,
        SpriteIdMF.WAVE_BEAM_CORE_X,
    ],
    "Zoro": [
        SpriteIdMF.ZORO,
        SpriteIdMF.BLUE_ZORO,
        SpriteIdMF.ZORO_COCOON,
        SpriteIdMF.ZORO_HUSK,
    ],
    "FakeTank": [SpriteIdMF.FAKE_ENERGY_TANK, SpriteIdMF.FAKE_MISSILE_TANK],
}


NETTORI_EXTRA_PALS = [
    (0x36A480, 1),  # Medium health palette
    (0x36A4A0, 1),  # Low health palette
    (0x36A4C0, 3),  # Animated palette
]
