import asyncio

from discord.ext.tasks import loop
from twisted.internet import task, reactor

import discord
from discord.ext import commands, tasks
import os
from itertools import cycle

client = commands.Bot(command_prefix='-')
status = cycle(
    ['being sus', 'sus like impostor', 'am sus', 'is sus', 'among sussy', 'being best bot', 'peeing', 'playing mongie'])


@client.command()
async def load(ctx, extension):
    poggie = ctx.message.author.id == 870357758208274463
    if poggie:
        client.load_extension(f'cogs.{extension}')
        await ctx.send("successfully loaded")


@client.command()
async def unload(ctx, extension):
    poggie = ctx.message.author.id == 870357758208274463
    if poggie:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send("successfully unloaded")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def on_ready():
    change_status.start()


@client.command()
async def autofart(ctx, delay):
    embed = discord.Embed(title="claire <3's lolis",
                          description=f"started disboard autobump with {delay} seconds of delay",
                          color=discord.Colour.blurple())
    await ctx.send(embed=embed, delete_after=20)
    delay = int(delay)
    client.bumploop = True
    while client.bumploop:
        await ctx.send("!d bump")
        randomdelay = random.randint(1, 15)
        delay = int((delay + randomdelay) * 60)
        await asyncio.sleep(delay)

@client.command()
async def stopautofart(ctx):
    if client.bumploop:
        client.bumploop = False
        embed = discord.Embed(title='bump stopped successfully', decription='stopped autobumping')
        await ctx.send(embed=embed)
    else:
        await ctx.send("you aren't autofarting")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


client.run('ODg3MTM3NTE3MDU1Mzg5NzA4.YT_xMg.MSG-cY5XUINRr8AhCL7-VCdtzmk')
