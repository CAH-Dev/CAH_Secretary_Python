from discord.ext import commands
from discord.ext.commands import bot

from Main.src.var_data import *

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    #in future try to load server roles once here if possible
    #load_server_roles()
    print ("Bot Ready!")
    print("I am running on" + bot.user.name)
    print("With the ID " + bot.user.id)
#######################################################################################################################

''''@bot.event(ctx)
def load_server_roles(ctx):
    roles = ctx.message.server.roles
    for role in roles:
        if (role.name not in locked_roles):
            roles_str.append(role.name + ", ")'''

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
async def role(ctx, arg : str):
    '''self roles user if not restricted'''
    user_roles = ctx.message.author.roles
    if arg in locked_roles:
        await bot.say("Ya doof! " + arg + " can't be self assigned!")
    for role in user_roles:
        if role.name in restricted_roles:
            await bot.say("Oops! "+ ctx.message.author.mention +" Accepted and Committed members cannot self role! "+
                          "Please contact a staff member if you would like to change your roles!")
            return
    #need to finish adding self roling. 1) compare with users current roles to check if he already has it 2) assign role



#######################################################################################################################
bot.run(token)