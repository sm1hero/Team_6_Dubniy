from TOKEN import token
import telebot
from telebot import types

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("День недели")
    item2 = types.KeyboardButton("Фамилии учителей")
    item3 = types.KeyboardButton("Номера кабинетов")
    markup.add(item1, item2, item3)
    item4 = types.KeyboardButton("Добавить")
    item5 = types.KeyboardButton("Редактировать")
    item6 = types.KeyboardButton("Удалить")
    markup1.add(item4, item5, item6)
    if message.chat.id == 1658431458:
        bot.send_message(message.chat.id, 'Здравствуйте! Желаете добавить, редактировать или удалить занятие?'.format(message.from_user,
                                                                                                     bot.get_me()),
                         reply_markup=markup1)
    else:
        bot.send_message(message.chat.id, 'Привет! Напиши мне день/учителя/номер кабинета и я покажу тебе расписание!'.format(message.from_user,
                                                                                                     bot.get_me()),
                         reply_markup=markup)
@bot.message_handler(content_types=['text'])
def chating(message):
    if message.chat.type == 'private':
        if message.text == 'Расписание занятий':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('День недели', callback_data='dayofweek')
            item2 = types.InlineKeyboardButton('Фамилия педагога', callback_data='surname')
            item3 = types.InlineKeyboardButton('Номер кабинета', callback_data='number')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Выберите, как вы хотите реализовать поиск :', reply_markup=markup)

                if message.text == 'День недели':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton('Понедельник')
                    item2 = types.KeyboardButton('Вторник')
                    item3 = types.KeyboardButton('Среда')
                    item4 = types.KeyboardButton('Четверг')
                    item5 = types.KeyboardButton('Пятница')
                    item6 = types.KeyboardButton('Суббота')
                    item7 = types.KeyboardButton('Воскресенье')
                    markup.add(item1, item2, item3, item4, item5, item6, item7)
                    bot.send_message(message.chat.id, 'Выберите день недели', reply_markup=markup)

                    @bot.callback_query_handler(func=lambda call: True)
                    def callback_inline(call):
                        if call.message:
                            if call.data == 'dayofweek':
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat_id,
                                                      text='Введите день недели: ')
                            elif call.data == 'surname':
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat_id,
                                                      text='Введите фамилию педагога: ')
                            elif call.data == 'number':
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat_id,
                                                      text='Введите номер кабинета: ')

                                if message.text == 'День недели':
                                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                    item1 = types.KeyboardButton('Понедельник')
                                    item2 = types.KeyboardButton('Вторник')
                                    item3 = types.KeyboardButton('Среда')
                                    item4 = types.KeyboardButton('Четверг')
                                    item5 = types.KeyboardButton('Пятница')
                                    item6 = types.KeyboardButton('Суббота')
                                    item7 = types.KeyboardButton('Воскресенье')
                                    markup.add(item1, item2, item3, item4, item5, item6, item7)
                                    bot.send_message(message.chat.id, 'Выберите день недели', reply_markup=markup)


bot.polling()