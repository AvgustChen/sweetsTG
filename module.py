from random import randint as ri
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters



who = 0
player1 = False
bot = False
bot1 = 0
sweets = 150
takesweet = 0
swp1 = 0
swp2 = 0


def whoisplay():
    global player1
    global bot
    who = (ri(1, 2))
    if who == 1:
        player1 = True
        bot = False
    else:
        bot = True
        player1 = False

def read_count(update):
    text = int(update)
    return text



async def game_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global player1
    global bot
    global sweets
    # sweets = 150
    global swp1
    global swp2
    takesweet = 0
    # swp1 = 0
    # swp2 = 0
    m = 28

    if player1==False and bot == False:
        whoisplay()
    while sweets > 0:
        await update.message.reply_text(f'В корзине {sweets} конфет')
        if player1:
            await update.message.reply_text(f'Твой ход 1\nУ тебя в корзине {swp1} конфет')
            await update.message.reply_text(f'Сколько конфет возмешь?')
            takesweet = read_count(update.message.text)
            update.message.text = ''
            while not (takesweet <= 28 and takesweet > 0 and sweets > 0 and takesweet<=sweets):
                await update.message.reply_text(f'В корзине {sweets} конфет')
                await update.message.reply_text('Вы берете слишком много конфет, попробуйте снова!')
                takesweet = read_count(update.message.text)
                update.message.text = ''
            sweets -= takesweet
            swp1 += takesweet
            bot = True
            player1 = False
            takesweet = 0

        if bot:
            await update.message.reply_text(f'Мой ход\nСейчас у меня {swp2} конфет')
            takesweet=sweets%(m+1) if not sweets%(m+1)==0 else 1
            await update.message.reply_text(f'Я возьму {takesweet} конфет')
            sweets -= takesweet
            swp2 += takesweet
            player1 = True
            bot = False
            
        if sweets == 0 and bot == True: 
            await update.message.reply_text('Я победил!!!') 
            break 
        elif sweets==0 and player1 == True:
            await update.message.reply_text('Поздравляю, ты победил!!!') 
            break
        


        