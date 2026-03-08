# GitHub User Activity CLI

Un semplice tool da riga di comando (CLI) per visualizzare le attività recenti di un utente GitHub.
Progetto realizzato seguendo le specifiche di [roadmap.sh](https://roadmap.sh/projects/github-user-activity).

## Caratteristiche

- 🐍 Scritto interamente in Python.
- 📦 **Zero dipendenze**: utilizza solo le librerie standard (`urllib`, `json`, `sys`).
- 🛡️ Gestione robusta degli errori (Utente non trovato, Rate Limit, Errori di connessione).
- 🎨 Output formattato per una facile lettura.

## Requisiti

- Python 3.x installato.

## Utilizzo

Esegui lo script passando l'username di GitHub come argomento:

```bash
python main.py <username>
```

### Esempio

```bash
python main.py torvalds
```

Output:

```text
Searching activities for user: torvalds
Pushed 2 commits to torvalds/linux
Starred facebook/react
Opened a new issue in microsoft/vscode
Created repository my-new-project
```
