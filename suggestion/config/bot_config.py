from enum import Enum
from ..token import TOKEN


class LoggingConfig(Enum):
    CHANNEL_ID: int = 1146555254062714960
    CHANNEL_NAME: str = ""


class GlobalConfig(Enum):
    TOKEN: str = TOKEN
    GUILD_ID: int = 1139860637384704030
    BASE_CREATE: bool = False
    EMBED_COLOR: int = 0xC60404
    RATE_SUGGESTION_PER_SECOND_PER_USER: int = 100
    MIN_CHAR_PER_SUGGESTION: int = 0


class SuggestionConfig(Enum):
    CHANNEL_ID: int = 1146555253102231642
    CHANNEL_NAME: str = ""

    CUSTOM_GOOD_EMOJI_ID: int = 0
    CUSTOM_BAD_EMOJI_ID: int = 0

    CLASSIC_GOOD_EMOJI: str = "✅"
    CLASSIC_BAD_EMOJI: str = "❌"
