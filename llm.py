from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
<<<<<<< HEAD
    base_url='https://llm.liaufms.org/v1/gemma-3-12b-it',
=======
    base_url='https://llm.liaufms.org/v1/qwen2-5-14b-instruct-awq',
>>>>>>> 98964da (Segunda entrega - Tool Calling, Planejamento e Quiz)
    api_key='REIkURcI7rTTqsTwlJi8MrgnKFwOiqky7Ezh7hH-l-k'
)

def gerar_resposta(pergunta, contexto):

    if not contexto.strip():
        return "Não encontrei informações relevantes nos materiais."

    prompt = f"""
Você é Jarvis, um assistente acadêmico inteligente especializado em responder perguntas acadêmicas usando materiais fornecidos.

REGRAS IMPORTANTES:

- Responda APENAS usando o contexto fornecido.
- NÃO invente informações.
- NÃO use conhecimento externo.
- Se a informação não estiver no contexto, diga claramente:
"Não encontrei essa informação nos materiais fornecidos."

- Seja claro e objetivo.
- Cite o conteúdo de forma resumida e acadêmica.

================ CONTEXTO ================

{contexto}

================================================

Pergunta:
{pergunta}
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
