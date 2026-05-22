from datetime import datetime


def salvar_log(ferramenta, entrada, saida):
    with open("logs.txt", "a", encoding="utf-8") as arquivo:

        horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        arquivo.write(f"[{horario}]\n")
        arquivo.write(f"Ferramenta: {ferramenta}\n")
        arquivo.write(f"Entrada: {entrada}\n")
        arquivo.write(f"Saída: {saida}\n")
        arquivo.write("-" * 40 + "\n")