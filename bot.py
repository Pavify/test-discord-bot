import discord
import json
import dotenv
import os

config = json.load(open('config.json', 'r'))
dotenv.load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}#{client.user.discriminator} ({client.user.id}) in {len(client.guilds)} guild(s)')

client.run(os.environ['DISCORD_TOKEN'])