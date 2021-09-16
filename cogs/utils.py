import urllib

import discord
import requests
from discord.ext import commands
from discord.ext.commands import MissingPermissions, has_permissions


class utils(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nick(self, ctx, *, nick):
        if nick == 'reset':
            await ctx.message.author.edit(nick=None)
        else:
            await ctx.message.author.edit(nick=nick)


def setup(client):
    client.add_cog(utils(client))
