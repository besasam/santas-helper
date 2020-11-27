from discord.ext import commands
import os
import json


class Leaderboard(commands.Cog):
    _url = 'https://adventofcode.com'
    _dir = 'data'
    ERROR = 0
    FILE_NOT_FOUND = 1

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def init(self, ctx, *args):
        if not ctx.author.guild_permissions.administrator:
            await ctx.send('You need admin permissions to do this')
            return
        guild = ctx.guild.id
        path = self._path(guild)
        if os.path.exists(path):
            await ctx.send('Leaderboard has already been initialized')
            return
        if len(args) != 1 or not args[0].isdigit():
            await ctx.send('Please enter a valid leaderboard id')
            return
        data = {'leaderboard_id': args[0]}
        save = self._save(guild, data)
        if save:
            await ctx.send('There was an error when saving leaderboard for this server')
            return
        await ctx.send(f'Leaderboard has been initialized. You can now use `aoc!setcode` to set the join code for this leaderboard.')

    @commands.command()
    async def setcode(self, ctx, *args):
        guild = ctx.guild.id
        path = self._path(guild)
        if not os.path.exists(path):
            await ctx.send('Leaderboard has not yet been initialized for this server')
            return
        if not ctx.author.guild_permissions.administrator:
            await ctx.send('You need admin permissions to do this')
            return
        if len(args) != 1:
            await ctx.send(f'Please enter a valid join code. You can find your join code on {self._url}/leaderboard/private')
            return
        data = self._load(guild)
        if 'error' in data:
            await ctx.send('There was an error when loading leaderboard for this server')
            return
        code = args[0]
        owner = ctx.author.id
        data.update({'code': code, 'owner': owner})
        save = self._save(guild, data)
        if save:
            await ctx.send('There was an error when saving your data')
            return
        await ctx.send(f'Join code has been set to `{code}`')

    @commands.command()
    async def code(self, ctx):
        guild = ctx.guild.id
        data = self._load(guild)
        if 'error' in data:
            if data['error'] == self.FILE_NOT_FOUND:
                await ctx.send('Leaderboard has not yet been initialized for this server')
                return
            await ctx.send('There was an error when loading leaderboard for this server')
            return
        if 'code' not in data:
            await ctx.send('No join code has been set for this server')
            return
        code = data['code']
        owner = self.bot.get_user(data['owner']).name
        await ctx.send(f'This server\'s join code is `{code}` (Owner: {owner})\n'
                       f'You can join the leaderboard by entering the above code on {self._url}/leaderboard/private')

    @commands.command()
    async def join(self, ctx, *args):
        guild = ctx.guild.id
        path = self._path(guild)
        if not os.path.exists(path):
            await ctx.send('Leaderboard has not yet been initialized for this server')
            return
        user = ctx.author.id
        data = self._load(guild)
        if 'error' in data:
            await ctx.send('There was an error when loading leaderboard for this server')
            return
        if 'members' not in data:
            data.update({'members': {}})
        elif str(user) in data['members']:
            await ctx.send('You have already joined this leaderboard')
            return
        if len(args) != 1 or not args[0].isdigit():
            await ctx.send(f'Please enter a valid user id. You can find your user id on {self._url}/settings')
            return
        id = args[0]
        data['members'].update({user: id})
        save = self._save(guild, data)
        if save:
            await ctx.send('There was an error when saving your data')
            return
        await ctx.send(f'You have joined this server\'s leaderboard! Don\'t forget to join it on Advent of Code as well (use `aoc!code` to get the join code)')

    def _load(self, guild):
        print(f'Loading leaderboard for {guild}')
        path = self._path(guild)
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            print(f'Loaded leaderboard for {guild}')
            return data
        except FileNotFoundError:
            print(f'File not found for {guild}')
            return {'error': self.FILE_NOT_FOUND}
        except BaseException:
            print(f'Error when loading file for {guild}')
            return {'error': self.ERROR}

    def _save(self, guild, data):
        print(f'Saving leaderboard for {guild}')
        path = self._path(guild)
        try:
            with open(path, 'w+') as f:
                json.dump(data, f)
            print(f'Saved leaderboard for {guild}')
            return
        except FileNotFoundError:
            print(f'File not found for {guild}')
            return {'error': self.FILE_NOT_FOUND}
        except:
            print(f'Error when saving file for {guild}')
            return {'error': self.ERROR}

    def _path(self, guild):
        return f'{self._dir}/{guild}.json'


def setup(bot):
    bot.add_cog(Leaderboard(bot))
