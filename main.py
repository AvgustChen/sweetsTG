from signal import Handlers
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import Update
import view, module

app = ApplicationBuilder().token("5617585493:AAF4JQJMtp4gxsUp9UDjyZzEVaNHrHpzwKs").build()



app.add_handler(CommandHandler("start", view.start))
app.add_handler(CommandHandler("help", view.help))
app.add_handler(MessageHandler(filters.TEXT, module.game_start))
app.run_polling()

