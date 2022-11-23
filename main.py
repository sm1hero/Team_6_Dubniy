import telebot
from telebot import types

#основной словарь
raspisanie = {}
course = ""

bot = telebot.TeleBot("5980407272:AAG5q_k07BI4G_hP8jX4KtkQUS30DVNee4g")
@bot.message_handler(commands=['start'])
def start_message(message):
    # определяем админа по id
    if message.chat.id == 1658431458:
        bot.send_message(message.chat.id, 'Здравствуйте! Напишите "добавить" чтобы начать')
    else:
        bot.send_message(message.chat.id, 'Привет! Напиши мне день и я покажу тебе расписание!')
@bot.message_handler(content_types='text')
def message_reg(message):
    if message.chat.id == 1658431458:
        if message.text.lower() == 'добавить':
            bot.send_message(message.chat.id, "Опишите курс (время и название): ")
    else:
        lessons = []
        # если по этому дню информации нет получается ошибка
        try:
            while True:
                lessons.append(raspisanie.pop(message))
        except:
            if lessons == lessons.clear():
                bot.send_message(message.chat.id, "Я не понимаю вас!")
                start_message(message)
            else:
                a = ""
                for i in range(0, len(lessons)):
                    a += lessons[i] + ", "
                bot.send_message(message.chat.id, "Занятия: " + a)

@bot.message_handler(content_types='text')
def message_admin(message):
    if message.chat.id == 1658431458:
        course = message.text
        bot.send_message(message.chat.id, "Напишите день недели, кабинет и фамилию учителя (через запятую): ")
    else:
        start_message(message)

@bot.message_handler(content_types='text')
def message_admin(message):
    if message.chat.id == 1658431458:
        params = message.text.split(",")
        raspisanie[params[0]] = course
        raspisanie[params[1]] = course
        raspisanie[params[2]] = course
    else:
        start_message(message)

bot.polling()