import tkinter as tk
from tkinter import messagebox
import random
import string

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para o tamanho da senha.")
        return

    usar_maiusculas = var_maiusculas.get()
    usar_minusculas = var_minusculas.get()
    usar_digitos = var_digitos.get()
    usar_simbolos = var_simbolos.get()

    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_digitos:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        messagebox.showerror("Erro", "Selecione pelo menos um tipo de caractere.")
        return

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    resultado_senha.set(senha)

# Janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("400x350")
janela.configure(bg="#f0f0f0")

# Título
titulo = tk.Label(janela, text="Gerador de Senhas", font=("Segoe UI", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=10)

# Tamanho da senha
tk.Label(janela, text="Tamanho da senha:", bg="#f0f0f0", font=("Segoe UI", 12)).pack()
entry_tamanho = tk.Entry(janela, font=("Segoe UI", 12), width=10)
entry_tamanho.pack(pady=5)

# Checkbuttons de opções
var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_digitos = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

tk.Checkbutton(janela, text="Letras maiúsculas", variable=var_maiusculas, bg="#f0f0f0", font=("Segoe UI", 11)).pack(anchor="w", padx=60)
tk.Checkbutton(janela, text="Letras minúsculas", variable=var_minusculas, bg="#f0f0f0", font=("Segoe UI", 11)).pack(anchor="w", padx=60)
tk.Checkbutton(janela, text="Dígitos (0-9)", variable=var_digitos, bg="#f0f0f0", font=("Segoe UI", 11)).pack(anchor="w", padx=60)
tk.Checkbutton(janela, text="Símbolos (!@#...)", variable=var_simbolos, bg="#f0f0f0", font=("Segoe UI", 11)).pack(anchor="w", padx=60)

# Botão gerar
tk.Button(janela, text="Gerar Senha", command=gerar_senha, bg="#4CAF50", fg="white", font=("Segoe UI", 12)).pack(pady=10)

# Resultado
resultado_senha = tk.StringVar()
tk.Entry(janela, textvariable=resultado_senha, font=("Segoe UI", 12), width=30, justify="center").pack(pady=5)

# Rodar interface
janela.mainloop()
