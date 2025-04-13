from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ton token Telegram
TOKEN = "7916770472:AAGB4ipLIM576vgMxnZdOI6deYOrvRSJB6U"

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue sur VIPSignalsXL_Bot !\nTon meilleur allié pour gagner facilement à tes jeux préférés !")

# Lancement du bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
