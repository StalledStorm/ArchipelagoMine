from rule_builder.rules import Rule


class FusionLocation:
    name: str
    major: bool
    rule: Rule

    def __init__(self, name, major, rule):
        self.name = name
        self.major = major
        self.rule = rule
