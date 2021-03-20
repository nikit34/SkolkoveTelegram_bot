import telebot
import sqlite3
import datetime

file1 = open('token.txt', 'r')
token = file1.readlines()[0]
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE books
                  (isbn text, taken text, date_taken text,
                   who_took text)
               """)

# Сохраняем изменения
conn.commit()

# Вставляем множество данных в таблицу используя безопасный метод "?"

cursor.execute("""INSERT INTO books VALUES ('5271036014', 'False' , NULL, NULL)""")
conn.commit()
isbn = cursor.execute("""SELECT isbn FROM books""").fetchmany()

bot = telebot.TeleBot(token)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Взять книгу', 'Вернуть книгу')
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('1', '2', '3', '4', '5', '6', '7', '8', '9,' '0')

take = False

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, {}, я работаю'.format(message.from_user.username), reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):

    take = False
    if message.text.lower() == 'взять книгу':
        bot.send_message(message.chat.id, 'Введи ISBN c форзаца книги (только цифры подряд)')
        take = True


    elif message.text.lower() == 'вернуть книгу':
        bot.send_message(message.chat.id, 'Давай')





bot.polling()