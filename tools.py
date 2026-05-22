import sqlite3

# adiciona nova tarefa
def adicionar_tarefa(descricao):

    conn = sqlite3.connect("jarvis.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tarefas (descricao) VALUES (?)",
        (descricao,)
    )

    conn.commit()

    conn.close()

    return "Tarefa adicionada com sucesso."


# lista tarefas salvas
def listar_tarefas():
    conexao = sqlite3.connect("jarvis.db")

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM tarefas"
    )

    tarefas = cursor.fetchall()

    conexao.close()

    if not tarefas:
        return "Nenhuma tarefa encontrada."

    texto = "Tarefas:\n\n"

    for tarefa in tarefas:

        status = "✓" if tarefa[2] == 1 else "✗"

        texto += (
            f"{tarefa[0]} - "
            f"{tarefa[1]} "
            f"[{status}]\n"
        )

    return texto

# marca tarefa como concluída
def concluir_tarefa(id_tarefa):

    conn = sqlite3.connect("jarvis.db")

    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tarefas SET concluida = 1 WHERE id = ?",
        (id_tarefa,)
    )

    conn.commit()

    conn.close()

    return "Tarefa concluída com sucesso."

# adiciona evento na agenda
def adicionar_evento(titulo, data):

    conn = sqlite3.connect("jarvis.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO agenda (titulo, data) VALUES (?, ?)",
        (titulo, data)
    )

    conn.commit()

    conn.close()

    return "Evento adicionado com sucesso."


# lista eventos da agenda
# lista eventos da agenda
def listar_agenda():

    conexao = sqlite3.connect("jarvis.db")

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM agenda"
    )

    eventos = cursor.fetchall()

    conexao.close()

    if not eventos:
        return "Agenda vazia."

    texto = "Agenda:\n\n"

    for evento in eventos:

        texto += (
            f"{evento[0]} - "
            f"{evento[1]} | "
            f"{evento[2]}\n"
        )

    return texto