class TextChannelIdNotValid(Exception):
    """
    Call when one or more CHANNEL ID are not valid in the configuration.    
    """

    def __str__(self) -> str:
        return "One or more CHANNEL ID parameter are not valid"


class TextChannelNameNotValid(Exception):
    """
    Call when one or more CHANNEL NAME are not valid in the configuration.    
    """

    def __str__(self) -> str:
        return "One or more CHANNEL NAME parameter are not valid."


class ChannelNameAlreadyExist(Exception):
    """
    Call when one or more channels,
    with the same name as the one defined in the configuration already exist on the discord server.    
    """

    def __str__(self) -> str:
        return "One or more CHANNEL NAME with the same channel name parameter already exist on the discord server."
