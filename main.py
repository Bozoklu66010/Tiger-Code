import os
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

token = os.environ.get('DISCORD_BOT_TOKEN')


SPAM_CHANNEL =  ["https://discord.gg/EMfADKgTdh runs you" , "Get ran" , "https://discord.gg/EMfADKgTdh" , "oops Beamed","https://discord.gg/CJGDSREU Beamed You","Shoulda Listened","Get beamed clowns","Beamed by https://discord.gg/CJGDSREU","oops got nuked","I run you","beamed by https://discord.gg/CJGDSREU","I run you","kinda got beamed by https://discord.gg/CJGDSREU"]
SPAM_MESSAGE = ["@everyone https://discord.gg/EMfADKgTdh"]

client = commands.Bot(command_prefix="+")


@client.event
async def on_ready():
   print(''' 
   
███╗░░██╗██╗░░░██╗██╗░░██╗███████╗  ██████╗░░█████╗░████████╗
████╗░██║██║░░░██║██║░██╔╝██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝ 
██╔██╗██║██║░░░██║█████═╝░█████╗░░  ██████╦╝██║░░██║░░░██║░░░ 
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░ 
██║░╚███║╚██████╔╝██║░╚██╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░  
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░ 
 ''')
   await client.change_presence(activity=discord.Game(name="Taming skids"))

@client.command()
@commands.is_owner()
async def 𝐁𝐨𝐭_𝐒𝐭𝐨𝐩(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

client.run(token, bot=True)
