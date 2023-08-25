import discord
from discord.ext import commands

from .config import GlobalConfig
from .commands import Status, SetupBot


class Suggestion(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix = "!", intents = discord.Intents.all())
    

    def start_bot(self) -> None:
        self.run(GlobalConfig.TOKEN.value)


    async def setup_hook(self) -> None:
        await self.add_cog(Status(self))


    async def on_ready(self) -> None:
        await self.add_cog(SetupBot(self)) # Si
        await self.tree.sync()

        print("Bot is started")


suggestion = Suggestion()
suggestion.start_bot()

# Je crois que on peut log dans un fichier avec le logging de python les crash de la lib discord py