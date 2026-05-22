from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url='https://llm.liaufms.org/v1/gemma-3-12b-it',
    api_key=os.getenv("API_KEY")
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
        model="google/gemma-3-12b-it",
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta.choices[0].message.content