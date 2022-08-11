from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = '5556469727:AAEHDNUTlfW7wqaFEu5X2Qn0Yj5psSYHmro'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def answer_start_command(message: types.Message):
    await message.answer(text='Введи что-нибудь из этого:\
                                        \nПриветсвия: Привет, Начать, Здаров\
                                        \nАссортимент: Что у тебя есть?, Что в наличии?, Че там?\
                                        \nЦены: Напиши также как и Бот интересующий товар')

@dp.message_handler(commands=['start'])
@dp.message_handler(text=['Привет', 'Начать', 'Здаров'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'{message.from_user.first_name} Здарова Брат! \nСамый лучший фруты с юга! \n(/help если не значешь, что спросить)')


@dp.message_handler(text=['Что у тебя есть?', 'Что в наличии?', 'Че там?'])
async def answer_start_text(message: types.Message):
    await message.answer(text='Арбузы, Абрикосы, Черешня, Клубника \nЧто интересует?')

@dp.message_handler(text=['Арбузы'])
async def answer_start_text(message: types.Message):
    await message.answer(text='Узбекские - 40р за кг \nДагестанские 60р за кг \nБери дагестанский, за качество атвичаю')

@dp.message_handler(text=['Абрикосы'])
async def answer_start_text(message: types.Message):
    await message.answer(text='230р за килогрммчик Брат')

@dp.message_handler(text=['Черешня'])
async def answer_start_text(message: types.Message):
    await message.answer(text='400 рубликой, но тебе за 350 отдам))')

@dp.message_handler(text=['Клубника'])
async def answer_start_text(message: types.Message):
    await message.answer(text='Клубника оч вкусная Брат, цена не так важна \nВсего 410 рублей')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)


    # print(message['from']['first_name'])
    # print(message.from_user.first_name)