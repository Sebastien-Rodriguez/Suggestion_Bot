import discord
from discord.ext import commands
from typing import List, Union

from ..config import LoggingConfig, GlobalConfig, SuggestionConfig


class GetObjectConfig:
    """
    Class with several utility methods.
    It all returns a discord type object for almost each config option.
    """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.guild = self.get_guild()


    def get_channel_logging(self) -> discord.TextChannel:
        """
        Return a channel logging object.
        """
        return self._get_channel(LoggingConfig.CHANNEL_ID.value, LoggingConfig.CHANNEL_NAME.value)


    def get_channel_suggestion(self) -> discord.TextChannel:
        """
        Return a channel suggestion object.
        """
        return self._get_channel(SuggestionConfig.CHANNEL_ID.value, SuggestionConfig.CHANNEL_NAME.value)


    def _get_channel(self, channel_id: int, channel_name: str) -> discord.TextChannel:
        """
        Check is getting the object of a channel and return object channel.
        """

        channel = self.bot.get_channel(channel_id)
        if not channel:
            channel = discord.utils.get(self.guild.text_channels, name = channel_name.lower())

        return channel


    def get_guild(self) -> discord.Guild:
        """
        Return a guild object.
        """
        return self.bot.get_guild(GlobalConfig.GUILD_ID.value)


    def get_emoji(self) -> Union[List[str], List[discord.Emoji]]:
        """
        Return a list of Emoji objects or STR of emoji.
        """
        
        custom_emojis_list = [
                self.bot.get_emoji(SuggestionConfig.CUSTOM_GOOD_EMOJI_ID.value),
                self.bot.get_emoji(SuggestionConfig.CUSTOM_BAD_EMOJI_ID.value)
        ]

        classic_emojis_list = [
                SuggestionConfig.CLASSIC_GOOD_EMOJI.value,
                SuggestionConfig.CLASSIC_BAD_EMOJI.value
        ]
        
        emoji_list = custom_emojis_list if all(custom_emojis_list) else classic_emojis_list
        return emoji_list