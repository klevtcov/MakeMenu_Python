import telebot
from config import token



def telegram_bot(token):
    bot = telebot.TeleBot(token)


# Выводит приветственное сообщение
    @bot.message_handler(commands=['start', 'help'])
    def start_message(message):
        bot.send_message(message.chat.id, "Добро пожаловать в MakeMenu\n\n"
                                          "Выбрать количество блюд /makemenu\n"  
                                          "Вызвать эту справку /help или /start\n")


    def gen_markup():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        pass



    @bot.message_handler(commands=['makemenu'])
    def make_menu(message):
        bot.send_message(message.chat.id, "Выберите количество блюд\n\n")

    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton("👋 Поздороваться")
    # btn2 = types.KeyboardButton("❓ Задать вопрос")
    # markup.add(btn1, btn2)


    # def gen_markup():
    #     markup = InlineKeyboardMarkup()
    #     markup.row_width = 2
    #     markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
    #                             InlineKeyboardButton("No", callback_data="cb_no"))
    #     return markup

    # @bot.callback_query_handler(func=lambda call: True)
    # def callback_query(call):
    #     if call.data == "cb_yes":
    #         bot.answer_callback_query(call.id, "Answer is Yes")
    #     elif call.data == "cb_no":
    #         bot.answer_callback_query(call.id, "Answer is No")

    # @bot.message_handler(func=lambda message: True)
    # def message_handler(message):
    #     bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())
















    bot.polling()


if __name__ == '__main__':
    print('Бот запущен')
    telegram_bot(token)
    
