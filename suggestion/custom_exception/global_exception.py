class GuildIdNotValid(Exception):
    """
    Call when GUILD ID is not valid in the configuration.    
    """

    def __str__(self) -> str:
        return "Guild ID parameter is invalid."


class RateSuggestionsNotValid(Exception):
    """
    Call when RATE SUGGESTION is not valid in the configuration.    
    """

    def __str__(self) -> str:
        return "Rate suggestion parameter is invalid."


class BaseCreateNotValid(Exception):
    """
    Call when BASE CREATE is not valid in the configuration.    

    """
    
    def __str__(self) -> str:
        return "Base create parameter is invalid."
