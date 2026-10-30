# Auto3D

Add-on open source per Blender che automatizza la creazione di modelli 3D per videogiochi e animazione, pensato per i principianti.

> **Stato del progetto:** prototipo (versione 0.4). Le funzioni sono poche e il codice cambia spesso.

## Cosa fa

- Propone un **menu con miniature**: si sceglie un oggetto cliccando la sua immagine.
- Genera con pochi clic sette oggetti pronti: **Albero**, **Pino alto**, **Alberello**, **Roccia**, **Masso**, **Casetta** e **Casa a due piani**.
- Permette di regolare dimensione, dettaglio e un **seme** che crea varianti sempre diverse dello stesso oggetto.
- Pulisce automaticamente il modello: lo posa a terra con l'origine alla base, come richiedono i motori di gioco.
- Mostra il numero di triangoli del modello.
- Esporta in **GLB (glTF)**, pronto per Unity, Unreal e Godot, anche con **LOD automatici** (tre livelli di dettaglio in tre file).

Funziona senza servizi a pagamento, senza account e senza connessione a internet.

## Requisiti

- Blender 5.2 LTS (gratuito, da blender.org)

## Installazione

1. Vai nella sezione **Releases** di questa pagina (a destra) e scarica il file `auto3d.zip`. **Non scompattarlo.**
2. In Blender vai in **Modifica → Preferenze → Add-on**.
3. Clicca la piccola freccia in alto a destra e scegli **Installa da disco** (*Install from Disk*), poi seleziona `auto3d.zip`.
4. Attiva **Auto3D** nell'elenco (accetta il permesso di scrittura dei file, serve per l'esportazione).

Dopo l'installazione l'add-on resta attivo anche quando riapri Blender.

Se hai una versione precedente di Auto3D (il vecchio file `auto3d_prototipo.py`), rimuovila prima dalle Preferenze e riavvia Blender, altrimenti le due versioni vanno in conflitto.

## Come si usa

1. Nella Vista 3D premi **N** e apri la scheda **Auto3D**.
2. Clicca la miniatura dell'oggetto che vuoi creare e scegline uno dalla griglia.
3. Se vuoi, ritocca dimensione, dettaglio e seme con i cursori.
4. Premi **Genera**.
5. Premi **Esporta GLB**. Il file viene salvato nel percorso indicato nel campo **File** (di default nella tua cartella utente). Se l'opzione LOD è attiva e il modello è abbastanza complesso, ottieni tre file: `_LOD0`, `_LOD1` e `_LOD2`.

Le miniature del menu sono per ora illustrazioni schematiche, non anteprime reali degli oggetti.

## Prossimi passi

- Altri preset (recinzioni, armi, edifici più vari)
- Miniature generate automaticamente da Blender
- Personaggi con scheletro automatico (Rigify) e animazioni libere da diritti
- Interfaccia ancora più semplice per chi non ha mai usato il 3D

## Contribuire

Idee, segnalazioni di problemi e proposte sono benvenute: apri una *issue* su GitHub.

## Licenza

Rilasciato con licenza **GPL-3.0**. Vedi il file `LICENSE`.
