import random

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from data import Models
from data.subloader import get_json
from keyboards.back_button import back
from keyboards.builders import hard_task_keyboard
from keyboards.main_menu import menu
from keyboards.tasks_menu import *
from utils.states import TaskClass

router = Router()


@router.message(F.text.lower() == 'легкое задание')
async def easy_task_call(message: Message, state: FSMContext):
    #Выбор рандомной загадки из json
    global easy_task_list, rand_easy_task, status
    status = 'easy'
    easy_task_list = await get_json('easy_tasks_direct_list')
    rand_easy_task = random.choice(list(easy_task_list))
    #Вывод рандомной загадки
    await message.answer(rand_easy_task)
    await message.answer('Ваш ответ:', reply_markup=back)
    await state.set_state(TaskClass.answer)


@router.message(F.text.lower() == 'среднее задание')
async def normal_task_call(message: Message, state: FSMContext):
    #Выбор рандомной загадки из json
    global normal_task_list, rand_normal_task, status
    status = 'normal'
    normal_task_list = await get_json('normal_tasks_direct_list')
    rand_normal_task = random.choice(list(normal_task_list))
    #Вывод рандомной загадки
    await message.answer(rand_normal_task)
    await message.answer('Ваш ответ:', reply_markup=back)
    await state.set_state(TaskClass.answer)


@router.message(F.text.lower() == 'сложное задание')
async def hard_task_call(message: Message, state: FSMContext):
    #Выбор рандомной загадки из json
    global hard_task_list, rand_hard_task, status
    status = 'hard'
    hard_task_list = await get_json('hard_tasks_direct_list')
    hard_task_list_ebal_vas_v_rot = list(hard_task_list)
    rand_hard_task = random.choice(hard_task_list_ebal_vas_v_rot)
    index = hard_task_list_ebal_vas_v_rot.index(rand_hard_task)
    photo = FSInputFile('data/' + rand_hard_task)
    #Вывод рандомной загадки
    await message.answer_photo(photo=photo, caption='Сложная задача')
    await message.answer('Ваш ответ:', reply_markup=hard_task_keyboard(index))
    await state.set_state(TaskClass.answer)


#Функция сравнения ответа
@router.message(TaskClass.answer)
async def compare_answer_normal(message: Message, state: FSMContext):
    #Проверка на сложность загадки
    if status == 'easy':
        await state.update_data(answer=message.text)

        if message.text.lower() == easy_task_list.get(rand_easy_task):
            await Models.edit_profile(message.from_user.id, easy_task)
            await message.answer(f'Вы отгадали, ваш баланс теперь '
                                 f'{Models.return_value(message.from_user.id)} '
                                 + emoji.emojize(':lollipop:'),
                                 reply_markup=menu)
        else:
            await message.answer('Не правильный ответ!')
            await message.answer('Ваш ответ:')
    # Проверка на сложность
    elif status == 'normal':
        await state.update_data(answer=message.text)

        if message.text.lower() == normal_task_list.get(rand_normal_task):
            await Models.edit_profile(message.from_user.id, normal_task)
            await message.answer(f'Вы отгадали, ваш баланс теперь '
                                 f'{Models.return_value(message.from_user.id)} '
                                 + emoji.emojize(':lollipop:'),
                                 reply_markup=menu)
        else:
            await message.answer('Не правильный ответ!')
            await message.answer('Ваш ответ:')
    else:
        await state.update_data(answer=message.text)

        if message.text.lower() == hard_task_list.get(rand_hard_task):
            await Models.edit_profile(message.from_user.id, hard_task)
            await message.answer(f'Вы отгадали, ваш баланс теперь '
                                 f'{Models.return_value(message.from_user.id)} '
                                 + emoji.emojize(':lollipop:'),
                                 reply_markup=menu)
        else:
            await message.answer('Не правильный ответ!')
            await message.answer('Ваш ответ:')
