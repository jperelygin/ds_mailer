import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)
img_list = {'1':'a.jpg', '2':'b.jpg', '3':'c.jpg'}

@bot.message_handler(content_types=["text"])
def button_pics(message):
	keyboard = types.InlineKeyboardMarkup()
	button = types.InlineKeyboardButton(text="Выбери1", callback_data='test1')
	button2 = types.InlineKeyboardButton(text="Выбери2", callback_data='test2')
	button3 = types.InlineKeyboardButton(text="Выбери3", callback_data='test3')
	keyboard.add(button,button2,button3)
	bot.send_message(message.chat.id, 'Message is non-empty!' ,reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	id = call.data[-1:]
	img = img_list[id]
	pic_path = r'c:/sqliteBD/pics/'
	img_cert = open(pic_path + img, 'rb')
	img_send = bot.send_photo(chat_id=call.message.chat.id, photo=img_cert)
	print(img_send)
	
	
	if call.message:
		if call.data == "test1":
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь1")
		elif call.data == "test2":
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь2")
		elif call.data == "test3":
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь3")
	
'''
bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.messag

e.message_id,
def certain_picture(message):
	if message.text in img_list:
		img = img_list[message.text]
		c = r'c:/sqliteBD/pics/'
		img_cert = open(c + img, 'rb')
		img_send = bot.send_photo(message.chat.id, img_cert)
		print(img_send)
		time.sleep(3)def certain_picture(message):
	if message.text in img_list:
		img = img_list[message.text]
		c = r'c:/sqliteBD/pics/'
		img_cert = open(c + img, 'rb')
		img_send = bot.send_photo(message.chat.id, img_cert)
		print(img_send)
		time.sleep(3)
'''

if __name__ == '__main__':
	bot.polling(none_stop=True)