from datetime import datetime      #MODULI DA AGGIUNGERE AGLI ALTRI, QUESTO CODICE CREA PROBLEMATICHE
import pytz

client = discord.Client()

@client.event
async def on_ready():
    print('The bot is ready!')

@client.event
async def on_message(message):
    if message.content.startswith('!time'):
        continents = {
            'africa': 'Africa/Cairo',
            'antarctica': 'Antarctica/Casey',
            'asia': 'Asia/Kolkata',
            'australia': 'Australia/Sydney',
            'europe': 'Europe/Paris',
            'north_america': 'America/New_York',
            'south_america': 'America/Sao_Paulo'
        }
        await message.channel.send('In quale continente vuoi l\'ora?')
        response = await client.wait_for('message', check=lambda message: message.author == message.author and message.channel == message.channel)
        if response.content in continents:
            time = datetime.now(pytz.timezone(continents[response.content]))
            await message.channel.send(f'L\'ora in {response.content} è: {time.strftime("%H:%M:%S")}')
        else:
            await message.channel.send('Continente non valido')
