import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@xuanbac20"
CHANNEL_LINK = "https://t.me/xuanbac20"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(m):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Tham gia @xuanbac20", url=CHANNEL_LINK))
    markup.add(InlineKeyboardButton("Da tham gia", callback_data="check"))
    bot.send_message(m.chat.id, "Phai tham gia kenh truoc!", reply_markup=markup)
@bot.callback_query_handler(func=lambda c: c.data=="check")
def check(c):
    try:
        member = bot.get_chat_member(CHANNEL, c.from_user.id)
        if member.status in ['member','administrator','creator']:
            bot.send_message(c.message.chat.id, "Ok da vao roi!")
        else:
            bot.answer_callback_query(c.id, "Ban chua join!")
    except:
        bot.answer_callback_query(c.id, "Ban chua join!")
bot.infinity_polling()
