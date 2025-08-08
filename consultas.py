import csv
from datetime import datetime

# Função interativa: mostra o histórico de consultas de um animal
def ver_historico_consultas():
    nome = input("Nome do animal para ver histórico: ")

    try:
        with open("consultas.csv", mode="r") as ficheiro:
            leitor = csv.reader(ficheiro)
            historico = [linha for linha in leitor if linha[0].lower() == nome.lower()]

            if historico:
                print(f"\nHistórico de consultas para {nome}:")
                for i, consulta in enumerate(historico, start=1):
                    sintomas = consulta[1]
                    recomendacao = consulta[2]
                    data = consulta[3] if len(consulta) > 3 else "Data não disponível"
                    print(f"{i}. {data} | Sintomas: {sintomas} | Recomendação: {recomendacao}")
            else:
                print(f"Nenhuma consulta encontrada para o animal '{nome}'.")
    except FileNotFoundError:
        print("Ficheiro de consultas não encontrado.")


# Função testável (sem input direto)
def gerar_consulta(nome, sintomas):
    recomendacao = "Levar ao veterinário" if "febre" in sintomas.lower() else "Monitorizar em casa"
    data = datetime.now().strftime("%Y-%m-%d")
    return [nome, sintomas, recomendacao, data]


# Função interativa (usa input e chama a função testável)
def realizar_consulta():
    nome = input("Nome do animal a consultar: ")
    sintomas = input("Descreva os sintomas: ")

    recomendacao = "Levar ao veterinário" if "febre" in sintomas.lower() else "Monitorizar em casa"

    with open("consultas.csv", mode="a", newline="") as ficheiro:
        writer = csv.writer(ficheiro)
        writer.writerow([nome, sintomas, recomendacao])

    print(f"Recomendação: {recomendacao}")



