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
