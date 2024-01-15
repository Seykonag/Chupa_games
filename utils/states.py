from aiogram.fsm.state import StatesGroup, State


class TaskClass(StatesGroup):
    answer = State()
