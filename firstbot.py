import os
import os.path

import discord
from dotenv import load_dotenv

from utils import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_message(msg):
    if await first_msg_exists():
        return

    # create file indicating first msg
    with open(FIRST_LOCK, "x") as file:
        pass

    print(f"{msg.author.name} got the first message of the day \"{msg.content}\"!")

client.run(TOKEN)
