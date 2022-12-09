import random
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

API_TOKEN = '5855113265:AAHR19MCB9qnlKQRnpRImGpvwxO4WrzOi2o'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def get_tasks_dict(src):
    with open(src, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.split('---')
    questions = []
    answers = []
    for task in text:
        try:
            q, a = task.split('///')
            questions.append(q)
            answers.append(a)
        except ValueError:
            pass

    tasks = {question:answer for question, answer in zip(questions, answers)}
    return tasks


def get_random_task(tasks_with_answers):
    task = random.choice(list(tasks_with_answers))
    answ = tasks_with_answers[task]
    return task, answ

russian_tasks = get_tasks_dict("Russian.txt")
biology_tasks = get_tasks_dict("Biology.txt")
chemistry_tasks = get_tasks_dict("Chemistry.txt")


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Химия", "Русский", "Биология"]
    keyboard.add(*buttons)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Химия"))
async def chemistry(message: types.Message):
    await message.reply(task)
    
@dp.message_handler(Text(equals="Русский"))
async def russian(message: types.Message):
    task, answ = get_random_task(russian_tasks)
    last_message = task
    await message.reply(task)


@dp.message_handler(Text(equals="Биология"))
async def biology(message: types.Message):
    task, answ = get_random_task(biology_tasks)
    last_message = task

    await message.reply(task)

@dp.message_handler()
async def get_message(message: types.Message):
    # try:
    #     if message.text == answ:
    #         await message.reply("+1")
    #     else:
    #         await message.reply("-1")
    # except NameError:
    #     print('error with name')
    print(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)