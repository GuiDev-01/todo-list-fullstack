import sqlite3
import os 

DATABASE_PATH = 'tasks.db'

def init_database():
    """Inicializa o banco de dados e cria a tabela de tarefas"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
#Inserir dados iniciais apenas se a tabela estiver vazia
    cursor.execute('SELECT COUNT(*) FROM tasks')
    count = cursor.fetchone()[0]

    if count == 0:
        initial_tasks = [
            ('Estudar Flask', 0),
            ('Criar API REST', 0),
            ('Implementar SQLite', 0)
        ]

        cursor.executemany(
            'INSERT INTO tasks (title, completed) VALUES(?,?)',
            initial_tasks
        )

    conn.commit()
    conn.close()

def get_all_tasks():
    """Retorna todas as tarefas do banco de dados"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT id, title, completed FROM tasks')
    tasks = cursor.fetchall()

    conn.close()

    #Converter para lista de dicionários
    return [
        {
            'id': task[0],
            'title': task[1],
            'completed': bool(task[2])
        }
        for task in tasks
    ]

def create_task(title):
    """Cria uma nova tarefa no banco de dados"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO tasks (title, completed) VALUES (?, ?)',
        (title, 0)
    )
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return {
        'id': task_id,
        'title': title,
        'completed': False
    }

def update_task(task_id, title=None, completed=None):
    """Atualiza uma tarefa existente no banco de dados"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    # Verificar se a tarefa existe (buscar id, title e completed)
    cursor.execute('SELECT id, title, completed FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()

    if not task:
        conn.close()
        return None

    # Atualizar apenas os campos fornecidos
    current_title = task[1]
    current_completed = bool(task[2])

    new_title = title if title is not None else current_title
    new_completed = completed if completed is not None else current_completed

    cursor.execute(
        'UPDATE tasks SET title = ?, completed = ? WHERE id = ?',
        (new_title, int(new_completed), task_id)
    )

    conn.commit()
    conn.close()

    return {
        'id': task_id,
        'title': new_title,
        'completed': new_completed
    }

def delete_task(task_id):
    """Deleta uma tarefa do banco de dados"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    # Verificar se a tarefa existe e recuperar seus dados
    cursor.execute('SELECT id, title, completed FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()

    if not task:
        conn.close()
        return None

    # Deletar a tarefa e retornar os dados da tarefa deletada
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

    return {
        'id': task[0],
        'title': task[1],
        'completed': bool(task[2])
    }