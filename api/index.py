import os
import sys
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types

# Добавляем корневую папку в путь, чтобы найти handlers.py
sys.path.append('..')
import handlers

# --- Конфигурация ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
dp.include_router(handlers.router)

# Создаем приложение FastAPI
app = FastAPI()

# --- Маршруты ---
@app.post(f"/{BOT_TOKEN}")
async def process_webhook(request: Request):
    update_data = await request.json()
    update = types.Update(**update_data)
    await dp.feed_update(bot=bot, update=update)
    return {"status": "ok"}

@app.get("/")
def health_check():
    return {"status": "ok"}