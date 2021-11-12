import json
import discord
from discord import member
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get


class utils(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief="changes ur nick")
    @has_permissions(change_nickname=True)
    async def nick(self, ctx, *, nick):
        embed = discord.Embed(title="changed nick", description=f"sucessfully changed nick to {nick}",
                              color=discord.Colour.blurple())

        if nick == "reset":
            mbed.description = f"nick reset sucessfully"
            await ctx.message.author.edit(nick=None)
            await ctx.send(embed=embed)

        await ctx.message.author.edit(nick=nick)
        await ctx.send(embed=embed)

    @commands.command(brief='changes bot prefix')
    @has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):

        embed = discord.Embed(title="changed prefix",
                              description=f"prolly changed prefix to {prefix}", color=discord.Colour.blurple())
        await ctx.send(embed=embed)

        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

    @changeprefix.error
    async def changeprefix_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("you don't have perms lol")

    @commands.command(brief='invite code for bot')
    async def invite(self, ctx):
        embed = discord.Embed(title="invite me to your server", color=discord.Colour.blurple(),
                              description=f"add me to your server via [this link](https://discord.com/api/oauth2/authorize?client_id=887137517055389708&permissions=8&scope=bot)")
        await ctx.send(embed=embed)

    @commands.command()
    async def pronouns(self, ctx, pronouns):
        if "/" in pronouns:
            allowedvalu = True
        elif pronouns == "no.pronouns" or "any.pronouns":
            allowedvalu = True
        else:
            allowedvalu = False

        if allowedvalu:
            if get(ctx.guild.roles, name=pronouns):
                pronounrole = get(ctx.guild.roles, name=pronouns)
                roleexists = True
            else:
                roleexists = False

            if roleexists:
                await ctx.message.author.add_roles(pronounrole, reason="pronoun cmd")
                await ctx,send(f"gave you the role '{pronounrole}'")
            elif not roleexists:
                newpronounrole = await ctx.guild.create_role(name=pronouns, mentionable=False,
                                                             reason='made by pronoun cmd')
                await ctx.message.author.add_roles(newpronounrole, reason="also pronounds command")
                embed = discord.Embed(title="added rple", description=f"added role '{pronouns}'",
                                      color=discord.Colour.blurple())

            await ctx.send(embed=embed)
        elif not allowedvalu:
            await ctx.send("uhh invalid role idk if ur trying to use no or any pronouns then it's like 'any.pronouns' or 'no.pronouns', lmk if there's anything else i'd need to whitelist tho")

    @commands.command()
    async def removepronouns(self, ctx, pronoun):
        if "/" in pronoun:
            allowedvalu = True
        elif pronoun == "no.pronouns" or "any.pronouns":
            allowedvalu = True
        else:
            allowedvalu = False

        if allowedvalu:
            roletoremove = get(ctx.message.author.roles, name=pronoun)
            await ctx.message.author.remove_roles(roletoremove, reason="remove cmd pronouns")
            embed = discord.Embed(title="removed role", description=f"removed role '{roletoremove}'", color=discord.Colour.blurple())
            await ctx.send(embed=embed)
        elif allowedvalu == False:
            await ctx.send("you either don't have the role or it's invalid idk")
        elif allowedvalu == None:
            await ctx.send("you either don't have the role or it's invalid idk")



def setup(client):
    client.add_cog(utils(client))
