import discord
from discord.ext import commands

from ..config import SuggestionConfig, LoggingConfig, GlobalConfig
from ..custom_exceptions import (
    TextChannelIdNotValid,
    TextChannelNameNotValid,
    ChannelNameAlreadyExist,

    EmojiNotValid,
    DuplicateEmoji,
    ConflictingEmoji,

    GuildIdNotValid,
    RateSuggestionsNotValid,
    BaseCreateNotValid
    )


import emoji


class CheckConfig:
    """
    Class with several methods to check the parameters of the config.
    """

    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        self.guild = bot.get_guild(GlobalConfig.GUILD_ID.value)


    def start_all_checks(self) -> None:
        """
        Calls all methods of the class.
        """ 

        self.check_guild_id()
        self.check_base_create()
        self.check_channels_id()
        self.check_channels_name()
        self.check_emoji()
        self.check_rate_suggestion()


    def check_guild_id(self) -> None:
        """
        Check if parameter guild ID is correct.

        Raises:
            GuildIdNotValide: Raised if a GUILD_ID parameter is incorrect.
        """

        if not self.guild:
            raise GuildIdNotValid


    def check_emoji(self) -> None:
        """
        Check if parameters emoji is correct.

        Raises:
            - ConflictingEmoji: Raised if parameters custom and classic emoji are define.
            - DuplicateEmoji: Raised if the good and bad emoji parameters have the same emoji.
            - EmojiNotValid: Raised if one parameter emoji is not valid.

        Notes:
            - Only one choice of emoji is possible, either custom or classic in file config.
            - Good and bad emoji cannot be the same.
        """

        custom_emojis_list = (
                self.bot.get_emoji(SuggestionConfig.CUSTOM_GOOD_EMOJI_ID.value),
                self.bot.get_emoji(SuggestionConfig.CUSTOM_BAD_EMOJI_ID.value)
            )

        classic_emojis_list = (
                emoji.is_emoji(SuggestionConfig.CLASSIC_GOOD_EMOJI.value),
                emoji.is_emoji(SuggestionConfig.CLASSIC_BAD_EMOJI.value)
            )
                    
        if any(custom_emojis_list) and any(classic_emojis_list):
            raise ConflictingEmoji
        
        elif all(custom_emojis_list):
            if SuggestionConfig.CUSTOM_GOOD_EMOJI_ID.value == SuggestionConfig.CUSTOM_BAD_EMOJI_ID.value:
                raise DuplicateEmoji

        elif all(classic_emojis_list):
            if SuggestionConfig.CLASSIC_GOOD_EMOJI.value == SuggestionConfig.CLASSIC_BAD_EMOJI.value:
                raise DuplicateEmoji
            
        else:
           raise EmojiNotValid

        return 


    def check_channels_name(self) -> None:
        """
        Check if parameters text channels name is correct.

        Raises:
            TextChannelNameNotValid: Raised if the different channels name parameters is incorrect.
        """

        if not GlobalConfig.BASE_CREATE.value:
            return

        try:
            parameters_channels_name_list = [str(LoggingConfig.CHANNEL_NAME.value).lower(),
                                             str(SuggestionConfig.CHANNEL_NAME.value).lower()]
        except ValueError:
            raise TextChannelNameNotValid

        text_channels_in_discord_server = self.guild.text_channels
        
        # Check if a channel with this name already exists on the discord server
        for channel in text_channels_in_discord_server:
            if channel.name in parameters_channels_name_list:
                raise ChannelNameAlreadyExist


    def check_channels_id(self) -> None: 
        """
        Check if parameters text channels ID is correct.

        Raises:
            - TextChannelIdNotValid: Raised if the different channel ID parameters is incorrect,
              and if BASE_CREATE is False.
        """

        if GlobalConfig.BASE_CREATE.value:
            return
        
        channels_list = (
            self.guild.get_channel(SuggestionConfig.CHANNEL_ID.value),
            self.guild.get_channel(LoggingConfig.CHANNEL_ID.value)
        )

        if not all(channels_list):
            raise TextChannelIdNotValid


    @staticmethod
    def check_rate_suggestion() -> None:
        """
        Check parameter max suggestion per day is correct.

        Raises:
            MaxSuggestionsNotValid: Raised if parameter is not convert to int.
        """
        
        if not isinstance(GlobalConfig.RATE_SUGGESTION_PER_SECOND_PER_USER.value, int):
            raise RateSuggestionsNotValid


    @staticmethod
    def check_base_create() -> None:
        """
        Check parameter base create is correct.

        Raises:
            BaseCreateNotValid: Raised if parameter is not convert to bool.
        """

        if not isinstance(GlobalConfig.BASE_CREATE.value, bool):
            raise BaseCreateNotValid

        
    @staticmethod
    def check_embed_color() -> None:
        """
        _summary_
        """

        if not isinstance(GlobalConfig.EMBED_COLOR.value, str):
            ...
        # A finir
        

    @staticmethod
    def check_min_char_suggestion() -> None:
        """
        _summary_
        """
        
        if not isinstance(GlobalConfig.MIN_CHAR_PER_SUGGESTION.value, int):
            ...