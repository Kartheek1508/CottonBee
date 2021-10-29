from discord.embeds import Embed
from redbot.core import commands, checks
import discord 

class Echo(commands.Cog):
    """echo"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)    
    async def echo(self, ctx, *, text):
        "Echo what you said"
        if ctx.channel.permissions_for(ctx.guild.me).manage_messages:
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
        if ctx.channel.permissions_for(ctx.guild.me).manage_messages:
            await ctx.message.delete()
             
        await ctx.send(embed=discord.Embed(description=text))
    
    @echo.command()
    @checks.admin()
    async def bold(self, ctx, *, text):
        """Bold echo"""
        await ctx.message.delete()
             
        await ctx.send (f"**{(text)}**")

    @echo.command()
    @checks.admin()
    async def italic(self, ctx, *, text):
        """Italic echo"""
        await ctx.message.delete()
             
        await ctx.send (f"*{(text)}*")