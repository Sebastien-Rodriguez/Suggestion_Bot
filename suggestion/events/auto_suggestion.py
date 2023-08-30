import discord
from discord.ext import commands

from ..config import SuggestionConfig


class AutoSuggestion(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        pass

    
    @commands.Cog.listener("on_message")
    async def get_suggestion(self, message: discord.Message) -> None:

        suggestion_channel_id = message.channel.id == SuggestionConfig.CHANNEL_ID.value
        suggestion_channel_name = message.channel.name == SuggestionConfig.CHANNEL_NAME.value

        if not suggestion_channel_id or suggestion_channel_name:
            return
        

    @staticmethod
    async def format_message(message : str) -> str:
        return ""
    

    async def modify_message_posted(self, id: discord.Message) -> None:
        pass