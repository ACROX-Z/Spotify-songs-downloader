# Spotify Downloader Bot & CLI Tool

A simple yet powerful Spotify music downloader built using **SpotDL**, **Python**, and **Telegram Bot API**.  
You can download **single songs** or **entire playlists** from Spotify directly via a Telegram bot or through a **command-line interface**.




# Features :

### **Telegram Bot**
- Download a **single Spotify song** by link.
- Download an **entire Spotify playlist**.
- Sends MP3 files directly to your Telegram chat.
- Deletes files after sending to save storage.
- Easy-to-use interface with **Reply Keyboard** buttons.
- Handles errors and invalid links gracefully.

### **CLI Tool**
- Download a single song from Spotify.
- Download an entire playlist from Spotify.
- Bulk download from a `.txt` file containing multiple Spotify links.
- Lightweight and terminal-friendly.

---

##  Installation

### **1. Clone the repository**

```bash
    git clone https://github.com/ACROX-Z/Spotify-songs-downloader 
```
```bash
    cd spotify-downloader
```
### **2. Install dependencies**
 - Make sure you have Python 3.10+ installed.
 ```bash
    pip install python-telegram-bot==20.3 spotdl pytz apscheduler
 ```

### **3. Set up your Telegram Bot**
---
- Open Telegram and search for @BotFather.
- Run /newbot and follow the steps.
- Copy your bot token and replace it in :
```bash
    TELEGRAM_BOT_TOKEN = "<YOUR_BOT_TOKEN>"
```
## Run the Telegram Bot
 ```bash
    python telegram_bot.py
 ```

 ## **Run the CLI Tool**
 ```bash
    python spotify_cli.py
 ```
 ### You can see this :
  ```bash
  Spotify Song Downloader using SpotDL

Options:
1. Download a Single Song
2. Download a Playlist
3. Bulk Download from File (songs.txt)
4. Exit
 ```
 ## 🛑 Disclaimer
### This project is intended solely for educational and personal use.
### Downloading copyrighted content without proper authorization may violate Spotify’s terms of service and copyright laws in your country.
### The author of this project is not responsible for any misuse of the code.
