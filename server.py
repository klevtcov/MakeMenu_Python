import telebot
from config import token



def telegram_bot(token):
    bot = telebot.TeleBot(token)


# Выводит приветственное сообщение
    @bot.message_handler(commands=['start', 'help'])
    def start_message(message):
        bot.send_message(message.chat.id, "Добро пожаловать в MakeMenu\n\n"
                                          "Вызвать эту справку /help или /start\n")


    bot.polling()


if __name__ == '__main__':
    print('Бот запущен')
    telegram_bot(token)
    
