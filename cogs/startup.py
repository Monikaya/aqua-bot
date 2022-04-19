import logging

from nextcord.ext import commands


class StartUp(commands.Cog):

    def __init__(self, client):
        self.client = client

    logger = logging.getLogger('nextcord')
    logger.setLevel(logging.WARNING)
    handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    @commands.Cog.listener()
    async def on_ready(self):
        print('am online')



def setup(client):
    client.add_cog(StartUp(client))
