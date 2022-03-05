import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.tix import AUTO


# Lista de Confiança
trust_list = ['90', '95', '95.5', '99']


# Config da Interface
window = tk.Tk()
window.title("Amostragem - Estasticas")
window.geometry("500x460")
window['bg'] = "#000000"


# Função Responsavel por manipular a interface e entregar o resultado
def sample():
    N = int(population_entry.get())
    Z = combobox_type.get()
    if Z == '90':
        Z = 1.65
    elif Z == '95':
        Z = 1.96
    elif Z == '95.5':
        Z = 2
    elif Z == '99':
        Z = 2.57
    proportion = float(entry_proportion.get())
    proportion /= 100
    errors = float(entry_erro_amonstral.get())
    errors /= 100

    n = (N * (Z**2) * proportion * (1 - proportion)) / \
        ((errors ** 2) * (N - 1) + (Z**2) * proportion * (1 - proportion))

    result["text"] = f'{n:.2f}'

def verify_empty():
    if population_entry.get()=="" or entry_erro_amonstral.get()=='':
        messagebox.showinfo(title="ERROR", message="Campo Necessario Vazio!")
        return;
    

all_commands = lambda:[verify_empty(), sample()]

# Configuração do "TITULO"
label_population = tk.Label(text="AMOSTRAGEM", bg="#7E57F2", fg="#e6e6e6", font="Arial 12 bold")
label_population.grid(row = 0, column = 0, padx=10, pady=10, sticky="nswe", columnspan=4)


# Configuração da caixa de texto de População
label_population = tk.Label(text="Tamanho da população", bg="#7E57F2", fg="#e6e6e6", font="Arial 12 bold")
label_population.grid(row=1, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

population_entry = tk.Entry(font="Arial 9 bold")
population_entry.grid(row=1, column=2, padx=10, pady=10, sticky="nswe", columnspan=2)

label_trust = tk.Label(text="Nivel de confiança (%)", bg="#7E57F2", fg="#e6e6e6", font="Arial 12 bold")
label_trust.grid(row=2, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

combobox_type = ttk.Combobox(values=trust_list, font="Arial 9 bold")
combobox_type.insert(0, 90)
combobox_type.grid(row=2, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_proportion = tk.Label(text="Estimativa da verdadeira  proporção (%)", bg="#7E57F2", fg="#e6e6e6", font="Arial 12 bold")
label_proportion.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_proportion = tk.Entry(font="Arial 9 bold")
# Inicia com 50
entry_proportion.insert(0, 50)
entry_proportion.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_erro_amonstral = tk.Label(text="Erro Amostral (%)", bg="#CD5C5C", fg="#e6e6e6", font="Arial 12 bold")
label_erro_amonstral.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_erro_amonstral = tk.Entry(font="Arial 9 bold")
entry_erro_amonstral.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

# Butão Responsavel pelo Calculo
button = tk.Button(text="Calcular", command=all_commands, bg="#7E57F2", fg="#e6e6e6", font="Arial 12 bold")
button.grid(row=5, column=0, padx=10, pady=10, sticky='we', columnspan=4)


result = tk.Label(window, text="", font="Arial 13 bold", fg="#90EE90", bg="#000000")
result.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

window.mainloop()



