class DuplicateEmoji(Exception):
    """
    Call when custom or classic emoji are the same in the configuration for bad and good.

    Exemple :
        - BAD_EMOJI = ✅ | GOOD_EMOJI = ✅
    """

    def __str__(self) -> str:
        return "Duplicate emoji are not allowed in the configuration."


class EmojiNotValid(Exception):
    """
    Call when one or more custom or classic emoji are not valid in the configuration.
    """

    def __str__(self) -> str:
        return "One or more emoji in the configuration are invalid."


class ConflictingEmoji(Exception):
    """
    Call when custom and classic emoji are defined in the configuration.
    """
    
    def __str__(self) -> str:
        return "Both custom and classic emoji are defined. Please define only one style of emoji in the configuration ."
