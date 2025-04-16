from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from states import StudentForm, AdminForm
from handlers import cmd_start, cmd_admin_login, process_admin_login, cmd_register_student, process_student_registration, process_student_registration_number, process_student_registration_code, cmd_view_registered_students, cmd_edit_admin_info, process_admin_username, process_admin_password, cmd_search_students, process_search_students, cmd_filter_students, process_filter_students

API_TOKEN = 'YOUR_BOT_API_TOKEN'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.middleware.setup(LoggingMiddleware())

dp.register_message_handler(cmd_start, commands=['start'])
dp.register_message_handler(cmd_admin_login, commands=['login'])
dp.register_message_handler(process_admin_login, state=AdminForm.login)
dp.register_message_handler(cmd_register_student, commands=['register'])
dp.register_message_handler(process_student_registration, state=StudentForm.name)
dp.register_message_handler(process_student_registration_number, state=StudentForm.number)
dp.register_message_handler(process_student_registration_code, state=StudentForm.code)
dp.register_message_handler(cmd_view_registered_students, commands=['view_students'])
dp.register_message_handler(cmd_edit_admin_info, commands=['edit_admin'])
dp.register_message_handler(process_admin_username, state=AdminForm.username)
dp.register_message_handler(process_admin_password, state=AdminForm.password)
dp.register_message_handler(cmd_search_students, commands=['search_students'])
dp.register_message_handler(process_search_students, state=AdminForm.search)
dp.register_message_handler(cmd_filter_students, commands=['filter_students'])
dp.register_message_handler(process_filter_students, state=AdminForm.filter)

if __name__ == '__main__':
    from handlers import cmd_start
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
