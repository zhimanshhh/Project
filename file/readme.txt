# Library Management System

A lightweight, menu-driven CLI **Library Management System** built in Python for managing book inventory, lending records, and persistent local storage[cite: 8].

## Features
- **Add Books**: Automatically assigns sequential IDs (`B101`, `B102`, ...) with non-empty title and author validation[cite: 8].
- **Issue & Return**: Tracks member checkouts, prevents duplicate issues, and updates live available book counts[cite: 8].
- **Search**: Case-insensitive partial or full search by **Title** or **Author**[cite: 8].
- **View Catalog**: Displays all books with their ID, title, author, and current status (`Available` / `Issued`)[cite: 8].
- **Persistent Storage**: Automatically loads and saves records in `library.txt`[cite: 8].

## Tech Stack
- **Python 3** (Standard Library only — zero external dependencies)[cite: 8]

## How to Run
```bash
python "library system project.py"