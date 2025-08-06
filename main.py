import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8200860779:AAEgfdHTRLPtWQrGqndHi8UlH4ddqbDVyjw"  # Jangan bocorkan ke publik ya!

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Perintah /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot scalping sudah aktif. Kirim perintah atau pesan apapun.")

# Balas semua pesan teks
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = f"Pesan kamu: {user_message}\n\n(Bot belum punya strategi, tapi sedang dikembangkan.)"
    await update.message.reply_text(response)

# Fungsi utama menjalankan bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
