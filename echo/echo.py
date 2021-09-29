from redbot.core import commands

class Echo(commands.Cog):
    """echo"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        
        if message.content.startswith('b.15082007'):
            await ctx delete

            await ctx(message.content[10:])

        await ctx.send("I can do stuff!")