from bot import bot # Импортируем объект бота
from messages import * # Инмпортируем все с файла сообщений
from db import users_db


@bot.message_handler(commands=['start', 'help'])
# Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    if not users_db.find_one({'chat_id': message.chat.id}):
        users_db.insert_one({'chat_id': message.chat.id, 'username': message.from_user.username})
        bot.reply_to(message, f'{HELLO_MESSAGE}, {message.from_user.first_name}')
    else:
        bot.send_message(message.chat.id, HELLO_AGAIN_MESSAGE)


@bot.message_handler(commands=['toeveryone'])
# Выполняется, когда пользователь нажимает на toeveryone
def get_text_messages(message)::
    if message.chat.id != 396751749:
        bot.reply_to(message, f'{DENY}, {message.from_user.first_name}')
    else:
        def get_text_messages(message):
            if message.text.lower() !=''
	       input_message = message.text.lower()
	       def send_message_to_all_users(message: str):
               # Функция для рассылки, принимает сообщение
               if message != '':
                   # Перебираем всех пользователей в бд
                   for user in users_db.find():
                       # Пытаемся отправить сообщение
                       try:
                           bot.send_message(user['chat_id'], message)
                       # Если какая-то ошибка - выводим это
                       except Exception as e:
                           bot.reply_to(message, f'{ERROR}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() in ['привет', 'привіт', 'hello', 'здоров', 'hi', 'hola']:
        bot.send_message(message.from_user.id, 'Привіт!')
    elif message.text.lower() in ['блять', 'fuck', 'сука', 'пизда', 'хуй', 'бля', 'шалава', 'блядь', 'нахуй', 'мудак', 'підарас', 'підар', 'підор', 'підарасіна', 'псіна', 'псіна сутула']:
        bot.send_message(message.from_user.id, 'УУУ хтось хоче получити по онлайн їбалу -_-')
    elif message.text.lower() in ['nigger', 'nigga', 'ніга', 'нігер']:
        bot.send_message(message.from_user.id, 'Тссс! Твітч почує))')
    else:
        bot.send_message(message.from_user.id, 'Я ще маленький і вмійю тільки вітатися. Привіт')


#@bot.message_handler(content_types=['text']) # Любой текст
#def repeat_all_messages(message):
#    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
     bot.polling(none_stop=True)
