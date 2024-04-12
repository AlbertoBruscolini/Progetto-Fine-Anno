import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Collegato come {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith( 'Come stai?'):
        await message.channel.send ('Bene, graziel')
client.run(TOKEN)

#!!NON ANCORA CONCLUSO!!
#settare i @client con botta e risposte, in caso caricare anche file
