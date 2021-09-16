import discord
from discord.ext import commands, tasks


class StartUp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('am online')


def setup(client):
    client.add_cog(StartUp(client))
