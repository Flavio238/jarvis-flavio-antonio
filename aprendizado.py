from llm import client


def gerar_perguntas(topico, contexto):

    prompt = f"""
    Você é um tutor acadêmico.

    Com base no contexto abaixo,
    gere 3 perguntas para ajudar
    um aluno a estudar.

    Contexto:
    {contexto}

    Tema:
    {topico}
    """

    resposta = client.chat.completions.create(
        model="google/gemma-3-12b-it",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta.choices[0].message.content


# =========================
# PERGUNTA ÚNICA
# =========================

def gerar_pergunta_unica(
    topico,
    contexto
):

    prompt = f"""
    Você é um professor.

    Gere apenas UMA pergunta curta
    para testar o aluno.

    Tema:
    {topico}

    Contexto:
    {contexto}
    """

    resposta = client.chat.completions.create(
        model="google/gemma-3-12b-it",
        temperature=0.5,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta.choices[0].message.content


# =========================
# AVALIAR RESPOSTA
# =========================

def avaliar_resposta(
    pergunta,
    resposta_usuario,
    contexto
):

    prompt = f"""
    Você é um professor avaliando
    a resposta de um aluno.

    Pergunta:
    {pergunta}

    Resposta do aluno:
    {resposta_usuario}

    Contexto correto:
    {contexto}

    Classifique a resposta como:

    - correta
    - parcialmente correta
    - incorreta

    Explique resumidamente o motivo.
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