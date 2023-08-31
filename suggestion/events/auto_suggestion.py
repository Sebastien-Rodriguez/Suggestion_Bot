import discord
from discord.ext import commands
import os

from ..config import SuggestionConfig, GlobalConfig
from ..tools import GetObjectConfig, ControlRateSuggestion

import aiofiles


class AutoSuggestion(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.object_config = GetObjectConfig(bot)
        self.suggestion_rate = ControlRateSuggestion()


    @commands.Cog.listener("on_message")
    async def control_suggestion(self, message: discord.Message) -> None:
        """
        Event which controls the messages sent in the suggestion channel, 
        then which formats them and sends them back.
        """

        check = True

        if not self.object_config.get_channel_suggestion():
            return
        
        elif message.author.bot:
            return
                
        elif self.suggestion_rate.user_at_suggestion_rate_limit(message.author.id):
            await message.reply(content = "You must wait before sending a new suggestion.", delete_after = 5.0, mention_author = True)
            check = False
        
        elif not len(message.content) > GlobalConfig.MIN_CHAR_PER_SUGGESTION.value:
            await message.reply(content = "Suggestion too short", delete_after = 5.0, mention_author = True)
            check = False

        if not check:
            await message.delete()
            return
        
        embed_object = await self.format_suggestion(message.content)
        message_object = await self.send_suggestion(embed_object)
        await self.add_reaction(message_object)

        self.suggestion_rate.add_user_to_rate_control(message.author.id)


    async def counter_suggestion(self) -> int:
        """
        Increments the total number of suggestions posted.

        Returns:
            - Return total number of suggestions posted updated.
        """

        path = os.path.abspath("suggestion/data/counter_suggestion.txt")

        async with aiofiles.open(path, "r+") as file:
            total_suggestion = await file.read()
            new_total = int(total_suggestion) + 1

            await file.seek(0)
            await file.write(str(new_total))

            return new_total

    async def format_suggestion(self, message_content : str) -> discord.Embed:
        """
        Format the message with an embed.

        Returns:
            - Return an embed object of the formatted message.
        """

        return discord.Embed(color = GlobalConfig.EMBED_COLOR.value,
                             title = f"#{await self.counter_suggestion()}",
                             description = message_content)
    

    #@logging
    async def send_suggestion(self, embed : discord.Embed) -> discord.Message:
        """
        Send a embed message to the suggestion channel.

        Returns:
            Return a object of the message that was send.
        """

        channel = self.object_config.get_channel_suggestion()
        message_object = await channel.send(embed = embed)
        return message_object


    async def add_reaction(self, message: discord.Message) -> None:
        """
        Adds reactions with emoji defined in the config to a message.
        """
        
        for emoji in self.object_config.get_emoji():
            await message.add_reaction(emoji)