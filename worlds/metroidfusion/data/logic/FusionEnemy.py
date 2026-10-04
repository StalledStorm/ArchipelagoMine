from collections import Counter
from enum import Enum


class Immunity(Enum):
    BEAM = 0,
    """Regular Beam shots"""
    CHARGE = 1,
    """Charged Beam shots"""
    MISSILE = 2,
    """Standard Missiles"""
    SUPER = 3,
    """Super Missiles. Intended for exclusive use with Gerons"""
    BOMB = 4,
    """Standard Bomb blasts"""
    PB = 5,
    """Power Bomb blasts"""
    SCREW = 6
    """Screw Attack contact damage"""

# Values translated from spreadsheet found at this link:
# https://docs.google.com/spreadsheets/d/1Tcem3usNfxDFJp_uoe79GgJyWZabJaLW8uKzQjwZsD8/edit?gid=0#gid=0
class Enemy(Enum):
    HORNOAD = (4,),
    HALZYN = (4,),
    ZEBESIAN_WALL = (6, [Immunity.BEAM]),
    MOTO = (6,),
    YAMEBA = (2,),
    KAGO = (5, [Immunity.BEAM, Immunity.CHARGE, Immunity.MISSILE, Immunity.BOMB, Immunity.PB]),
    ATMOSPHERIC_STABILIZER_PARASITE = (21, [Immunity.BEAM, Immunity.BOMB]),
    ZEELA = (8,),
    ZOMBIE = (2,),
    GEEMER = (4,),
    ARACHNUS = (150,),
    WAVER = (12,),
    SCISER = (8,),
    SIDEHOPPER = (24, [Immunity.BEAM]),
    DESSGEEGA = (14,),
    GERON = (30, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB]),
    ZAZABI = (100, [Immunity.BEAM, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    """Zazabi HP is arbitrarily based on damaging projectile count regardless of type or damage value.
    Two strikes per segment (total of 3 segments) and four strikes when only the head remains,
    for a total of 10 strikes without overflow. Next segment cannot be damaged until the previous detonates."""
    YAKUZA = (1000, [Immunity.BEAM, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    CHOZO_STATUE = (1,),
    SCIENTIST = (1,),
    NETTORI = (2000, [Immunity.BEAM, Immunity.BOMB, Immunity.SCREW]),
    ZORO = (16,),
    KIHUNTER_AIR = (40,),
    KIHUNTER_GROUND = (40,),
    REO = (10,),
    NAMIHE = (82, [Immunity.BEAM]),
    FUNE = (32, [Immunity.BEAM]),
    ZORO_BLUE = (120,),
    GERUDA = (12,),
    SKULTERA = (12,),
    SKULTERA_LARGE = (28, [Immunity.BEAM]),
    SOVA = (10,),
    YARD = (60, [Immunity.BEAM]),
    EVIR = (80, [Immunity.BEAM]),
    BULL = (18,),
    MEMU = (6,),
    GERUBUS = (45, [Immunity.BEAM, Immunity.BOMB, Immunity.PB]),
    CHOOT = (16,),
    ZEBESIAN_GROUND = (90, [Immunity.BEAM]),
    HORNOAD_QUARANTINE_BAY = (4,),
    GERON_SUPER = (90, [Immunity.BEAM, Immunity.CHARGE, Immunity.MISSILE, Immunity.BOMB]),
    GERON_POWER = (17, [Immunity.BEAM, Immunity.CHARGE, Immunity.MISSILE, Immunity.SUPER, Immunity.BOMB]),
    RIPPER = (1, [Immunity.BEAM, Immunity.CHARGE, Immunity.MISSILE, Immunity.SUPER, Immunity.BOMB, Immunity.PB]),
    SCISER_GOLD = (16, [Immunity.BEAM]),
    GADORA = (24, [Immunity.BEAM, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    ZEBESIAN_GOLD = (135, [Immunity.BEAM, Immunity.BOMB, Immunity.PB]),
    ZEELA_RED = (82,),
    OWTCH = (10,),
    SERRIS = (50, [Immunity.BEAM, Immunity.BOMB, Immunity.PB]),
    GENESIS = (60,),
    PUYO = (4,),
    MIMIC_E = (1, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    MIMIC_M = (1, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    ZEBESIAN_AQUA = (90, [Immunity.BEAM]),
    POWAMP = (1, [Immunity.BEAM, Immunity.CHARGE, Immunity.MISSILE, Immunity.SUPER, Immunity.BOMB, Immunity.PB]),
    ZOZORO = (8,),
    SA_X_PHASE_1 = (350, [Immunity.BEAM, Immunity.MISSILE, Immunity.SUPER, Immunity.BOMB, Immunity.PB]),
    SA_X_PHASE_2 = (600, [Immunity.BEAM, Immunity.MISSILE, Immunity.SUPER, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    OMEGA_METROID = (1200, [Immunity.MISSILE, Immunity.SUPER, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    RIDLEY = (4500, [Immunity.BEAM, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    NIGHTMARE_PHASE_3 = (1200, [Immunity.BEAM, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    HALZYN_WING = (15, [Immunity.BEAM]),
    CORE_X_MORPH = (30, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    CORE_X_CHARGE = (33, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    BOX = (60, [Immunity.BEAM, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    CORE_X_WIDE = (150, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    CORE_X_PLASMA = (200, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    CORE_X_WAVE = (170, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    CORE_X_HIJUMP = (40, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    CORE_X_SPEED = (50, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    CORE_X_VARIA = (180, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    CORE_X_SPACE = (240, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    CORE_X_GRAVITY = (240, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    # Table says Screw Core-X has 30 HP, but takes 6 full power missiles (45 damage each) to defeat.
    CORE_X_SCREW = (270, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    X_BOX = (260, [Immunity.BEAM, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    X_BOX_MISSILE = (5,),
    CORE_X_ICE = (240, [Immunity.BEAM, Immunity.CHARGE, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    MEGA_X = (100, [Immunity.BEAM, Immunity.MISSILE, Immunity.SUPER, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    # Table has one value for the cannon at 120 HP. These values are based on research by Randovania.
    NIGHTMARE_CANNON_PHASE_1 = (130, [Immunity.BEAM, Immunity.BOMB, Immunity.PB, Immunity.SCREW]),
    NIGHTMARE_CANNON_PHASE_2 = (470, [Immunity.BEAM, Immunity.BOMB, Immunity.PB, Immunity.SCREW])


    def __init__(self,
                 hp: int,
                 immunities: list[Immunity] = None):
        self.hp: int = hp
        self.immunities: list[Immunity] = immunities or []

    def __repr__(self):
        return f"{self.name}(hp={self.hp!r}, immunities=[{", ".join(immunity.name for immunity in self.immunities)}])"

    def __str__(self):
        return self.name.title().replace("_", " ")

    def can_be_damaged(self,
                       inventory: Counter[str],
                       speed_booster_override: bool = False) -> bool:
        """Can the enemy be damaged based on ``inventory``?

        :param inventory: A dict of item name and quantity
        :param speed_booster_override: Toggle when room space allows for charging a speed boost to deal damage.
            Defaults to False.
        """

        has_missile: bool = "Missile Data" in inventory and inventory["Missile Data"] > 0
        has_morph: bool = "Morph Ball" in inventory and inventory["Morph Ball"] > 0
        if (speed_booster_override
            and "Speed Booster" in inventory
            and inventory["Speed Booster"] > 0):
            return True
        elif (Immunity.CHARGE not in self.immunities
              and "Charge Beam" in inventory
              and inventory["Charge Beam"] > 0):
            return True
        elif (Immunity.MISSILE not in self.immunities
              and has_missile):
            return True
        elif (Immunity.SUPER not in self.immunities
              and has_missile
              and "Super Missile" in inventory
              and inventory["Super Missile"] > 0):
            return True
        elif (Immunity.BOMB not in self.immunities
              and has_morph
              and "Bomb Data" in inventory
              and inventory["Bomb Data"] > 0):
            return True
        elif (Immunity.PB not in self.immunities
              and has_morph
              and "Power Bomb Data" in inventory
              and inventory["Power Bomb Data"] > 0):
            return True
        elif (Immunity.SCREW not in self.immunities
              and "Screw Attack" in inventory
              and inventory["Screw Attack"] > 0):
            return True
        elif Immunity.BEAM not in self.immunities:
            return True
        else:
            return False

    def can_be_damaged_by(self,
                          method: Immunity,
                          inventory: Counter[str]) -> bool:
        """Check for a specific immunity and appropriate inventory to deal damage if that immunity does not exist"""
        match method:
            case Immunity.CHARGE:
                return (Immunity.CHARGE not in self.immunities
                        and "Charge Beam" in inventory
                        and inventory["Charge Beam"] > 0)
            case Immunity.MISSILE:
                return (Immunity.MISSILE not in self.immunities
                        and "Missile Data" in inventory
                        and inventory["Missile Data"] > 0)
            case Immunity.SUPER:
                return (Immunity.SUPER not in self.immunities
                        and "Missile Data" in inventory
                        and inventory["Missile Data"] > 0
                        and "Super Missile" in inventory
                        and inventory["Super Missile"] > 0)
            case Immunity.BOMB:
                return (Immunity.BOMB not in self.immunities
                        and "Morph Ball" in inventory
                        and inventory["Morph Ball"] > 0
                        and "Bomb Data" in inventory
                        and inventory["Bomb Data"] > 0)
            case Immunity.PB:
                return (Immunity.PB not in self.immunities
                        and "Morph Ball" in inventory
                        and inventory["Morph Ball"] > 0
                        and "Power Bomb Data" in inventory
                        and inventory["Power Bomb Data"] > 0)
            case Immunity.SCREW:
                return (Immunity.SCREW not in self.immunities
                        and "Screw Attack" in inventory
                        and inventory["Screw Attack"] > 0)
            case Immunity.BEAM:
                return Immunity.BEAM not in self.immunities
            case _:
                return False

