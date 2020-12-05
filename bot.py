import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import sqlite3
intents = discord.Intents.default()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = 'aoc!'

cogs = ['functions.levels', 'functions.leaderboard']

client = commands.Bot(command_prefix=PREFIX, help_command=None, intents=intents)
client.url = 'https://adventofcode.com'
client.conn = sqlite3.connect('data.db')
client.db = client.conn.cursor()


# Creates SQLite tables if they don't yet exist
# users: Discord user info (global)
# guilds: Server info and AoC leaderboard
# guild_members: user to server mapping
# Also I have never used SQLite before so I hope this will work lmao
def setup_db(conn):
    users = '''CREATE TABLE IF NOT EXISTS users (
    id      INTEGER PRIMARY KEY NOT NULL,
    aoc     INTEGER NOT NULL,
    github  CHAR(39),
    repo    CHAR(100)
    );'''
    guilds = '''CREATE TABLE IF NOT EXISTS guilds (
    id              INTEGER PRIMARY KEY NOT NULL,
    leaderboard     INTEGER,
    code            CHAR(20),
    owner           INTEGER
    );'''
    guild_members = '''CREATE TABLE IF NOT EXISTS guild_members (
    id      INTEGER NOT NULL,
    user    INTEGER NOT NULL,
    PRIMARY KEY(id, user)
    );'''
    for stmt in [users, guilds, guild_members]:
        conn.execute(stmt)


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
    setup_db(client.conn)


client.run(TOKEN)
