from TOKEN import token
import telebot
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
bot.polling()
class Raspisanie():
    def __init__(self, day, group, time, ):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
