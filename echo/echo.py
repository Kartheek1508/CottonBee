from redbot.core import commands

class Echo(commands.Cog):
    """echo"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def b.echo(self, ctx, *, text):
        """This does more stuff!"""
        await ctx.message.delete()
        await ctx.send(text)