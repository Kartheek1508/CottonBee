from redbot.core import commands, checks
import discord 

class Echo(commands.Cog):
    """echo"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *, text):
        "Echo what you said (only for admins)"
        await ctx.message.delete()
        if await self.bot.is_admin(ctx.author):
            response = text
        else:
            response = f"{text}  - <@{ctx.author.id}>"
        await ctx.send(response, allowed_mentions=discord.AllowedMentions.none())        