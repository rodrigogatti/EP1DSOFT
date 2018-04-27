# -*- coding: utf-8 -*-

from firebase import firebase #armezando os dados em nuvem , usando Firebase
firebase=firebase.FirebaseApplication('https://teste-22bbc.firebaseio.com/',None)
if firebase.get('Estoque',None) is None:
    estoque={} #estoque é representado por um dicionário
else:
    estoque=firebase.get('Estoque',None)

i=1 #variável utilizada para manter o loop no sistema
while i!=0: 
    print("Controle de loja: \n0 - Acessar uma loja \n1 - Adicionar loja \n2 - Excluir loja \n3 - Sair do Sistema")
    selecione=int(input('Faca sua escolha: '))
    
    if selecione==0:
        print('Lojas disponiveis: ')
        for k in estoque:
            print(k)
        loja=input('Qual loja gostaria de acessar? ')
        loja=loja.lower()
        if loja not in estoque:
            print('Loja inválida')
        else: #permite acomodar o estoque simultâneo de várias lojas
            print(" Controle de estoque da loja {0}: \n0 - sair \n1 - Adicionar item \n2 - remover item \n3 - alterar item \n4 - imprimir estoque \n5 - modificar preço \n6 - mostrar estoque negativo \n7 - imprimir valor monetário ".format(loja))
            x=1
            while x!=0:
                escolha= int(input("Faça sua escolha: "))
    
                if escolha == 0: #opção sair
                    print("Obrigada pela participação! Execução Encerrada!")
                    x=0
        
                elif escolha == 1: #opção adicionar item
                    nome_do_produto = (input("Qual o produto?: "))
                    nome_do_produto = nome_do_produto.lower() #lower: padroniza as palavras sempre em minúsculas
                    if nome_do_produto not in estoque:
                        estoque[loja][nome_do_produto]={}
                        quantidade_inicial = (int(input("Qual a quantidade inicial?: ")))
                        while quantidade_inicial < 0:
                            print(" A quantidade inicial não pode ser negativa! ")
                            quantidade_inicial = (int(input("Qual a quantidade inicial?: ")))
                        estoque[loja][nome_do_produto]['quantidade']=quantidade_inicial
                        preco=float(input("Qual o preço?: "))
                        while preco < 0:
                            print(" O valor não pode ser negativo. Digite um novo preço.")
                            preco=float(input("Qual o preço?: "))
                        estoque[loja][nome_do_produto]['preco']=preco
                        print(estoque)
                    else:
                        print("Já tem no estoque!")
    
                elif escolha == 2: #opção remover item
                    nome_do_item = (input("Qual o item a ser removido?: "))
                    nome_do_item = nome_do_item.lower()
                    if nome_do_item in estoque[loja]:
                        del estoque[loja][nome_do_item]
                    else:
                        print("Elemento não encontrado! ")
                    print(estoque)
        
                elif escolha == 3: #opção alterar item
                    nome_do_item = (input("Qual o item? "))
                    nome_do_item = nome_do_item.lower()
                    if nome_do_item in estoque[loja]:
                        valor_alterado = int(input("Quanto Adicionar?: "))
                        valor_original=estoque[loja][nome_do_item]['quantidade']
                        novo_valor = valor_original+valor_alterado
                        estoque[loja][nome_do_item]['quantidade']=novo_valor
                        print(estoque)
                    else:
                        print("Produto não encontrado! ")
            
                elif escolha == 4: #opção imprimir estoque
                    for k,v in estoque[loja].items(): #k:Chave: Nome dos produtos
                        print(k,v['quantidade'])#v:Valor: Dicionário que contém uma única chave (string quantidade)
                elif escolha == 5: #registro de preço unitário de cada produto
                    nome_do_item=input('Qual o produto?' )
                    nome_do_item = nome_do_item.lower()
                    if nome_do_item in estoque[loja]:
                        novo_preco=float(input('Qual o novo preco?' ))
                        while novo_preco<0:
                            print('Preco nao pode ser negativo') #número real não nulo
                            novo_preco=float(input('Qual o novo preco?' ))
                        estoque[loja][nome_do_item]['preco']=novo_preco
                        print(estoque)
                    else:
                        print('Nao existe esse produto no estoque')
                elif escolha == 6: #lista os produtos com quantidade de estoque negativa
                    for k,v in estoque[loja].items():
                        if estoque[loja][k]['quantidade'] < 0:
                            print(k,v['quantidade'])
                        else:
                            print("Não há estoque negativo!")
                elif escolha == 7: #imprime o valor monetário total em estoque
                    soma=0
                    for k,v in estoque[loja].items():
                        x=v['preco']*v['quantidade']
                        soma+=x
                    print('Valor monetário total em estoque: {0}'.format(soma))
    elif selecione==1:
        loja=input('Qual loja gostaria de adicionar? ')
        loja=loja.lower()
        if loja in estoque:
            print('Loja já existente')
        else:
            estoque[loja]={}
    elif selecione==2:
        loja=input('Qual loja gostaria de excluir? ')
        loja=loja.lower()
        if loja in estoque:
            del estoque[loja]
            firebase.delete('Estoque',loja)
            print('Loja {0} Excluida'.format(loja))
        else:
            print('Loja inexistente')
            
    elif selecione==3:
        i=0 
        print("Sessão encerrada!")
        
    
firebase.patch('/Estoque',estoque)
    
            
            
            
            
    
        