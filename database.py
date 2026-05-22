import sqlite3

# cria conexão com o banco
conn = sqlite3.connect("jarvis.db")

# permite executar comandos SQL
cursor = conn.cursor()

# cria tabela de tarefas
cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT,
    concluida INTEGER DEFAULT 0
)
""")

# cria tabela da agenda
cursor.execute("""
CREATE TABLE IF NOT EXISTS agenda (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    data TEXT
)
""")

# salva alterações
conn.commit()

# fecha conexão
conn.close()

print("Banco criado com sucesso.")