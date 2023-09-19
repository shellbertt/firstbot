import logging
import os
import os.path
from datetime import timedelta

import discord
from dotenv import load_dotenv

from utils import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info(f"{client.user} has connected to Discord!")

@client.event
async def on_message(msg):
    if msg.author.id == client.user.id:
        return

    await remove_old_claim()

    if claim_exists():
        return

    # create file indicating first msg
    with open(FIRST_LOCK, "x") as file:
        file.write(f"{msg.author.name}")

    reply = f"{msg.author.name} got the first message of the day \" {msg.content} \"!"
    logging.info(reply)
    await msg.channel.send(reply)

    await msg.delete()

    try:
        await msg.author.timeout(timedelta(hours=11, minutes=55), reason="First message")
    except discord.errors.Forbidden as e:
        logging.error(f"No permission to timeout {msg.author.name}")

@client.event
async def on_member_update(before, after):
    if before.timed_out_until is not None and after.timed_out_until is None:
        logging.info(f"Timeout removed from {after}!")
        if get_current_claimee().id == after.id:
            pass
            # remove points

client.run(TOKEN)
