from enum import Enum
from typing import Optional


class LoggingConfig(Enum):
    CHANNEL_ID: int = 00000000
    CHANNEL_NAME: str = "Logging"


class GlobalConfig(Enum):
    TOKEN: str = ""
    GUILD_ID: int = 1139860637384704030
    LINK_IMAGE_FOOTER: str = ""
    FORCE_CREATE: bool = True
    EMBED_COLOR: int = 11111


class SuggestionConfig(Enum):
    CHANNEL_ID: int = 00000000
    CHANNEL_NAME: str = "Suggestion"

    CUSTOM_GOOD_EMOJI_ID: Optional[int] = None
    CUSTOM_BAD_EMOJI_ID: Optional[int] = None

    CLASSIC_GOOD_EMOJI: str = ""
    CLASSIC_BAD_EMOJI: str = ""
