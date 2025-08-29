# � Full-Stack To-Do List Application

> **🚧 Status: Em Desenvolvimento** | **Fase Atual: Backend API Completa**

Um aplicativo completo de lista de tarefas desenvolvido como projeto de aprendizado, demonstrando habilidades em desenvolvimento full-stack com Python/Flask no backend e React Native no frontend.

## 🚀 Sobre o Projeto

Este projeto implementa uma aplicação completa de gerenciamento de tarefas com arquitetura full-stack:

- **Backend:** API REST em Python com Flask (✅ Completo)
- **Frontend:** Aplicativo mobile em React Native (🚧 Em desenvolvimento)
- **Banco de Dados:** SQLite (📋 Próxima fase)

### ✨ Funcionalidades

- ✅ **Listar todas as tarefas** - `GET /tasks`
- ✅ **Criar nova tarefa** - `POST /tasks`
- ✅ **Atualizar tarefa** - `PUT /tasks/<id>`
- ✅ **Deletar tarefa** - `DELETE /tasks/<id>`
- ✅ **Tratamento de erros** (404 para tarefas não encontradas)
- ✅ **CORS habilitado** para integração com frontend

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Flask** - Framework web minimalista
- **Flask-CORS** - Habilitação de CORS
- **JSON** - Formato de dados da API

## 📋 Estrutura do Projeto

```
Projeto_TODO_LIST/
├── backend/
│   ├── app.py              # Aplicação principal Flask
│   └── requirements.txt    # Dependências Python
├── frontend/               # (Em desenvolvimento)
├── .gitignore             # Arquivos ignorados pelo Git
└── README.md              # Este arquivo
```

## ⚙️ Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/todo-list-api.git
cd todo-list-api
```

2. **Crie um ambiente virtual**
```bash
python -m venv .venv
```

3. **Ative o ambiente virtual**

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

4. **Instale as dependências**
```bash
cd backend
pip install -r requirements.txt
```

5. **Execute a aplicação**
```bash
python app.py
```

A API estará rodando em: `http://localhost:5000`

## 📡 Endpoints da API

### 📋 Listar Tarefas
```http
GET /tasks
```

**Resposta:**
```json
[
  {
    "id": 1,
    "title": "Estudar Flask",
    "completed": false
  }
]
```

### ➕ Criar Tarefa
```http
POST /tasks
Content-Type: application/json

{
  "title": "Nova tarefa"
}
```

**Resposta:**
```json
{
  "id": 2,
  "title": "Nova tarefa",
  "completed": false
}
```

### ✏️ Atualizar Tarefa
```http
PUT /tasks/{id}
Content-Type: application/json

{
  "title": "Tarefa atualizada",
  "completed": true
}
```

### 🗑️ Deletar Tarefa
```http
DELETE /tasks/{id}
```

**Resposta:**
```json
{
  "message": "Tarefa deletada com sucesso",
  "task": { ... }
}
```

## 🧪 Testando a API

Recomendo usar o [Postman](https://www.postman.com/) para testar os endpoints.

Importe a collection do Postman: [Link para collection]

## 🎯 Próximos Passos

### Backend (Próximas melhorias)
- [ ] Implementar banco de dados SQLite para persistência
- [ ] Adicionar autenticação de usuários
- [ ] Validações avançadas de dados
- [ ] Testes automatizados

### Frontend Mobile (Em desenvolvimento)
- [ ] Setup do React Native com Expo
- [ ] Interface de usuário intuitiva
- [ ] Integração completa com a API
- [ ] Gerenciamento de estado global

### Deploy e Produção
- [ ] Deploy da API na nuvem (Heroku/Railway)
- [ ] CI/CD pipeline
- [ ] Documentação com Swagger
- [ ] Publicação do app mobile

## 👨‍💻 Desenvolvido por

**Antonio Guilherme**

- LinkedIn: [Seu LinkedIn]
- GitHub: [Seu GitHub]
- Email: [Seu Email]

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

⭐ Se este projeto te ajudou, deixe uma estrela!
