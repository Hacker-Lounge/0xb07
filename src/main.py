#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Basic Imports
import os

# External Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Our Plugins
from bot_commands import ctftime, crypto


def invalid_command_msg():
    return "Invalid Command!\ncommands: "+" ".join([x for x in bot_commands.keys()])

discord_bot = commands.Bot(command_prefix='!')

bot_commands = { 
    # "ctftime" : ctftime,
    # "crypto"  : crypto,
    "a2h"   : crypto.ascii_to_hex,
    "h2a"   : crypto.hex_to_ascii,

    "rot13"   : crypto.rot13,
    "brute_rot": crypto.brute_rot,
}

@discord_bot.event
async def on_ready():
    print("[*] Started bot")
    print("[*] Guilds:", ' '.join([guild.name for guild in discord_bot.guilds]))

@discord_bot.command()
async def echo(ctx, arg):
    await ctx.send(arg)

@discord_bot.command()
async def ctf(ctx, *args):
    if args[0] in bot_commands.keys():
        try:
            print(*args[1:])
            xyz = bot_commands[args[0]](*args[1:])
            # TODO: check if xyz exceeds limit
            if type(xyz) == str:
                await ctx.send(xyz)
            else:
                for result in xyz:
                    await ctx.send(result)
        except Exception as e:
            await ctx.send(e)
    else:
        await ctx.send(invalid_command_msg())

# @discord_bot.event
# async def on_message(message):
#     if message.author == discord_bot.user: return
#     results = []
#     if message.content.startswith("!CTF."):
#         parts = message.content.split('.')
        
#         try:
#             results =commands[parts[1]][parts[2][:parts[2].find(':')] if ':' in parts[2] else parts[2]](message.content)
#         except KeyError:
#             results.append("Unknown command")
            
#     for result in results:
#         await message.channel.send(result)

if __name__ == "__main__":
    load_dotenv("..\\.env" if os.name == "nt" else "../.env")
    TOKEN = os.getenv('TOKEN')
    discord_bot.run(TOKEN)