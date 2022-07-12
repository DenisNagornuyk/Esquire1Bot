from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from gtts import gTTS
from aiogram import *
import os
# https://t.me/Esquire1Bot
API_TOKEN = '5324328907:AAHFTr15nAQMwAJP9dWpjz5LkDWJNYEro3Q'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)








# @dp.message_handler(commands='voiceUA')
# async def ua(message: types.Message):
# 	await bot.send_message(message.chat.id, 'що хочете озвучити?')#, reply_markup=markup)
# @dp.message_handler()
# async def mesUA(message: types.Message):
# 	t = gTTS(text=message.text, lang='uk', slow=False)
# 	t.save(f"{message.text}.mp3")
# 	await bot.send_audio(message.chat.id, open(f'{message.text}.mp3', 'rb'))
# 	os.remove(f"{message.text}.mp3")



@dp.message_handler(commands='voiceRU')
async def ruu(message: types.Message):
	await bot.send_message(message.chat.id, 'что хотите озвучить?')#, reply_markup=markup)
@dp.message_handler()
async def ryski(message: types.Message):
	t = gTTS(text=message.text, lang='ru', slow=False)
	t.save(f"{message.text}.mp3")
	await bot.send_audio(message.chat.id, open(f'{message.text}.mp3', 'rb'))
	os.remove(f"{message.text}.mp3")



# @dp.message_handler(commands='voiceEnglish')
# async def enn(message: types.Message):
# 	await bot.send_message(message.chat.id, 'what do you want to say?')#, reply_markup=markup)
# @dp.message_handler()
# async def engli(message: types.Message):
# 	t = gTTS(text=message.text, lang='en', slow=False)
# 	t.save(f"{message.text}.mp3")
# 	await bot.send_audio(message.chat.id, open(f'{message.text}.mp3', 'rb'))
# 	os.remove(f"{message.text}.mp3")











# kb1 = InlineKeyboardButton(text='Українській', callback_data='ukk')
# kb2 = InlineKeyboardButton(text='Русский'    , callback_data='ruu')
# kb3 = InlineKeyboardButton(text='English'    , callback_data='enn')
# delete = InlineKeyboardButton('Видалити|Удалить|Delete'      , callback_data='message_delete')
# markup = InlineKeyboardMarkup().add(kb1, kb2, kb3).insert(delete)

#Реагируем на команду /start, при этом выводим сообщение с инлайн кнопкой
# @dp.message_handler(commands='voice')
# async def del_mes(message: types.Message):
#     await bot.send_message(message.chat.id, 'что хотите озвучить?')#, reply_markup=markup)

# #Если нажимаем на кнопку - удаляется сообщение.
# @dp.callback_query_handler(lambda c: c.data == 'message_delete')
# async def send_msg_to_user(call: types.CallbackQuery):
#     await call.answer('Удалено')
#     await bot.delete_message(call.message.chat.id, call.message.message_id)


#UK
# @dp.callback_query_handler(lambda c: c.data == 'ukk')
# async def send_uk(call: types.CallbackQuery):
# 	await call.answer('Українська')# повідомлення на єкран
# 	if call.data == 'ukk':
# 		await bot.send_message(call.message.chat.id, 'Напишіть ваш текст для Озвучення')
# @dp.message_handler()
# async def mesuk(message: types.Message):
# 	t = gTTS(text=message.text, lang='uk', slow=False)
# 	t.save(f"{message.text}.mp3")
# 	await bot.send_audio(message.chat.id, open(f'{message.text}.mp3', 'rb'))
# 	os.remove(f"{message.text}.mp3")


#RU
# @dp.callback_query_handler(lambda c: c.data == 'ruu')
# async def send_ru(call: types.CallbackQuery):
	# await call.answer('Русский')# повідомлення на єкран
	# if call.data == 'ruu':
	# 	await bot.send_message(call.message.chat.id, 'Напишите ваш текст для Озвучивания')
# @dp.message_handler()
# async def mesru(message: types.Message):
# 	t = gTTS(text=message.text, lang='ru', slow=False)
# 	t.save(f"{message.text}.mp3")
# 	await bot.send_audio(message.chat.id, open(f'{message.text}.mp3', 'rb'))
# 	os.remove(f"{message.text}.mp3")


#EN

# @dp.callback_query_handler(lambda c: c.data == 'enn')
# async def send_en(call: types.CallbackQuery):
# 	await call.answer('English')# повідомлення на єкран
# 	if call.data == 'enn':
# 		await bot.send_message(call.message.chat.id, 'Write your text for Voiceover')
# @dp.message_handler()
# async def mesen(message: types.Message):
# 	t = gTTS(text=message.text, lang='en', slow=False)
# 	t.save(f"{message.text}.mp3")
# 	await bot.send_audio(message.chat.id, open(f'{message.text}.mp3', 'rb'))
# 	os.remove(f"{message.text}.mp3")

	print("id: ", message.from_user.id, 
		  "\nName: ", message.from_user.full_name, 
		  "\nmessage: ", message.text)

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
