#!/usr/bin/env python3

import os
import sys
import io
import pathlib

import dotenv
import discord
from discord.ext import commands

from script import get_pc_info_for_user, show_stats
import matplotlib.pyplot as plt

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def pcfails(ctx, jstris_player: str):
    # https://stackoverflow.com/questions/65526991
    data_stream = io.BytesIO()

    # FIXME(gkm): This uses "requests" module which is synchronous,
    # we should use async functions instead.
    # FIXME(gkm): get_pc_info_for_user might have a security hole (SSRF)
    pc_nums, pc_pieces = get_pc_info_for_user(jstris_player)
    show_stats(pc_pieces, uname=jstris_player)

    filename = pathlib.PurePath("pcfails.webp")

    plt.savefig(data_stream, format=filename.suffix[1:])
    plt.close()

    data_stream.seek(0)
    chart = discord.File(data_stream, filename=str(filename))

    embed = discord.Embed()
    embed.set_image(
       url=f"attachment://{filename}"
    )

    await ctx.send(embed=embed, file=chart)


def main():
    dotenv.load_dotenv()

    token = os.getenv("BOT_TOKEN")
    if token is None:
        sys.exit("No discord bot token in .env file!")
    else:
        bot.run(token)

if __name__ == "__main__":
    main()
