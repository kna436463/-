import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- Главное меню ---
main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Какие боты я делаю (Услуги и Цены)", callback_data="services")],
    [InlineKeyboardButton(text="Примеры моих работ", callback_data="portfolio")],
    [
        InlineKeyboardButton(text="Зачем это бизнесу?", callback_data="why_bot"),
        InlineKeyboardButton(text="Обо мне", callback_data="about_me")
    ],
    [InlineKeyboardButton(text="✅ Заказать бесплатную консультацию", callback_data="contact_me")]
])

# --- Кнопка "Назад" ---
back_to_main_menu_button = InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="to_main_menu")

# --- Меню для связи с тобой (УЛУЧШЕННАЯ ВЕРСИЯ) ---
# 1. Получаем имя пользователя из переменной окружения.
#    Если переменная не найдена, используется 'kurbannz' как запасной вариант.
# --- Меню для связи с тобой (ФИНАЛЬНАЯ ВЕРСИЯ) ---
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "kurbannz")

# Используем прямую ссылку tg://resolve, которая гарантированно открывает чат
contact_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Написать мне в Telegram", url=f"tg://resolve?domain={ADMIN_USERNAME}")],
    [back_to_main_menu_button]
])