import discord
import json

config = json.load(open('config.json', 'r'))

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}#{client.user.discriminator} ({client.user.id}) in {len(client.guilds)} guild(s)')

client.run(config['discordToken'])
