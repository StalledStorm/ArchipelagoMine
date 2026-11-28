from rule_builder.rules import Rule, False_
from .Connection import Connection
from .FusionLocation import FusionLocation

class FusionRegion:
    name: str
    connections: list[Connection]
    locations: list[FusionLocation]

    def __init__(self,
                 name: str,
                 connections: list[Connection] = None,
                 locations: list[FusionLocation] = None):
        self.name = name
        self.connections = connections or []
        self.locations = locations or []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

def connection_to(region_from: FusionRegion, region: FusionRegion) -> Rule:
    return next((connection.rule for connection in region_from.connections if connection.destination == region), False_())
