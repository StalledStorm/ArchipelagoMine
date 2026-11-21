from enum import Enum

from BaseClasses import ItemClassification
from .logic.regions.Sector4 import PumpControl
from .logic.regions.MainDeck import OperationsDeck

class FusionItemEnum(Enum):
    LEVEL_0_KEYCARD = (ItemClassification.progression, ["Keycards"], 1),
    MISSILE_DATA = (ItemClassification.progression, ["Weapons", "Missiles"], 2),
    MORPH_BALL = (ItemClassification.progression, ["Movement", "Morph Ball"], 3),
    CHARGE_BEAM = (ItemClassification.progression, ["Weapons", "Beams"], 4),
    LEVEL_1_KEYCARD = (ItemClassification.progression, ["Keycards"], 5),
    BOMB_DATA = (ItemClassification.progression, ["Weapons", "Morph Ball"], 6),
    HI_JUMP = (ItemClassification.progression, ["Movement"], 7),
    SPEED_BOOSTER = (ItemClassification.progression, ["Movement"], 8),
    LEVEL_2_KEYCARD = (ItemClassification.progression, ["Keycards"], 9),
    SUPER_MISSILE = (ItemClassification.progression, ["Weapons", "Missiles"], 10),
    VARIA_SUIT = (ItemClassification.progression, ["Suit", "Defense"], 11),
    LEVEL_3_KEYCARD = (ItemClassification.progression, ["Keycards"], 12),
    ICE_MISSILE = (ItemClassification.progression, ["Weapons", "Missiles"], 13),
    WIDE_BEAM = (ItemClassification.progression, ["Weapons", "Beams"], 14),
    POWER_BOMB_DATA = (ItemClassification.progression, ["Weapons", "Morph Ball"], 15),
    SPACE_JUMP = (ItemClassification.progression, ["Movement"], 16),
    PLASMA_BEAM = (ItemClassification.progression, ["Weapons", "Beams"], 17),
    GRAVITY_SUIT = (ItemClassification.progression, ["Suit", "Defense"], 18),
    LEVEL_4_KEYCARD = (ItemClassification.progression, ["Keycards"], 19),
    DIFFUSION_MISSILE = (ItemClassification.progression, ["Weapons", "Missiles"], 20),
    WAVE_BEAM = (ItemClassification.progression, ["Weapons", "Beams"], 21),
    SCREW_ATTACK = (ItemClassification.progression, ["Weapons", "Suit"], 22),
    ICE_BEAM = (ItemClassification.progression, ["Weapons", "Beams"], 23),
    MISSILE_TANK = (ItemClassification.filler, ["Weapons", "Missiles"], 24),
    ENERGY_TANK = (ItemClassification.progression_deprioritized_skip_balancing, ["Suit", "Defense"], 25),
    POWER_BOMB_TANK = (ItemClassification.filler, ["Weapons", "Bombs"], 26),
    ICE_TRAP = (ItemClassification.trap, [], 27),
    INFANT_METROID = (ItemClassification.progression, ["Metroid"], 28),
    NOTHING = (ItemClassification.trap, [], 29)

    def __init__(self, item_class: ItemClassification, groups: list[str], id_value: int):
        self.item_class = item_class
        self.groups = groups or []
        self.id_value = id_value

    def __repr__(self):
        return f"{self.name}(item_class={self.item_class!r}, group={self.groups!r}, id_value={self.id_value!r})"

    def __str__(self):
        if self == FusionItemEnum.HI_JUMP:
            return "Hi-Jump"
        return self.name.title().replace("_", " ")


class FusionEventEnum(Enum):
    VICTORY = (ItemClassification.progression, OperationsDeck.name, "Victory"),
    PUMP_CONTROL = (ItemClassification.progression, PumpControl.name, "Pump Control Activated")

    def __init__(self, item_class: ItemClassification, location_name: str, full_name: str):
        self.item_class = item_class
        self.location_name = location_name
        self.full_name = full_name

    def __repr__(self):
        return (f"{self.name}(item_class={self.item_class!r}, " +
                f"location_name={self.location_name!r}, full_name={self.full_name!r})")

    def __str__(self):
        return self.name.title().replace("_", " ")


all_item_data = [
    # Name, Major, Groups, ID
    ("Level 0 Keycard", ItemClassification.progression, ["Keycards"], 1),
    ("Missile Data", ItemClassification.progression, ["Weapons", "Missiles"], 2),
    ("Morph Ball", ItemClassification.progression, ["Movement", "Morph Ball"], 3),
    ("Charge Beam", ItemClassification.progression, ["Weapons", "Beams"], 4),
    ("Level 1 Keycard", ItemClassification.progression, ["Keycards"], 5),
    ("Bomb Data", ItemClassification.progression, ["Weapons", "Morph Ball"], 6),
    ("Hi-Jump", ItemClassification.progression, ["Movement"], 7),
    ("Speed Booster", ItemClassification.progression, ["Movement"], 8),
    ("Level 2 Keycard", ItemClassification.progression, ["Keycards"], 9),
    ("Super Missile", ItemClassification.progression, ["Weapons", "Missiles"], 10),
    ("Varia Suit", ItemClassification.progression, ["Suit", "Defense"], 11),
    ("Level 3 Keycard", ItemClassification.progression, ["Keycards"], 12),
    ("Ice Missile", ItemClassification.progression, ["Weapons", "Missiles"], 13),
    ("Wide Beam", ItemClassification.progression, ["Weapons", "Beams"], 14),
    ("Power Bomb Data", ItemClassification.progression, ["Weapons", "Morph Ball"], 15),
    ("Space Jump", ItemClassification.progression, ["Movement"], 16),
    ("Plasma Beam", ItemClassification.progression, ["Weapons", "Beams"], 17),
    ("Gravity Suit", ItemClassification.progression, ["Suit", "Defense"], 18),
    ("Level 4 Keycard", ItemClassification.progression, ["Keycards"], 19),
    ("Diffusion Missile", ItemClassification.progression, ["Weapons", "Missiles"], 20),
    ("Wave Beam", ItemClassification.progression, ["Weapons", "Beams"], 21),
    ("Screw Attack", ItemClassification.progression, ["Weapons", "Suit"], 22),
    ("Ice Beam", ItemClassification.progression, ["Weapons", "Beams"], 23),
    ("Missile Tank", ItemClassification.filler, ["Weapons", "Missiles"], 24),
    ("Energy Tank", ItemClassification.progression_deprioritized_skip_balancing, ["Suit", "Defense"], 25),
    ("Power Bomb Tank", ItemClassification.filler, ["Weapons", "Bombs"], 26),
    ("Ice Trap", ItemClassification.trap, [], 27),
    ("Infant Metroid", ItemClassification.progression, ["Metroid"], 28),
    ("Nothing", ItemClassification.trap, [], 29),
]

events: list[tuple[str, ItemClassification, str, str]] = [
    ("Victory", ItemClassification.progression, OperationsDeck.name, "Victory"),
    ("Pump Control", ItemClassification.progression, PumpControl.name, "Pump Control Activated")
]
