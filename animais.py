import csv

def registar_animal():
    nome = input("Nome do animal: ")
    especie = input("Espécie: ")
    idade = input("Idade: ")

    with open("animais.csv", mode="a", newline="") as ficheiro:
        writer = csv.writer(ficheiro)
        writer.writerow([nome, especie, idade])

    print("Animal registado com sucesso!")

