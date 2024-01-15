from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import emoji

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=emoji.emojize('📄') + 'Инструкция'),
            KeyboardButton(text=emoji.emojize('📃') + 'Правила')
        ],
        [
            KeyboardButton(text=emoji.emojize('💼') + 'Задания'),
            KeyboardButton(text=emoji.emojize('🎮') + 'Игра')
        ],
        [
            KeyboardButton(text=emoji.emojize(':lollipop:') + 'Баланс')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Меню'
)
