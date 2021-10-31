import discord
import requests
from discord import channel
from discord.ext import commands
import aiohttp
from discord.ext.commands import is_nsfw


class nsfw(commands.Cog):

    def __init__(self, client):
        self.clicent = client

    @commands.command(brief="you can guess")
    async def hentai(self, ctx):
        channelnsfw = ctx.channel.is_nsfw()
        if channelnsfw:
            r = requests.get("https://nekos.life/api/v2/img/classic")
            res = r.json()
            embed = discord.Embed(title="hentai lol", color=discord.Colour.blurple())
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
        else:
            await ctx.send("you aren't in nsfw channel")

    @commands.command(brief='self explanatory')
    async def boobs(self, ctx):
        channelnsfw = ctx.channel.is_nsfw()
        if channelnsfw:
            r = requests.get("https://nekos.life/api/v2/img/tits")
            res = r.json()
            embed = discord.Embed(title="boobies :D", color=discord.Colour.blurple())
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
        else:
            await ctx.send("you aren't in nsfw channel")

    @commands.command(aliases=['toes'], brief='for the funny yes yes')
    async def feet(self, ctx, *, bypass=None):
        channelnsfw = ctx.channel.is_nsfw()
        if channelnsfw:
            r = requests.get("https://nekos.life/api/v2/img/feetg")
            res = r.json()
            embed = discord.Embed(title="feet. wtf.", color=discord.Colour.red())
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
        else:
            await ctx.send("you aren't in nsfw channel")

    @commands.command(hidden=True)
    async def sendfeet(self, ctx):
        if ctx.message.author.id == 870357758208274463:
            r = requests.get("https://nekos.life/api/v2/img/feetg")
            res = r.json()
            embed = discord.Embed(title="feet. wtf.", color=discord.Colour.red())
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
        else:
            await ctx.send("you aren't me ngl")

    @commands.command()
    async def waifu(self, ctx):
        r = requests.get('https://nekos.life/api/v2/img/waifu')
        res = r.json()
        embed = discord.Embed(title="waifu lmao", color=discord.Colour.blurple())
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(nsfw(client))
