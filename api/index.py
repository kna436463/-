import os
import logging
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiohttp import web

sys.path.append('..')
import handlers

# --- Конфигурация ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
app = web.Application()

# --- Главный обработчик вебхука ---
async def handle_webhook(request):
    try:
        update = types.Update(**(await request.json()))
        dp = Dispatcher()
        dp.include_router(handlers.router)
        bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
        await dp.feed_update(bot=bot, update=update)
        return web.Response(status=200)
    except Exception as e:
        logging.exception("Error processing update")
        return web.Response(status=500)

# --- Обработчик для проверки "пульса" ---
async def health_check(request):
    return web.Response(text="I am alive")

# --- Регистрация маршрутов ---
app.router.add_post(f"/{BOT_TOKEN}", handle_webhook) # Telegram будет стучаться сюда
app.router.add_get("/", health_check) # Мы будем проверять "пульс" здесь