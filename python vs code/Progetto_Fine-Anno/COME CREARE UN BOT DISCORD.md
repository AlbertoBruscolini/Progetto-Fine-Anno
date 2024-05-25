# CREAZIONE BOT DISCORD UTILIZZANDO PYTHON
Creare un bot Discord con Python è abbastanza “semplice”, grazie alla libreria discord.py, che fornisce un'API per interagire con l'API di Discord. Ecco una guida rapida su come farlo:
## Step 1: Installazione
	Assicurati di avere Python installato sul tuo sistema. Puoi installare discord.py eseguendo il seguente comando in un terminale o prompt dei comandi:
pip install discord.py
	
## Step 2: Creazione bot Discord
	Vai su Discord Developer Portal e crea una nuova applicazione. Puoi settare il bot come ti pare, l’importante e generare l’URL da copia incollare in una nuova finestra, consentendoti di collegare il bot al tuo account discord e aggiungerlo a qualunque server.  Dopodiché, sotto l'opzione "Bot" nel pannello di sinistra, crea un nuovo bot e ottieni il suo token.

questa sarà la tua schermata (in questo caso con il mio bot)
Codifica:
un esempio di codifica è quella illustrata nel file python contenente il codice per il bot.
 


## Step 3: Esecuzione codice
Salva lo script Python in un file, ad esempio bot.py, e eseguilo da terminale o prompt dei comandi:
Copy code
python (nome del file)
es) |python bot_discord.py

## Step 4: Aggiungi il Bot al tuo server Discord
	Per far funzionare il tuo bot su un server Discord, devi aggiungere il bot al server. Vai sulla pagina di autorizzazione del tuo bot nel pannello di sviluppo Discord e ottieni l'URL di autorizzazione. Accedi con un account che ha il permesso di aggiungere bot ai server e segui le istruzioni per aggiungere il bot al server.
	Copia l'ID del tuo bot Discord dall'interfaccia del Developer Portal.
	Visita l'URL seguente nel tuo browser web, sostituendo <BOT_CLIENT_ID> con l'ID del tuo bot: