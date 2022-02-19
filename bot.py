import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
 
API_TOKEN = "1853491222:AAHfRwt4GAhrMCYdQSbrPxwgST6fiazI42I"
wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Wikipedia botiga Xush kelibsiz!")

@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bunday maqola topilmadi")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)