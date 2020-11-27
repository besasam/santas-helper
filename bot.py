import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
intents = discord.Intents.default()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = 'aoc!'

cogs = ['Functions.levels', 'Functions.leaderboard']

client = commands.Bot(command_prefix=PREFIX, help_command=None, intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(status=discord.Status.online)
    for cog in cogs:
        try:
            print(f'Loading cog {cog}')
            client.load_extension(cog)
            print(f'Loaded cog {cog}')
        except Exception as e:
            print(f'Failed to load cog {cog}\n{type(e).__name__}: {e}')


client.run(TOKEN)
