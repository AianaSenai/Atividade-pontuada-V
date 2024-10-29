import os
os.system("cls|| clear")

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