import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties # ИЗМЕНЕНИЕ 1: Добавили импорт

import handlers

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    logging.basicConfig(level=logging.INFO)
    
    # ИЗМЕНЕНИЕ 2: Поменяли способ указания parse_mode
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    
    dp = Dispatcher()
    dp.include_router(handlers.router)
    
    print("Бот для саморекламы успешно запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())