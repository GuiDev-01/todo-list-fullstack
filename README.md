# 👨🏻‍💻 Full-Stack To-Do List Application

> **🚧 Status: Em Desenvolvimento** | **Fase Atual: Frontend Mobile Implementado**

Um aplicativo completo de lista de tarefas desenvolvido como projeto de aprendizado, demonstrando habilidades em desenvolvimento full-stack com Python/Flask no backend e React Native no frontend.

## 🚀 Sobre o Projeto

Este projeto implementa uma aplicação completa de gerenciamento de tarefas com arquitetura full-stack:

- **Backend:** API REST em Python com Flask (✅ Completo)
- **Frontend:** Aplicativo mobile em React Native (✅ Interface básica implementada)
- **Banco de Dados:** SQLite (✅ Integrado)

### ✨ Funcionalidades

**Backend API:**
- ✅ **Listar todas as tarefas** - `GET /tasks`
- ✅ **Criar nova tarefa** - `POST /tasks`
- ✅ **Atualizar tarefa** - `PUT /tasks/<id>`
- ✅ **Deletar tarefa** - `DELETE /tasks/<id>`
- ✅ **Tratamento de erros** (404 para tarefas não encontradas)
- ✅ **CORS habilitado** para integração com frontend
- ✅ **Banco SQLite integrado** com persistência de dados

**Frontend Mobile:**
- ✅ **Interface básica** com React Native
- ✅ **Input para nova tarefa** com validação
- ✅ **Lista de tarefas** responsiva
- ✅ **Estilos modernos** e user-friendly
- 🚧 **Integração com API** (próxima etapa)

## 🛠️ Tecnologias Utilizadas

**Backend:**
- **Python 3.12**
- **Flask** - Framework web minimalista
- **Flask-CORS** - Habilitação de CORS
- **SQLite** - Banco de dados local

**Frontend:**
- **React Native** - Desenvolvimento mobile multiplataforma
- **Expo** - Plataforma de desenvolvimento React Native
- **JavaScript ES6+** - Linguagem de programação

## 📋 Estrutura do Projeto

```
Projeto_TODO_LIST/
├── backend/
│   ├── app.py              # Aplicação principal Flask
│   ├── database.py         # Operações do banco SQLite
│   ├── todo_tasks.db       # Banco de dados SQLite
│   └── requirements.txt    # Dependências Python
├── frontend/
│   └── TodoApp/
│       ├── App.js          # Componente principal React Native
│       ├── package.json    # Dependências Node.js
│       └── ...            # Configurações Expo
├── .gitignore             # Arquivos ignorados pelo Git
└── README.md              # Este arquivo
```

## ⚙️ Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## ⚙️ Como Executar

### Pré-requisitos

**Backend:**
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

**Frontend:**
- Node.js 16 ou superior
- npm ou yarn
- Expo CLI (`npm install -g @expo/cli`)
- Expo Go app no celular (para testar)

### Instalação e Execução

#### 🔧 Backend (API)

1. **Clone o repositório**
```bash
git clone https://github.com/GuiDev-01/todo-list-fullstack.git
cd todo-list-fullstack
```

2. **Configure o ambiente Python**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
cd backend
pip install -r requirements.txt
```

4. **Execute a API**
```bash
python app.py
```
🌐 **API rodando em:** `http://localhost:5000`

#### 📱 Frontend (Mobile)

1. **Configure o ambiente Node.js**
```bash
cd frontend/TodoApp
npm install
```

2. **Execute o app**
```bash
npx expo start
```

3. **Teste no dispositivo**
- Escaneie o QR code com Expo Go (Android/iOS)
- Ou pressione `w` para abrir no navegador

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

Importe a collection do Postman: [Link para collection](https://guidev-01-5029446.postman.co/workspace/Guilherme's-Team's-Workspace~a3b8049f-d39a-487e-842d-ba4e5364cbc7/collection/48009682-439caca7-b147-469a-a173-c766bc5362b2?action=share&source=copy-link&creator=48009682)

## 🎯 Próximos Passos

### Backend ✅ (Concluído)
- [x] ✅ API REST Flask com 4 endpoints CRUD
- [x] ✅ Implementar banco de dados SQLite para persistência
- [x] ✅ Validações de dados e tratamento de erros
- [x] ✅ Estrutura modular (separação database/API)
- [ ] 🔄 Adicionar autenticação de usuários
- [ ] 🔄 Testes automatizados

### Frontend Mobile (Em desenvolvimento)
- [ ] 🚧 Setup do React Native com Expo
- [ ] 🚧 Interface de usuário intuitiva
- [ ] 🚧 Integração completa com a API
- [ ] 🚧 Gerenciamento de estado global

### Deploy e Produção (Futuro)
- [ ] 📋 Deploy da API na nuvem (Heroku/Railway)
- [ ] 📋 CI/CD pipeline
- [ ] 📋 Documentação com Swagger
- [ ] 📋 Publicação do app mobile

### 📊 Status Atual
**Backend: 100% Funcional** 🎉
- ✅ API REST completa
- ✅ Banco SQLite integrado
- ✅ Dados persistentes
- ✅ Testado com Postman

**Frontend: Em desenvolvimento** 🚧
- 🔄 React Native setup em andamento

## 👨‍💻 Desenvolvido por

**Antonio Guilherme**

- LinkedIn: [LinkedIn](https://www.linkedin.com/in/antonio-guilherme-santos/)
- GitHub: [GitHub](https://github.com/GuiDev-01)


## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

⭐ Se este projeto te ajudou, deixe uma estrela!
