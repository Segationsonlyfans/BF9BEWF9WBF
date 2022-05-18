import discord
import asyncio
import discord.utils
from discord.utils import get
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$', intents=intents)
client.remove_command('help')

"""
MIT License

Copyright (c) 2022 Admin Helper team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name='DM ME $app'),
        status=discord.Status.dnd)

    print('Loggedin')

from discord.ext.forms import Form


@client.command(aliases=["application"])
@commands.dm_only()
@commands.cooldown(1, 60, commands.BucketType.user)
async def app(ctx):
    #blacklist = [] Add ID to blacklist. You wont become messages about a application od that user
 try:
    form = Form(ctx,'Kiwi Application')
    form.add_question('What is your age?','first')
    form.add_question('Where are you from + your discord?','second')
    form.add_question('Why do you want Kiwi?','third')
    form.add_question('How long have you used hacked clients in minecraft?', 'fourth')
    form.add_question('What other clients do you have/currently use?', 'fifth')
    form.add_question('Why do you think we should pick you to receive Kiwi?', 'sixth')
    form.add_question('tell us about yourself.', 'seventh')
    form.add_question('Do you understand that if you share Kiwi you will be blacklisted', 'eighth')
    result = await form.start()
    embed = discord.Embed(title="", description="**Thank you!**", colour=0x2ecc71)
    await ctx.send(embed=embed)
    await asyncio.sleep(2)
    embed = discord.Embed(title="", description="**This has been delivered to a Staff member!\nSomeone will reach out to you in a short amount of time!**", colour=0x2ecc71)
    embed.set_footer(text="Segations cum dump", icon_url=(f"{client.user.avatar_url}"))
    await ctx.send(embed=embed)
    auser = client.get_channel(int(976575687441907742)) #Set your Channel ID
    await auser.send("A new application has been sent!\n\nUsername: **{}**\nID: **{}**\n\nAnswers:\n\nWhat is your age?: **{}**\nWhere are you from + your discord?: **{}**\nWhy do you want Kiwi?: **{}**\nHow long have you used hacked clients in minecraft?: **{}**\nWhat other clients do you have/currently use?: **{}**\nWhy do you think we should pick you to receive Kiwi?: **{}**\nTell us something about yourself.: **{}**\nDo you understand that if you share Kiwi you will be blacklisted.: **{}**".format(ctx.author, ctx.author.id, result.first, result.second, result.third, result.fourth, result.fifth, result.sixth, result.seventh, result.eighth))
    return result     #Add role id above to ping
 except:
     embed = discord.Embed(title="", description="**You can only use this command in my DM's!**", colour=0x2fbd3a)
     await ctx.send(embed=embed)


#Just a backup

#@client.command()
#@commands.has_permissions(administrator=True)
#async def accept(ctx, *, member: discord.Member = None):
# if member == None:
#     embed = discord.Embed(title="", description="Please Mention a applicant!", colour=0x2fbd3a)
#     await ctx.send(embed=embed)
# else:
#     embed = discord.Embed(title="", description=f"<:smalltick:953286467323592744> Welcome in the team buddy!", colour=0x2ecc71)
#     await member.send(embed=embed)
#     embed = discord.Embed(title="", description="A Staff Member will message you shortly!", colour=0x2ecc71)
#     await member.send(embed=embed)
#     role = discord.utils.get(ctx.guild.roles, id=953063650967560222)
#     await member.add_roles(role)

@client.command()
@commands.has_permissions(administrator=True)
async def accept(ctx, *, member: discord.Member = None):
 if member == None:
   embed = discord.Embed(title="", description="Please Mention a applicant!", colour=0x2fbd3a)
   await ctx.send(embed=embed)
 else:
     embed = discord.Embed(title="", description=f"Welcome to kiwi!\nA Staff Member will reach out to you shortly!", colour=0x2ecc71)
     embed.set_footer(text="Segations cum dump", icon_url=(f"{client.user.avatar_url}"))
     await member.send(embed=embed)
    #guild = ctx.guild
    #staffRole = discord.utils.get(guild.roles, name="Staff")#
    #if not staffRole:
    #    staffRole = await guild.create_role(name="Staff")
    #await member.add_roles(staffRole)
    #print("finish")


@client.command()
@commands.has_permissions(administrator=True)
async def decline(ctx, user: discord.User = None, *, reason="No Reason Specified"):
 if user == None:
     embed = discord.Embed(title="", description="Please Mention a applicant!", colour=0x2fbd3a)
     await ctx.send(embed=embed)
 else:
     embed = discord.Embed(title="", description=f"You have been **rejected** from Kiwi!\nReason: **{reason}**", colour=0x2fbd3a)
     embed.set_footer(text="Segations cum dump", icon_url=(f"{client.user.avatar_url}"))
     await user.send(embed=embed)
     embed = discord.Embed(title="", description=f"__If you think this was a mistake, please message {ctx.author}__!", colour=0x2fbd3a)
     await user.send(embed=embed)


@accept.error
async def accept_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="", description="**Hey! You Don\'t Have Permissions To Use That Command!**", colour=0x2fbd3a)
        embed.set_footer(text="Segations cum dump", icon_url=(f"{client.user.avatar_url}"))
        await ctx.send(embed=embed)

@decline.error
async def decline_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="", description="**Hey! You Don\'t Have Permissions To Use That Command!**", colour=0x2fbd3a)
        embed.set_footer(text="Segations cum dump", icon_url=(f"{client.user.avatar_url}"))
        await ctx.send(embed=embed)

@app.error
async def dm_only(ctx, error):
    embed = discord.Embed(title="", description="**You can only use this command in my DM's!**", colour=0x2fbd3a)
    embed.set_footer(text="Segations cum dump", icon_url=(f"{client.user.avatar_url}"))
    await ctx.send(embed=embed)


client.run("ODY3NTQ5NTgwNDMzMDMxMzA4.GPRkkB.9wrfWWFSCoQi4gBptzRlRQRtKN3tm4897m_7xw")
