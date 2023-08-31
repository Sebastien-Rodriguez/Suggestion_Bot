import discord
from discord.ext import commands

from .config import GlobalConfig
from .commands import Status, BotSetup
from .events import AutoSuggestion
from .tools import CheckConfig


class Suggestion(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix = "!", intents = discord.Intents.all())


    def start_bot(self) -> None:
        self.run(GlobalConfig.TOKEN.value)

    
    async def on_ready(self) -> None:
        CheckConfig(self).start_all_checks()

        await self.add_cog(BotSetup(self))
        await self.add_cog(AutoSuggestion(self))
        await self.tree.sync()

        print("Bot is started")


suggestion = Suggestion()
suggestion.start_bot()