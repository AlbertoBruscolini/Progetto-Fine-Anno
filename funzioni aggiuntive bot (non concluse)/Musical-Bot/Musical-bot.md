# Librerie Utilizzate
ELENCO DI MODULI UTILIZZATI PER QUESTO SPECIFICO BOT
## youtube_dl:
Una libreria potente per scaricare video e audio da YouTube e altre piattaforme.
## discord_player: 
Libreria personalizzata (o rimossa) per gestire la riproduzione audio su Discord. Questa libreria a quanto pare non è più disponibile, il che spiega perché il codice non puo' funzionare.
## FFmpegAudioSource:
Una classe che  utilizza FFmpeg (un potente strumento per la manipolazione di audio e video) per creare sorgenti audio da riprodurre.
# Struttura del Codice
SPIEGAZIONE DEI COMANDI/FUNZIONI
## Funzione search_song(search):

Questa funzione prende una stringa di ricerca come input.
Utilizza youtube_dl per cercare il primo risultato corrispondente su YouTube.
Estrae l'URL della migliore sorgente audio disponibile e il titolo del video.
Restituisce un dizionario contenente l'URL della sorgente audio e il titolo della canzone.
## Comandi del Bot:

    !play <ricerca>:
-Controlla se l'utente è in un canale vocale.
-Connette il bot al canale vocale dell'utente.
-Cerca la canzone utilizzando la funzione search_song.
-Crea una sorgente audio FFmpeg dall'URL ottenuto.
-Accoda la canzone alla coda di riproduzione del bot.
-Invia un messaggio di conferma all'utente.
!skip: Salta alla canzone successiva nella coda.
!pause: Mette in pausa la riproduzione.
!resume: Riprende la riproduzione.
!queue: Mostra la coda delle canzoni.
## Eventi del Bot:

    on_ready() 
Viene eseguito quando il bot è pronto e connesso a Discord. Stampa un messaggio di conferma.
    on_song_end()
Viene eseguito quando una canzone finisce. Attende un secondo e poi riproduce la prossima canzone nella coda se disponibile.


