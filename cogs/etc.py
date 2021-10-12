import discord
from discord import AsyncWebhookAdapter, Webhook
from discord.ext import commands
import aiohttp


class etc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(
                'https://discord.com/api/webhooks/897256513096257556/pyUaTSnhZFFNYiXQ9UEPZ0tdsAoVaNN2jGIju94rvJB8anJGGrfJpxufwwn9Ou759UQ0',
                adapter=AsyncWebhookAdapter(session))

            embed = discord.Embed(title="Bot was invited into a server",
                                  description=f"servername: {guild.name} \n serverid: {guild.id} \n membercount: {guild.member_count}",
                                  color=discord.Colour.blurple())
            await webhook.send(embed=embed, username="Aqua Join Logs", avatar_url="https://cdn.discordapp.com/attachments/875661506887426088/897269923636715541/amongie.jpg")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url("https://discord.com/api/webhooks/897256513096257556/pyUaTSnhZFFNYiXQ9UEPZ0tdsAoVaNN2jGIju94rvJB8anJGGrfJpxufwwn9Ou759UQ0",
                                       adapter=AsyncWebhookAdapter(session))

            embed = discord.Embed(title="Bot was removed from a server",
                                  description=f"servername: {guild.name} \n serverid: {guild.id} \n this is not a poggie moment",
                                  color=discord.Colour.blurple())
            await webhook.send(embed=embed, username="Aqua Leave Log", avatar_url="https://cdn.discordapp.com/attachments/875661506887426088/897269923636715541/amongie.jpg")


def setup(client):
    client.add_cog(etc(client))
