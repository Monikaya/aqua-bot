import asyncio
from discord.ext.tasks import loop
import discord
from discord.ext import commands, tasks
import os
from itertools import cycle
import json
from pretty_help import PrettyHelp, DefaultMenu


def get_prefix(client, message):
    try:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        return prefixes[str(message.guild.id)]
    except KeyError:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        return prefixes[str(666)]


menu = DefaultMenu(delete_after_timeout=True, active_time=60)

client = commands.Bot(command_prefix=get_prefix, help_command=PrettyHelp(color=discord.Colour.blurple(), menu=menu))

status = cycle(
    ['being sus', 'sus like impostor', 'am sus', 'is sus', 'among sussy', 'being best bot', 'peeing', 'playing mongie'])


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
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(title=f"invalid command", description=f"command not found lolmao", color=ctx.author.color)
        await ctx.send(embed=em)


client.run('ODkxMzM2ODk5MDMyMTQxODY1.YU84LA.Q888JJbywpeinDDvw716RrJHZpY')
