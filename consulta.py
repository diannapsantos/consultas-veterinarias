def realizar_consulta():
    print("Consulta em construção...")

import csv

def realizar_consulta():
    nome = input("Nome do animal a consultar: ")
    sintomas = input("Descreva os sintomas: ")

    recomendacao = "Levar ao veterinário" if "febre" in sintomas.lower() else "Monitorizar em casa"

    with open("consultas.csv", mode="a", newline="") as ficheiro:
        writer = csv.writer(ficheiro)
        writer.writerow([nome, sintomas, recomendacao])

    print(f"Recomendação: {recomendacao}")
