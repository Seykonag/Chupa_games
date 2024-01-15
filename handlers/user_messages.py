from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.tasks_menu import *
from keyboards.main_menu import menu

from data import Models

import emoji


router = Router()


@router.message(F.text.lower() == emoji.emojize('📄') + 'инструкция')
async def instructions():
    pass


@router.message(F.text.lower() == emoji.emojize('📃') + 'правила')
async def rules():
    pass


@router.message(F.text.lower() == emoji.emojize('💼') + 'задания')
async def task(message: Message):
    await message.answer(f'Легкое задание - {easy_task}' + emoji.emojize(':lollipop:') + '\n'
                         f'Среднее задание - {normal_task}' + emoji.emojize(':lollipop:') + '\n'
                         f'Сложное задание - {hard_task}' + emoji.emojize(':lollipop:'),
                         reply_markup=tasks)


@router.message(F.text.lower() == (emoji.emojize(':lollipop:') + 'баланс'))
async def easy_task_call(message: Message):
    await message.answer(f'Ваш баланс {Models.return_value(message.from_user.id)} ' + emoji.emojize(':lollipop:'))


@router.message(F.text.lower() == emoji.emojize('⬅') + 'назад')
async def back_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Меню', reply_markup=menu)
