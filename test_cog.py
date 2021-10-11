from redbot.core import commands

class TestCog(commands.Cog):
    """test_cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom2(self, ctx, *, text):
        """This does more stuff!"""
        await ctx.message.delete()
        await ctx.send(text)