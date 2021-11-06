import json
import threading
import time

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from kahot import join


class utils(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief="changes ur nick")
    @has_permissions(change_nickname=True)
    async def nick(self, ctx, *, nick):
        embed = discord.Embed(title="changed nick", description=f"sucessfully changed nick to {nick}",
                              color=discord.Colour.blurple())

        if nick == "reset":
            embed.description = f"nick reset sucessfully"
            await ctx.message.author.edit(nick=None)
            await ctx.send(embed=embed)

        await ctx.message.author.edit(nick=nick)
        await ctx.send(embed=embed)

    @commands.command(brief='changes bot prefix')
    @has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):

        embed = discord.Embed(title="changed prefix",
                              description=f"prolly changed prefix to {prefix}", color=discord.Colour.blurple())
        await ctx.send(embed=embed)

        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

    @changeprefix.error
    async def changeprefix_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("you don't have perms lol")

    @commands.command(brief='invite code for bot')
    async def invite(self, ctx):
        embed = discord.Embed(title="invite me to your server", color=discord.Colour.blurple(),
                              description=f"add me to your server via [this link](https://discord.com/api/oauth2/authorize?client_id=887137517055389708&permissions=8&scope=bot)")
        await ctx.send(embed=embed)

    @commands.command()
    async def kahot(self, ctx, code, user, instances):
        await ctx.send("starting kahot spam")
        thread_list = list()
        instances = int(instances)
        for i in range(instances):
            t = threading.Thread(target=join, args=(code, user))
            t.start()
            time.sleep(0.3)
            thread_list.append(t)
        for thread in thread_list:
            thread.join()


def setup(client):
    client.add_cog(utils(client))
