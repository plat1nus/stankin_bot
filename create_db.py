import sqlite3

conn = sqlite3.connect("AllTasks.db")
cursor = conn.cursor()

def get_tasks_dict(src, name):
    with open(src, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.split('---')
    questions = []
    answers = []
    for task in text:
        try:
            q, a = task.split('///')
            cursor.execute("INSERT OR IGNORE INTO `{}` (`Task`, `Answer`) VALUES (?, ?)".format(name), (q, a))
        except ValueError:
            pass
    
    pass

sub_name = ""
get_tasks_dict("{}.txt".format(sub_name), "{}".format(sub_name))
conn.commit()
