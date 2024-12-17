import logging
from aiogram import Bot, Dispatcher, types
import aiohttp
import asyncio
from aiogram.filters import Command, CommandStart

API_TOKEN = '7948855425:AAEDGa6c_xYt2dOJ-2NsuyCpVv6yZczM2to'
WEATHER_API_KEY = 'd78a34abf4271ad4d860ebf2ee05edef'
CITY = 'Samara'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher.from_types(Bot, types.Message)

async def get_weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric&lang=ru'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

    if data.get('cod') != 200:
        return "Не удалось получить данные о погоде."

    main_data = data.get('main')
    weather_data = data.get('weather')[0]

    temperature = main_data.get('temp')
    description = weather_data.get('description')

    weather_info = f"Температура: {temperature}°C\nОписание: {description.capitalize()}"
    return weather_info

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который может показать погоду в Самаре. Напиши /weather, чтобы узнать текущую погоду.")

@dp.message(Command('help'))
async def send_help(message: types.Message):
    help_text = """
    Доступные команды:
    /start - Приветственное сообщение
    /help - Список доступных команд
    /weather - Получить актуальную погоду в Самаре
    """
    await message.reply(help_text)

@dp.message(Command('weather'))
async def weather_command(message: types.Message):
    weather_info = await get_weather()
    await message.reply(weather_info)

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
