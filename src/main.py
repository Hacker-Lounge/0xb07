#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# External Imports
import discord
from dotenv import load_dotenv
import premade_messages
# Our Plugins
from bot_commands import ctftime, crypto

client = discord.Client()

exported_functions = []


@client.event
async def onMessage(message):
    if message.author == client.user:
        return

    results = []

    packages = [func.getPackage() for func in exported_functions]
    commands = [func.getCommand() for func in exported_functions]

    if message.content.startswith('!'):
        message_package = message.content[1:].split(' ')[0]
        message_command = message.content[1:].split(' ')[1]

        if message_package not in packages or message_command not in commands:
            results.append(premade_messages.error_message)

        else:
            for exported_function in exported_functions:
                if (exported_function.getPackage(),exported_function.getCommand()) == (message_package, message_command):
                    try:
                        results = exported_function.call(message.content)
                    except Exception:
                        results.append(exported_function.getHelpMesssage)
                    

    for result in results:
        if len(result) <= 2000:
            await message.channel.send("```"+result+"```")
        else:
            for partition in [result[i:i+2000] for i in range(0, len(result), 2000)]:
                await message.channel.send("```"+partition+"```")
                

if __name__ == "__main__":
    load_dotenv("..\\.env" if os.name == "nt" else "../.env")
    
    TOKEN = os.getenv('TOKEN')
    client.run(TOKEN)