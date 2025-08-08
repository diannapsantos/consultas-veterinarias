# === interface.py ===

# VERSÃO 1: Menu preliminar (para demonstração inicial do projeto)

def menu_principal():
    print("=== Sistema de Consultas Veterinárias ===")
    print("1. Registar novo animal")
    print("2. Iniciar nova consulta")
    print("3. Ver histórico de consultas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Função de registar animal ainda não implementada.")
    elif opcao == "2":
        print("Função de consulta ainda não implementada.")
    elif opcao == "3":
        print("Função de histórico ainda não implementada.")
    elif opcao == "4":
        print("A sair do sistema.")
    else:
        print("Opção inválida.")

from consulta import realizar_consulta
from animais import registar_animal

def menu_principal():
    while True:
        print("\n=== Sistema de Consultas Veterinárias ===")
        print("1. Registar Animal")
        print("2. Realizar Consulta")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registar_animal()
        elif opcao == "2":
            realizar_consulta()
        elif opcao == "3":
            print("A sair do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

from consulta import realizar_consulta, ver_historico_consultas

def mostrar_menu():
    while True:
        print("\n=== Sistema de Consultas Veterinárias ===")
        print("1. Registar Animal")
        print("2. Realizar Consulta")
        print("3. Ver Histórico de Consultas")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            registar_animal()
        elif escolha == "2":
            realizar_consulta()
        elif escolha == "3":
            ver_historico_consultas()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

import csv
from datetime import datetime

def realizar_consulta():
    nome = input("Nome do animal a consultar: ")
    sintomas = input("Descreva os sintomas: ")
    data = datetime.now().strftime("%Y-%m-%d")  # <- nova linha

    recomendacao = "Levar ao veterinário" if "febre" in sintomas.lower() else "Monitorizar em casa"

    with open("consultas.csv", mode="a", newline="") as ficheiro:
        writer = csv.writer(ficheiro)
        writer.writerow([nome, sintomas, recomendacao, data])  # <- agora com 4 colunas

    print(f"Recomendação: {recomendacao}")

# VERSÃO 2: Menu funcional completo com chamadas aos módulos

from consulta import realizar_consulta, ver_historico_consultas
from animais import registar_animal

def mostrar_menu():
    while True:
        print("\n=== Sistema de Consultas Veterinárias ===")
        print("1. Registar Animal")
        print("2. Realizar Consulta")
        print("3. Ver Histórico de Consultas")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            registar_animal()
        elif escolha == "2":
            realizar_consulta()
        elif escolha == "3":
            ver_historico_consultas()
        elif escolha == "4":
            print("A sair do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")