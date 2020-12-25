import logging
from aiogram.utils import callback_data
from config import *
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery
from telebot import types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api_token)
dp = Dispatcher(bot)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Купить подписку"),
            KeyboardButton("Инструкции")
        ],
        [
            KeyboardButton("Партнерская программа"),
            KeyboardButton("Преимущества платной подписки")
        ],
        [
            KeyboardButton("Обучение"),
            KeyboardButton("Инвест-идеи")
        ],
        [
            KeyboardButton("Контакты📲"),
            KeyboardButton("Профиль👤")
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)


@dp.message_handler(commands=["start"])
async def welcome(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name} {message.from_user.last_name}! \n \n<b>Добро пожаловать в БОТ канала "Принципы Баффета"!</b> 🤝 \n \nЯ создан, для того, чтобы сделать максимально удобными следующие процессы: \n \n✅ прием всех видов оплат за подписку на канал \n✅ автоматическое добавление на VIP канал (для подписчиков #silver) \n✅ автоматическое добавление в закрытый чат, а также в библиотеку (пакет #gold). \n\nЗа пару дней до окончания подписки я напомню о себе для вашего удобства 😉\n\n<i>"Самая важная инвестиция — это инвестиция в себя." Уоррен Баффетт</i>.\n\n<b>Переход на основной канал тут</b> 👉\nhttps://t.me/buffetsignals', reply_markup=menu, parse_mode='html')


@dp.message_handler(content_types=['text'])
async def buy_sub(message: Message):
    if message.chat.type == 'private':
        if message.text == 'Купить подписку':
            buy_1 = InlineKeyboardMarkup(row_width=1)
            but_1 = InlineKeyboardButton('Ввести промокод', callback_data='promo')
            but_2 = InlineKeyboardButton('⚪️ SILVER 1 мес - 1900👌', callback_data='silver')
            but_3 = InlineKeyboardButton('🟡 GOLD 1 мес - 2900👌', callback_data='gold')
            but_4 = InlineKeyboardButton('⚪️ SILVER (3M - 5100 👍 скидка 10%)', callback_data='silver_1')
            but_5 = InlineKeyboardButton('🟡 GOLD (3M - 7800 👍 скидка 10%)', callback_data='gold_1')
            but_6 = InlineKeyboardButton('⚪️ SILVER ➡️ 🟡 GOLD: 1000 доплата', callback_data='silver_2')
            but_7 = InlineKeyboardButton('🎁 GOLD ДЕМО на 24 часа', callback_data='gold_demo')
            but_8 = InlineKeyboardButton('📚 БИБЛИОТЕКА 490 рублей (30 дней)', callback_data='lib_m')
            but_9 = InlineKeyboardButton('📚 БИБЛИОТЕКА 3490 рублей на год 🔥', callback_data='lib_y')
            buy_1.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9)
            await message.answer("Выберите тариф:", reply_markup=buy_1)
        elif message.text == 'Инструкции':
            await message.answer('<b>F.A.Q</b>\n1. Нажмите "Купить подписку".\n\n2. Выберите подходящий для Вас пакет (#silver или #gold) и кликните по нему.\n\nПодробнее:\nhttps://telegra.ph/Kak-podpisatsya-na-kanal-09-25', parse_mode='HTML')
        elif message.text == 'Партнерская программа':
            ref = InlineKeyboardMarkup(row_width=1)
            ref_1 = InlineKeyboardButton('Вывести руб.', callback_data='rub')
            ref_2 = InlineKeyboardButton('Моя команда', callback_data='team')
            ref.add(ref_1,ref_2)
            await message.answer('Реферальная ссылка:\n\nЭто ваша персональная ссылка по которой вы можете приглашать новых пользователей в наш проект и получать с каждого реферала % от оплаченных тарифов с 2 уровней партнерской программы: \n\nhttp://t.me/Buffett_Pay_BOT?start=362763546\n\nЗаработано за все время: 0 руб.\nЗаработано комиссионных: 0 руб.\nЗаработано бонусов: 0 руб.\nВыведено из системы: 0 руб.\nДоступно к выводу: 0 руб.\n\nМинимальная сумма на вывод: 1000 руб.\n\nПо уровням: \n1 - 0 👤\n2 - 0 👤', reply_markup=ref)
        elif message.text == 'Преимущества платной подписки':
            await message.answer("<b>В чем разница между тарифами SILVER и GOLD?</b>\n\nhttps://telegra.ph/Opisanie-tarifov-Gold-i-Silver-09-25\n\n <b>Как купить подписку?</b>\n\nhttps://telegra.ph/Kak-podpisatsya-na-kanal-09-25\n\n<b>Как работать с сигналами?</b>\n\nhttps://telegra.ph/Kak-rabotat-s-signalami-10-01\n\n<b>Сколько я зарабатываю на трейдинге (подробные отчеты)</b>\n\nhttps://telegra.ph/Skolko-ya-zarabatyvayu-10-09\n\n<b>Подробнее о нашей библиотеке трейдера для подписчиков Gold</b>\n\nhttps://telegra.ph/Opisanie-biblioteki-trejdera-paket-Gold-09-25", parse_mode='HTML')
        elif message.text == 'Профиль👤':
            await message.answer(f"{message.from_user.first_name} {message.from_user.last_name}, здесь вы можете увидеть свои активные подписки:\n\n-")


@dp.callback_query_handler(text='rub')
async def rub(call: CallbackQuery):
    await call.answer("ОШИБКА: На вашем балансе недостаточно средств для вывода.")


@dp.callback_query_handler(text="promo")
async def promo_write(call: CallbackQuery):
    await call.message.answer("Напишите промокод:")


@dp.callback_query_handler(text="silver")
@dp.callback_query_handler(text="gold")
@dp.callback_query_handler(text="silver_1")
@dp.callback_query_handler(text="gold_1")
@dp.callback_query_handler(text="silver_2")
@dp.callback_query_handler(text="gold_demo")
@dp.callback_query_handler(text="lib_m")
@dp.callback_query_handler(text="lib_y")
async def buy_under_sub(call: CallbackQuery):
    await call.message.answer("Введите, пожалуйста, Email (если вы будете пользоваться библиотекой, то лучше указать почту на gmail.com): \n\nПосле ввода email нажмите на кнопку с нужным пакетом и бот сразу предложит варианты оплаты.")


@dp.message_handler()
async def not_command(message: Message):
    await message.answer('Нет такой команды!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
