import os
os.system("cls|| clear")

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
