import os
import logging
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiohttp import web
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Добавляем корневую папку в путь, чтобы Vercel мог найти handlers.py
# Это нужно, потому что Vercel запускает этот файл из папки /api
sys.path.append('..')
import handlers

# --- Конфигурация ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Vercel автоматически предоставит эту переменную
VERCEL_URL = os.getenv('VERCEL_URL')
WEBHOOK_PATH = f'/api/{BOT_TOKEN}' # Путь должен совпадать с путем к файлу
WEBHOOK_URL = f"https://{VERCEL_URL}{WEBHOOK_PATH}"

# --- Инициализация ---
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
dp.include_router(handlers.router)

# --- Функции жизненного цикла ---
async def on_startup(app):
    logging.warning(f"Setting webhook on: {WEBHOOK_URL}")
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(app):
    logging.warning("Deleting webhook")
    await bot.delete_webhook()

# --- Главный обработчик, которого ждет Vercel ---
async def handle_webhook(request):
    try:
        update_data = await request.json()
        update = types.Update(**update_data)
        await dp.feed_update(bot=bot, update=update)
        return web.Response(status=200)
    except Exception as e:
        logging.error(f"Error handling update: {e}")
        return web.Response(status=500)

# --- Создание веб-приложения, которое Vercel будет запускать ---
app = web.Application()
app.router.add_post(f'/{BOT_TOKEN}', handle_webhook) # Конечная точка для Telegram

# Vercel не поддерживает on_startup/on_shutdown, поэтому мы их не используем
# Установка и удаление вебхука будет производиться вручную