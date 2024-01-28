import sqlite3
from classes import Task
DB_NAME = "tasks.db"

def query(sql: str = "", data: tuple = ()):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        return cur.execute(sql, data).fetchall()

def new_task(description, date , category):
    data = (description , date  , category)
    query("INSERT INTO tasks (description, date , category) VALUES (?, ? ,?)", data)

def get_tasks():
    task_tuple_list = query("SELECT * FROM tasks ")
    return [Task(task) for task in task_tuple_list]

def delete_task(id):
    query(f"DELETE from tasks WHERE id ={id}")

