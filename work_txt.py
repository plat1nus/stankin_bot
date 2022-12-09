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

    tasks = {question:answer for question, answer in zip(questions, answers)}
    return tasks

russian_tasks = get_tasks_dict("Russian.txt")
biology_tasks = get_tasks_dict("Biology.txt")
chemistry_tasks = get_tasks_dict("Chemistry.txt")

task = random.choice(list(russian_tasks))

answ = russian_tasks[task]

print(task, answ, sep='\n')