from discord.ext import commands


# TODO
class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, *args):
        if len(args) != 1 or not args[0].isdigit():
            await ctx.send(f'Please enter a valid user id. You can find your id on {self.bot.url}/settings')
            return
        user = ctx.author.id
        aoc = int(args[0])

    async def set(self, id, aoc):
        return

def setup(bot):
    bot.add_cog(User(bot))
