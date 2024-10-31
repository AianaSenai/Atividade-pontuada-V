import os
os.system("cls|| clear")

<<<<<<< HEAD
contador = 0
def logo_categoria():
    os.system("cls || clear")
    print("""
===========================================
| Categoria  de livros      Preços        |
| Romance                 | R$40          |
| Comedia                 | R$30          | 
| Autoajuda               | R$25          |
| Fantasia                | R$45          |
===========================================
=======
def logo_categoria():
    os.system("cls || clear")
    print("""
**********************************************
| Categoria  de livros      Preços           |
| 1- Romance                 | R$40          |
| 2- Comedia                 | R$30          | 
| 3- Autoajuda               | R$25          |
| 4- Fantasia                | R$45          |
**********************************************
>>>>>>> menu-livros
|""")
def logo_pagamentos():
    os.system("cls|| clear")
    print("""
=================================
| 1 - Cartao de Credito         | 
| 2 - Cartao de Debito          |
| 3 - Pix                       |
|       !ATENÇÃO!               | 
|CREDITO: acrescimo de 10%      |
<<<<<<< HEAD
|DEBITO E PIX : desconto de 15% |                              
=================================
""")

logo_categoria()
livros = input ("Digite a categoria desejada: ").strip().lower()

def valor_livros(livros):
    while True:
        if livros == 'Romance':
            valor = 40
        elif livros == 'Comedia':
            valor = 30
        elif livros =='Autoajuda': 
            valor = 25
        else:
            valor = 45
        return valor

def descontos_acrescimo(livros):
    credito =  0.10
    debito =  0.15
    pix =  0.15
    if pagamento == 'credito':
        valor_livros - credito
    elif pagamento == 'debito':
        valor_livros + debito
    else:
        valor_livros + debito
    return  valor_livros - credito, valor_livros + debito, valor_livros+ pix

logo_pagamentos()
pagamento = input("Digite a forma de pagamento: ")
metodo_escolhido = descontos_acrescimo(pagamento)
=======
|DEBITO E PIX : desconto de 15% |
=================================
""")
    


lista_do_cliente: []
def categoria():
    romance = 40
    comedia = 30
    autoajuda = 25
    fantasia = 45

cliente = int (input("Digite o numero da categoria desejada: "))

def escolha_livro(cliente):
    while True():
        if cliente == "1":
            escolha = input("Deseja mais um livro: ").upper()
            if escolha == "Sim":
               pergunta = cliente 
               contador =+ pergunta
            else:
                break

final = escolha_livro(cliente)
>>>>>>> menu-livros
