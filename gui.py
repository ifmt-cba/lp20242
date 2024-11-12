'''
Exemplo de Graphics User Interface (GUI) com Python
'''

from tkinter import Tk, Label, Entry, Button, messagebox

def show_nome():
    lbl_resultado.config(text =  lbl_resultado.cget('text') + txt_nome.get() + '\n')
    messagebox.showinfo(
            title='Seja Bem Vindo!',
            message=f'Olá {txt_nome.get()}')
    txt_nome.delete(0, len(txt_nome.get()))

window = Tk()
window.title('Minha Janela')
window.config(padx=10, pady=10)

# Labels
lbl_nome = Label(text='Nome:')
lbl_nome.grid(row=0, column=0)
lbl_resultado = Label(text='')
lbl_resultado.grid(row=2, column=0, columnspan=3, sticky='W')

# Entries
txt_nome = Entry(width=35)
txt_nome.grid(row=0, column=1, columnspan=2, sticky='W')
txt_nome.focus()
btn_ok = Button(text="OK", width=20, command=show_nome)
btn_ok.grid(row=1, column=0, columnspan=3)

window.mainloop()