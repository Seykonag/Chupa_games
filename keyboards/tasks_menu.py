from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import emoji

tasks = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Легкое задание')
        ],
        [
            KeyboardButton(text='Среднее задание')
        ],
        [
            KeyboardButton(text='Сложное задание')
        ],
        [
            KeyboardButton(text=emoji.emojize('⬅') + 'Назад')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Задания'
)

easy_task = 10
normal_task = 15
hard_task = 20
