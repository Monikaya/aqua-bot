import asyncio

import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, has_permissions, bot_has_permissions, BotMissingPermissions


class admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['clear'], brief='purges msgs')
    @has_permissions(manage_messages=True)
    @bot_has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("you don't have perms")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you didn't put in amount smh")
        if isinstance(error, BotMissingPermissions):
            await ctx.send("bot doesn't have perms :c")

    @commands.command(brief='kicks ppl')
    @has_permissions(kick_members=True)
    @bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        await ctx.guild.kick(member, reason=reason)
        await ctx.send(f'kicked {member} for {reason}')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("you don't have perms lol")
        if isinstance(error, BotMissingPermissions):
            await ctx.send("bot missing permissions")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you didn't tell me who to kick")

    @commands.command(brief='bans a member')
    @has_permissions(ban_members=True)
    @bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"banned {member} for {reason}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("you don't have perms")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you didn't tell me who to ban")
        if isinstance(error, BotMissingPermissions):
            await ctx.send("bot doesn't have perms </3")

    class DurationConverter(commands.Converter):
        async def convert(self, ctx, argument):
            amount = argument[:-1]
            unit = argument[-1]
            print(amount)
            print(unit)

            if amount.isdigit() and unit in ['s', 'm', 'h', 'd', 'mo', 'y']:
                return int(amount), unit

            raise commands.BadArgument(message="not valid duration")

    @commands.command(brief='tempbans a member')
    @has_permissions(ban_members=True)
    @bot_has_permissions(ban_members=True)
    async def tempban(self, ctx, member: commands.MemberConverter, duration: DurationConverter, *, reason=None):

        multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'w': 604800, 'mo': 2629800, 'y': 31557600}
        amount, unit = duration
        await ctx.guild.ban(member)
        embed = discord.Embed(title='member tempbanned', color=discord.Colour.blurple(),
                              description=f'{member} has been banned for {amount}{unit}')
        await ctx.send(embed=embed)
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)

    @tempban.error
    async def tempban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("you don't have perms lol")
        if isinstance(error, BotMissingPermissions):
            await ctx.send("bot doesn't have perms </3")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you didn't tell me who to tempban :c")

    @commands.command(brief='unbans someone who is banned')
    @has_permissions(ban_members=True)
    async def unban(self, ctx, *, member: discord.Member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'unbanned {user.mention}')
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("you don't have perms")


def setup(client):
    client.add_cog(admin(client))
