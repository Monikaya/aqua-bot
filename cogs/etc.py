import nextcord
from nextcord.ext import commands
import aiohttp


class etc(commands.Cog):

    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(etc(client))
