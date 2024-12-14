from aiogram.types.web_app_info import WebAppInfo
from currency_converter import CurrencyConverter
import json
import requests
import sqlite3
import telebot
import webbrowser
from telebot import types
bot = telebot.TeleBot("7214959245:AAGjvIlEmJ9Z9vVNmVZ1_0NKyWCwO_TsEIc")
@bot.message_handler(commands=["start"])
def start(message):
    murkup = types.ReplyKeyboardMarkup()
    murkup.add(types.KeyboardButton("Открыть веб страницу", web_app=WebAppInfo(url="https://itproger.com")))
    #murkup.add(types.InlineKeyboardButton("Открыть веб страницу",webbrowser.open("https://itproger.com")))
    bot.send_message(message.chat.id, "Приветмой друг", reply_markup = murkup)
    
    


#*********************************ДРУГАЯ БИБЛИОТЕКА********************************************************

#from currency_converter import CurrencyConverter
#import json
#import requests
#import sqlite3
#import telebot
#import webbrowser
#from telebot import types

#**********************бот конвертатор
#bot = telebot.TeleBot("7214959245:AAGjvIlEmJ9Z9vVNmVZ1_0NKyWCwO_TsEIc")
#currency = CurrencyConverter()
#dan = 0
#@bot.message_handler(commands = ["start"])
#def start(message):
    #bot.send_message(message.chat.id, "Привет, введите сумму")
    #bot.register_next_step_handler(message, summa)

#def summa(message):
    #global dan
    #try:
        #dan = int(message.text.strip())
    #except ValueError:
        #bot.send_message(message.chat.id, "Ошибка! Введите сумму")
        #bot.register_next_step_handler(message,summa)
        #return
    #if dan > 0:
        #murkup = types.InlineKeyboardMarkup(row_width=2)
        #btn1 = types.InlineKeyboardButton("USD/EUR", callback_data="usd/eur")
        #btn2 = types.InlineKeyboardButton("EUR/USD", callback_data="eur/usd")
        #btn3 = types.InlineKeyboardButton("USD/GBP", callback_data="usd/gbp")
        #btn4 = types.InlineKeyboardButton("Другое значение", callback_data="else")
        #murkup.add(btn1,btn2,btn3,btn4)
        #bot.send_message(message.chat.id,"Выберите пару валют",reply_markup=murkup)
    #else:
        #bot.send_message(message.chat.id, "Число должно быть больше 0! Введите сумму")
        #bot.register_next_step_handler(message,summa)

#@bot.callback_query_handler(func=lambda call: True)
#def callback(call):
    #if call.data != "else":
        #values = call.data.upper().split("/")
        #res = currency.convert(dan,values[0], values[1])
        #bot.send_message(call.message.chat.id, f"Получается {round(res,2)}. Можите заново вписать сумму")
        #bot.register_next_step_handler(call.message, summa)
    #else:
        #bot.send_message(call.message.chat.id, "Введите пару значений через /")
        #bot.register_next_step_handler(call.message, my_currency)

#def my_currency(message):
    #try:
        #values = message.text.upper().split("/")
        #res = currency.convert(dan,values[0], values[1])
        #bot.send_message(message.chat.id, f"Получается {round(res,2)}. Можите заново вписать сумму")
        #bot.register_next_step_handler(message, summa)
    #except Exception:
        #bot.send_message(message.chat.id, "Что то не так")
        #bot.register_next_step_handler(message, my_currency)






















#****************бот погоды

#API = "e7a15f468d723a8b56b201659a46e505"
#@bot.message_handler(commands = ["start"])
#def start(message):
    #bot.send_message(message.chat.id, "Привет, рад тебя видеть! Напиши название города")

#@bot.message_handler(content_types = "text")
#def get_weather(message):
    #city = message.text.strip().lower()
    #pogoda = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    #data = json.loads(pogoda.text)
    #bot.reply_to(message, f'Сейчас темпиратура: {data["main"]["temp"]}')







#**********************************************Обращение к базе данных и вывод списка зарегестрированных
#name1 = None
#@bot.message_handler(commands = ["start"])
#def start(message):
    #conn = sqlite3.connect("base.sql")
    #cur = conn.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key,name varchar(50), pass varchar(50))")
    #conn.commit()
    #cur.close()
    #conn.close()
    #bot.send_message(message.chat.id, "Привет, сейчас тебя зарегистрируем! Введие свое имя")
    #bot.register_next_step_handler(message, user_name)

#def user_name(message):
    #global name1
    #name1 = message.text.strip()
    #bot.send_message(message.chat.id, "Введите ваш пароль")
    #bot.register_next_step_handler(message, user_pass)

#def user_pass(message):
    #password = message.text.strip()
    #conn = sqlite3.connect("base.sql")
    #cur = conn.cursor()
    #cur.execute("INSERT INTO users(name, pass) VALUES ('%s', '%s')" % (name1, password)  )
    #conn.commit()
    #cur.close()
    #conn.close()

    #murkup = types.InlineKeyboardMarkup()
    #murkup.add(types.InlineKeyboardButton("Список зарегестрированных пользователей", callback_data = "users"))
    #bot.send_message(message.chat.id, "Вы успешно зарегистрировались!", reply_markup = murkup)
    
#@bot.callback_query_handler(func = lambda call:True)
#def callback(call):
    #conn = sqlite3.connect("base.sql")
    #cur = conn.cursor()
    #cur.execute("SELECT * FROM users")
    #users = cur.fetchall()

    #spisok = ""
    #for el in users:
        #spisok += f"Имя: {el[1],}, Пароль: {el[2]}\n"
    #cur.close()
    #conn.close()
    #bot.send_message(call.message.chat.id, spisok)

#**********************************************************************



#Создает кнопки при вводе команды старт
    #markup = types.ReplyKeyboardMarkup()
    #button1 = types.KeyboardButton("Перейти на сайт")
    #markup.row(button1)
    #button2 = types.KeyboardButton("Удалить фото ")
    #button3 = types.KeyboardButton("Изменить текст ")
    #markup.row(button2, button3)
    #file1 = open("image/star.bmp","rb")
    #bot.send_photo(message.chat.id, file1, reply_markup = markup )
    #bot.send_message(message.chat.id, "Привет", reply_markup = markup)
    #bot.register_next_step_handler(message, on_click)

#Дает функцианал кнопкам
#def on_click(message):
    #if message.text == "Перейти на сайт":
        #bot.send_message(message.chat.id, "Website is open")
    #elif message.text == "Удалить фото":
        #bot.send_message(message.chat.id, "Delete")
        








#Создает кнопки после определенного сообщения(InLine)
#@bot.message_handler(content_types = ["photo"])#может  принимать много значений
#def get_photo(message):
    #markup = types.InlineKeyboardMarkup()
    #button1 = types.InlineKeyboardButton("Перейти на сайт", url= "https://google.com")
    #markup.row(button1)
    #button2 = types.InlineKeyboardButton("Удалить фото ", callback_data = "delete")
    #button3 = types.InlineKeyboardButton("Изменить текст ", callback_data = "edit")
    #markup.row(button2, button3)
    #bot.send_message(message.chat.id,"Какое красивое фото", reply_markup = markup)

#Дает функцианал InLine кнопкам
#@bot.callback_query_handler(func=lambda callback: True)
#def callback_message(callback):
    #if callback.data == "delete":
        #bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    #elif callback.data == "edit":
        #bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id)

#Информация о чате
#@bot.message_handler()
#def info(message):
    #if message.text.lower() == "привет":
        #bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}')
    #elif message.text.lower() == "id":
        #bot.reply_to(message, f"ID: {message.from_user.id}")

#Обрабатывает команду хелп
#@bot.message_handler(commands=["help"])
#def main(message):
    #bot.send_message(message.chat.id, "help information")


bot.polling(none_stop= True)