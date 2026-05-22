from openai import OpenAI
import json

client = OpenAI(
    base_url='https://llm.liaufms.org/v1/gemma-3-12b-it',
    api_key='Cxt2ftLF7d3mHS2JdiFqB-eSDAQeZvFATPXPs02lV9A'
)

def decidir_tool(pergunta):

    prompt = f"""
Você é um sistema de tool calling.

Responda APENAS em JSON.

NÃO escreva explicações.
NÃO use markdown.
NÃO use ```json.
Retorne apenas o objeto JSON puro.

Ferramentas disponíveis:

1. adicionar_tarefa
2. listar_tarefas
3. concluir_tarefa
4. consultar_agenda
5. buscar_material_rag
6. gerar_perguntas

Exemplos:

Pergunta: adicionar tarefa estudar IA
Resposta:
{{
    "tool": "adicionar_tarefa",
    "args": {{
        "tarefa": "estudar IA"
    }}
}}

Pergunta: listar tarefas
Resposta:
{{
    "tool": "listar_tarefas",
    "args": {{}}
}}

Pergunta: concluir tarefa 2
Resposta:
{{
    "tool": "concluir_tarefa",
    "args": {{
        "id": 2
    }}
}}

Pergunta: o que existe no pdf embeddings?
Resposta:
{{
    "tool": "buscar_material_rag",
    "args": {{
        "query": "embeddings"
    }}
}}

Pergunta: me faça perguntas sobre embeddings
Resposta:
{{
    "tool": "gerar_perguntas",
    "args": {{
        "topico": "embeddings"
    }}
}}

Pergunta: gere perguntas sobre IA
Resposta:
{{
    "tool": "gerar_perguntas",
    "args": {{
        "topico": "IA"
    }}
}}

Pergunta: oi
Resposta:
{{
   "tool": "conversa_normal",
   "args": {{
      "mensagem": "oi"
   }}
}}

Pergunta: aaaaaaaaa
Resposta:
{{
   "tool": "conversa_normal",
   "args": {{
      "mensagem": "Não entendi sua solicitação."
   }}
}}

Pergunta: me teste sobre LSPI
Resposta:
{{
    "tool": "quiz_interativo",
    "args": {{
        "topico": "LSPI"
    }}
}}

Pergunta: tenho prova de matemática quinta
Resposta:
{{
    "tool": "adicionar_evento",
    "args": {{
        "evento": "prova de matemática",
        "data": "quinta"
    }}
}}

Pergunta: agendar prova de cálculo quarta
Resposta:
{{
    "tool": "adicionar_evento",
    "args": {{
        "evento": "prova de cálculo",
        "data": "quarta"
    }}
}}

Pergunta: listar agenda
Resposta:
{{
    "tool": "consultar_agenda",
    "args": {{}}
}}

Pergunta: aaaaaaaaa
Resposta:
{{
    "tool": "desconhecido",
    "args": {{}}
}}

Pergunta do usuário:
{pergunta}
"""

    resposta = client.chat.completions.create(
        model="google/gemma-3-12b-it",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    texto = resposta.choices[0].message.content

    texto = texto.replace("```json", "")
    texto = texto.replace("```", "")
    texto = texto.strip()

    tools_validas = [
    "adicionar_tarefa",
    "listar_tarefas",
    "concluir_tarefa",
    "adicionar_evento",
    "consultar_agenda",
    "buscar_material_rag",
    "gerar_perguntas",
    "conversa_normal",
    "quiz_interativo",
    "desconhecido"
    ]

    try:

        resultado = json.loads(texto)

        if resultado["tool"] not in tools_validas:

            return {
                "tool": "buscar_material_rag",
                "args": {
                    "query": pergunta
                }
            }

        print("\nTOOL ESCOLHIDA:")
        print(resultado)
        return resultado

    except Exception as e:

        print("Erro no tool calling:", e)

        return {
            "tool": "buscar_material_rag",
            "args": {
                "query": pergunta
            }
        }