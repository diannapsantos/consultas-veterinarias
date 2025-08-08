import csv  # Biblioteca para trabalhar com ficheiros CSV

# Função genérica para guardar dados num ficheiro CSV
def guardar_dados(ficheiro, dados):
    # Abre o ficheiro no modo "append" (adicionar no fim)
    with open(ficheiro, mode="a", newline="") as f:
        writer = csv.writer(f)
        # Escreve uma linha com os dados fornecidos
        writer.writerow(dados)

# Nota:
# Esta função deve ser chamada a partir de outros ficheiros como
# consulta.py ou animais.py, onde as variáveis como `nome`, `sintomas`, etc.
# Evitar executar diretamente aqui para não causar erro.
