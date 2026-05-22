from aprendizado import (
    gerar_perguntas,
    gerar_pergunta_unica,
    avaliar_resposta
)
from logger import salvar_log
from tool_calling import decidir_tool

from agente import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    adicionar_evento
)

from agente import listar_agenda

from rag import (
    carregar_documentos,
    criar_chunks_documentos,
    gerar_embeddings,
    criar_indice,
    responder_pergunta,
    recuperar_contexto,
    modelo
)

# =========================
# CARREGAR RAG
# =========================

documentos = carregar_documentos()

chunks = criar_chunks_documentos(documentos)

embeddings = gerar_embeddings(chunks)

indice = criar_indice(embeddings)

# =========================
# LOOP PRINCIPAL
# =========================

print("Jarvis iniciado!")
print("Digite 'sair' para encerrar.\n")

while True:

    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        print("Encerrando Jarvis...")
        break

    resultado = decidir_tool(pergunta)

    tool = resultado["tool"]
    args = resultado["args"]

    # =========================
    # EXECUÇÃO DAS TOOLS
    # =========================

    if tool == "adicionar_tarefa":

        resposta = adicionar_tarefa(
            args["tarefa"]
        )

        salvar_log(
            "adicionar_tarefa",
            args["tarefa"],
            resposta
        )
    
    elif tool == "conversa_normal":

        resposta = args["mensagem"]

    elif tool == "listar_tarefas":

        resposta = listar_tarefas()

        salvar_log(
            "listar_tarefas",
            "nenhuma entrada",
            resposta
        )

    elif tool == "concluir_tarefa":

        resposta = concluir_tarefa(
            args["id"]
        )

        salvar_log(
            "concluir_tarefa",
            args["id"],
            resposta
        )
    elif tool == "adicionar_evento":

        resposta = adicionar_evento(
            args["evento"],
            args["data"]
        )

        salvar_log(
            "adicionar_evento",
            args["evento"],
            resposta
        )

    elif tool == "consultar_agenda":

        resposta = listar_agenda()

        salvar_log(
            "consultar_agenda",
            "nenhuma entrada",
            resposta
        )

    elif tool == "buscar_material_rag":

        resposta = responder_pergunta(
            pergunta,
            modelo,
            indice,
            chunks
        )

        salvar_log(
            "buscar_material_rag",
            pergunta,
            resposta
        )

    elif tool == "gerar_perguntas":

        contexto = recuperar_contexto(
            args["topico"],
            modelo,
            indice,
            chunks
        )

        resposta = gerar_perguntas(
            args["topico"],
            contexto
        )

        salvar_log(
            "gerar_perguntas",
            args["topico"],
            resposta
        )

    elif tool == "quiz_interativo":

        contexto = recuperar_contexto(
            args["topico"],
            modelo,
            indice,
            chunks
        )

        pergunta_quiz = gerar_pergunta_unica(
            args["topico"],
            contexto
        )

        print("\nJarvis:")
        print(pergunta_quiz)

        resposta_usuario = input(
            "\nSua resposta: "
        )

        avaliacao = avaliar_resposta(
            pergunta_quiz,
            resposta_usuario,
            contexto
        )

        resposta = avaliacao

        salvar_log(
            "quiz_interativo",
            args["topico"],
            resposta
        )

    elif tool == "desconhecido":

        resposta = (
        "Não consegui entender o comando."
        )

    else:

        resposta = "Ferramenta não encontrada."

    print("\nJarvis:")
    print(resposta)
    print()