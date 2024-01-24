from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from data.Models import create_profile, return_value, check_user
from keyboards.main_menu import menu

import emoji


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'{message.from_user.first_name},'
                         f' добро пожаловать в игру "Chupa games"',
                         reply_markup=menu)

    await create_profile(user_id=message.from_user.id)

    if not check_user(message.from_user.id):
        await message.answer("Вы получили бонус за регистрацию!")
        await message.answer(f'Ваш баланс {return_value(message.from_user.id)} ' + emoji.emojize(':lollipop:'))
