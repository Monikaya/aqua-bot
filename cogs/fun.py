import random
import nextcord
import requests
from nextcord.ext import commands
from nextcord import *

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='pong')
    async def ping(self, ctx):
        await ctx.send(f"pong :doom: {round(client.latency * 1000)}ms")

    @commands.command(aliases=['eightball', '8ball'], brief='8ball', description='answers your question with magic idk')
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

    @commands.command(hidden=True)
    async def among(self, ctx):
        poggie = ctx.message.author.id == 870357758208274463
        if poggie:
            await ctx.send("wtf poggies")
        else:
            await ctx.send("sad mongie")

    @commands.command(brief='hugs someone :D')
    async def hug(self, ctx, member: commands.MemberConverter):
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        embed = nextcord.Embed(title=f"{ctx.message.author} hugged {member}", color=nextcord.Colour.blurple())
        embed.set_footer(text="made by Aquazarine#0001")
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command(brief='baka')
    async def baka(self, ctx, member: commands.MemberConverter):
        r = requests.get("https://nekos.life/api/v2/img/baka")
        res = r.json()
        embed = nextcord.Embed(title=f"{member} is sussy baka", color=nextcord.Colour.blurple())
        embed.set_footer(text="made by Aquazarine#0001")
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command(brief='pokes someone')
    async def poke(self, ctx, member: commands.MemberConverter):
        r = requests.get("https://nekos.life/api/v2/img/poke")
        res = r.json()
        sender = ctx.message.author
        embed = nextcord.Embed(title=f"{member} got poked by {sender}", color=nextcord.Colour.blurple())
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command(brief='cuddle')
    async def cuddle(self, ctx, member: commands.MemberConverter):
        r = requests.get("https://nekos.life/api/v2/img/cuddle")
        res = r.json()
        sender = ctx.message.author
        embed = nextcord.Embed(title=f"{sender} cuddles {member}", color=nextcord.Colour.blurple())
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command(brief='*pat*')
    async def pat(self, ctx, member: commands.MemberConverter):
        r = requests.get("https://nekos.life/api/v2/img/pat")
        res = r.json()
        sender = ctx.message.author
        embed = nextcord.Embed(title=f"{sender} pats {member}", color=nextcord.Colour.blurple())
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command(brief='flips coin')
    async def coinflip(self, ctx):
        CoinSides = ['heads',
                    'tails']
        await ctx.send(f'{random.choice(CoinSides)}')

    @commands.command(brief='rolls a die')
    async def roll(self, ctx):
        DiceSides = ['one', 'two', 'three', 'four', 'five', 'six']
        await ctx.send(f"you rolled a {random.choice(DiceSides)}")

    @commands.command(brief='troll lol', hidden=True)
    async def troll(self, ctx):
        await ctx.send("https://clipartcraft.com/images/troll-face-transparent-1.png")

    @commands.command(brief='rly cool')
    async def embarrass(self, ctx, member):
        print("piss")
        pfp = member.avatar_url
        print(pfp)
        weebhook = await ctx.create_webhook(name="member", avatar=pfp)
        await ctx.send("pee")
        print(weebhook)


def setup(client):
    client.add_cog(fun(client))
