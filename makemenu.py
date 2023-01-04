import telebot
from telebot import types
from config import token
import backend
import re



def telegram_bot(token):
    bot = telebot.TeleBot(token)


# Выводит приветственное сообщение
    @bot.message_handler(commands=['start', 'help'])
    def start_message(message):
        bot.send_message(message.chat.id, "Добро пожаловать в MakeMenu\n\n"
                                          "Выбрать количество блюд /makemenu\n"  
                                          "Вызвать эту справку /help или /start\n")


    @bot.message_handler(commands=['makemenu'])
    def make_menu(message):
        bot.send_message(message.chat.id, "Выберите количество блюд\n\n", reply_markup=gen_markup())


    def gen_markup():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("1")
        btn_2 = types.KeyboardButton("2")
        markup.add(btn_1, btn_2)
        return markup

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        btn_rmv = telebot.types.ReplyKeyboardRemove()
        if re.search(r"[0-5]", message.text):
            result = backend.make_uniqu_plates(1)

            bot.send_message(message.chat.id, result, reply_markup=btn_rmv)


        # match message.text:
        #     case "1":
        #         backend.make_uniqu_plates(1)
        #         bot.send_message(message.chat.id,
        # if message.text == "1":
        #     a = telebot.types.ReplyKeyboardRemove()
        #     bot.send_message(message.from_user.id, 'Что', reply_markup=a)


# match http_code:
#     case "200":
#         print("OK")
#         do_something_good()
#     case "404":
#         print("Not Found")
#         do_something_bad()
#     case "418":
#         print("I'm a teapot")
#         make_coffee()
#     case _:
#         print("Code not found")


    # @bot.callback_query_handler(func=lambda call: True)
    # def callback_query(call):
    #     if call.data == "1_menu":
    #         bot.answer_callback_query(call.id, "Answer is 1")
    #     elif call.data == "2_menu":
    #         bot.answer_callback_query(call.id, "Answer is 2")


    # @bot.message_handler(content_types=['text'])
    # def handle_text(message):
    #     if message.text == "Wunderlist":
    #         a = telebot.types.ReplyKeyboardRemove()
    #         bot.send_message(message.from_user.id, 'Что', reply_markup=a)


    # @bot.message_handler(commands=['start'])
    # def start(message):
        # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton("👋 Поздороваться")
        # btn2 = types.KeyboardButton("❓ Задать вопрос")
        # markup.add(btn1, btn2)
        # bot.send_message(message.chat.id, text="Привет", reply_markup=markup)


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
    
