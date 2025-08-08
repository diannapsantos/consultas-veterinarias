# === animais.py ===

import csv  # Importa a biblioteca para trabalhar com ficheiros CSV

# Função para registar os dados de um novo animal
def registar_animal():
    # Recolhe dados básicos do animal através do input do utilizador
    nome = input("Nome do animal: ")
    especie = input("Espécie: ")
    idade = input("Idade: ")

    # Abre (ou cria) o ficheiro CSV em modo de adição ("append")
    with open("animais.csv", mode="a", newline="") as ficheiro:
        writer = csv.writer(ficheiro)
        # Escreve uma nova linha no ficheiro com os dados do animal
        writer.writerow([nome, especie, idade])

    # Confirmação visual para o utilizador
    print("Animal registado com sucesso!")

