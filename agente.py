from tools import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    adicionar_evento,
    listar_agenda
)

from rag import responder_pergunta


def processar_comando(
    pergunta,
    modelo,
    indice,
    chunks
):

    pergunta_lower = pergunta.lower()


    if (
    "adicionar tarefa" in pergunta_lower
    or "preciso estudar" in pergunta_lower
    or "tenho que estudar" in pergunta_lower
    ):

        tarefa = pergunta

        comandos = [
            "adicionar tarefa",
            "preciso estudar",
            "tenho que estudar"
        ]

        for comando in comandos:

            tarefa = tarefa.replace(
                comando,
                ""
            )

        tarefa = tarefa.strip()

        adicionar_tarefa(tarefa)

        return f"Tarefa '{tarefa}' adicionada com sucesso."


    elif "listar tarefas" in pergunta_lower:

        tarefas = listar_tarefas()

        texto = "Tarefas:\n\n"

        for tarefa in tarefas:

            status = "✓" if tarefa[2] == 1 else "✗"

            texto += (
                f"{tarefa[0]} - "
                f"{tarefa[1]} "
                f"[{status}]\n"
            )

        return texto
    
    elif "concluir tarefa" in pergunta_lower:

        numero = pergunta_lower.replace(
            "concluir tarefa",
            ""
        ).strip()

        concluir_tarefa(int(numero))

        return f"Tarefa {numero} concluída."


    elif (
    "adicionar evento" in pergunta_lower
    or "tenho prova" in pergunta_lower
    or "tenho apresentação" in pergunta_lower
    ):

        evento = pergunta

        comandos = [
            "adicionar evento",
            "tenho prova",
            "tenho apresentação"
        ]

        for comando in comandos:

            evento = evento.replace(
                comando,
                ""
            )

        evento = evento.strip()

        adicionar_evento(
            evento,
            "sem data"
        )

        return f"Evento '{evento}' adicionado."
    
    elif "listar agenda" in pergunta_lower:

        eventos = listar_agenda()

        texto = "Agenda:\n\n"

        for evento in eventos:

            texto += (
                f"{evento[0]} - "
                f"{evento[1]} | "
                f"{evento[2]}\n"
            )

        return texto

    else:

        return responder_pergunta(
            pergunta,
            modelo,
            indice,
            chunks
        )