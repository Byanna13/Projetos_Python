#add os novos elementos a primeira lista
lista = [4,10,5]
lista.extend([14,2])
print(lista)

#retorna a posição do elemento
lista = [4,10,5]
print(lista.index(10))

#Adiciona um elemento em uma posição específica
lista = [4,10,5]
lista.insert(1, 100)
print(lista)

#Remove um elemento especifico
lista = [4,10,5]
lista.remove(10)
print(lista)

#1. Desenvolva um algoritmo em Python que armazene cinco números em uma lista. 
# Em seguida, deverá imprimir cada um dos números armazenados em linhas separadas.

numeros = [2, 5, 3, 7, 9]
for num in numeros:
    print([num])


#2. Desenvolva um algoritmo em Python que peça para o suário digitar cinco números (os números devem
# ser salvos em uma lista - utilizar estrutura de repetição para isso). Em seguida, deverá imprimir
# cada um dos números armazenados em linhas separadas.

numeros = []
for num in range(5):
    numeros.append(int(input("Digite um número: ")))

for num in numeros:
    print([num])

#3. Desenvolva um algoritmo em Python que peça para o usuário digitar cinco números (os
# números devem ser salvos em uma lista - utilizar estrutura de repetição para isso). Em
# seguida, deverá imprimir os números em ordem inversa à que foram digitados em linhas
# separadas. Ex.: se digitou 5 2 10 13 -2. deverá imprimir -2 13 10 2 5

numeros = []
for num in range(5):
    numeros.append(int(input("Digite um número: ")))
    numeros.reverse()
for num in numeros:
    print(numeros)

#
numeros = []
for num in range(5):
    numeros.append(int(input("Digite um número")))

for num in numeros:
    if num>0:
        print(num)