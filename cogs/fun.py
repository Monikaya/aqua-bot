import random
import discord
import requests
from discord.ext import commands


class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"pong :doom: {round(client.latency * 1000)}ms")

    @commands.command(aliases=['eightball', '8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['noe',
                     'literally no',
                     'sure idk',
                     'nope',
                     'only sometimes'
                     'yk',
                     'yes but also no',
                     'depends',]
        await ctx.send(f'{random.choice(responses)}')

    @commands.command()
    async def among(self, ctx):
        poggie = ctx.message.author.id == 870357758208274463
        if poggie:
            await ctx.send("wtf poggies")
        else:
            await ctx.send("sad mongie")

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        embed = discord.Embed(title=f"{ctx.message.author} hugged {member}", color=discord.Colour.blurple())
        embed.set_footer(text="made by Aquazarine#0001")
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command()
    async def baka(self, ctx, member: discord.Member):
        r = requests.get("https://nekos.life/api/v2/img/baka")
        res = r.json()
        embed = discord.Embed(title=f"{member} is sussy baka", color=discord.Colour.blurple())
        embed.set_footer(text="made by Aquazarine#0001")
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(fun(client))
