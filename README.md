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
- planejamento simples de estudos

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

O Jarvis possui gerenciamento simples de agenda acadêmica.

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

## 4. Planejamento de Estudos

O sistema consegue auxiliar na priorização de estudos utilizando tarefas e agenda acadêmica.

### Exemplos

```bash
o que devo priorizar hoje?
monte um plano de estudos
```

---

## 5. Quiz Interativo e Active Recall

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
2. A LLM interpreta a intenção
3. O sistema identifica a ferramenta apropriada
4. A ferramenta é executada
5. O resultado retorna para a LLM
6. A resposta final é gerada para o usuário

## Logs

O sistema registra:

- ferramenta utilizada
- entrada recebida
- saída retornada
- horário da execução

---

# Dataset

O dataset utilizado contém 10 documentos acadêmicos relacionados a:

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

## Tipo de conteúdo

Os PDFs utilizados possuem:

- conteúdo teórico
- conceitos de inteligência artificial
- algoritmos de machine learning
- técnicas de recuperação semântica
- exemplos acadêmicos

## Limitações

- alguns PDFs possuem formatação inconsistente
- imagens e tabelas não são interpretadas completamente
- a recuperação depende da qualidade do chunking
- perguntas muito genéricas podem recuperar contexto parcialmente relevante

---

# Estratégia de Chunking

Os documentos são divididos em chunks para melhorar a recuperação semântica e preservar contexto relevante.

## Estratégia utilizada

- divisão do texto em trechos menores
- utilização de overlap entre chunks
- preservação parcial de contexto semântico

## Impacto no RAG

A estratégia de chunking melhora:

- recuperação de contexto relevante
- continuidade semântica entre trechos
- precisão das respostas
- qualidade da busca vetorial utilizando embeddings

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
jarvis-flavio-antonio/
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

- melhoria da recuperação semântica
- melhorias nos prompts utilizados pela LLM
- expansão do dataset acadêmico
- melhorias no sistema de quiz
- melhorias no tratamento de erros

---

# Ferramentas de IA Utilizadas

Durante o desenvolvimento do projeto foram utilizadas ferramentas de IA como apoio para:

- revisão de código
- sugestões de arquitetura
- identificação de bugs
- melhorias na documentação
- auxílio na organização do projeto

## Ferramentas utilizadas

- ChatGPT (OpenAI)

O desenvolvimento, adaptação e entendimento do código foram realizados manualmente.

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
