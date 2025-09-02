from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup

import keyboards as kb

router = Router()

# --- Приветствие ---
# Это первое, что видит клиент. Текст должен быть идеальным.
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Здравствуйте! 👋\n\n"
        "Я — ваш личный бот-помощник, созданный для демонстрации моих услуг по разработке Telegram-ботов.\n\n"
        "Я помогаю бизнесу экономить время и зарабатывать больше с помощью автоматизации. "
        "Посмотрите, как это работает, и представьте такого помощника у себя.",
        reply_markup=kb.main_menu
    )

# --- Логика для всех кнопок ---

# Кнопка "Назад"
@router.callback_query(F.data == "to_main_menu")
async def back_to_main_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Вы вернулись в главное меню. Чем еще могу помочь?",
        reply_markup=kb.main_menu
    )
    await callback.answer()

# Кнопка "Какие боты я делаю (Услуги и Цены)"
@router.callback_query(F.data == "services")
async def services_and_prices(callback: types.CallbackQuery):
    text = (
        "<b>⭐ Мои услуги по разработке ботов:</b>\n\n"
        "<b>1. «Бот-Визитка» — от 5 000 ₽</b>\n"
        "<i>Современный способ рассказать о себе. Включает меню, контакты, описание услуг.</i>\n\n"
        "<b>2. «Бот для Записи Клиентов» — от 15 000 ₽</b>\n"
        "<i>Автоматически собирает заявки 24/7 и присылает их вам. Экономит время и деньги. Хит продаж!</i>\n\n"
        "<b>3. «Бот по вашему сценарию» — от 40 000 ₽</b>\n"
        "<i>Интеграция с таблицами, прием оплаты, рассылки — реализую любую вашу идею.</i>\n\n"
        "<b>🔧 Техподдержка — от 2 000 ₽/мес.</b>\n"
        "<i>Полное спокойствие за работоспособность вашего бота.</i>"
    )
    # Создаем клавиатуру с кнопкой "Назад" прямо здесь
    back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[kb.back_to_main_menu_button]])
    await callback.message.edit_text(text, reply_markup=back_keyboard, parse_mode="HTML")
    await callback.answer()

# Кнопка "Примеры моих работ"
@router.callback_query(F.data == "portfolio")
async def portfolio(callback: types.CallbackQuery):
    await callback.answer(
        "Этот бот — и есть главный пример моей работы!\n\n"
        "Также скоро я добавлю сюда ссылки на ботов, которых сделал для своих клиентов.",
        show_alert=True # Всплывающее уведомление
    )

# Кнопка "Зачем это бизнесу?"
@router.callback_query(F.data == "why_bot")
async def why_bot(callback: types.CallbackQuery):
    text = (
        "<b>🤔 Какую пользу приносит бот?</b>\n\n"
        "<b>1. ЭКОНОМИТ ВРЕМЯ:</b> Бот сам отвечает на типовые вопросы и записывает на услуги.\n"
        "<b>2. ПРИНОСИТ ДЕНЬГИ:</b> Работает 24/7 и не упустит клиента, который написал поздно вечером.\n"
        "<b>3. УЛУЧШАЕТ СЕРВИС:</b> Клиенты получают мгновенный ответ, что повышает их лояльность.\n"
        "<b>4. АВТОМАТИЗИРУЕТ РУТИНУ:</b> Бот не устает, не ошибается и не просит зарплату."
    )
    back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[kb.back_to_main_menu_button]])
    await callback.message.edit_text(text, reply_markup=back_keyboard, parse_mode="HTML")
    await callback.answer()

# Кнопка "Обо мне"
@router.callback_query(F.data == "about_me")
async def about_me(callback: types.CallbackQuery):
    # Замени [Твое Имя] на свое
    text = "Меня зовут Курбан, я занимаюсь созданием полезных Telegram-ботов для бизнеса. Моя цель — не просто написать код, а создать инструмент, который реально помогает. Свяжитесь со мной, и мы обсудим задачи именно вашего бизнеса."
    back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[kb.back_to_main_menu_button]])
    await callback.message.edit_text(text, reply_markup=back_keyboard)
    await callback.answer()

# Кнопка "Заказать бесплатную консультацию"
@router.callback_query(F.data == "contact_me")
async def contact_me(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Отличный выбор! Чтобы получить бесплатную консультацию и обсудить вашего будущего бота, просто нажмите на кнопку ниже и напишите мне.",
        reply_markup=kb.contact_menu
    )
    await callback.answer()