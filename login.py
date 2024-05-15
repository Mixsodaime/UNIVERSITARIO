
import tkinter as tk



from tkinter import Label,PhotoImage,Button,messagebox,Entry

# Use a breakpoint in the code line below to debug your script.
# Press F9 to toggle the breakpoint.
def sair():
    resposta = messagebox.askquestion("Sair","Sair do programa ?")
    if (resposta=='yes'):
        app.destroy()

def entrar():
    janela2 = tk.Toplevel()
    janela2.title('Login')
    label_usuario = tk.Label(janela2, text="Usuário")
    label_senha = tk.Label(janela2, text="Senha")
    label_usuario.grid(row=0, column=0)
    label_senha.grid(row=1, column=0)
    entry_usuario = tk.Entry(janela2)
    entry_senha = tk.Entry(janela2,show="*")
    entry_usuario.grid(row=0, column=1)
    entry_senha.grid(row=1, column=1)
    botao_voltar = tk.Button(janela2, text='Fechar a janela', command=janela2.destroy)
    botao_voltar.grid(row=2, column=0)

    # Press the green button in the gutter to run the script.
#principal
app = tk.Tk()
app.title('Teste com imagem')
# Ajustar tamanho e posição da janela
window_width = 600
window_height = 600
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
center_x = int((screen_width - window_width) / 2)
center_y = int((screen_height - window_height) / 2)
app.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Definir imagem para o label
image1 = PhotoImage(file="estudante.png")
label = Label(app, image=image1).pack()

botaoentrar = Button(app, text="Entrar", command=entrar).pack()
botaosair = Button(app, text="Sair", command=sair).pack()
app.mainloop()
