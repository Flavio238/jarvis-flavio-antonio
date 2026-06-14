# Avaliação do Sistema

O sistema foi avaliado utilizando perguntas relacionadas aos documentos presentes no dataset acadêmico.

O objetivo da avaliação foi analisar:

- qualidade da recuperação semântica
- coerência das respostas
- desempenho do sistema RAG
- comportamento do tool calling

---

# Resultados da Avaliação

| Pergunta | Documento Recuperado | Resumo da Resposta | Avaliação |
|---|---|---|---|
| O que é Q-learning? | Q-learning-1992.pdf | Explicou aprendizado otimizado em domínios Markovianos e atualização de ações por recompensa. | Correta |
| Explique reinforcement learning | Q-learning-1992.pdf | Explicou aprendizado por reforço utilizando recompensas, penalidades e tentativa e erro. | Correta |
| O que é aprendizado baseado em recompensas? | Q-learning-1992.pdf | Explicou aprendizado baseado em recompensas utilizando ações e penalidades. | Correta |
| Como agentes aprendem no Q-learning? | Q-learning-1992.pdf | Explicou o aprendizado através de tentativa e erro e recompensas descontadas. | Correta |
| Explique diferenças temporais | Q-learning-1992.pdf | Relacionou o método TD com aprendizado baseado em recompensas e avaliação de estados. | Correta |
| O que é recompensa descontada? | Q-learning-1992.pdf | Explicou o conceito de recompensa descontada no longo prazo. | Correta |
| Como funciona aprendizado por reforço? | Mod3 Fundamentos de Machine Learning.pdf | Recuperou chunks parcialmente relacionados e não respondeu completamente. | Parcialmente correta |
| O que são domínios markovianos? | Q-learning-1992.pdf | Relacionou domínios Markovianos com ambientes de aprendizado para agentes. | Parcialmente correta |
| Como funciona o método TD? | Mod3 Fundamentos de Machine Learning.pdf | Recuperou chunks não relacionados ao tema solicitado. | Incorreta |
| O que tem no PDF Zouetal? | Nenhum documento relevante | O sistema não conseguiu identificar corretamente o documento solicitado. | Incorreta |

---

# Análise dos Resultados

Durante os testes, o sistema apresentou melhor desempenho em perguntas diretamente relacionadas aos conteúdos mais presentes no dataset.

Os melhores resultados ocorreram em perguntas relacionadas a:

- Q-learning
- reinforcement learning
- aprendizado baseado em recompensas
- diferenças temporais

As principais limitações observadas foram:

- dificuldade na recuperação semântica de alguns temas específicos
- recuperação de chunks parcialmente irrelevantes
- dificuldade em identificar nomes específicos de documentos
- baixa precisão em perguntas mais genéricas

Também foi observado que o tool calling funcionou corretamente durante os testes, identificando automaticamente a ferramenta `buscar_material_rag`.

---

# Considerações

O sistema demonstrou capacidade de:

- utilizar tool calling com LLM
- recuperar informações relevantes utilizando RAG
- integrar embeddings com busca vetorial
- responder perguntas acadêmicas utilizando documentos locais

As principais limitações estão relacionadas à recuperação semântica e à qualidade do contexto recuperado pelos embeddings.
