import telebot
from telebot import types
token = "8725822842:AAHbicydombOVV1uvVk21E0lyxCtU8DzyiA"
mybot = telebot.TeleBot(token)
questions = {
  1: {
  "question": "Что такое прорезь?",
  "answer1": "Вид рыболовной сети",
  "answer2": "Разновидность рыболовецких лодок",
  "answer3": "Часть такелажа",
  "answer4": "Морской узел",
  "correct_answer": 2
},
 2: {
  "question": "Что такое xnjxnj",
  "answer1": "Вид рыболовнmй сети",
  "answer2": "Разновидность рыболоmnецких лодок",
  "answer3": "Часть такелажn",
  "answer4": "Морcкой узел",
  "correct_answer": 3
},
 3: {'question':"Что такое куклы в рыболовстве?",
    'answer1':"Специальные поплавки",
    'answer2':"Отрезки сетного полотна в виде жгута",
    'answer3':"Элементы оснастки невода",
    'answer4':"Вид рыболовных крючков",
    "correct_answer":2
}
}
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
    keyboard = types.InlineKeyboardMarkup()
    button2_1= types.InlineKeyboardButton(text = , callback_data= "quiz")
    button2_2 = types.InlineKeyboardButton(text = "Начать викторину", callback_data= "quiz")
    button2_3 = types.InlineKeyboardButton(text = "Начать викторину", callback_data= "quiz")
    button2_4 = types.InlineKeyboardButton(text = "Начать викторину", callback_data= "quiz")
    mybot.send_message(text= 'я тут', chat_id= call.message.chat.id)
    #цикл for который проходится по question, брать 1 вопрос с помощью соо с помощью mybot.send_message(keyboard на 4 кнопки)
    #if коллбек совпадает с корректом из списка в райт_анс +1
mybot.infinity_polling()