from dotenv import load_dotenv
import discord
import asyncio
import os

# Load environment variables from .env file
load_dotenv()

token = os.environ.get("DISCORD_TOKEN")
channel_id = os.environ.get("DISCORD_CHANNEL_ID")
if not token:
    raise ValueError("DISCORD_TOKEN is not set in the environment or .env file.")

TOKEN = token
CHANNEL_ID = channel_id
if not channel_id:
    raise ValueError("DISCORD_CHANNEL_ID is not set in the environment or .env file.")

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    print(f'Listening to channel: {channel.name} ({channel.id})')

@client.event
async def on_message(message):
    # Avoid responding to its own messages
    if message.author == client.user:
        return

    # Only log messages from the specified channel
    if message.channel.id == CHANNEL_ID:
        print(f"[{message.author}] {message.content}")
        with open("log_file.txt", "a", encoding="utf-8") as f:
            f.write(message.content + "\n")

client.run(TOKEN)