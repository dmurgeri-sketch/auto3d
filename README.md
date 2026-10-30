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

## Come si usa

1. Apri Blender e vai nella scheda **Scripting**.
2. Nell'editor di testo clicca **Apri**, scegli `auto3d_prototipo.py` e premi **Esegui script**.
3. Torna alla scheda **Layout**, passa il mouse sulla Vista 3D e premi **N**: apri la scheda **Auto3D**.
4. Scegli un preset, regola i cursori e premi **Genera**.
5. Premi **Esporta GLB**. Se l'opzione LOD è attiva e il modello è abbastanza complesso, ottieni tre file: `_LOD0`, `_LOD1` e `_LOD2`.

Per ora lo script va rieseguito ogni volta che si riapre Blender. L'installazione come add-on permanente è tra le cose da fare.

## Prossimi passi

- Altri preset (recinzioni, armi, edifici più vari)
- Personaggi con scheletro automatico (Rigify) e animazioni libere da diritti
- Installazione come vero add-on di Blender
- Interfaccia ancora più semplice per chi non ha mai usato il 3D

## Contribuire

Idee, segnalazioni di problemi e proposte sono benvenute: apri una *issue* su GitHub.

## Licenza

Rilasciato con licenza **GPL-3.0**. Vedi il file `LICENSE`.
