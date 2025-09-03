import os
import sys
import json
from http.server import BaseHTTPRequestHandler
from aiogram import Bot, Dispatcher, types

# Добавляем корневую папку в путь, чтобы Vercel нашел handlers.py
sys.path.insert(0, os.path.abspath('..'))
import handlers

# --- Конфигурация ---
BOT_TOKEN = os.getenv("BOT_TOKEN")

# --- Глобальные экземпляры ---
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
dp.include_router(handlers.router)

# --- Vercel Handler ---
# Это стандартный обработчик, который Vercel ищет и запускает
class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Получаем размер тела запроса
        content_len = int(self.headers.get('Content-Length'))
        # Читаем тело запроса
        post_body = self.rfile.read(content_len)
        
        # Создаем объект Update
        update_data = json.loads(post_body)
        update = types.Update(**update_data)
        
        # Запускаем обработку
        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(dp.feed_update(bot=bot, update=update))
        
        # Отправляем ответ, что все хорошо
        self.send_response(200)
        self.end_headers()
        return

    def do_GET(self):
        # Обработчик для "пульса"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Bot is alive!")
        return