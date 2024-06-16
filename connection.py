import sqlite3

def connect_db():
    conn = sqlite3.connect('tasks.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                           id INTEGER PRIMARY KEY,
                           task TEXT NOT NULL,
                           completed INTEGER NOT NULL DEFAULT 0
                         )''')
    conn.commit()
    conn.close()

def add_task(task):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def update_task(task_id, completed):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (completed, task_id))
    conn.commit()
    conn.close()

def get_task():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks
