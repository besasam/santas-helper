from discord.ext import commands
from datetime import datetime
import pytz


class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._timezone = pytz.timezone('America/New_York')
        year = datetime.now(self._timezone).year
        self._years = [y for y in range(2015, year + 1)]
        self._url = 'https://adventofcode.com'

    @commands.command()
    async def level(self, ctx, *args):
        if len(args) > 2:
            await ctx.send('Please enter a valid command (type `aoc!help` to get a list of commands)')
            return
        if len(args) == 2:
            year = args[0]
            day = args[1]
        else:
            today = datetime.now(self._timezone)
            year = str(today.year)
            if not args:
                day = str(today.day)
            else:
                day = args[0]
        await ctx.send(self._get_day(day, year))

    def _get_day(self, day, year):
        if not day.isdigit() or int(day) > 31:
            return f'{day} is not a valid day!'
        if not year.isdigit() or int(year) not in self._years:
            return f'{year} is not a valid year!'
        today = datetime.now(self._timezone)
        if int(year) == today.year:
            if today.month < 12:
                return 'This year\'s Advent of Code has not started yet!'
            if int(day) == today.day and int(day) > 25:
                return 'This year\'s Advent of Code is already over!'
            if int(day) > today.day:
                return 'This day is not unlocked yet!'
        if int(day) > 25:
            return f'{day} is not a valid day!'
        return f'[{year}] Day {day}: {self._url}/{year}/day/{day}'


def setup(bot):
    bot.add_cog(Levels(bot))
