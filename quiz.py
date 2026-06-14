from llm import client

def avaliar_resposta(
    pergunta,
    resposta_usuario,
    contexto
):

    prompt = f"""
Você é um professor avaliando uma resposta de um aluno.

Pergunta:
{pergunta}

Resposta do aluno:
{resposta_usuario}

Contexto correto:
{contexto}

Avalie a resposta do aluno.

Diga se ela está:

- correta
- parcialmente correta
- incorreta

Explique resumidamente o motivo.
"""

    resposta = client.chat.completions.create(
        model='Qwen/Qwen2.5-14B-Instruct-AWQ',
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta.choices[0].message.content