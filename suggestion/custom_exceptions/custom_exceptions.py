class CustomEmojiNotValid(Exception):
    def __str__(self) -> str:
        return "Custom emoji is not valid, please verify file config and emojis ID."
    

class ClassicEmojiNotValid(Exception):
    def __str__(self) -> str:
        return "Classic emoji is not valid, please verify file config."
    

class DuplicateEmoji(Exception):
    def __str__(self) -> str:
        return "Emojis custom and classic emojis are defined, please define just one style of emojis"
    

class TextChannelIdNotValid(Exception):
    def __str__(self) -> str:
        return "Text channel ID is not valid, please verify file config and channel ID."


class TextChannelNameNotValid(Exception):
    def __str__(self) -> str:
        return "Text channel name is not valid, please verify file config."


class GuildIdNotValide(Exception):
    def __str__(self) -> str:
        return "Guild ID parameter is not valide, please verify file config."
    

# Ajoute la couleur rouge au exceptions