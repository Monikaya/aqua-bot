import json
import os
from itertools import cycle
import aiohttp
import nextcord
from nextcord.ext import commands, tasks


def get_prefix(client, message):
    prefixlist = os.getcwd() + "/prefixes.json"
    if not os.path.exists(prefixlist):
        with open(prefixlist, 'w') as f:
            f.write('{}')
        with open(prefixlist, 'r') as f:
            prefixes = json.load(f)

        prefixes[str(666)] = '-'
        with open(prefixlist, "w") as f:
            json.dump(prefixes, f, indent=4)
    try:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        return prefixes[str(message.guild.id)]
    except KeyError:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        return prefixes[str(666)]

client = commands.Bot(command_prefix=get_prefix)

status = cycle(
    ['being sus', 'sus like impostor', 'am sus', 'is sus', 'among sussy', 'peeing', 'playing mongie', 'sussy baka'])


@client.command(hidden=True)
async def load(ctx, extension):
    poggie = ctx.message.author.id == 870357758208274463
    if poggie:
        client.load_extension(f'cogs.{extension}')
        await ctx.send("successfully loaded")


@client.command(hidden=True)
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
    await client.change_presence(activity=nextcord.Game(next(status)))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = nextcord.Embed(title=f"invalid command", description=f"command not found lolmao",
                           color=nextcord.Colour.blurple())
        await ctx.send(embed=em)


client.run('OTMyMDY2Nzc1NjQ5MTEyMTg1.YeNk1A.QZyfXWiDfErPUMCHNeswtB4cOSI')
