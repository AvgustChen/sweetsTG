count = 0
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
    print(player1, bot)
    who = (ri(1, 2))
    if who == 1:
        player1 = True
        bot = False
    else:
        bot = True
        player1 = False
    print(player1, bot)

async def game_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global player1
    global bot
    global sweets
    if player1==False and bot == False:
        whoisplay()
        print(player1, bot)
    elif player1==True and bot == False:
        game_player1(update, context)
    elif player1==False and bot == True:
        game_bot(update, context)
    elif sweets == 0:
        win(update, context)





async def win(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global swp2
    if swp2 == 150:
        await update.message.reply_text('Я победил!!!')
    else:
        await update.message.reply_text('Поздравляю, ты победил!!!')

async def game_player1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global player1
    global bot
    global swp1
    global sweets
    await update.message.reply_text(f'Cейчас в корзине {sweets} конфет')
    if player1:
        runp1 = True
        while runp1:
            await update.message.reply_text(f'Твой ход 1\nУ тебя в корзине {swp1} конфет')
            await update.message.reply_text(f'Сколько конфет возмешь?')
            takesweet = int(update.message.text)
            if takesweet <= 28 and takesweet > 0 and sweets > 0 and takesweet<=sweets:
                for i in range(takesweet):
                    sweets -= 1
                    swp1 += 1
                    runp1 = False
            else:
                await update.message.reply_text('Вы берете слишком много конфет, попробуйте снова!')
                await update.message.reply_text(f'Cейчас в корзине {sweets} конфет')
        bot = True
        player1 = False


async def game_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global player1
    global bot
    global swp2
    global sweets
    await update.message.reply_text(f'Мой ход\nСейчас у меня {swp2} конфет')

    if sweets > 80 and sweets % 2 == 0:
        await update.message.reply_text(f'Я возьму 28 конфет')
        sweets -= 28
        swp2+=28
        player1 = True
        bot = False
    elif sweets > 56 and sweets % 2 != 0:
        await update.message.reply_text(f'Я возьму 21 конфет')
        sweets -= 21
        swp2+=21
        player1 = True
        bot = False
    elif sweets < 28:
        await update.message.reply_text(f'Я возьму {sweets} конфет')
        sweets -= sweets
        swp2+=sweets
        player1 = True
        bot = False
    elif sweets > 28 and sweets <= 56:
        takesweet = 0
        for takesweet in range(28):
            if sweets - takesweet == 29:
                await update.message.reply_text(f'Я возьму {takesweet}  конфет')
                sweets -= takesweet
                swp2+=takesweet
        player1 = True
        bot = False 