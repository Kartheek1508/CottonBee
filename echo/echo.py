from redbot.core import commands, checks
import discord 

class Echo(commands.Cog):
    """echo"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)    
    async def echo(self, ctx, *, text):
        "Echo what you said"
        await ctx.message.delete()
        if await self.bot.is_admin(ctx.author):
            response = text
        else:
            response = f"{text}  - <@{ctx.author.id}>"
        await ctx.send(response, allowed_mentions=discord.AllowedMentions.none())        


    @echo.command()
    @checks.admin()
    async def embed(self, ctx, *, text):
        """Embed echo"""
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(description=text))