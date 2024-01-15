from aiogram import Router, F
from aiogram.types import Message

from keyboards.game_keyboard import game_start


router = Router()


@router.message(F.text.lower() == 'игра')
async def start_game(message: Message):
    await message.answer('Хотите сыграть?', reply_markup=game_start)
