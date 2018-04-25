# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:10:58 2018

@author: Ester Quintino
"""
import json

with open ("arquivo.json", "r") as arquivo:
    estoque = json.loads(arquivo.read())

print(" Controle de estoque: \n0 - sair \n1 - Adicionar item \n2 - remover item \n3 - alterar item \n4 - imprimir estoque \n5 - modificar preço \n6 - mostrar estoque negativo \n7 - imprimir valor monetário ")


i=1
while i!=0:
    escolha= int(input("Faça sua escolha: "))

    if escolha == 0:
        print("Obrigada pela participação! Execução Encerrada!")
        i=0
    
    elif escolha == 1:
        nome_do_produto = (input("Qual o produto?: "))
        nome_do_produto = nome_do_produto.lower()
        if nome_do_produto not in estoque:
            estoque[nome_do_produto]={}
            quantidade_inicial = (int(input("Qual a quantidade inicial?: ")))
            while quantidade_inicial < 0:
                print(" A quantidade inicial não pode ser negativa! ")
                quantidade_inicial = (int(input("Qual a quantidade inicial?: ")))
            #estoque[nome_do_produto]={'quantidade':quantidade_inicial}
            estoque[nome_do_produto]['quantidade']=quantidade_inicial
            preco=float(input("Qual o preço?: "))
            while preco < 0:
                print(" O valor não pode ser negativo. Digite um novo preço.")
                preco=float(input("Qual o preço?: "))
            estoque[nome_do_produto]['preco']=preco
            print(estoque)
        else:
            print("Já tem no estoque!")

    elif escolha == 2:
        nome_do_item = (input("Qual o item a ser removido?: "))
        nome_do_item = nome_do_item.lower()
        if nome_do_item in estoque:
            del estoque[nome_do_item]
        else:
            print("Elemento não encontrado! ")
        print(estoque)
    
    elif escolha == 3:
        nome_do_item = (input("Qual o item? "))
        nome_do_item = nome_do_item.lower()
        if nome_do_item in estoque:
            valor_alterado = int(input("Quanto Adicionar?: "))
            valor_original=estoque[nome_do_item]['quantidade']
            novo_valor = valor_original+valor_alterado
            estoque[nome_do_item]['quantidade']=novo_valor
            print(estoque)
        else:
            print("Produto não encontrado! ")
        
    elif escolha == 4:
        for k,v in estoque.items():
            print(k,v['quantidade'])
    elif escolha == 5:
        nome_do_item=input('Qual o produto?' )
        nome_do_item = nome_do_item.lower()
        if nome_do_item in estoque:
            novo_preco=float(input('Qual o novo preco?' ))
            while novo_preco<0:
                print('Preco nao pode ser negativo')
                novo_preco=float(input('Qual o novo preco?' ))
            estoque[nome_do_item]['preco']=novo_preco
        else:
            print('Nao existe esse produto no estoque')
    elif escolha == 6:
        for k,v in estoque.items():
            if estoque[k]['quantidade'] < 0:
                print(k,v['quantidade'])
    elif escolha == 7:
        soma=0
        for k,v in estoque.items():
            x=v['preco']*v['quantidade']
            soma+=x
        print('Valor monetário total em estoque: {0}'.format(soma))
        
    
estoque_com_json = json.dumps(estoque, sort_keys = True, indent = 4 )
with open("arquivo.json","w") as arquivo:
    arquivo.write(estoque_com_json)





          
    

        
        
        
        

    