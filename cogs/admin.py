import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, has_permissions


class admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['clear'])
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("you don't have perms")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you didn't put in amount smh")

    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'kicked {member.mention} for {reason}')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("you don't have perms")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you didn't tell me who to kick")

    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"banned {member.mention} for {reason}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("you don't have perms")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you didn't tell me who to ban")

    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
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
