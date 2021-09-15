import discord
from discord.ext import commands, tasks
import os
from itertools import cycle

client = commands.Bot(command_prefix='-')
status = cycle(['being sus', 'sus like impostor', 'am sus', 'is sus'])


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("successfully loaded")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("successfully unloaded")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def on_ready():
    change_status.start()


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


client.run('ODg3MTM3NTE3MDU1Mzg5NzA4.YT_xMg.Q_lr1CI8TM1MAW1XwGdFru-oz5U')
