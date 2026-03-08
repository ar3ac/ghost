# GitHub User Activity CLI — TODO

Obiettivo: Costruire un tool da riga di comando che accetta un username GitHub e stampa a schermo le sue ultime attività pubbliche, usando solo le librerie standard di Python.

---

## Fase 1 — Setup e Interfaccia CLI

L'obiettivo qui è solo prendere l'input dall'utente senza errori.

- [x] Implementa `sys.argv` o `argparse` per catturare lo username (es: `python main.py kamranahmedse`).
- [x] Gestisci il caso in cui l'utente lancia lo script senza passare nessuno username (mostra un messaggio di aiuto).
- [x] Salva lo username in una variabile e stampalo a schermo (es. "Cerco le attività per: kamranahmedse") per confermare che la CLI funziona.

Criterio "done":

- Lo script non va in crash se dimentico l'username, e se lo inserisco lo legge correttamente.

---

## Fase 2 — La Connessione (HTTP Request con urllib)

L'obiettivo qui è fare la chiamata API al server di GitHub (senza usare la libreria esterna `requests`).

- [x] Importa il modulo standard `urllib.request`.
- [x] Costruisci l'URL dinamico: `https://api.github.com/users/<username>/events`.
- [x] Crea una funzione che fa la richiesta HTTP a quell'URL usando `urllib.request.urlopen()`.
- [x] Leggi la risposta del server e decodificala (di solito arriva in formato _byte_, devi trasformarla in stringa/testo).
- [x] Per ora, stampa l'intero blocco di testo grezzo nel terminale per assicurarti che i dati arrivino.

Criterio "done":

- Inserendo un username valido, il terminale si riempie di testo grezzo in formato JSON proveniente da GitHub.

---

## Fase 3 — Parsing del JSON ed Estrazione Dati

GitHub ci manda un mucchio di dati, noi dobbiamo estrarre solo quelli utili usando il modulo standard `json`.

- [x] Importa il modulo standard `json`.
- [x] Usa `json.loads()` per trasformare il testo grezzo scaricato prima in una vera lista di dizionari Python.
- [x] Fai un ciclo `for` su questa lista.
- [x] Per ogni evento (elemento della lista), estrai il tipo di evento (es. la chiave `type`) e il nome del repository (es. dentro la chiave `repo` -> `name`).
- [x] Stampa questi due dati a schermo in modo grezzo.

Criterio "done":

- Il terminale non mostra più il testo illeggibile, ma una lista semplice tipo: "PushEvent - user/repo".

---

## Fase 4 — Formattazione dell'Output

"PushEvent" non è molto bello da leggere. Dobbiamo tradurre i nomi tecnici di GitHub in frasi leggibili per un essere umano.

- [x] Crea una logica (es. `if/elif` o `match/case`) per tradurre i tipi di evento più comuni:
  - Se è `PushEvent` -> "Pushed X commits to <repo>"
  - Se è `IssuesEvent` -> "Opened a new issue in <repo>"
  - Se è `WatchEvent` -> "Starred <repo>"
  - Se è `CreateEvent` -> "Created <repo>"
- [x] Stampa l'output finale pulito, riga per riga, esattamente come richiesto da roadmap.sh.

Criterio "done":

- L'output finale è identico all'esempio di roadmap.sh.

---

## Fase 5 — Gestione degli Errori (Robustezza)

Cosa succede se internet non va o l'utente non esiste?

- [x] Aggiungi un blocco `try/except` intorno alla tua chiamata di rete (`urlopen`).
- [x] Gestisci l'Errore 404 (Not Found): stampa "Errore: L'utente specificato non esiste su GitHub".
- [x] Gestisci l'Errore 403 o 429 (Rate Limit): GitHub limita le chiamate anonime. Se superi il limite, stampa "Errore: Limite di chiamate API raggiunto".
- [x] Gestisci errori generici di rete (es. Wi-Fi spento): stampa "Errore di connessione".

Criterio "done":

- Qualsiasi errore venga causato dall'utente o dalla rete viene gestito con un messaggio pulito senza mostrare il "Traceback" (il testo rosso di errore di Python).
