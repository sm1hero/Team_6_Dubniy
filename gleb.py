from TOKEN import token
import telebot
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    if message.chat.id == 1658431458:
        bot.send_message(message.chat.id, 'Здравствуйте! Желаете добавить, редактировать или удалить занятие?')
bot.polling()
class Raspisanie():
    def __init__(self, day, type, group, time, teacher, number):
        self.day = day
        self.type = type
        self.group = group
        self.time = time
        self.teacher = teacher
        self.number = number

