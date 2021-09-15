import discord
from discord.ext import commands
import aiohttp


class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        vc = await channel.connect()

    @commands.command()
    async def play(self, ctx, *, url):
        channel = ctx.author.voice.channel
        vc = await channel.connect()

        player = await vc.create_ytdl_player(url)
        player.start()

    BASE = "https://youtube.com/results"

    @commands.command()
    async def youtube(self, ctx, *, search, base="https://youtube.com/results"):
        p = {"search_query": search}
        # Spoof a user agent header or the request will immediately fail
        h = {"User-Agent": "Mozilla/5.0"}
        async with aiohttp.ClientSession() as client:
            async with client.get(base, params=p, headers=h) as resp:
                dom = await resp.text()
                # open("debug.html", "w").write(dom)
        found = re.findall(r'href"\/watch\?v=([a-zA-Z0-9_-]{11})', dom)
        return f"https://youtu.be/{found[0]}"


def setup(client):
    client.add_cog(Music(client))
