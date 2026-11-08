from dataclasses import dataclass
from enum import Enum, auto
from typing import ClassVar

from .frozendict import frozendict
from typing_extensions import Self

from .mf.auto_generated_types import Itemmessages
from .text import Language


class ItemMessagesKind(Enum):
    CUSTOM_MESSAGE = auto()
    MESSAGE_ID = auto()


@dataclass(frozen=True)
class ItemMessages:
    kind: ItemMessagesKind
    item_messages: frozendict[Language, str]
    centered: bool
    message_id: int

    LANG_ENUMS: ClassVar[dict[str, Language]] = {
        "JapaneseKanji": Language.JAPANESE_KANJI,
        "JapaneseHiragana": Language.JAPANESE_HIRAGANA,
        "English": Language.ENGLISH,
        "German": Language.GERMAN,
        "French": Language.FRENCH,
        "Italian": Language.ITALIAN,
        "Spanish": Language.SPANISH,
    }

    KIND_ENUMS: ClassVar[dict[str, ItemMessagesKind]] = {
        "CustomMessage": ItemMessagesKind.CUSTOM_MESSAGE,
        "MessageID": ItemMessagesKind.MESSAGE_ID,
    }

    @classmethod
    def from_json(cls, data: Itemmessages) -> Self:
        item_messages: dict[Language, str] = {}
        centered = True
        kind: ItemMessagesKind = cls.KIND_ENUMS[data["Kind"]]
        message_id = 0
        if kind == ItemMessagesKind.CUSTOM_MESSAGE:
            for lang_name, message in data["Languages"].items():
                lang = cls.LANG_ENUMS[lang_name]
                item_messages[lang] = message
            centered = data.get("Centered", True)
        else:
            message_id = data["MessageID"]

        return cls(kind, frozendict(item_messages), centered, message_id)
