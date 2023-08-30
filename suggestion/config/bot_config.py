from enum import Enum


class LoggingConfig(Enum):
    CHANNEL_ID: int = 0
    CHANNEL_NAME: str = "s"


class GlobalConfig(Enum):
    TOKEN: str = ""
    GUILD_ID: int = 1139860637384704030
    BASE_CREATE: bool = True
    EMBED_COLOR: str = "87CEEB"
    RATE_SUGGESTION_PER_SECOND_PER_USER: int = 0


class SuggestionConfig(Enum):
    CHANNEL_ID: int = 0
    CHANNEL_NAME: str = ""

    CUSTOM_GOOD_EMOJI_ID: int = 0
    CUSTOM_BAD_EMOJI_ID: int = 0

    CLASSIC_GOOD_EMOJI: str = "✅"
    CLASSIC_BAD_EMOJI: str = "❌"
