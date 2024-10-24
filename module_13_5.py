from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api =_________________________________
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
Button = KeyboardButton( text = 'Рассчитать')
Button2 = KeyboardButton( text = 'Информация')
kb.add(Button)
kb.add(Button2)

class UserState(StatesGroup):
    age= State()
    growth= State()
    weight= State()

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)


@dp.message_handler(text= 'Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст.')
    await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    date = await state.get_data()
    await message.answer('Введите свой рост.')
    await UserState.growth.set()

@dp.message_handler(state= UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    date = await state.get_data()
    await message.answer('Введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight= message.text)
    date = await state.get_data()
    result = (int(date['weight']) * 10) + (6.25 * int(date['growth'])) - (int(date['age']) + 5)
    await message.answer('Ваша норма калорий: %s' % (result))
    await State.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)