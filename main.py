#!/usr/bin/env python3

import os
import sys

import dotenv
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def pcfails(ctx, jstris_player: str):
    await ctx.send(jstris_player)


def main():
    dotenv.load_dotenv()

    token = os.getenv("BOT_TOKEN")
    if token is None:
        sys.exit("No discord bot token in .env file!")
    else:
        bot.run(token)

if __name__ == "__main__":
    main()
