from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

game_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Запустить игру!', web_app=WebAppInfo(url='https://seykonag.github.io/'))
        ]
    ]
)
