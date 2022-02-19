from aiogram import types
import wikipedia
from loader import dp

wikipedia.set_lang('uz')

@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bunday maqola topilmadi")