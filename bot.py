import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='-')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('ODg3MTM3NTE3MDU1Mzg5NzA4.YT_xMg.Q_lr1CI8TM1MAW1XwGdFru-oz5U')
