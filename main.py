from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='token')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    mess = f'Привет, {message.from_user.first_name}! Для того, чтобы посмотреть список команд напиши /help'
    await message.answer(mess)


#
# # echo
# '''
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)
# '''


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    kb = [[types.InlineKeyboardButton(text="/help")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    mess = f'Команды, которые есть в данном боте: /Github  ,  /monkey , /button '
    await message.answer(mess, reply_markup=keyboard)


@dp.message_handler(commands=['Github'])
async def website3(message: types.Message):
    kb = [[types.InlineKeyboardButton(text="/Github")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('https://github.com/nastyakurzanova', reply_markup=keyboard)


@dp.message_handler(commands=['monkey'])
async def website3(message: types.Message):
    kb = [[types.InlineKeyboardButton(text="/monkey")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D0%B5%D0%B7%D1%8C%D1%8F%D0%BD%D1%8B', reply_markup=keyboard)

@dp.message_handler(commands=['button'])
async def button(message: types.Message):
    markupu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    it1 = types.KeyboardButton('Первая обезьянка')
    it2 = types.KeyboardButton('Вторая обезьянка')
    it3 = types.KeyboardButton('Третья обезьянка')
    it4 = types.KeyboardButton('/help')
    markupu.add(it1, it2, it3, it4)
    await bot.send_message(message.chat.id, ":)", reply_markup=markupu)

@dp.message_handler(content_types=['text'])
async def send_photo(message: types.Message):
    if message.text == 'Первая обезьянка':
        photo = open('123.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo)
    if message.text == 'Вторая обезьянка':
        photo = open('1234.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo)
    if message.text == 'Третья обезьянка':
        photo = open('12345.jpeg', 'rb')
        await bot.send_photo(message.chat.id, photo)


if __name__ == '__main__':
    executor.start_polling(dp)
