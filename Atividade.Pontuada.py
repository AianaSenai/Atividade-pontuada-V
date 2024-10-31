import os
os.system("cls|| clear")

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


def valor_livros(livros):
    while True:
        if livros == 'Romance':
            return 40
        elif livros == 'Comedia':
            return 30
        elif livros =='Autoajuda': 
            return 25
        else:
           return 45 

def descontos_acrescimo(valor, pagamento):
    credito =  0.10
    debito_pix =  0.15
    
    if pagamento == 'credito':
        return valor * (1 + credito)
    elif pagamento in ['debito', 'pix']:
        return valor * (1 - debito_pix)
    else:
        return valor 


logo_categoria()
livros = input ("Digite a categoria desejada: ").strip().lower()
valor = valor_livros(livros)

logo_pagamentos()
pagamento = input("Digite a forma de pagamento: ")
preco_final = descontos_acrescimo(valor, pagamento)
print(f"O preço final do livro na categoria {livros} é: R${preco_final}")
