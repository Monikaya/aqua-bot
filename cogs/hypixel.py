import discord
from discord.ext import commands
import requests


class hypixelstuf(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hypixel(self, ctx, *, mcuser):
        data = requests.get(url="https://api.hypixel.net/player",
                            params={
                                "key": "6dabe323-e57b-4a1d-aa55-8553a6c6b08c",
                                "name": mcuser
                            }).json()
        skywarscoins = data["player"]["stats"]["SkyWars"]["coins"]
        await ctx.send(skywarscoins)



def setup(client):
    client.add_cog(hypixelstuf(client))
