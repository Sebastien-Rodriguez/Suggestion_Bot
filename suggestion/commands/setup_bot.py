import discord
from discord.ext import commands

from ..tools import Logging
from ..config import SuggestionConfig, LoggingConfig, GlobalConfig
from ..custom_exceptions import (
    TextChannelIdNotValid,
    TextChannelNameNotValid,
    CustomEmojiNotValid,
    ClassicEmojiNotValid,
    DuplicateEmoji,
    GuildIdNotValide
    )


class SetupBot(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.guild: discord.Guild


    @discord.app_commands.command(name="setup_bot_suggestion")
    async def setup_bot_command(self, interaction: discord.Interaction) -> None:
        """
        Check file config and setup suggestion bot.
        """

        self.check_guild_id
        await self.check_channels()
        self.check_emojis()


    async def check_channels(self):
        """
        Check if channels exist.

        Raises:
            - TextChannelIdNotValid: Raised if text channel ID is not valid.
            - TextChannelNameNotValid: Raised if text channel name is not valid.

        Notes:
            - If text channels do not exist and FORCE_CREATE parameter is allowed,
              the system creates text channels.
            - Parameter CHANNEL_NAME is useless if CHANNEL_ID is correcly.
        """

        channels_list = (
            (self.guild.get_channel(SuggestionConfig.CHANNEL_ID.value), SuggestionConfig.CHANNEL_NAME.value),
            (self.guild.get_channel(LoggingConfig.CHANNEL_ID.value), LoggingConfig.CHANNEL_NAME.value)
        )

        for channel_info in channels_list:
            is_created, name = channel_info

            if not is_created and GlobalConfig.FORCE_CREATE.value:
                if not name:
                    raise TextChannelNameNotValid
                await self.create_channel()
            else:
                raise TextChannelIdNotValid


    async def create_channel(self, name: str) -> None:

        if name is SuggestionConfig.CHANNEL_NAME:
            permission = {
                ...
            }
        
        elif name is LoggingConfig.CHANNEL_NAME:
            permission = {
                ...
            }
        
        await self.guild.create_text_channel(name=name, overwrites=permission)


    def check_emojis(self) -> None:
        """
        Check the validity of emojis.

        Raises:
            - CustomEmojiNotValid: Raised if a custom emoji is not valid.
            - ClassicEmojiNotValid: Raised if a classic emoji is not valid.
            - DuplicateEmoji: Raised if both custom and classic emojis are defined.

        Notes:
            - Only one choice of emoji is possible, either custom or classic.
        """

        custom_emojis_list = (
            self.bot.get_emoji(SuggestionConfig.CUSTOM_GOOD_EMOJI_ID.value),
            self.bot.get_emoji(SuggestionConfig.CUSTOM_BAD_EMOJI_ID.value)
        )

        classic_emojis_list = (
            SuggestionConfig.CLASSIC_GOOD_EMOJI.value,
            SuggestionConfig.CLASSIC_BAD_EMOJI.value
        )

        if all(custom_emojis_list) and all(classic_emojis_list):
            raise DuplicateEmoji

        elif SuggestionConfig.CUSTOM_GOOD_EMOJI_ID.value is not None and SuggestionConfig.CUSTOM_BAD_EMOJI_ID.value is not None:
            if not all(custom_emojis_list):
                raise CustomEmojiNotValid

        elif not all(classic_emojis_list):
            raise ClassicEmojiNotValid


    def check_guild_id(self) -> None:
        """
        Check if guild_id is valid.

        Raises:
            GuildIdNotValide: Raised if a guild_id parameter is not valid.

        Notes:
            - The check must be done first,
            because the other method of the class we need a guild instance.
        """

        self.guild = self.bot.get_guild(GlobalConfig.GUILD_ID.value)

        if self.guild is None:
            raise GuildIdNotValide
        

    @staticmethod
    def check_embed_color() -> None:
        pass
