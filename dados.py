import csv

def guardar_dados(ficheiro, dados):
    with open(ficheiro, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(dados)

guardar_dados("consultas.csv", [nome, sintomas, recomendacao])
