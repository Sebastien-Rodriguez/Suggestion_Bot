import discord
from discord.ext import commands

from ..tools import Logging, CheckConfig
from ..config import SuggestionConfig, LoggingConfig, GlobalConfig


class BotSetup(commands.Cog):
    """
    Class used to configure the bot.
    """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.guild = bot.get_guild(GlobalConfig.GUILD_ID.value)
        self.check_config = CheckConfig(bot=bot)


    @discord.app_commands.command(name="setup_bot_suggestion")
    @discord.app_commands.checks.has_permissions(administrator = True)
    async def setup_bot_suggestion(self, interaction: discord.Interaction) -> None:
        """
        Setup suggestion bot.
        """

        if GlobalConfig.BASE_CREATE.value:
            await self.create_channels()

        await interaction.response.send_message("The suggestion bot has been successfully setup.")


    async def create_channels(self) -> None:
        """
        Create discord channels with X permissions.
        """

        permission_channel_suggestion = {
            self.guild.default_role: discord.PermissionOverwrite(
                read_messages=True,
                send_messages=True,
                add_reactions=True,
                manage_messages=False,
                embed_links=False,
                attach_files=False,
                external_emojis=False,
                mention_everyone=False,
                use_external_emojis=False,
                manage_webhooks=False,
                create_instant_invite=False,
                manage_channels=False,
                manage_permissions=False,
                manage_roles=False,
                manage_nicknames=False,
                use_application_commands=False,
                create_public_threads=False,
                create_private_threads=False,
                use_external_stickers=False,
                send_tts_messages=False,
                speak=False,
                connect=False,
                stream=False,
                use_voice_activation=False,
                priority_speaker=False,
                move_members=False,
                request_to_speak=False,
                manage_threads = False,
                send_messages_in_threads = False,
            )
        }

        permission_channel_logging = {
            self.guild.default_role: discord.PermissionOverwrite(
                read_messages=False,
                send_messages=False,
                add_reactions=False,
                manage_messages=False,
                embed_links=False,
                attach_files=False,
                external_emojis=False,
                mention_everyone=False,
                use_external_emojis=False,
                manage_webhooks=False,
                create_instant_invite=False,
                manage_channels=False,
                manage_permissions=False,
                manage_roles=False,
                manage_nicknames=False,
                use_application_commands=False,
                create_public_threads=False,
                create_private_threads=False,
                use_external_stickers=False,
                send_tts_messages=False,
                speak=False,
                connect=False,
                stream=False,
                use_voice_activation=False,
                priority_speaker=False,
                move_members=False,
                request_to_speak=False,
                manage_threads = False,
                send_messages_in_threads = False,            
            )
        }
        
        await self.guild.create_text_channel(name=LoggingConfig.CHANNEL_NAME.value, overwrites=permission_channel_logging)
        await self.guild.create_text_channel(name=SuggestionConfig.CHANNEL_NAME.value, overwrites=permission_channel_suggestion)


    @setup_bot_suggestion.error
    async def setup_bot_suggestion_error(self, interaction: discord.Interaction, error) -> None:
        """
        Collect and process errors generated by the setup command.
        """
        if isinstance(error, discord.app_commands.MissingPermissions):
            await interaction.response.send_message(
                content = "You cannot run this command. You must have the administrator permission.", ephemeral = True)
        
        await interaction.response.send_message("Something went wrong.")