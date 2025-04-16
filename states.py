from aiogram.dispatcher.filters.state import State, StatesGroup

class StudentForm(StatesGroup):
    name = State()
    number = State()
    code = State()

class AdminForm(StatesGroup):
    login = State()
    username = State()
    password = State()
    search = State()
    filter = State()
