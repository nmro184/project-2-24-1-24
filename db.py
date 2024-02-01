import sqlite3
from classes import Task
DB_NAME = "tasks.db"

def query(sql: str = "", data: tuple = ()):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        return cur.execute(sql, data).fetchall()

def new_task(description, date , category , username):
    data = (description , date  , category , username)
    query("INSERT INTO tasks (description, date , category , username) VALUES (?, ? ,? ,?)", data)

def get_tasks(username):
    if username == "admin":
        task_tuple_list = query("SELECT * FROM tasks ")
    else:
        task_tuple_list = query(f"SELECT * FROM tasks WHERE username ='{username}'")
    return [Task(task) for task in task_tuple_list]

def delete_task(id , username):
  if username == "admin":
      query(f"DELETE FROM tasks WHERE id = {id} ")
  data = (id,username)
  query("DELETE FROM tasks WHERE id = ? AND username = ?", data)

def update_task(new_description , new_date , new_category  , updateid , username):
    data = (new_description , new_date, new_category, updateid , username )
    query("UPDATE tasks SET description = ?, date = ?, category = ? WHERE id = ? AND username = ?" , data)