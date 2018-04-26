# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:43:01 2018

@author: mathe
"""

import tkinter as tk
import json
from bequeup import loja_manager

class MeuAplicativo:
    
    with open ("arquivo.json", "r") as arquivo:
        estoque = json.loads(arquivo.read())
        
    def __init__(self):
        #Inicializa janela
        self.window =tk.Tk()
        self.window.title("Controle de Estoque")
        self.window.geometry("280x280")
        self.window.wm_iconbitmap("icone.ico")
        self.window.configure(background="#D791FF")
        
        #Widgets
        self.roger=tk.PhotoImage(file="titulo.gif")
        titulo1=tk.Label(self.window,image=self.roger)
        global titulo2
        titulo2=tk.Label(self.window,text="Bem Vindo ao Gerenciamento de Estoque",bg="#D791FF")
        #entrada=tk.Entry(self.window)
        
        #Teste
        global botao
        global sair
        
        def bot_ini():
            botao.destroy()
            sair.destroy()
            titulo2.destroy()
            #Cria botoes novos
            lbl=tk.Label(self.window,text="Escolha uma opção:",bg="#D791FF")
            acessar=tk.Button(self.window,text="Acessar loja",bg="#D791FF",fg="#47016F")
            adicionar=tk.Button(self.window,text="Adicionar loja",bg="#D791FF",fg="#47016F")
            excluir=tk.Button(self.window,text="Excluir loja",bg="#D791FF",fg="#47016F")
            sair2=tk.Button(self.window,text="Sair",bg="#D791FF",fg="#47016F",command=bot_close)
            lbl.pack()
            acessar.pack(pady=5)
            adicionar.pack(pady=5)
            excluir.pack(pady=5)
            sair2.pack(pady=5)
            
        #Função para fechar
        def bot_close():
            self.window.destroy()
            
        botao=tk.Button(self.window,text="Inicar",bg="#D791FF",fg="#47016F",command=bot_ini)
        sair=tk.Button(self.window,text="Sair",bg="#D791FF",fg="#47016F",command=bot_close)
        
        # entrada.pack()
        titulo1.pack(side=tk.TOP)
        titulo2.pack()
        botao.pack(pady=10)
        sair.pack(pady=10)
        
    #loop principal
    def iniciar(self):
        self.window.mainloop()
    
    
app=MeuAplicativo()
app.iniciar()