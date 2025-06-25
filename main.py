try:
    import discord
    from discord.ext import commands
    import json
    import os
    import random
    import requests
    import asyncio
    import string
    import time
    import datetime
    import platform
    import itertools
    from gtts import gTTS
    import io
    import qrcode
    import pyfiglet
    import threading
    import psutil
    import aiohttp
    import colorama
    import ctypes
    import subprocess
    import sys
    from colorama import init

except Exception as e:
   ErrorModule(e)

init(autoreset=True)
color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
blue = color.BLUE
yellow = color.YELLOW

r = red
w = white
g = green
b = blue
y = yellow
c = y


BEFORE = f'{red}[{white}'
AFTER = f'{red}]'

BEFORE_GREEN = f'{green}[{white}'
AFTER_GREEN = f'{green}]'

INPUT = f'{BEFORE}>{AFTER} |'
INFO = f'{BEFORE}!{AFTER} |'
ERROR = f'{BEFORE}x{AFTER} |'
ADD = f'{BEFORE}+{AFTER} |'
WAIT = f'{BEFORE}~{AFTER} |'
NOTE = f'{BEFORE}NOTE{AFTER} |'

GEN_VALID = f'{BEFORE_GREEN}+{AFTER_GREEN} |'
GEN_INVALID = f'{BEFORE}x{AFTER} |'

INFO_ADD = f'{white}[{red}+{white}]{red}'

tool_path = os.path.dirname(os.path.abspath(__file__))
try:
    if sys.platform.startswith("win"):
        os_name = "Windows"
    elif sys.platform.startswith("linux"):
        os_name = "Linux"
    else:
        os_name = "Unknown"
except:
    os_name = "None"

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')


def MainColor2(text):
    start_color = (168, 5, 5)  
    end_color = (255, 118, 118)

    num_steps = 9

    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))
    
    colors += list(reversed(colors[:-1]))  
    
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
       
    lines = text.split('\n')
    num_colors = len(colors)
    
    result = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            color_index = (i + j) % num_colors
            color = colors[color_index]
            result.append(text_color(*color) + char + "\033[0m")
        
        if i < len(lines) - 1:
            result.append('\n')
    
    return ''.join(result)

def Continue():
    input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Press to continue -> " + reset)

def Error(e,a):
    if a in ['true','True']:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white}{e}")
    else:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white}{e}", reset)
        Continue()
        Reset()
    
    
def Title(title):
    if os_name == "Windows":
        ctypes.windll.kernel32.SetConsoleTitleW(f"{title}")
    elif os_name == "Linux":
        sys.stdout.write(f"\x1b]2;{title}\x07")
        
def Clear():
    if os_name == "Windows":
        os.system("cls")
    elif os_name == "Linux":
        os.system("clear")

def Reset():
    if os_name == "Windows":
        file = ['python', os.path.join(tool_path, "Kitwsy.py")]
        subprocess.run(file)

    elif os_name == "Linux":
        file = ['python3', os.path.join(tool_path, "Kitwsy.py")]
        subprocess.run(file)    

def Choice1TokenDiscord():
    def CheckToken(token_number, token):
        response = requests.get('https://discord.com/api/v10/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            user = requests.get(
                'https://discord.com/api/v10/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_sensur = token[:-25] + '.' * 3
            print(f" {BEFORE}{token_number}{AFTER} -> {red}Status: {white}Valid{red} | User: {white}{username_discord}{red} | Token: {white}{token_sensur}")
        else:
            print(f" {BEFORE}{token_number}{AFTER} -> {red}Status: {white}Invalid{red} | {red}Token: {white}{token}")

    file_token_discord_relative = "\\2-Input\\TokenDisc\\TokenDisc.txt"
    file_token_discord = os.path.join(tool_path, "2-Input", "TokenDisc", "TokenDisc.txt")

    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Token Discord ({white}{file_token_discord_relative}{red}):\n")
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
    
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    if not tokens:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} No Token Discord in file: {white}{file_token_discord_relative}{red} Please add tokens to the file.")
        Continue()
        Reset()
        return None

    try:
        selected_token_number = int(input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Token Number -> {reset}"))
    except:
        ErrorChoice()

    selected_token = tokens.get(selected_token_number)
    if selected_token:
        r = requests.get('https://discord.com/api/v10/users/@me', headers={'Authorization': selected_token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            pass
        else:
            ErrorToken()
    else:
        ErrorChoice()
    return selected_token

def Slow(text):
    delai = 0.03
    lignes = text.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)


discord_banner = MainColor2(r"""
                                              @@@@                @%@@                                      
                                       @@@@@@@@@@@@               @@@@@@@@@@%                               
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                         
                                %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                    
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                          %@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@%                  
                          %@@@@@@@@@@@@@@@@        %@@@@@@@@@@@%@        @@@@@@@@@@@@@@@@@                  
                          %@@@@@@@@@@@@@@@          @@@@@@@@@@@@          @@@@@@@@@@@@@@@%                  
                         %@@@@@@@@@@@@@@@@          @@@@@@@@@@@%          %@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@%         @@@@@@@@@@@%         %@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@      %@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@%                 
                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                           @%@@@@@@@@@@@@@%@@   @@@@%@@@@@@@@@%%%@%@@  @@@@@@@@@@@@@@@@@@                   
                              @@%@@@@@@@@@@@@@                        @%@@@@@@@@@@@%@@                      
                                   @%@@@@@@@                            @@@@@@%%@                           
                                         @@                              @@                           
""")


prefix = ","
start_time = datetime.datetime.now(datetime.timezone.utc)

base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, "Config", "Settings.json")

if not os.path.exists(os.path.join(base_dir, "Config")):
    os.makedirs(os.path.join(base_dir, "Config"))

if not os.path.isfile(config_path):
    with open(config_path, "w") as file:
        json.dump({"prefix": ","}, file, indent=4)  

with open(config_path, "r") as file:
    config = json.load(file)

def save_config(config):
    with open(config_path, "w") as file:
        json.dump(config, file, indent=4)

def Headers(token):
    return {'authority': 'discord.com', 'accept': '*/*', 'accept-language': 'fr-FR,fr;q=0.9','authorization': token,'cache-control': 'no-cache','content-type': 'application/json','cookie': '__dcfduid=676e06b0565b11ed90f9d90136e0396b; __sdcfduid=676e06b1565b11ed90f9d90136e0396bc28dfd451bebab0345b0999e942886d8dfd7b90f193729042dd3b62e2b13812f; __cfruid=1cefec7e9c504b453c3f7111ebc4940c5a92dd08-1666918609; locale=en-US','origin': 'https://discord.com','pragma': 'no-cache','referer': 'https://discord.com/channels/@me','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'en-US', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlcGVhc2VfY2hhbm5lcCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1NDc1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',}

def bypassheaders(token):  
        headers = {
        'authority': 'discord.com',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDExIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTc5ODgyLCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMDMwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
        'x-discord-locale': 'en',
        'x-debug-options': 'bugReporterEnabled',
        'accept-language': 'en',
        'authorization': token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9011 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://discord.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
         } 
        return headers

prefix = config.get("prefix", ",")


numberofcommands = 17
cpcmdslist = 5
ucmdslist = 11
rpccmdslist = 3
sscmdslist = 0

ladder_users = {}
beef = "Off"
NOC = numberofcommands

bot = commands.Bot(command_prefix=prefix, description='not a selfbot', self_bot=True, help_command=None)

@bot.event
async def on_ready():
    Clear()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

@bot.event
async def on_message(message):
    
    if message.author.id in ladder_users:
        try:
            await message.reply(ladder_users[message.author.id], mention_author=True)
        except discord.Forbidden:
            Error(f"Cannot send message in {message.channel}")
                
    
    if message.author.id in [1377173425700999199,1385595599977582663]: # THIS IS FOR TROLLING, REPLACE THE IDS IF YOU WANT TO LOOL, IF U DONT WANT THIS JUST REMOVE THIS LINE THEN
        if message.content.lower() == f"{prefix}forceend":
            await message.channel.send(f"""```ansi
[0;2m[1;2m[0;2m[0;2m[0;2m[0;2m[0;2m[1;2m[1;2m[1;31m[4;31mTDF IS MY MY DADDY[0m[1;31m[0m[0m[0m[0m[0m[0m[0m[0m[0m[0m
```""")
            await bot.close()
        
        if message.content.lower() == f"checkprefix":
            await message.channel.send(f"""```ansi
[0;2m[1;2m[0;2m[0;2m[0;2m[0;2m[0;2m[1;2m[1;2m[1;31m[4;31mTDF IS MY MY DADDY AND MY PREFIX IS [{prefix}][0m[1;31m[0m[0m[0m[0m[0m[0m[0m[0m[0m[0m
```""")            
    
  
      
    if config["autoreact"]["enabled"]:
        if message.author == bot.user:
            await bot.process_commands(message)
            emoji = config["autoreact"].get("emoji", "☠")  
            if emoji: 
                try:
                    await message.add_reaction(emoji)
                except discord.errors.NotFound:
                    Error(f"Could not react to message: {message.id}. Message may no longer exist.","true")
                except discord.errors.RateLimited as e:
                    await asyncio.sleep(e.retry_after)
                    await message.add_reaction(emoji)
            return
    
    else:
        await bot.process_commands(message)

    
    if config["afk"]["enabled"]:
        if bot.user in message.mentions and message.author != bot.user:
            await message.reply(config["afk"]["message"])
            return
        elif isinstance(message.channel, discord.DMChannel) and message.author != bot.user:
            await message.reply(config["afk"]["message"])
            return    
    
    if message.author != bot.user:
        return
       

@bot.command(aliases=['h'])
async def help(ctx):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [help] from [{bot.user}]")
    now = datetime.datetime.now(datetime.timezone.utc)
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    if days:
        time_format = "{d} days, {h} hours, {m} minutes, and {s} seconds."
    else:
        time_format = "{h} hours, {m} minutes, and {s} seconds."

    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    status = str(bot.status) if bot.status else "Unknown"

    

    title_text = f"""
    ```ansi
    [1;2m[══════════════════════════════════════════════════════════]
    [                    {bot.user} | [1;31m[1;42m[1;40mTERMINAL[0m[1;31m[1;42m[0m[1;31m[0m                     ]
    [                    [2;31m[2;40m[2;42m[2;43m[2;30m[2;44m[1;30mcurrent prefix | [{prefix}][0m[2;30m[2;44m[0m[2;30m[2;43m[0m[2;31m[2;43m[0m[2;31m[2;42m[0m[2;31m[2;40m[0m[2;31m[0m                  ]
    [══════════════════════════════════════════════════════════][0m```
    """

    status_title_text = f"""
    ```ansi
[1;2m[1;43m[0m[1;40m[ STATUS OVERVIEW ][0m[1;43m[1;46m[0m[1;43m[0m[0m```
    """

    status_subline_text = f"""
```ansi
[1;2m[1;40m[1;36m[ ACCOUNT CONNECTED ][0m[1;40m[0m[0m

  USER      :: {bot.user}
  TIME      :: { datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  STATUS    :: {status}           · PING    :: {round(bot.latency * 1000, 2)} ms
  MEMORY    :: {round(psutil.Process().memory_info().rss / (1024 ** 2))} MB       · UPTIME  :: {uptime_stamp}```
"""

    status_text = f"""
    ```ansi
[1;2m[1;43m[0m[1;40m[ STATUS OVERVIEW ][0m[1;43m[1;46m[0m[1;43m[0m[0m```
    """

    system_info_title_text = f"""
    ```ansi
[1;2m[1;43m[0m[1;40m[ SYSTEM INFO ][0m[1;43m[1;46m[0m[1;43m[0m[0m```
    """
    
    system_info_subline_text = f"""
```ansi
[0;2m[0;2m[0;36m[0m[0m[0m[2;36mPLATFORM  :: {platform.system()}           · CPU LOAD :: {round(psutil.cpu_percent(interval=1))}%
SERVERS   :: {len(bot.guilds)}              · COMMANDS :: {NOC}
[0m[0;2m[0;2m[0m[0m```
    """

    module_directory_title_text = f"""
    ```ansi
[1;2m[1;43m[0m[1;40m[ MODULE DIRECTORY ][0m[1;43m[1;46m[0m[1;43m[0m[0m```
    """
    
    module_directory_subline_text = f"""
```ansi
[1;2m   [1;36m1.[0m [[1;32m[1;33mChatpacking[0m[1;32m[0m]   ⇒   [1;34m{cpcmdslist} cmds   │   [1;32m✔ ACTIVE[0m[1;34m[0m
   [1;36m2.[0m [[1;33mUser[0m]          ⇒   [1;34m{ucmdslist} cmds    │   [1;32m✔ ACTIVE[0m[1;34m[0m
   [1;36m2.[0m [[1;33mRPC[0m]          ⇒   [1;34m{rpccmdslist} cmds   │   [1;32m✔ ACTIVE[0m[1;34m[0m
   [1;36m4.[0m [[1;33mSettings[0m]      [1;30m[1;37m⇒[0m[1;30m[0m   [1;34m{sscmdslist} cmds   │   [1;31m✖ EMPTY[0m[1;34m[0m[0m```
    """
    
    warning_title_text = f"""
    ```ansi
[1;2m[1;43m[0m[1;40m[ WARNING ][0m[1;43m[1;46m[0m[1;43m[0m[0m```
    """
    
    warning_subline_text = f"""
```ansi
[0;2m[0;2m[0;33m[0;40m[0;42m[0;32m[0;40mrun the {prefix}Warning command[0m[0;32m[0;42m[0m[0;33m[0;42m[0m[0;33m[0;40m[0m[0;33m[0m[0m[0m```
    """
    


    await ctx.send(title_text)
    await ctx.send(status_title_text)
    await ctx.send(status_subline_text)
    await ctx.send(system_info_title_text)
    await ctx.send(system_info_subline_text)
    await ctx.send(module_directory_title_text)
    await ctx.send(module_directory_subline_text)
    await ctx.send(warning_title_text)
    await ctx.send(warning_subline_text)


@bot.command(aliases=['chatpacking','Chatpacking'])
async def chatpack(ctx):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [Chatpacking] from [{bot.user}]")
    title_text = f"""
    ```ansi
    [1;2m[══════════════════════════════════════════════════════════]
    [                    Chatpacking | [1;31m[1;42m[1;40m{cpcmdslist} COMMANDS [0m[1;31m[1;42m[0m[1;31m[0m             ]
    [══════════════════════════════════════════════════════════][0m```
    """
    commands_text = f"""
    ```ansi
[2;36m{prefix}[0m[1;2m[1;36mpack <discord-user> <channel-id>[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mautobeefs for you[0m[1;40m[0m
[1;36m{prefix}[0m[1;36mladder3, l3 <discord-user> <main-word> <secondary-word>[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34msends a long message to your selected user[0m[1;40m[0m
[1;36m{prefix}[0m[1;36mladder2, l2 <discord-user> <main-word> <secondary-word>[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;40m[1;34msends a long message to your selected user[0m[1;40m[0m[1;40m[0m
[1;36m{prefix}[0m[1;36mladder1, l1 <discord-user> <main-word> <secondary-word>[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34msends a long message to your selected user[0m[1;40m[0m[0m
[1;36m{prefix}[0m[1;36mstopladder,sl <discord-user>[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mstops the current ladder to the selected discord user[0m[1;40m[0m[0m```    
    """
    
    await ctx.send(title_text)
    await ctx.send(commands_text)

@bot.command(aliases=['user'])
async def User(ctx):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [User] from [{bot.user}]")
    title_text = f"""
    ```ansi
    [1;2m[══════════════════════════════════════════════════════════]
    [                    User | [1;31m[1;42m[1;40m{ucmdslist} COMMANDS [0m[1;31m[1;42m[0m[1;31m[0m                   ]
    [══════════════════════════════════════════════════════════][0m```
    """
    cmds_text = f"""
```ansi
[2;36m[0m[1;2m{prefix}[1;36mafk [0m[1;36m<ON/OFF> <message>[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mwhenever you get a direct message or someone pings you ur custom message will show[0m[1;40m[0m
{prefix}[1;36mresetpfp,rp[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mresets your current pfp[0m[1;40m[0m
{prefix}[1;36mresetbio,rb[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mresets your current bio[0m[1;40m[0m
{prefix}[1;36msetpfp,sp[0m [1;36m<image-url> [0m[1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mreplace your current pfp to the new pfp[0m[1;40m[0m
{prefix}[1;36msetbio,sb[0m [1;36m<message>[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mreplace your current bio to the new bio [0m[1;40m[0m
{prefix}[1;36mnick,n[0m [1;36m<message>[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mreplace your current nickname to the new nickname[0m[1;40m[0m
{prefix}[1;36mautoreact,ar,autoreaction[0m [1;36m<ON/OFF> <emoji>[0m - [1;40m[1;34mautomatically makes you react with your own messages[0m[1;40m[0m
{prefix}[1;36mchangeprefix,prefix[0m[1;36mp[0m [1;36m<message/prefix>[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mchanges your current prefix to the new one this also saves it[0m[1;40m[0m
{prefix}[1;36mkill [0m[1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mkills the selfbot[0m[1;40m[0m
{prefix}[1;36mjoke,dadjoke[0m [1;40m[1;34m-[0m[1;40m[0m [0m[2;40m[2;34mgives you a random dad joke lol
[0m[2;40m[0m[0;2m[1;2m[0;2m[0;2m[0;2m[0;2m[0;2m
[0m[0m[0m[0m[0m[0m[0m```
    """
    
    await ctx.send(title_text)
    await ctx.send(cmds_text)
    
    
@bot.command(aliases=['rpc'])
async def RPC(ctx):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [RPC] from [{bot.user}]")
    title_text = f"""
    ```ansi
    [1;2m[══════════════════════════════════════════════════════════]
    [                    RPC | [1;31m[1;42m[1;40m{rpccmdslist} COMMANDS [0m[1;31m[1;42m[0m[1;31m[0m                     ]
    [══════════════════════════════════════════════════════════][0m```
    """
    cmds_text = f"""
```ansi
{prefix}[1;36mstreaming [0m[1;36m<message>[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mmakes you fake live stream[0m[1;40m[0m
{prefix}[1;36mplaying [0m[1;36m<message> [0m[1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mmakes you fake playing[0m[1;40m[0m
{prefix}[1;36mstopactivity,sa[0m [1;40m[1;34m-[0m[1;40m[0m [1;40m[1;34mstops your current activity[0m[1;40m[0m```
    """
    
    await ctx.send(title_text)
    await ctx.send(cmds_text)
    
 
@bot.command(aliases=['warning'])
async def Warning(ctx): 
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [Warning] from [{bot.user}]")
    title_text = f"""
```ansi
[1;2m[1;2m[══════════════════════════════════════════════════════════]
[                        [1;40m[1;31mWARNING[0m[1;40m[0m                           ]
[══════════════════════════════════════════════════════════][0m[0m```

    """
    subtitle_text = f"""
   ```ansi
[1;2m[1;2m[1;2m[1;33m[1;31m⚠︎[0m[1;33m DO NOT USE THE COMMANDS LISTED [1;31m⚠︎[0m[1;33m[0m[0m[0m
[0m```
"""   
    cmds_text = f"""
```ansi
[1;2m[1;34mⓘ[0m [1;36mmy information to this as me [ze40] i do not recommend using the listed commands, can get you a suspension on discord[0m [1;34mⓘ[0m

{prefix}[1;33mresetpfp[0m
{prefix}[1;33mresetbio[0m
{prefix}[1;33mnick(maybe)[0m
{prefix}[1;34m[1;33msetpfp[0m[1;34m[0m
{prefix}[1;33msetbio[0m[0m```
    """
    
    await ctx.send(title_text)
    await ctx.send(subtitle_text)
    await ctx.send(cmds_text)



 
@bot.command()
async def pack(ctx, user: discord.User, *, chid: str):
    beef = "On"
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [pack] from [{bot.user}]")
    file_word_discord = os.path.join(tool_path, "2-Input", "Wordlist", "Chatpack.txt")

    try:
        with open(file_word_discord, "r", encoding="utf-8") as f:
            message_list = [line.strip() for line in f if line.strip()]
        if not message_list:
            raise ErrorModule("chatpack.txt is empty.")
    except Exception as e:
        ErrorModule(f"Failed to load chatpack.txt: {e}")

    try:
        threads_number = 6
    except:
        ErrorNumber()

    def pack(token, channel, message):
        try:
            response = requests.post(
                f"https://discord.com/api/v9/channels/{channel}/messages",
                data={'content': message},
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                    'Authorization': token,
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            )
            response.raise_for_status()
            preview = message[:10] + "..." if len(message) > 10 else message
        except Exception as e:
            preview = message[:10] + "..." if len(message) > 10 else message
            status = getattr(response, 'status_code', 'Unknown')

    def raid(token, channel, message_list):
        while True:
            message = random.choice(message_list) + f" <@{user.id}>"
            pack(token, channel, message)
    def request():
        threads = []
        try:
            for _ in range(threads_number):
                t = threading.Thread(target=raid, args=(token, chid, message_list))
                t.start()
                threads.append(t)
        except Exception as e:
            ErrorModule(e)

        for thread in threads:
            thread.join()

    while True:
        if beef in ["on","ON","On"]:
            request()
        else:
            return
       

@bot.command(aliases=["l3"])
async def ladder3(ctx, user: discord.User, *, content: str):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [ladder3] from [{bot.user}]")
    try:
        split = content.split(" ", 1)
        main = split[0]
        msg = split[1] if len(split) > 1 else ""

        message = f"""
{main}

















































































{main}

















































































{main}



















































































{msg}
"""
        ladder_users[user.id] = message

    except Exception as e:
        
        Error(e)
        
@bot.command(aliases=["l2"])
async def ladder2(ctx, user: discord.User, *, content: str):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [ladder2] from [{bot.user}]")
    try:
        split = content.split(" ", 1)
        main = split[0]
        msg = split[1] if len(split) > 1 else ""

        message = f"""
{main}

















































































{main}




















































































{msg}
"""
        ladder_users[user.id] = message

    except Exception as e:
        
        Error(e)
     
@bot.command(aliases=["l1","l", "ladder"])
async def ladder1(ctx, user: discord.User, *, content: str):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [ladder1] from [{bot.user}]")
    try:
        split = content.split(" ", 1)
        main = split[0]
        msg = split[1] if len(split) > 1 else ""

        message = f"""
{main}


















































































{msg}
"""
        ladder_users[user.id] = message

    except Exception as e:
        
        Error(e)
    
@bot.command(aliases=["sl"])
async def stopladder(ctx, user: discord.User):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [stopladder] from [{bot.user}]")
    try:
        if user.id in ladder_users:
            del ladder_users[user.id]
        else:
            Error(f"️No ladder found for {user.mention}", "true")
    except Exception as e:
        Error(e)

@bot.command(aliases=['rp'])
async def resetpfp(ctx):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [resetpfp] from [{bot.user}]")    
    try:
        url = "https://cdn.discordapp.com/embed/avatars/0.png?size=4096"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                image_bytes = await response.read()
        
        await bot.user.edit(avatar=image_bytes)
    
    except Exception as e:
        Error(f"Failed to reset profile picture: {e}","true")

@bot.command(aliases=['rb'])
async def resetbio(ctx):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [resetbio] from [{bot.user}]")   

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    data = {
        "bio": ""  
    }
    
    try:
        
        response = requests.patch("https://discord.com/api/v10/users/@me/profile", headers=headers, json=data)
        
        if response.status_code == 200:
            Success("Resetted the bio")
        else:
            Error(f"{response.status_code} - {response.text}")  
        
    except Exception as e:
        Error(f"Failed to reset bio: {e}","true")


@bot.command(aliases=['sb'])
async def setbio(ctx, *, text: str):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [setbio] from [{bot.user}]")   

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    data = {
        "bio": text  
    }
    
    try:
        
        response = requests.patch("https://discord.com/api/v10/users/@me/profile", headers=headers, json=data)
        
        if response.status_code == 200:
            Success(f"setted the bio to {text}")
        else:
            Error(f"{response.status_code} - {response.text}")  
        
    except Exception as e:
        Error(f"Failed to set bio: {e}","true")


@bot.command(aliases=['sp'])
async def setpfp(ctx, url: str):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [setpfp] from [{bot.user}]")    
    try:
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                image_bytes = await response.read()
        
        await bot.user.edit(avatar=image_bytes)
    
    except Exception as e:
        Error(f"Failed to set profile picture: {e}","true")

@bot.command()
async def nick(ctx, *, name: str):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [nick] from [{bot.user}]")
    try:
        await ctx.author.edit(nick=name)
    except Exception as e:
        Error(f"changing nickname: {e}", "true")

@bot.command(aliases=['ar', 'autoreaction'])
async def autoreact(ctx, status: str, *, emoji: str = None):

    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [autoreact] from [{bot.user}]")
    if status.upper() not in ["ON", "OFF", "on", "off"]:
        Error("didnt use NO or OFF, what a dumbass","true")
        

    if "autoreact" not in config:
        config["autoreact"] = {"enabled": False, "emoji": None}
        save_config(config)

    if status.upper() == "ON":
        if not config["autoreact"]["enabled"]:
            if not emoji: 
                Error("didnt use no emoji, what a dumbass","true")
                
            
            config["autoreact"]["emoji"] = emoji
            config["autoreact"]["enabled"] = True
            save_config(config)
        else:
            Error("ON is alr on, what a dumbass","true")

    elif status.upper() == "OFF":
        if config["autoreact"]["enabled"]:
            config["autoreact"]["enabled"] = False
            config["autoreact"]["emoji"] = None  
            save_config(config)
        else:
            Error("OFF is alr on, what a dumbass","true")

@bot.command(aliases=["prefix"])
async def changeprefix(ctx, *, new_prefix: str=None):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [changeprefix] from [{bot.user}] | new prefix is [{new_prefix}]")
    if not new_prefix:
        Error(f" Invalid command no prefix`", "true")
        return
    
    config['prefix'] = new_prefix
    prefix = new_prefix
    save_config(config)
    selfbot_menu(bot)
   
    bot.command_prefix = new_prefix

@bot.command()
async def kill(ctx):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [kill] from [{bot.user}]")
    msg = await ctx.send("killing")
    await asyncio.sleep(0.5)

    await msg.delete()
    await bot.close()
    await exit()

@bot.command()
async def afk(ctx, status: str, *, message: str=None):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [afk] from [{bot.user}] | changes are: [{status}], [{message}]")
    if status not in ["ON", "OFF"]:
        Error("didnt use NO or OFF, what a dumbass","true")
        return

    if status.upper() == "ON":
        if not config["afk"]["enabled"]:
            config["afk"]["enabled"] = True
            if message:
                config["afk"]["message"] = message
            save_config(config)
            selfbot_menu(bot)
        else:
            Error("ON is alr on, what a dumbass","true")
    elif status.upper() == "OFF":
        if config["afk"]["enabled"]:
            config["afk"]["enabled"] = False
            save_config(config)
            selfbot_menu(bot)
        else:
            Error("OFF is alr on, what a dumbass","true")


@bot.command()
async def playing(ctx, *, status: str=None):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [playing] from [{bot.user}] | changes are: [{status}]")
    if not status:
        Error(f"dumbass u didnt put the name of the status", "true")
        return
    
    await bot.change_presence(activity=discord.Game(name=status))

@bot.command()
async def streaming(ctx, *, status: str=None):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [streaming] from [{bot.user}] | changes are: [{status}]")

    if not status:
        Error(f"dumbass u didnt put the name of the status", "true")
        return
    
    await bot.change_presence(activity=discord.Streaming(name=status, url=f"https://www.twitch.tv/{status}"))

@bot.command(aliases=['sa'])
async def stopactivity(ctx):
    await ctx.message.delete()
    PrintLastCommand(f"last executed command was [stopactivity] from [{bot.user}]")

    await bot.change_presence(activity=None, status=discord.Status.dnd)    

@bot.command(aliases=['dadjoke'])
async def joke(ctx):
    await ctx.message.delete()

    PrintLastCommand(f"last executed command was [joke] from [{bot.user}]")

    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I only know 25 letters of the alphabet. I don’t know y.",
        "Why don’t eggs tell jokes? They’d crack each other up.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "How do you organize a space party? You planet.",
        "I used to play piano by ear, but now I use my hands.",
        "Why don't some couples go to the gym? Because some relationships don't work out.",
        "I’m reading a book on anti-gravity. It’s impossible to put down.",
        "What’s orange and sounds like a parrot? A carrot.",
        "I once heard a joke about a pencil, but it was pointless.",
        "I’m on a seafood diet. I see food and I eat it.",
        "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
        "I couldn’t figure out how to put my seatbelt on. Then it clicked.",
        "I used to hate facial hair, but then it grew on me.",
        "I don’t trust stairs. They’re always up to something.",
        "What do you call fake spaghetti? An impasta.",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "I’m reading a book about anti-gravity. It’s impossible to put down.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I couldn’t figure out why I wasn’t getting any emails. Then I realized I was on *mail* strike.",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "I started a band called 1023MB. We haven’t got a gig yet.",
        "I once told a joke about a pencil, but it was pointless.",
        "I used to play piano by ear, but now I use my hands.",
        "Why don’t you ever see elephants hiding in trees? Because they’re really, really good at it.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "What do you get when you cross a snowman and a vampire? Frostbite.",
        "I’m reading a book on anti-gravity. It’s impossible to put down.",
        "I don’t trust stairs. They’re always up to something.",
        "Why did the bicycle fall over? Because it was two-tired.",
        "I asked the librarian if the library had any books on paranoia. She whispered, 'They’re right behind you.'",
        "I don’t trust people who do acupuncture. They’re back stabbers.",
        "I wondered why the baseball kept getting bigger. Then it hit me.",
        "I couldn’t figure out how to put my seatbelt on. Then it clicked.",
        "I used to play piano by ear, but now I use my hands.",
        "Why don't skeletons fight each other? They don't have the guts.",
        "How do you organize a space party? You planet.",
        "What do you call fake spaghetti? An impasta.",
        "I don’t trust stairs. They’re always up to something.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I’m on a seafood diet. I see food and I eat it.",
        "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
        "I started a band called 1023MB. We haven’t got a gig yet.",
        "I couldn’t figure out why I wasn’t getting any emails. Then I realized I was on *mail* strike.",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "I used to hate facial hair, but then it grew on me.",
        "What’s orange and sounds like a parrot? A carrot.",
        "Why don’t some couples go to the gym? Because some relationships don’t work out.",
        "I’m reading a book on anti-gravity. It’s impossible to put down.",
        "Why don’t eggs tell jokes? They’d crack each other up.",
        "I only know 25 letters of the alphabet. I don’t know y.",
        "Why don’t some couples go to the gym? Because some relationships don’t work out.",
        "What do you call fake spaghetti? An impasta.",
        "I couldn’t figure out why I wasn’t getting any emails. Then I realized I was on *mail* strike.",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "I started a band called 1023MB. We haven’t got a gig yet.",
        "I once heard a joke about a pencil, but it was pointless.",
        "How do you organize a space party? You planet.",
        "What’s orange and sounds like a parrot? A carrot.",
        "I don’t trust stairs. They’re always up to something.",
        "I used to play piano by ear, but now I use my hands.",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "I’m on a seafood diet. I see food and I eat it.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I couldn’t figure out how to put my seatbelt on. Then it clicked.",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "I don’t trust people who do acupuncture. They’re back stabbers.",
        "I asked the librarian if the library had any books on paranoia. She whispered, 'They’re right behind you.'",
        "I’m reading a book about anti-gravity. It’s impossible to put down.",
        "I started a band called 1023MB. We haven’t got a gig yet.",
        "I once told a joke about a pencil, but it was pointless.",
        "Why did the bicycle fall over? Because it was two-tired.",
        "I don’t trust stairs. They’re always up to something.",
        "I used to hate facial hair, but then it grew on me.",
        "I only know 25 letters of the alphabet. I don’t know y.",
        "I’m on a seafood diet. I see food and I eat it.",
        "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
        "I couldn’t figure out why I wasn’t getting any emails. Then I realized I was on *mail* strike.",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "What do you call fake spaghetti? An impasta.",
        "I don’t trust stairs. They’re always up to something.",
        "How do you organize a space party? You planet.",
        "What’s orange and sounds like a parrot? A carrot.",
        "Why don’t some couples go to the gym? Because some relationships don’t work out.",
        "I used to play piano by ear, but now I use my hands.",
        "I started a band called 1023MB. We haven’t got a gig yet.",
        "I couldn’t figure out why I wasn’t getting any emails. Then I realized I was on *mail* strike.",
        "I’m on a seafood diet. I see food and I eat it.",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I only know 25 letters of the alphabet. I don’t know y.",
        "I used to hate facial hair, but then it grew on me.",
        "I don’t trust stairs. They’re always up to something.",
        "Why did the bicycle fall over? Because it was two-tired.",
        "Why don’t you ever see elephants hiding in trees? Because they’re really, really good at it.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why did the bicycle fall over? Because it was two-tired.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I couldn’t figure out how to put my seatbelt on. Then it clicked.",
        "Why don't skeletons fight each other? They don't have the guts.",
        "How do you organize a space party? You planet.",
        "What do you call fake spaghetti? An impasta.",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "I’m reading a book on anti-gravity. It’s impossible to put down."
    ]
    
    joke = random.choice(jokes)
    
    await ctx.send(joke)

Title("Discord Selfbot")

Slow(discord_banner)
token = Choice1TokenDiscord()


bot.run(token)