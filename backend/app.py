from flask import Flask, jsonify, request
from flask_cors import CORS

#Criar a aplicação Flask
app = Flask(__name__)

#Habilitar CORS para todas as rotas 
CORS(app)

#Lista temporária para armazenar as tarefas
tasks = [
{"id": 1, "title": "Estudar Flask", "completed": False},
{"id": 2, "title": "Criar API REsT", "completed": False}
]

#Variável para controlar o próximo ID
next_id = 3

#Rota para listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

#Rota para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.get_json()

    new_task = {
        "id": next_id,
        "title": data.get('title', ''),
        "completed": False
    }

    tasks.append(new_task)
    next_id += 1

    return jsonify(new_task)

#Rota para atualizar uma tarefa específica
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = None
    for t in tasks:
        if t['id'] == task_id:
            task = t
            break

    #Se não encontrar a tarefa, retornar erro
    if not task:
        return jsonify({'error': 'Tarefa não encontrada.'}), 404

    #Pegar os dados enviados
    data = request.get_json()

    #Atualizar os campos da tarefa
    if 'title' in data:
        task['title'] = data['title']
    if 'completed' in data:
        task['completed'] = data['completed']

    return jsonify(task)

#Rota para deletar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks

    #Procurar o índice da tarefa pelo ID
    task_index = None
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            task_index = i
            break

    if task_index  is None:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    
    deleted_task = tasks.pop(task_index)

    return jsonify({'message': 'Tarefa deletada com sucesso', 'task': deleted_task})


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=5000)