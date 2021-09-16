import random
import discord
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


def setup(client):
    client.add_cog(fun(client))