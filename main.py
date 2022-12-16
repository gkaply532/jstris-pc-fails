#!/usr/bin/env python3

import discord
import os
import dotenv
import sys

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

def main():
    dotenv.load_dotenv()

    token = os.getenv("BOT_TOKEN")
    if token is None:
        sys.exit("No discord bot token in .env file!")
    else:
        client.run(token)

if __name__ == "__main__":
    main()
