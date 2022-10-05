#from cgitb import text
#from statistics import quantiles


from cgitb import text


texto = "Fabiana"
print(texto[0])
print(texto[2])
print(texto[3])

print(texto + " de Souza")
#quantidade de letras do texto (jeito 1)
print(len(texto))
#quantidade de letras do texto (jeito 2)
quantidade = len(texto)
print(quantidade)

#capitalize() - Transforma primeira letra em maiúscula
texto = "campus canguaretama"
print(texto.capitalize())

texto = "Analise"
print(texto[2:5])
print(texto[:5])
print(texto[2:])

texto = "Analise"
print(texto[::2])
print(texto[1::2])

texto = "Analise"
print(texto[::-1])

texto = 'Aluna possui {0} anos e nasceu em {1}'
print(texto.format(25, 1997))

texto = 'IFRN'
print('IFRN' == texto)

"""Desenvolva um algoritmo em Python que peça para o usuário digitar um texto. Logo em
seguida deverá imprimir quantos caracteres foram digitados."""

texto = input("Digite um texto: ")
print(len(texto))

"""Desenvolva um algoritmo em Python que peça para o usuário digitar um texto. Logo em
seguida deverá imprimir cada letra da palavra em uma linha diferente."""

texto = input("Digite um texto: ")
for palavra in texto:
    print(palavra)

'''Desenvolva um algoritmo em Python que peça para o usuário digitar dois textos (duas
entradas). Em seguida o programa deverá imprimir se os textos digitados são iguais ou
diferentes, imprimindo esta informação (IGUAIS ou DIFERENTES).'''

texto_1 = input("Digite um texto: ")
texto_2 = input("Digite um texto: ")
#print(texto_1 == texto_2)
if texto_1 == texto_2:
    print("Iguais")
else:
    print("Diferente")

'''Desenvolva um algoritmo em Python que peça para o usuário digitar um texto. Logo em
seguida deverá imprimir se o texto digitado é palíndromo (de trás para frente) ou não.'''

texto1 = input("Digite um texto: ")
if(texto == texto[::-1]):
    print('É palíndromo!')
else:
    print('Não é palíndromo!')