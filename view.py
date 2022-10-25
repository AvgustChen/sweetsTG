from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!\nЭто бот для игры в конфеты, набери /help чтобы узнать правила, или введи любой текст чтобы начать играть')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}\n\
       Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.\
       Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
       Все конфеты оппонента достаются сделавшему последний ход.')