# Librerie Utilizzate

## datetime: 
Questa libreria standard di Python offre strumenti per lavorare con date e ore.
## pytz:
Questa libreria consente di gestire i fusi orari, essenziali per calcolare l'ora in diverse parti del mondo.
## discord: 
Libreria discord.py usata per interagire con l'API di Discord e creare bot.
# Struttura del Codice
Analizziamo il codice
### Importazioni: 
Con il seguente codice si importano le librerie necessarie per gestire date, fusi orari e interazioni Discord.

### Client Discord:
Crea un'istanza del client Discord 
    (client = discord.Client())

### Evento on_ready:

Questo evento si attiva quando il bot è connesso a Discord e pronto a funzionare.
Stampa un semplice messaggio ""The bot is ready!"" nella console per confermare l'avvio.
### Evento on_message:

Evento principale che gestisce i messaggi inviati dagli utenti nel server Discord.
### Controllo del comando: 
Verifica se il messaggio inizia con ""!time"". Se è così, procede con la logica per fornire l'ora.
### Dizionario dei continenti: 
Definisce un dizionario (continents) che associa i nomi dei continenti (come chiavi) ai rispettivi fusi orari (come valori).
### Richiesta del continente: 
Invia un messaggio all'utente chiedendo in quale continente desidera conoscere l'ora.
### Attesa della risposta:
Attende un nuovo messaggio dell'utente nello stesso canale.
### Verifica della risposta: 
Controlla se la risposta dell'utente corrisponde a uno dei continenti nel dizionario.
### Se valida:
-Ottiene l'ora corrente nel fuso orario del continente specificato usando pytz.timezone.
-Formatta l'ora nel formato HH:MM:SS (ore:minuti:secondi).
-Invia un messaggio con l'ora al canale.
#### Se non valida: 
-Invia un messaggio di errore "Continente non valido".

# Funzionamento Bot

1. Il bot si connette a Discord e aspetta i messaggi.

2. Quando un utente invia il messaggio "!time", il bot risponde chiedendo il continente.

3. L'utente digita il nome del continente (ad esempio, "europe").

4. Il bot cerca il fuso orario associato al continente nel dizionario.

5. Utilizza datetime.now() e pytz.timezone() per ottenere l'ora corrente nel fuso orario corretto.

6. Formatta l'ora e la invia all'utente nel canale Discord.
