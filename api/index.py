import os
import sys
from fastapi import FastAPI, Request, Response
from aiogram import Bot, Dispatcher, types

# Добавляем корневую папку в путь, чтобы Vercel нашел handlers.py
# Это стандартный и рабочий способ
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import handlers

# --- Конфигурация ---
BOT_TOKEN = os.getenv("BOT_TOKEN")

# --- Глобальные экземпляры (создаются один раз при "холодном старте") ---
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
dp.include_router(handlers.router)
app = FastAPI()

# --- СТАТИЧНЫЙ, ПРЕДСКАЗУЕМЫЙ ПУТЬ ДЛЯ ВЕБХУКА ---
# Telegram будет всегда стучаться сюда. Без токенов в URL.
WEBHOOK_PATH = "/api/webhook"

# --- Обработчики ---
@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    """Принимает обновление от Telegram и передает его в Dispatcher"""
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)
    return Response(status_code=200)

@app.get("/")
def health_check():
    """Проверка "пульса" - говорит, что бот жив"""
    return {"status": "ok"}