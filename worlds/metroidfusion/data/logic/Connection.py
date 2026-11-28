from typing import TYPE_CHECKING

from .....rule_builder.rules import Rule

if TYPE_CHECKING:
    from .FusionRegion import FusionRegion
    from ... import MetroidFusionOptions

class Connection:
    destination: "FusionRegion"
    rule: Rule
    two_way: bool

    def __init__(self, destination, rule, two_way=False):
        self.destination = destination
        self.rule = rule
        self.two_way = two_way

    def determine_destination(
            self,
            options: "MetroidFusionOptions",
            region_map: dict["FusionRegion", "FusionRegion"]):
        pass
