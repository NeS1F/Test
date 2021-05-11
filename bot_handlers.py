from bot import bot # Импортируем объект бота
from messages import * # Инмпортируем все с файла сообщений
from db import users_db


@bot.message_handler(commands=['start', 'help'])
# Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    if not users_db.find_one({'chat_id': message.chat.id}):
        users_db.insert_one({'chat_id': message.chat.id}, {'chat_id': message.from_user.username})
        bot.reply_to(message, f'{HELLO_MESSAGE}, {message.from_user.first_name}')
    else:
        bot.send_message(message.chat.id, HELLO_AGAIN_MESSAGE)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет' or message.text.lower() == 'привіт' or message.text.lower() == 'hello':
        bot.send_message(message.from_user.id, 'Привіт!')
    else:
        bot.send_message(message.from_user.id, 'Я ще маленький і вмійю тільки вітатися. Привіт')


#@bot.message_handler(content_types=['text']) # Любой текст
#def repeat_all_messages(message):
#    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
     bot.polling(none_stop=True)
