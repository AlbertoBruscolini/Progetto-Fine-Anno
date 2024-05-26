#NUOVI MODULI SOLO PER QUESTO BOT (DA AGGIUNGERE AGLI ALTRI), ---> #discord_player E' STATO RIMOSSO, PER QUESTO NON FUNZIONA PIU'.
import youtube_dl
from discord_player import Player, FFmpegAudioSource

# Funzione per cercare una canzone su YouTube
async def search_song(search):
    with youtube_dl.YoutubeDL({'format': 'bestaudio/best', 'noplaylist': True}) as ydl:
        info = ydl.extract_info(f"ytsearch:{search}", download=False)['entries'][0]
    return {'source': info['formats'][0]['url'], 'title': info['title']}

# Comando !play per cercare e riprodurre musica/video
@bot.command()
async def play(ctx, *, search):
    channel = ctx.author.voice.channel
    if channel:
        await player.connect(ctx)
        song = await search_song(search)
        source = FFmpegAudioSource(song['source'])
        await player.queue.put(source, channel=channel)
        await ctx.send(f"Aggiunto alla coda: {song['title']}")
    else:
        await ctx.send("Devi essere in un canale vocale per riprodurre musica!")

# Comando !skip per saltare alla canzone successiva
@bot.command()
async def skip(ctx):
    await player.skip()

# Comando !pause per mettere in pausa la riproduzione
@bot.command()
async def pause(ctx):
    await player.pause()

# Comando !resume per riprendere la riproduzione
@bot.command()
async def resume(ctx):
    await player.resume()

# Comando !queue per mostrare la coda delle canzoni
@bot.command()
async def queue(ctx):
    if player.queue.empty():
        await ctx.send("La coda è vuota.")
    else:
        queue_str = "\n".join([f"{i+1}. {song.title}" for i, song in enumerate(player.queue)])
        await ctx.send(f"Coda attuale:\n{queue_str}")

# Evento per quando il bot è pronto
@bot.event
async def on_ready():
    print(f'Connesso come {bot.user.name}!')

# Evento per quando una canzone finisce
@player.on_end
async def on_song_end(ctx, song):
    await asyncio.sleep(1)  # Aspetta un secondo prima di riprodurre la prossima
    if not player.queue.empty():
        await player.play()

#CONCEPT, SPERIMENTAZIONE, NON DEL TUTTO FUNZIONANTE.
