from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import emoji

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=emoji.emojize('⬅') + 'Назад')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Назад'
)
