from flask import Flask, jsonify, request
from flask_cors import CORS
from database import init_database, get_all_tasks, create_task as db_create_task, update_task as db_update_task, delete_task as db_delete_task

# Criar a aplicação Flask
app = Flask(__name__)

# Habilitar CORS para todas as rotas
CORS(app)

# Rota para listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Retorna todas as tarefas do banco de dados"""
    try:
        tasks = get_all_tasks()
        return jsonify(tasks)
    except Exception as e:
        return jsonify({'error': 'Erro ao buscar tarefas'}), 500

# Rota para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    """Cria uma nova tarefa no banco de dados"""
    try:
        data = request.get_json()
        
        if not data or not data.get('title'):
            return jsonify({'error': 'Título é obrigatório'}), 400
        
        title = data.get('title').strip()
        if not title:
            return jsonify({'error': 'Título não pode estar vazio'}), 400
        
        new_task = db_create_task(title)
        return jsonify(new_task), 201
        
    except Exception as e:
        return jsonify({'error': 'Erro ao criar tarefa'}), 500

# Rota para atualizar uma tarefa específica
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Atualiza uma tarefa existente"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
        
        title = data.get('title')
        completed = data.get('completed')
        
        # Validar título se fornecido
        if title is not None:
            title = title.strip()
            if not title:
                return jsonify({'error': 'Título não pode estar vazio'}), 400
        
        updated_task = db_update_task(task_id, title, completed)
        
        if not updated_task:
            return jsonify({'error': 'Tarefa não encontrada'}), 404
        
        return jsonify(updated_task)
        
    except Exception as e:
        return jsonify({'error': 'Erro ao atualizar tarefa'}), 500

# Rota para deletar uma tarefa específica
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Deleta uma tarefa do banco de dados"""
    try:
        deleted_task = db_delete_task(task_id)
        
        if not deleted_task:
            return jsonify({'error': 'Tarefa não encontrada'}), 404
        
        return jsonify({
            'message': 'Tarefa deletada com sucesso',
            'task': deleted_task
        })
        
    except Exception as e:
        return jsonify({'error': 'Erro ao deletar tarefa'}), 500

if __name__ == '__main__':
    # Inicializar banco de dados ao iniciar a aplicação
    print("Inicializando banco de dados...")
    init_database()
    print("Banco de dados inicializado com sucesso!")
    
    # Iniciar servidor Flask
    print("Iniciando servidor Flask...")
    app.run(debug=True, host='0.0.0.0', port=5000)