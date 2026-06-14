# Análise de Erros

## Falha 1

### Tipo

Recuperação (RAG)

### Descrição

Ao perguntar:

> "me explique machine learning"

o sistema recuperou principalmente trechos sobre Q-Learning e aprendizado por reforço, em vez de uma definição geral de Machine Learning.

### Causa

A busca vetorial encontrou chunks semanticamente próximos ao termo *machine learning*, porém os documentos recuperados não continham uma explicação introdutória adequada. Além disso, alguns PDFs possuem conteúdo muito específico, fazendo o sistema recuperar contextos parcialmente relacionados.

### Possíveis Soluções

- Melhorar o chunking.
- Aumentar a diversidade dos documentos.
- Implementar reranking dos resultados recuperados.
- Utilizar mais chunks recuperados antes da geração da resposta.

---

## Falha 2

### Tipo

Geração

### Descrição

Durante os testes do planejamento de estudos, o sistema gerou informações que não estavam diretamente presentes nos materiais recuperados.

**Exemplo:** recomendações detalhadas sobre IA, Estrutura de Dados e Matemática mesmo quando o contexto recuperado tratava principalmente de Machine Learning.

### Causa

A LLM utilizou conhecimento próprio para complementar a resposta, extrapolando o conteúdo fornecido pelo RAG.

### Possíveis Soluções

- Tornar os prompts mais restritivos.
- Exigir que o modelo cite explicitamente as fontes recuperadas.
- Reduzir a temperatura do modelo.
- Validar automaticamente se a resposta utiliza informações presentes no contexto.

---

## Falha 3

### Tipo

Ambiguidade de Intenção (Tool Calling)

### Descrição

Ao perguntar:

> "preciso estudar banco de dados"

o sistema selecionou a ferramenta de planejamento de estudos quando o esperado poderia ser a ferramenta de adicionar tarefa.

### Causa

A frase pode ser interpretada de duas formas:

1. Adicionar uma tarefa.
2. Solicitar um plano de estudos.

O modelo escolheu uma interpretação diferente da intenção do usuário.

### Possíveis Soluções

- Adicionar mais exemplos no prompt de tool calling.
- Criar regras específicas para frases como:
  - "preciso estudar"
  - "tenho que estudar"
- Implementar confirmação quando houver ambiguidade.

---

## Falha 4

### Tipo

Recuperação de Documentos

### Descrição

Algumas consultas retornaram chunks contendo apenas referências bibliográficas ou trechos pouco informativos.

### Causa

O sistema indexa praticamente todo o texto extraído dos PDFs, incluindo seções de referências e bibliografia.

### Possíveis Soluções

- Remover automaticamente referências bibliográficas.
- Filtrar páginas com baixa densidade de conteúdo.
- Ignorar seções de referências durante a indexação.

---
