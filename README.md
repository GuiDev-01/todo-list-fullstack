# 📱 TODO List Full-Stack

> **🚀 Status: Frontend Completo | Backend Completo | Pronto para Integração**

Um aplicativo completo de lista de tarefas desenvolvido como projeto de aprendizado, demonstrando habilidades em desenvolvimento full-stack com Python/Flask no backend e React Native no frontend.

## 🚀 Sobre o Projeto

Este projeto implementa uma aplicação completa de gerenciamento de tarefas com arquitetura full-stack:

- **Backend:** API REST em Python com Flask (✅ Completo)
- **Frontend:** Aplicativo mobile em React Native (✅ Completo)
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

**Frontend Mobile:** (Atualizado)
- ✅ **Interface completa** com React Native
- ✅ **Adicionar novas tarefas** com input e validação
- ✅ **Marcar tarefas como concluídas** (checkbox interativo)
- ✅ **Deletar tarefas** (botão delete)
- ✅ **Lista responsiva** com scroll automático
- ✅ **Design moderno** e intuitivo
- ✅ **Estados visuais** (concluída/pendente)
- 🔄 **Integração com API** (próxima etapa)

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
- **React Hooks** - useState para gerenciamento de estado

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
│       ├── app.json        # Configurações Expo
│       └── assets/         # Recursos (ícones, imagens)
├── .gitignore             # Arquivos ignorados pelo Git
└── README.md              # Este arquivo
```

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
# source .venv/bin/activate  # Linux/Mac
```

3. **Instale as dependências**
```bash
cd backend
pip install flask flask-cors
```

4. **Execute a API**
```bash
python app.py
```
🌐 **API rodando em:** `http://localhost:5000`

#### 📱 Frontend (Mobile)

Nota: este repositório foi atualizado para usar Expo SDK 54 para compatibilidade com Expo Go (se você atualizou o projeto localmente esta mudança já foi aplicada).

1. **Configure o ambiente Node.js**
```powershell
cd frontend/TodoApp
npm install
```

2. **Execute o app**
```powershell
# use a CLI local (recomendada) invocando via npx
npx expo start
```

Se você tiver problemas de desempenho durante instalações/upgrade (ex.: downloads lentos), considere mover o projeto para fora do OneDrive (ex.: `C:\dev\`) — OneDrive pode introduzir locks e I/O lento.

3. **Teste no dispositivo**
- Baixe o **Expo Go** na Play Store/App Store
- Escaneie o QR code que aparece no terminal
- O app será carregado automaticamente no seu celular

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

## 📱 Screenshots do App

*Em breve - screenshots da interface mobile*

## 🎯 Próximos Passos

### ✅ Concluído
- [x] ✅ API REST Flask com 4 endpoints CRUD
- [x] ✅ Banco de dados SQLite para persistência
- [x] ✅ Validações de dados e tratamento de erros
- [x] ✅ Estrutura modular (separação database/API)
- [x] ✅ Interface React Native completa
- [x] ✅ Funcionalidades CRUD no frontend
- [x] ✅ Design responsivo e intuitivo

### 🔄 Próximas Etapas
- [ ] 🚧 Conectar frontend com backend via HTTP requests
- [ ] 🚧 Sincronização de dados em tempo real
- [ ] 📋 Adicionar autenticação de usuários
- [ ] 📋 Testes automatizados
- [ ] 📋 Deploy da API na nuvem (Heroku/Railway)
- [ ] 📋 Publicação do app mobile

## 📊 Status Atual

**🎉 Projeto 90% Completo!**

- ✅ **Backend:** 100% Funcional
- ✅ **Frontend:** 100% Funcional  
- 🔄 **Integração:** Próximo passo
- 📋 **Deploy:** Planejado

## 📌 Notas sobre dependências e atualização

- Backend: as dependências Python estão em `backend/requirements.txt`. Para instalar tudo de uma vez a partir da raiz do repositório:
```powershell
cd "C:\Users\Antonio Santos\OneDrive\Desktop\Projeto_TODO_LIST"
pip install -r requirements.txt
```

- Frontend: para manter o SDK do Expo compatível com o Expo Go do seu celular, use `npx expo upgrade` dentro de `frontend/TodoApp` quando precisar atualizar o SDK e então rode `npm install`.

- Se você preferir instalar as dependências do backend isoladamente:
```powershell
cd backend
pip install -r requirements.txt
```

Se quiser, eu posso preparar um script simples (PowerShell) para automatizar criação do ambiente, instalação das dependências e inicialização do backend+frontend.

## 🤝 Contribuições

Este projeto foi desenvolvido como parte do meu aprendizado em desenvolvimento full-stack. Sugestões e feedback são sempre bem-vindos!

## 👨‍💻 Desenvolvido por

**Antonio Guilherme Santos**

- LinkedIn: [Antonio Guilherme Santos](https://www.linkedin.com/in/antonio-guilherme-santos/)
- GitHub: [GuiDev-01](https://github.com/GuiDev-01)

---

⭐ Se este projeto te ajudou de alguma forma, deixe uma estrela no repositório!
