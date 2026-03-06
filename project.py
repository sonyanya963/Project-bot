import telebot
from telebot import types
token = "8453123900:AAFVyY7XA1vi0yGKf1-ZmPmHFjbW7BviDSQ"
mybot = telebot.TeleBot(token)

@mybot.message_handler(command = ['start'])
def start(message):
    text1 = "привет!"
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text = "Начать викторину", callback_data= "quiz")
    keyboard.add(button1)
    mybot.send_message(text= text1, chat_id= message.chat.id, reply_markup= keyboard)

    
mybot.infinity_polling()