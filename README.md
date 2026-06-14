# Jarvis Flávio

Assistente acadêmico inteligente desenvolvido em Python utilizando:

<<<<<<< HEAD
- RAG (Retrieval Augmented Generation)
- Tool Calling
- LLM Gemma 3 12B
- Busca semântica com embeddings
- Sistema de aprendizado interativo
=======
* RAG (Retrieval Augmented Generation)
* Tool Calling
* LLM Qwen 2.5 14B Instruct AWQ
* Busca semântica com embeddings
* Sistema de aprendizado interativo
>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)

O objetivo do projeto é estudar a integração entre modelos de linguagem, recuperação de informação e agentes inteligentes aplicados ao contexto acadêmico.

---

# Objetivo do Projeto

Este projeto foi desenvolvido para a disciplina de Inteligência Artificial com foco em:

<<<<<<< HEAD
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
=======
* construção de assistentes inteligentes
* integração de LLMs
* recuperação semântica de informações
* tool calling
* aprendizado interativo
* engenharia de sistemas baseados em IA

O sistema busca auxiliar estudantes em:

* organização acadêmica
* consultas a materiais
* revisão de conteúdos
* planejamento simples de estudos
>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)

---

# Funcionalidades

## 1. Sistema RAG (Retrieval Augmented Generation)

O Jarvis consegue responder perguntas utilizando documentos acadêmicos carregados na pasta `data/`.

### O sistema realiza:

<<<<<<< HEAD
- leitura de PDFs
- divisão em chunks
- geração de embeddings
- indexação vetorial com FAISS
- recuperação semântica
- geração de respostas utilizando LLM
=======
* leitura de PDFs
* divisão em chunks
* geração de embeddings
* indexação vetorial com FAISS
* recuperação semântica
* geração de respostas utilizando LLM
>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)

### Exemplos

```bash
me explique LSPI
o que tem no pdf Zouetal?
me explique roteamento
```

---

<<<<<<< HEAD
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
=======
## 2. Gerenciamento de Tarefas

O sistema permite:

* adicionar tarefas
* listar tarefas
* concluir tarefas
>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)

### Exemplos

```bash
preciso estudar matemática
listar tarefas
concluir tarefa 3
```

---

## 3. Agenda Acadêmica

O Jarvis possui gerenciamento simples de agenda acadêmica.

### Funcionalidades

* adicionar eventos
* consultar agenda
* listar compromissos

### Exemplos

```bash
tenho prova de matemática quinta
listar agenda
```

---

## 4. Planejamento de Estudos

O sistema consegue auxiliar na priorização de estudos utilizando tarefas, agenda acadêmica e materiais carregados.

### Exemplos

```bash
o que devo priorizar hoje?
monte um plano de estudos para IA
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
me teste sobre machine learning
me teste sobre LSPI
me teste sobre roteamento
```

---

<<<<<<< HEAD
# Tool Calling

O sistema utiliza tool calling para permitir que a LLM decida automaticamente quais ferramentas utilizar com base na intenção do usuário.

## Ferramentas implementadas

- adicionar_tarefa
- listar_tarefas
- concluir_tarefa
- consultar_agenda
- buscar_material_rag
=======
## Exemplo de Quiz

```bash
Você: me teste sobre machine learning

Jarvis:
O que é um algoritmo de aprendizagem supervisionada?

Sua resposta:
É um algoritmo treinado com dados rotulados.

Jarvis:
Classificação: Correta

Motivo:
A resposta descreve corretamente o conceito de aprendizagem supervisionada.
```

---

# Tool Calling

O sistema utiliza Tool Calling para permitir que a LLM decida automaticamente quais ferramentas utilizar com base na intenção do usuário.

## Ferramentas Implementadas

* adicionar_tarefa
* listar_tarefas
* concluir_tarefa
* adicionar_evento
* consultar_agenda
* buscar_material_rag
* gerar_perguntas
* quiz_interativo
* planejar_estudos
>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)

## Fluxo do Tool Calling

1. Usuário envia mensagem
2. A LLM interpreta a intenção
3. O sistema identifica a ferramenta apropriada
4. A ferramenta é executada
5. O resultado retorna para a LLM
6. A resposta final é gerada para o usuário

<<<<<<< HEAD
=======
---

>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)
## Logs

O sistema registra:

<<<<<<< HEAD
- ferramenta utilizada
- entrada recebida
- saída retornada
- horário da execução
=======
* ferramenta utilizada
* entrada recebida
* saída retornada
* horário da execução
>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)

---

# Dataset

<<<<<<< HEAD
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
=======
O dataset utilizado contém documentos acadêmicos relacionados a:

* Machine Learning
* NLP
* RAG
* Reinforcement Learning
* Redes DTN
* Sistemas Inteligentes

## Origem dos Dados

Os documentos foram obtidos de:

* artigos científicos
* apostilas acadêmicas
* materiais didáticos
* ebooks técnicos

## Tipo de Conteúdo

Os PDFs utilizados possuem:

* conteúdo teórico
* conceitos de inteligência artificial
* algoritmos de machine learning
* técnicas de recuperação semântica
* exemplos acadêmicos

## Limitações

* alguns PDFs possuem formatação inconsistente
* imagens e tabelas não são interpretadas completamente
* a recuperação depende da qualidade do chunking
* perguntas muito genéricas podem recuperar contexto parcialmente relevante
>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)

---

# Estratégia de Chunking

Os documentos são divididos em chunks para melhorar a recuperação semântica e preservar contexto relevante.

<<<<<<< HEAD
## Estratégia utilizada

- divisão do texto em trechos menores
- utilização de overlap entre chunks
- preservação parcial de contexto semântico
=======
## Estratégia Utilizada

* divisão do texto em trechos menores
* utilização de overlap entre chunks
* preservação parcial de contexto semântico
>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)

## Impacto no RAG

A estratégia de chunking melhora:

- recuperação de contexto relevante
- continuidade semântica entre trechos
- precisão das respostas
- qualidade da busca vetorial utilizando embeddings

* recuperação de contexto relevante
* continuidade semântica entre trechos
* precisão das respostas
* qualidade da busca vetorial utilizando embeddings


---

# Tecnologias Utilizadas

* Python
* FAISS
* Sentence Transformers
* SQLite
* OpenAI SDK
* Qwen 2.5 14B Instruct AWQ
* RAG
* Tool Calling
* NLP

---

# Estrutura do Projeto

```bash
jarvis-flavio-antonio/
│
├── main.py
├── rag.py
├── aprendizado.py
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

## 1. Clonar o Projeto

```bash
git clone https://github.com/Flavio238/jarvis-flavio-antonio.git
```

---

## 2. Criar Ambiente Virtual

### Windows

```bash
python -m venv venv
```

### Ativar Ambiente Virtual

```bash
venv\Scripts\activate
```

---

## 3. Instalar Dependências

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

## Adicionar Tarefa

```bash
Você: preciso estudar IA

Jarvis:
Tarefa adicionada com sucesso.
```

---

## Consultar PDFs

```bash
Você: me explique LSPI

Jarvis:
LSPI é um algoritmo utilizado para...
```

---

## Quiz Interativo

```bash
Você: me teste sobre machine learning

Jarvis:
O que é um algoritmo de aprendizagem supervisionada?
```

---

## Planejamento de Estudos

```bash
Você:
o que devo priorizar hoje?

Jarvis:
Plano de estudos baseado nas tarefas,
agenda e materiais acadêmicos.
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

<<<<<<< HEAD
- melhoria da recuperação semântica
- melhorias nos prompts utilizados pela LLM
- expansão do dataset acadêmico
- melhorias no sistema de quiz
- melhorias no tratamento de erros
=======
* melhoria da recuperação semântica
* melhorias nos prompts utilizados pela LLM
* expansão do dataset acadêmico
* melhorias no sistema de quiz
* melhorias no tratamento de erros
>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)

---

# Ferramentas de IA Utilizadas

Durante o desenvolvimento do projeto foram utilizadas ferramentas de IA como apoio para:

<<<<<<< HEAD
- revisão de código
- sugestões de arquitetura
- identificação de bugs
- melhorias na documentação
- auxílio na organização do projeto

## Ferramentas utilizadas

- ChatGPT (OpenAI)
=======
* revisão de código
* sugestões de arquitetura
* identificação de bugs
* melhorias na documentação
* auxílio na organização do projeto

## Ferramentas Utilizadas

* ChatGPT (OpenAI)
>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)

O desenvolvimento, adaptação e entendimento do código foram realizados manualmente.

---

# Autor

Flávio Antônio dos Santos Matos

Projeto desenvolvido para estudos de:

<<<<<<< HEAD
- Inteligência Artificial
- RAG
- Agentes Inteligentes
- NLP
- Tool Calling
- LLM Engineering
=======
* Inteligência Artificial
* RAG
* Agentes Inteligentes
* NLP
* Tool Calling
* LLM Engineering
>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)
