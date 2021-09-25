import asyncio
from discord.ext.tasks import loop
import discord
from discord.ext import commands, tasks
import os
from itertools import cycle
import json


def get_prefix(client, message):
    try:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        return prefixes[str(message.guild.id)]
    except KeyError:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        return prefixes[str(666)]



client = commands.Bot(command_prefix=get_prefix)
bot = client

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


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '-'

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def invite(ctx):
    embed = discord.Embed(title="invite me to your server", color=discord.Colour.blurple(),
                          description=f"add me to your server via [this link](https://discord.com/api/oauth2/authorize?client_id=887137517055389708&permissions=8&scope=bot)")
    await ctx.send(embed=embed)


client.run('ODg3MTM3NTE3MDU1Mzg5NzA4.YT_xMg.MSG-cY5XUINRr8AhCL7-VCdtzmk')
