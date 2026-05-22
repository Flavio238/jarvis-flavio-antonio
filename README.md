# Jarvis Flávio

Assistente acadêmico inteligente desenvolvido em Python utilizando:

- RAG (Retrieval Augmented Generation)
- Tool Calling
- LLM Gemma 3 12B
- Busca semântica com embeddings
- Sistema de aprendizado interativo

O objetivo do projeto é estudar a integração entre modelos de linguagem, recuperação de informação e agentes inteligentes aplicados ao contexto acadêmico.

---

# Objetivo do Projeto

Este projeto foi desenvolvido para a disciplina de Inteligência Artificial com foco em:

- construção de assistentes inteligentes
- integração de LLMs
- recuperação semântica de informações
- tool calling
- aprendizado interativo
- engenharia de sistemas baseados em IA

O sistema busca auxiliar estudantes em:
- organização acadêmica
- consultas a materiais
- revisão de conteúdos
- planejamento de estudos

---

# Funcionalidades

## 1. Sistema RAG (Retrieval Augmented Generation)

O Jarvis consegue responder perguntas utilizando documentos acadêmicos carregados na pasta `data/`.

### O sistema realiza:

- leitura de PDFs
- divisão em chunks
- geração de embeddings
- indexação vetorial com FAISS
- recuperação semântica
- geração de respostas utilizando LLM

### Exemplos

```bash
me explique LSPI
o que tem no pdf Zouetal?
me explique roteamento
```

---

## 2. Gerenciamento de tarefas

O sistema permite:

- adicionar tarefas
- listar tarefas
- concluir tarefas

### Exemplos

```bash
preciso estudar matemática
listar tarefas
concluir tarefa 3
```

---

## 3. Agenda acadêmica

O Jarvis também possui gerenciamento de agenda acadêmica.

### Funcionalidades

- adicionar eventos
- consultar agenda
- listar compromissos

### Exemplos

```bash
adicionar prova de cálculo quinta
listar agenda
```

---

## 4. Quiz Interativo e Active Recall

O sistema consegue gerar perguntas automaticamente utilizando os conteúdos dos PDFs carregados.

### Fluxo

1. Recupera contexto usando RAG
2. Gera perguntas automaticamente
3. Recebe respostas do usuário
4. Avalia automaticamente
5. Fornece feedback

### Exemplos

```bash
me teste sobre LSPI
me teste sobre roteamento
```

---

# Tool Calling

O sistema utiliza tool calling para permitir que a LLM decida automaticamente quais ferramentas utilizar com base na intenção do usuário.

## Ferramentas implementadas

- adicionar_tarefa
- listar_tarefas
- concluir_tarefa
- consultar_agenda
- buscar_material_rag

## Fluxo do Tool Calling

1. Usuário envia mensagem
2. LLM interpreta intenção
3. Sistema seleciona ferramenta adequada
4. Ferramenta é executada
5. Resultado retorna para a LLM
6. Resposta final é gerada

O sistema também registra logs das ferramentas utilizadas.

---

# Dataset

O dataset utilizado contém artigos, apostilas e materiais acadêmicos relacionados a:

- Machine Learning
- NLP
- RAG
- Reinforcement Learning
- Redes DTN
- Sistemas Inteligentes

## Origem dos dados

Os documentos foram obtidos de:

- artigos científicos
- apostilas acadêmicas
- materiais didáticos
- ebooks técnicos

## Limitações

- alguns PDFs possuem formatação inconsistente
- imagens e tabelas não são interpretadas completamente
- qualidade da recuperação depende da qualidade do chunking
- documentos muito longos podem gerar recuperação parcial

---

# Estratégia de Chunking

Os documentos são divididos em chunks para melhorar a recuperação semântica.

## Estratégia utilizada

- divisão em trechos menores
- utilização de overlap entre chunks
- preservação parcial de contexto

## Impacto no RAG

A estratégia de chunking melhora:

- recuperação de contexto relevante
- precisão das respostas
- continuidade semântica
- qualidade da busca vetorial

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
├── rag.py
├── aprendizado.py
├── quiz.py
├── agente.py
├── tool_calling.py
├── llm.py
├── logger.py
├── database.py
│
├── data/
│   ├── WangWang-2006.pdf
│   ├── Zouetal-2019.pdf
│   └── ...
│
├── requirements.txt
└── README.md
```

---

# Instalação

## 1. Clonar o projeto

```bash
git clone https://github.com/Flavio238/jarvis-flavio-antonio.git
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

- interface gráfica
- memória conversacional
- voz
- agente autônomo
- integração com Google Calendar
- OCR para PDFs/imagens
- busca híbrida
- web search
- fine-tuning

---

# Ferramentas de IA Utilizadas

Durante o desenvolvimento do projeto foram utilizadas ferramentas de IA como apoio para:

- revisão de código
- sugestões de arquitetura
- identificação de bugs
- melhorias no README
- auxílio na organização do projeto

---

## Ferramentas utilizadas

- ChatGPT (OpenAI)

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
