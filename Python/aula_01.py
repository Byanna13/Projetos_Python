print("Hello World")

numero = 10
print("O número é: ",numero)
print(type(numero))

#cometario de uma linha
'''Comentário de 
varias linhas, ou com as aspas duplas, \n qurbra de linha'''

print(10/3)
print(10//3)
print(2**3)

#input sempre retorna texto (str)
nome = input("Digite seu nome: ")
print("Nome digitado: ",nome)

idade = int(input("Digite sua idade:"))
print("Idade: ",idade)

preco = float(input("Digite o preço:"))
print("Preço é:", preco)

x = int(input("Digite o preço:"))
print("resultado1: ",x*15/100)
print("resultado2: ",x*0.15)
'\n'
y = float(input("Digite o valor:"))
print("resultado1",y-y*15/100)
print("resultado2",y*0.85)
print("resultado3",y-y*0.15)


numero = int(input("Digite um número: "))

if numero == 0:
    print("Número digitado é zero!")
    print("Entrou no IF")
else:
    print("Número não é zero")

if numero == 0: print("Número digitado é zero!")
else: print("Número não é zero")