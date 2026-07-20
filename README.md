# Rick and Morty Telegram Bot

A Telegram bot built with **Python** and **aiogram 3** that allows users to search characters from the Rick and Morty universe using the official Rick and Morty API.

## Features

- 🎲 Get a random character
- 🔍 Search characters by name
- 📊 Search characters by status (`Alive`, `Dead`, `Unknown`)
- 🖼 Display character image and information
- ⚡ Asynchronous HTTP requests using `aiohttp`
- 🧠 State management with FSM (Finite State Machine)

## Technologies

- Python 3.13+
- aiogram 3
- aiohttp
- python-dotenv

## Project Structure

```text
.
├── handlers/
│   ├── random_character.py
│   ├── search_by_name.py
│   ├── search_by_status.py
│   └── ...
├── keyboards/
├── services/
│   └── rick_and_morty_api.py
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Nez0uS/rick-and-morty-telegram-bot.git
```

Go to the project directory:

```bash
cd rick-and-morty-telegram-bot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

macOS / Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token
```

## Run

```bash
python main.py
```

## API

This project uses the official Rick and Morty API:

https://rickandmortyapi.com/

## Future Improvements

- Search by species
- Search by gender
- Search by episode
- Character pagination
- Better error handling
- Unit tests
- Docker support

## Author

GitHub: https://github.com/Nez0uS