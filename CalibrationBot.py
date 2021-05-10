pip install pytelegrambotapi
import telebot
bot = telebot.TeleBot('1713086812:AAHhAQEOyZ8FXHPmlf3O8D9yVFN1iaGk3TA')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот для обчислення коефіцієнтів калібрування. Приємно познайомитися!, {message.from_user.first_name}')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет' or message.text.lower() == 'привіт' or message.text.lower() == 'hello':
        bot.send_message(message.from_user.id, 'Привіт!')
    elif message.text.lower() == 'my':
        bot.send_message(message.from_user.id, 'my little familyy group member =) (='
    else
        bot.send_message(message.from_user.id, 'Я ще маленький і вмійю тільки вітатися. Привіт =)'
bot.polling(none_stop=True)