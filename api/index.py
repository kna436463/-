import os
import logging
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiohttp import web

# Это НЕ загрузит .env на Vercel, но нужно для локального теста, если понадобится
from dotenv import load_dotenv
load_dotenv()

# Добавляем корневую папку в путь
sys.path.append('..')
import handlers

# --- ИСПРАВЛЕННАЯ КОНФИГУРАЦИЯ ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
VERCEL_URL = os.getenv('VERCEL_URL')
# Путь теперь простой и правильный
WEBHOOK_PATH = "/api/index"
WEBHOOK_URL = f"https://{VERCEL_URL}{WEBHOOK_PATH}"

# --- Инициализация ---
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
dp.include_router(handlers.router)

# --- Главный обработчик ---
async def handle_webhook(request):
    try:
        update = types.Update(**(await request.json()))
        await dp.feed_update(bot=bot, update=update)
        return web.Response(status=200)
    except Exception as e:
        logging.exception("Error processing update")
        return web.Response(status=500)

# --- Создание приложения ---
app = web.Application()
app.router.add_post(WEBHOOK_PATH, handle_webhook)