import discord
import requests
from discord import channel
from discord.ext import commands
import aiohttp
from discord.ext.commands import is_nsfw


class nsfw(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
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


    @commands.command()
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


    @commands.command()
    async def feet(self, ctx):
        channelnsfw = ctx.channel.is_nsfw()
        if channelnsfw:
            r = requests.get("https://nekos.life/api/v2/img/feetg")
            res = r.json()
            embed = discord.Embed(title="feet. wtf.", color=discord.Colour.red())
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
        else:
            await ctx.send("you aren't in nsfw channel")


    @commands.command()
    async def trap(self, ctx):
        channelnsfw = ctx.channel.is_nsfw()
        if channelnsfw:
            r = requests.get("https://nekos.life/api/v2/img/trap")
            res = r.json()
            embed = discord.Embed(title="trap lol", color=discord.Colour.blurple())
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
        else:
            await ctx.send("you aren't in nsfw channel")


    @commands.command()
    async def femdom(self, ctx):
        channelnsfw = ctx.channel.is_nsfw()
        if channelnsfw:
            r = requests.get("https://nekos.life/api/v2/img/femdom")
            res = r.json()
            embed = discord.Embed(title="femdom", color=discord.Colour.blurple())
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
        else:
            await ctx.send("you aren't in nsfw channel")



def setup(client):
    client.add_cog(nsfw(client))
