import telebot
import random


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

    tasks = {question: answer for question, answer in zip(questions, answers)}
    return tasks


def get_random_task(tasks_with_answers):
    task = random.choice(list(tasks_with_answers))
    answ = tasks_with_answers[task]
    return task, answ


russian_tasks = get_tasks_dict("Russian.txt")
biology_tasks = get_tasks_dict("Biology.txt")
chemistry_tasks = get_tasks_dict("Chemistry.txt")


class Bot:
    bot = telebot.TeleBot("5855113265:AAHR19MCB9qnlKQRnpRImGpvwxO4WrzOi2o")
    SUBJECTS = ('Химия', 'Русский', 'Биология')

    def __init__(self):
        self.subjects = ('Химия', 'Русский', 'Биология')
        self.task = ''
        self.answer = ''

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Чем будем кормить Поспелика?")

    @bot.message_handler(func=lambda message: True)
    def get_task(self, message):
        text_message = message.text
        if text_message in self.subjects:
            if text_message == 'Химия':
                self.task, self.answer = get_random_task(chemistry_tasks)
            elif text_message == 'Русский':
                self.task, self.answer = get_random_task(russian_tasks)
            elif text_message == 'Биология':
                self.task, self.answer = get_random_task(biology_tasks)
            bot.register_next_step_handler(message, self.check_answer)

    def check_answer(self, message):
        if self.answer == message:
            bot.reply_to(message, "Правильно")
        else:
            bot.reply_to(message, "Неправильно")

    def run_bot(self):
        self.bot.infinity_polling()


if __name__ == "__main__":
    bot = Bot()
    bot.run_bot()
