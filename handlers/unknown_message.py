from aiogram import Router
from aiogram.types import Message

from keyboards.main_menu import menu


router = Router()


@router.message()
async def echo(message: Message):
    await message.answer('Я не понимаю тебя', reply_markup=menu)
