from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- Главное меню: твоя воронка продаж ---
main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Какие боты я делаю (Услуги и Цены)", callback_data="services")],
    [InlineKeyboardButton(text="Примеры моих работ", callback_data="portfolio")],
    [
        InlineKeyboardButton(text="Зачем это бизнесу?", callback_data="why_bot"),
        InlineKeyboardButton(text="Обо мне", callback_data="about_me")
    ],
    [InlineKeyboardButton(text="✅ Заказать бесплатную консультацию", callback_data="contact_me")]
])

# --- Кнопка "Назад" для удобной навигации ---
back_to_main_menu_button = InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="to_main_menu")

# --- Меню для связи с тобой ---
contact_menu = InlineKeyboardMarkup(inline_keyboard=[
    # ВАЖНО: Замени "ТВОЙ_НИКНЕЙМ" на свой реальный ник в Telegram
    [InlineKeyboardButton(text="Написать мне в Telegram", url="https://t.me/@kurbannz")],
    [back_to_main_menu_button]
])