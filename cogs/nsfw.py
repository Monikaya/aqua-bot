import re
import string
import discord
import requests
from discord.ext import commands
import os

try:
    from pygelbooru import Gelbooru
except ImportError:
    os.system('pip install pygelbooru')
    from pygelbooru import Gelbooru


class nsfw(commands.Cog):

    def __init__(self, client):
        self.client = client

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

    @commands.command()
    async def succ(self, ctx, member):
        channelnsfw = ctx.channel.is_nsfw()
        if channelnsfw:
            embed = discord.Embed(title='sucks ducc', description=f"{ctx.message.author.mention} sucks off {member}",
                                  color=discord.Color.blurple())
            r = requests.get("https://nekos.life/api/v2/img/bj")
            res = r.json()
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
        else:
            await ctx.send("channel isn't nsfw smh")

    @commands.command()
    async def gelbooru(self, ctx, *, tags):
        if ctx.channel.is_nsfw():
            tagsnew = re.sub('[' + string.punctuation + ']', '', tags).split()
            gelbooru = Gelbooru(
                '&api_key=571aee667df493a3acb132a79fe89642e a7d189a14dd43a07b5538c57731ffea&user_id=904295', '904295')
            res = await gelbooru.random_post(tags=tagsnew)
            if res is None:
                embed = discord.Embed(title="rip", description=f"there was no result for '{tags}'",
                                      color=discord.Colour.blurple())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(color=discord.Colour.blurple())
                embed.set_image(url=str(res))
                await ctx.send(embed=embed)
        else:
            await ctx.send("channel  isn't nsfw smh")


def setup(client):
    client.add_cog(nsfw(client))
