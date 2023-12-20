import telebot


bot = telebot.TeleBot('6567424774:AAHercxUd64r4mqrPP_dfm_PsRVkMFHDnXk')


@bot.message_handler(commands=['start'])
def message_start(message):
    user_id = message.from_user.id

    bot.send_message(user_id, 'Добро пожаловать, рады вас приветствовать! '
                              'Напишите /help что-бы узнать справочную информацию')

    bot.register_next_step_handler(message, help_info)


def help_info(message):
    user_id = message.from_user.id

    bot.send_message(user_id, 'Тут находится справочная информация =)')

    bot.register_next_step_handler(message, message_start)




bot.infinity_polling()