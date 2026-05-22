# Jarvis Flávio

Assistente pessoal desenvolvido em Python com:

- Sistema de tarefas
- Agenda
- RAG com PDFs
- Quiz interativo
- Tool Calling com LLM
- Busca semântica com embeddings

---

# Funcionalidades

## Gerenciamento de tarefas

O Jarvis consegue:

- Adicionar tarefas
- Listar tarefas
- Concluir tarefas

### Exemplos

```bash
preciso estudar matemática
listar tarefas
concluir tarefa 3
```

---

## Agenda

O sistema também possui gerenciamento simples de agenda.

### Funcionalidades

- Adicionar eventos
- Consultar agenda

### Exemplos

```bash
adicionar prova de cálculo quinta
listar agenda
```

---

## Sistema RAG (Retrieval Augmented Generation)

O Jarvis consegue responder perguntas utilizando PDFs carregados na pasta `data/`.

### O sistema realiza:

- Leitura de PDFs
- Divisão em chunks
- Geração de embeddings
- Indexação vetorial com FAISS
- Busca semântica
- Geração de respostas com LLM

### Exemplos

```bash
me explique LSPI
o que tem no pdf Zouetal?
me explique roteamento
```

---

## Quiz Interativo

O sistema consegue gerar perguntas automaticamente utilizando o conteúdo dos PDFs.

### Fluxo

1. Recupera contexto usando RAG
2. Gera perguntas
3. Recebe resposta do usuário
4. Avalia automaticamente

### Exemplos

```bash
me teste sobre LSPI
me teste sobre roteamento
```

---

# Tecnologias Utilizadas

- Python
- FAISS
- Sentence Transformers
- SQLite
- OpenAI SDK
- Gemma 3 12B
- RAG
- Tool Calling
- NLP

---

# Estrutura do Projeto

```bash
jarvis-flavio/
│
├── main.py
├── RAG.py
├── aprendizado.py
├── quiz.py
├── agente.py
├── tool_calling.py
├── llm.py
├── logger.py
│
├── data/
│   ├── WangWang-2006.pdf
│   ├── Zouetal-2019.pdf
│   └── ...
│
├── tarefas.db
├── agenda.db
│
├── requirements.txt
└── README.md
```

---

# Instalação

## 1. Clonar o projeto

```bash
git clone https://github.com/seuusuario/jarvis-flavio.git
```

---

## 2. Criar ambiente virtual

### Windows

```bash
python -m venv venv
```

### Ativar ambiente virtual

```bash
venv\Scripts\activate
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Executando o Projeto

```bash
py main.py
```

---

# Exemplos de Uso

## Adicionar tarefa

```bash
Você: preciso estudar IA
Jarvis: Tarefa adicionada com sucesso.
```

---

## Consultar PDFs

```bash
Você: me explique LSPI
Jarvis: LSPI é um algoritmo...
```

---

## Quiz interativo

```bash
Você: me teste sobre roteamento
Jarvis: Quais são os desafios...
```

---

# Como o RAG Funciona

1. PDFs são carregados
2. Texto é dividido em chunks
3. Embeddings são gerados
4. FAISS cria o índice vetorial
5. Pergunta é transformada em embedding
6. Chunks relevantes são recuperados
7. A LLM gera a resposta baseada no contexto

---

# Melhorias Futuras

- Interface gráfica
- Memória conversacional
- Voz
- Agente autônomo
- Integração com Google Calendar
- OCR para PDFs/imagens
- Busca híbrida
- Web search
- Fine-tuning

---

# Autor

Flávio Antônio dos Santos Matos

Projeto desenvolvido para estudos de:

- Inteligência Artificial
- RAG
- Agentes Inteligentes
- NLP
- Tool Calling
- LLM Engineering

