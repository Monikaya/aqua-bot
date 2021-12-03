import json
import os
from itertools import cycle

import aiohttp
import discord
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands, tasks
from pretty_help import PrettyHelp, DefaultMenu

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


menu = DefaultMenu(delete_after_timeout=True, active_time=60)

client = commands.Bot(command_prefix=get_prefix, help_command=PrettyHelp(color=discord.Colour.blurple(), menu=menu))

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
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(title=f"invalid command", description=f"command not found lolmao",
                           color=discord.Colour.blurple())
        await ctx.send(embed=em)


@client.command()
async def suggest(ctx, *, suggestion):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(
            'https://discord.com/api/webhooks/908182336695332874/5ei956Ky0ucSwu7Z1UuxRw0yrdk2_OoAXnz0N5g_RphAEMXl-a10YQNvKIF8Jgw5sSSF',
            adapter=AsyncWebhookAdapter(session))
        sender = ctx.message.author
        embed = discord.Embed(title=f"suggestion from {sender}",
                              description=f"'{sender.mention}' suggested this:\n{suggestion}", color=discord.Colour.blurple())
        await webhook.send(embed=embed, username="Aqua Suggestions",
                           avatar_url="https://cdn.discordapp.com/attachments/875661506887426088/897269923636715541/amongie.jpg")
        embed = discord.Embed(title="sent suggestion", description="sent your suggestion sucessfully thanks! :D", color=discord.Colour.blurple())
        await ctx.send(embed)


client.run('ODg3MTM3NTE3MDU1Mzg5NzA4.YT_xMg.MSG-cY5XUINRr8AhCL7-VCdtzmk')
