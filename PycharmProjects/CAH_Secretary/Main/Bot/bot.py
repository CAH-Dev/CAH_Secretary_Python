import discord
from discord.ext import commands
from discord.ext.commands import bot
from Main.Bot.var_data import *

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():

    print ("Bot Ready!")
    print("I am running on" + bot.user.name)
    print("With the ID " + bot.user.id)
#######################################################################################################################

@bot.command(pass_context=True)
async def ping(ctx):
    '''responds with pong'''
    await bot.say(":ping_pong: pong")

@bot.command(pass_context=True)
async def roles(ctx):
    '''replies with a list of all the roles the user can self role'''
    '''in future so that result string generated once on_ready'''
    roles = ctx.message.server.roles
    result = "The roles are:\n"
    for role in roles:
        if (role.name not in locked_roles):
            result += role.name + ", "
    await bot.say(result[:-2])

@bot.command(pass_context = True)
async def role(ctx, user: discord.Member):
    '''self roles user if not restricted'''
    if not set(user.roles).isdisjoint(restricted_roles):
        await bot.say("Oops! "+ user.mention +"Accepted and Committed members cannot self role! Please contact a staff member.")
    await bot.say("success")


#######################################################################################################################
bot.run(token)