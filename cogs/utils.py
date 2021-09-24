import json

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class utils(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nick(self, ctx, *, nick):
        if nick == 'reset':
            await ctx.message.author.edit(nick=None)
        else:
            await ctx.message.author.edit(nick=nick)

    @commands.command()
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



def setup(client):
    client.add_cog(utils(client))
