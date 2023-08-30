import discord
from discord.ext import commands


class Status(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @discord.app_commands.command(name = "status")
    async def commande_status(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Latancy : {int(self.bot.latency * 1000)}", ephemeral = True)
        # Il faut refaire ça