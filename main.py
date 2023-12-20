import telebot

bot = telebot.TeleBot('6567424774:AAHercxUd64r4mqrPP_dfm_PsRVkMFHDnXk')


@bot.message_handler(commands=['start'])
def message_start(message):
    user_id = message.from_user.id

    bot.send_message(user_id, 'Добро пожаловать, рады вас приветствовать! '
                              'Напишите /help что-бы узнать справочную информацию')



@bot.message_handler(commands=['help'])
def help_info(message):
    user_id = message.from_user.id

    bot.send_message(user_id, 'Тут находится справочная информация =)')



bot.infinity_polling()
