import sqlite3 as sq
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
import wikipedia
import goslate
from googletrans import Translator

bot = Bot(token = "Ваш токен")
dp = Dispatcher()
gs = goslate.Goslate()
translator = Translator()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello!")

@dp.message()
async def wiki(message: types.Message):
  try:
    #Первый способ обращения к вики через библеотку goslate
    text_ru = message.text
    text_en = gs.translate(text_ru, "en")
    await message.answer("Уже ищю ответ")
    wiki_search = wikipedia.summary(text_en, sentences=2)
    await message.reply(gs.translate(wiki_search, "ru"))
  except:
    #Второй способ обращения к вики через библеотку googletrans
    #P.S если первый не сработал
    text_en = translator.translate(text_ru, dest='en')
    await message.answer("Уже ищю ответ")
    wiki_search = wikipedia.summary(text_en, sentences=2)
    await message.reply(translator.translate(wiki_search, dest='ru'))


async def main():
    await dp.start_polling(bot)
asyncio.run(main())