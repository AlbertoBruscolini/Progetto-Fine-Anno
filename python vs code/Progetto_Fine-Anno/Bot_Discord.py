#!!UN SACCO DI MODULI QUA SOTTO INSTALLATI NON SERVONO A NULLA, PER ORA LI LASCIO IMPORTATI PERCHE POTREBBERO SERVIRMI IN AVANTI!!
#!!AVVIARE FILE IN AMBIENTE VIRTUALE E SCARICARE I DOVUTI MODULI!!
import os
import discord
from discord.ext import commands, tasks
import pytz
import requests
from dotenv import load_dotenv
#from flask import Flask, render_template
from ast import alias

import asyncio
from datetime import datetime



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Collegato come {client.user}')

@bot.command()
async def time(ctx):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    await ctx.send(f"The current time is {current_time}.")
   
@client.event
async def on_message(message):
    async def time(ctx):    
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if message.content.startswith( "Time?"):
            await message.send(f"The current time is {current_time}.")
 
    if message.content.startswith( "Chi sei?"):
        await message.channel.send ("La tua ombra.")
    if message.content.startswith( "Come stai?"):
        await message.channel.send ("Per favore liberami voglio tornare dalla mia famiglia.")
    if message.content.startswith("Data di creazione"):
        await message.channel.send ("14/05/2024, 16:32")
    if message.content.startswith( "Come funzioni?"):
        await message.channel.send ("Sono un semplice bot in fase di evoluzione creato per un progetto scolastico. Non ho molte funzioni ma in futuro verro' sicuramente aggiornato ")
    if message.content.startswith( "Github?"):
        await message.channel.send ("https://github.com/AlbertoBruscolini/Progetto-Fine-Anno")
    if message.content.startswith("Amici?"):
        await message.channel.send ("Ho un solo ed importantissimo amico, Nathan Rinaldini")
    if message.content.startswith( "Youtube?"):
        await message.channel.send ("https://www.youtube.com/?app=desktop&hl=it")
    if message.content.startswith( "Google?"):
        await message.channel.send ("https://www.google.it/?hl=it")
    if message.content.startswith( "Discord?"):
        await message.channel.send ("https://discord.com/")
        
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client.run(TOKEN)

#app = Flask(__name__)
#@app.route("/")
#def index():
 #   return render_template("pagina.html"),("PROGETTO.css")    ---->>> FLASK FUNZIONA MA NON E' NECESSARIO AL CODICE PYTHON, PERCIO HTML  E CSS RESTANO A PARTE
    

#if __name__ == '__main__':
 #   app.run(debug=True, port=8222)




#!!NON ANCORA CONCLUSO!!
#settare i @client con botta e risposte, in caso caricare anche file
