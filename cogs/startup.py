import discord
from discord.ext import commands, tasks
from itertools import cycle


class StartUp(commands.Cog):

    def __init__(self, client):
        self.client = client
        status = cycle(
            ['being sus', 'is kinda sussy', 'sus like impostor', 'gayming', 'doing sus things', 'playing mogus'])

    @commands.Cog.listener()
    async def on_ready(self):
        print('am online')


def setup(client):
    client.add_cog(StartUp(client))
