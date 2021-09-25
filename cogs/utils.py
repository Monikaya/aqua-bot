import json

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class utils(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='changes your nickname')
    @has_permissions(change_nickname=True)
    async def nick(self, ctx, *, nick):
        if nick == 'reset':
            await ctx.message.author.edit(nick=None)
        else:
            await ctx.message.author.edit(nick=nick)

    @nick.error
    async def nick_error(self, ctx):
        if isinstance(error, MissingPermissions):
            await ctx.send("you don't have perms </3")

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


def setup(client):
    client.add_cog(utils(client))
