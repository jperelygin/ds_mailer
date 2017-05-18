import config
import telebot
import os, sys, time
from telebot import types

bot = telebot.TeleBot(config.token)
img_list = {'/1':'a.jpg', '/2':'b.jpg', '/3':'c.jpg'}

@bot.message_handler(commands=['help'])
def send_image_help(help):
	#for file in os.open('c:\sqliteBD'):
		img = open('C:\sqliteBD\iii.jpg', 'rb')
		img_send = bot.send_photo(help.chat.id, img)
		print(img_send)
		time.sleep(1)

@bot.message_handler(commands=['1','2','3'])
def certain_picture(message):
	if message.text in img_list:
		img = img_list[message.text]
		v = r'c:/sqliteBD/pics/'
		img_cert = open(v + img, 'rb')
		img_send = bot.send_photo(message.chat.id, img_cert)
		print(img_send)
		time.sleep(3)

@bot.message_handler(commands=["pictures"])
def button_pics(message):
	keyboard = types.InlineKeyboardMarkup()
	button = types.InlineKeyboardButton(text="Первая", callback_data='test1')
	button2 = types.InlineKeyboardButton(text="Вторая", callback_data='test2')
	button3 = types.InlineKeyboardButton(text="Третья", callback_data='test3')
	keyboard.add(button,button2,button3)
	bot.send_message(message.chat.id, 'Выбери картинку сам' ,reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	id = str('/' + call.data[-1:])
	img = img_list[id]
	pic_path = r'c:/sqliteBD/pics/'
	img_cert = open(pic_path + img, 'rb')
	img_send = bot.send_photo(chat_id=call.message.chat.id, photo=img_cert)
	print(img_send)
	
	
	if call.message:
		if call.data == "test1":
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь 1")
		elif call.data == "test2":
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь 2")
		elif call.data == "test3":
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь 3")
		
		
@bot.message_handler(commands=['start','Start','START'])
def start_comm(start):
	bot.send_message(start.chat.id, 'Здрасти!\n /1, /2, /3 или /pictures - для картинок\n /help - для отдыха\n И не обзывайтесь на этого бота.\n А ему - можно	')

bad_words = ["лох", "пидр", "говно", "тупой", "тварь", "пидор"]
@bot.message_handler(content_types=["text"])
def mess(message):
	if any(x in message.text.lower() for x in bad_words):
		bot.send_message(message.chat.id, 'Это не правда')
	else:
		bot.send_message(message.chat.id, 'Ты написал: \"' + message.text + '\", и ты - редиска.')

'''
def find_files(message):
	for file in os.listdir('c:\sqliteBD'):
		if file.split('.') == "jpg":
			f = open('c:\sqliteBD\ '+file, 'rb')
			res = bot.send_image(message.chat.id, f, None)
			print(res)
		time.sleep(3)
'''

if __name__ == '__main__':
	bot.polling(none_stop=True)