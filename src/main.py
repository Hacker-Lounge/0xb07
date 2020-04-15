#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import discord
import ctftime, crypto
from dotenv import load_dotenv

client = discord.Client()

commands = { "ctftime" : { "now" : ctftime.now,
                           "next_week" : ctftime.next_week
                         },
             "crypto" : { "rot13" : crypto.rot13,
                          "a2h" : crypto.a2h,
                          "h2a" : crypto.h2a
                        }
           }

@client.event
async def on_ready():
    print("[*] Started bot")
    print("[*] Guilds:", ' '.join([guild.name for guild in client.guilds]))


@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    results = []
    if message.content.startswith("!CTF."):
        parts = message.content.split('.')
        
        try:
            results =commands[parts[1]][parts[2][:parts[2].find(':')] if ':' in parts[2] else parts[2]](message.content)
        except KeyError:
            results.append("Unknown command")
            
    for result in results:
        await message.channel.send(result)
if __name__ == "__main__":
    load_dotenv("..\\.env" if os.name == "nt" else "../.env")

    client.run(os.getenv("TOKEN"))
