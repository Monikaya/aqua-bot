import asyncio
import discord
from discord.ext import commands, tasks
import logging

def gaysex():
    asyncio.run(peepee())


class StartUp(commands.Cog):

    def __init__(self, client):
        self.client = client

    logger = logging.getLogger('discord')
    logger.setLevel(logging.WARNING)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    @commands.Cog.listener()
    async def on_ready(self):
        print('am online')



def setup(client):
    client.add_cog(StartUp(client))
