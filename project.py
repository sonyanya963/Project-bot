import telebot
from telebot import types
token = "8725822842:AAHbicydombOVV1uvVk21E0lyxCtU8DzyiA"
mybot = telebot.TeleBot(token)
#сюда добавить массив questions
right_ans = ()
@mybot.message_handler(['start'])
def start(message):
    text1 = "привет!"
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text = "Начать викторину", callback_data= "quiz")
    keyboard.add(button1)
    mybot.send_message(text= text1, chat_id= message.chat.id, reply_markup= keyboard)


@mybot.callback_query_handler(func= lambda call: call.data == "quiz")
def quiz(call):
    mybot.send_message(text= 'я тут', chat_id= call.message.chat.id)
    #цикл for который проходится по question, брать 1 вопрос с помощью соо с помощью mybot.send_message(keyboard на 4 кнопки)
    #if коллбек совпадает с корректом из списка в райт_анс +1
mybot.infinity_polling()