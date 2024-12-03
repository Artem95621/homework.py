from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio
import crud_functions
import sqlite3

api = _
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

all_products = crud_functions.get_all_products()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
Button = KeyboardButton( text = 'Рассчитать')
Button2 = KeyboardButton( text = 'Информация')
Button3 = KeyboardButton(text='Купить')
kb.row(Button, Button2)
kb.add(Button3)

kb2 = InlineKeyboardMarkup(resize_keyboard=True)
In_Button = InlineKeyboardButton( text = 'Рассчитать норму калорий', callback_data = 'calories')
In_Button2 = InlineKeyboardButton( text = 'Формулы расчёта', callback_data = 'formulas')
In_Button3 = KeyboardButton( text= 'Назад',  callback_data = 'back_to_catalog')
kb2.add(In_Button)
kb2.add(In_Button2)
kb2.add(In_Button3)

kb3 = InlineKeyboardMarkup(resize_keyboard=True)
In_Button_buy = InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')
In_Button_buy2 = InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')
In_Button_buy3 = InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')
In_Button_buy4 = InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
kb3.row(In_Button_buy, In_Button_buy2, In_Button_buy3, In_Button_buy4)



class UserState(StatesGroup):
    age= State()
    growth= State()
    weight= State()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        await message.answer(f'Название: {number} | Описание: описание{number} | Цена: {number * 100}')
        with open(f'photo/pic{i}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb3)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')

@dp.message_handler(commands = ['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer(text='Выберите опцию', reply_markup=kb2)

@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('На текущий момент я пока только могу рассчитать необходимое количество килокалорий (ккал) '
                         'в сутки для каждого конкретного человека. \n По формулуe Миффлина-Сан Жеора, разработанной '
                         'группой американских врачей-диетологов под руководством докторов Миффлина и Сан Жеора. \n'
                         'А ещё пробую создать меню покупок продуктов для здоровья')

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('Мужчины: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n',
                              'Женщины: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()

@ dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст.')
    await call.answer()
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
