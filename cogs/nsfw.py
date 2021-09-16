import discord
import requests
from discord.ext import commands
import aiohttp


class nsfw(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hentai(self, ctx):
        r = requests.get("https://nekos.life/api/v2/img/classic")
        res = r.json()
        embed = discord.Embed(title="hentai lol", color=discord.Colour.blurple())
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command()
    async def boobs(self, ctx):
        r = requests.get("https://nekos.life/api/v2/img/tits")
        res = r.json()
        embed = discord.Embed(title="boobies :D", color=discord.Colour.blurple())
        embed.set_image(url=res['url'])


def setup(client):
    client.add_cog(nsfw(client))
