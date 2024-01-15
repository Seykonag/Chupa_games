from aiogram.utils.keyboard import ReplyKeyboardBuilder

import emoji

items = [
    ['87', '99', '60', '68'],
    ['7', '4', '6', '5'],
    ['Дочерей', 'Сыновей', 'Поровну', 'Никого'],
    ['8', '9', '7', '10'],
    ['1', '4', '3', '2'],
]


def hard_task_keyboard(num):
    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items[num]]
    builder.button(text=emoji.emojize('⬅') + 'Назад')
    builder.adjust(4, 1)

    return builder.as_markup(resize_keyboard=True)
