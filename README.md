# Auto3D

Add-on open source per Blender che automatizza la creazione di modelli 3D per videogiochi e animazione, pensato per i principianti.

> **Stato del progetto:** prototipo (versione 0.3). Le funzioni sono poche e il codice cambia spesso.

## Cosa fa

- Genera oggetti 3D parametrici con pochi clic: **albero**, **roccia** e **casetta**.
- Permette di regolare dimensione, dettaglio e un **seme** che crea varianti sempre diverse dello stesso oggetto.
- Pulisce automaticamente il modello: lo posa a terra con l'origine alla base, come richiedono i motori di gioco.
- Mostra il numero di triangoli del modello.
- Esporta in **GLB (glTF)**, pronto per Unity, Unreal e Godot, anche con **LOD automatici** (tre livelli di dettaglio in tre file).

Funziona senza servizi a pagamento, senza account e senza connessione a internet.

## Requisiti

- Blender 5.2 LTS (gratuito, da blender.org)

## Installazione

1. Scarica il file `auto3d_prototipo.py` da questa pagina: aprilo e clicca **Download raw file** (l'icona con la freccia verso il basso).
2. In Blender vai in **Modifica → Preferenze → Add-on**.
3. Clicca la piccola freccia in alto a destra e scegli **Installa da disco** (*Install from Disk*), poi seleziona il file scaricato.
4. Cerca **Auto3D** nell'elenco e spunta la casella per attivarlo.

Dopo l'installazione l'add-on resta attivo anche quando riapri Blender.

## Come si usa

1. Nella Vista 3D premi **N** e apri la scheda **Auto3D**.
2. Scegli un preset, regola i cursori e premi **Genera**.
3. Premi **Esporta GLB**. Il file viene salvato nel percorso indicato nel campo **File** (di default nella tua cartella utente). Se l'opzione LOD è attiva e il modello è abbastanza complesso, ottieni tre file: `_LOD0`, `_LOD1` e `_LOD2`.

## Prossimi passi

- Altri preset (recinzioni, armi, edifici più vari)
- Personaggi con scheletro automatico (Rigify) e animazioni libere da diritti
- Interfaccia ancora più semplice per chi non ha mai usato il 3D

## Contribuire

Idee, segnalazioni di problemi e proposte sono benvenute: apri una *issue* su GitHub.

## Licenza

Rilasciato con licenza **GPL-3.0**. Vedi il file `LICENSE`.
