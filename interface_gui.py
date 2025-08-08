# interface_gui.py
import tkinter as tk
from tkinter import messagebox
from animais import registar_animal
from consultas import realizar_consulta, ver_historico_consultas

# Funções de interface
def abrir_janela_registo():
    def guardar():
        nome = entrada_nome.get()
        especie = entrada_especie.get()
        idade = entrada_idade.get()
        if nome and especie and idade:
            with open("animais.csv", mode="a", newline="") as f:
                import csv
                writer = csv.writer(f)
                writer.writerow([nome, especie, idade])
            messagebox.showinfo("Sucesso", f"{nome} registado com sucesso!")
            janela_registo.destroy()
        else:
            messagebox.showwarning("Erro", "Preenche todos os campos.")

    janela_registo = tk.Toplevel(root)
    janela_registo.title("Registar Animal")

    tk.Label(janela_registo, text="Nome:").grid(row=0, column=0)
    tk.Label(janela_registo, text="Espécie:").grid(row=1, column=0)
    tk.Label(janela_registo, text="Idade:").grid(row=2, column=0)

    entrada_nome = tk.Entry(janela_registo)
    entrada_especie = tk.Entry(janela_registo)
    entrada_idade = tk.Entry(janela_registo)

    entrada_nome.grid(row=0, column=1)
    entrada_especie.grid(row=1, column=1)
    entrada_idade.grid(row=2, column=1)

    tk.Button(janela_registo, text="Guardar", command=guardar).grid(row=3, columnspan=2, pady=10)

def abrir_janela_consulta():
    def guardar_consulta():
        nome = entrada_nome.get()
        sintomas = entrada_sintomas.get()
        if nome and sintomas:
            recomendacao = "Levar ao veterinário" if "febre" in sintomas.lower() else "Monitorizar em casa"
            with open("consultas.csv", mode="a", newline="") as f:
                import csv
                from datetime import datetime
                writer = csv.writer(f)
                data = datetime.now().strftime("%Y-%m-%d")
                writer.writerow([nome, sintomas, recomendacao, data])
            messagebox.showinfo("Recomendação", recomendacao)
            janela_consulta.destroy()
        else:
            messagebox.showwarning("Erro", "Preenche todos os campos.")

    janela_consulta = tk.Toplevel(root)
    janela_consulta.title("Nova Consulta")

    tk.Label(janela_consulta, text="Nome do Animal:").grid(row=0, column=0)
    tk.Label(janela_consulta, text="Sintomas:").grid(row=1, column=0)

    entrada_nome = tk.Entry(janela_consulta)
    entrada_sintomas = tk.Entry(janela_consulta)

    entrada_nome.grid(row=0, column=1)
    entrada_sintomas.grid(row=1, column=1)

    tk.Button(janela_consulta, text="Guardar Consulta", command=guardar_consulta).grid(row=2, columnspan=2, pady=10)

def abrir_janela_historico():
    def mostrar_historico():
        nome = entrada_nome.get()
        try:
            with open("consultas.csv", mode="r") as f:
                import csv
                leitor = csv.reader(f)
                historico = [linha for linha in leitor if linha[0].lower() == nome.lower()]
            if historico:
                resultado = f"Histórico de {nome}:\n"
                for h in historico:
                    resultado += f"{h[3]} | Sintomas: {h[1]} | Recomendação: {h[2]}\n"
                messagebox.showinfo("Histórico", resultado)
            else:
                messagebox.showinfo("Histórico", f"Nenhuma consulta encontrada para '{nome}'.")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Ficheiro de consultas não encontrado.")

    janela_historico = tk.Toplevel(root)
    janela_historico.title("Histórico de Consultas")

    tk.Label(janela_historico, text="Nome do Animal:").grid(row=0, column=0)
    entrada_nome = tk.Entry(janela_historico)
    entrada_nome.grid(row=0, column=1)

    tk.Button(janela_historico, text="Ver Histórico", command=mostrar_historico).grid(row=1, columnspan=2, pady=10)

# Janela principal
root = tk.Tk()
root.title("Sistema de Consultas Veterinárias")

tk.Button(root, text="Registar Animal", width=30, command=abrir_janela_registo).pack(pady=10)
tk.Button(root, text="Realizar Consulta", width=30, command=abrir_janela_consulta).pack(pady=10)
tk.Button(root, text="Ver Histórico de Consultas", width=30, command=abrir_janela_historico).pack(pady=10)
tk.Button(root, text="Sair", width=30, command=root.quit).pack(pady=10)

root.mainloop()
