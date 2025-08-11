from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler
import subprocess
import os
import time
from pytz import timezone
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Telegram bot token
TELEGRAM_BOT_TOKEN = "7815383601:AAE3lMDLmO34w5O8LOmiKMssQu8Cm4DYDmI"
BOT_NAME = "SpoArcane_bot"

# Scheduler (future use)
scheduler = AsyncIOScheduler(timezone=timezone("UTC"))

# States for conversation
CHOOSING, SINGLE_SONG, PLAYLIST = range(3)

# Start command
async def start(update: Update, context: CallbackContext):
    reply_keyboard = [["Single Song", "Playlist"]]
    await update.message.reply_text(
        "🎵 What would you like to download?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return CHOOSING

# Choice handler
async def choice_handler(update: Update, context: CallbackContext):
    user_choice = update.message.text.strip().lower()
    if user_choice == "single song":
        await update.message.reply_text("🎶 Send me the Spotify song link:")
        return SINGLE_SONG
    elif user_choice == "playlist":
        await update.message.reply_text("🎶 Send me the Spotify playlist link:")
        return PLAYLIST
    else:
        await update.message.reply_text("❌ Please choose 'Single Song' or 'Playlist'.")
        return CHOOSING

# Single song download
async def handle_single_song(update: Update, context: CallbackContext):
    spotify_url = update.message.text.strip()

    if not spotify_url.startswith("https://open.spotify.com/track"):
        await update.message.reply_text("❌ Please send a valid Spotify song link.")
        return SINGLE_SONG

    download_folder = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_folder, exist_ok=True)

    try:
        result = subprocess.run(
            ["spotdl", spotify_url, "--output", download_folder],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            downloaded_files = [f for f in os.listdir(download_folder) if f.endswith(".mp3")]
            if downloaded_files:
                file_path = os.path.join(download_folder, downloaded_files[0])
                await update.message.reply_document(document=open(file_path, "rb"))
                await update.message.reply_text(f"✅ Song sent!\n{BOT_NAME} says Thank you! 😊")
                os.remove(file_path)
            else:
                await update.message.reply_text("⚠️ Song downloaded but file not found.")
        else:
            await update.message.reply_text("❌ Error during download.")
    except Exception as e:
        await update.message.reply_text(f"❌ Exception: {str(e)}")

    return ConversationHandler.END

# Playlist download
async def handle_playlist(update: Update, context: CallbackContext):
    playlist_url = update.message.text.strip()

    if not playlist_url.startswith("https://open.spotify.com/playlist"):
        await update.message.reply_text("❌ Please send a valid Spotify playlist link.")
        return PLAYLIST

    download_folder = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_folder, exist_ok=True)

    try:
        subprocess.run(
            ["spotdl", playlist_url, "--output", download_folder],
            capture_output=True,
            text=True
        )

        downloaded_files = [f for f in os.listdir(download_folder) if f.endswith(".mp3")]
        if downloaded_files:
            for song in downloaded_files:
                file_path = os.path.join(download_folder, song)
                if os.path.getsize(file_path) <= 50 * 1024 * 1024:
                    await update.message.reply_document(document=open(file_path, "rb"))
                else:
                    await update.message.reply_text(f"⚠️ '{song}' too large to send.")
                os.remove(file_path)
            await update.message.reply_text(f"✅ Playlist sent!\n{BOT_NAME} says Thank you! 😊")
        else:
            await update.message.reply_text("⚠️ No songs found after download.")

    except Exception as e:
        await update.message.reply_text(f"❌ Exception: {str(e)}")

    return ConversationHandler.END

# Cancel
async def cancel(update: Update, context: CallbackContext):
    await update.message.reply_text("❌ Operation cancelled.")
    return ConversationHandler.END

# Run bot
def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING: [MessageHandler(filters.TEXT & ~filters.COMMAND, choice_handler)],
            SINGLE_SONG: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_single_song)],
            PLAYLIST: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_playlist)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
