from tkinter import Y

'''Construir um programa Python de nome exerc01_1.py para calcular e exibir a
média aritmética de 5 números dados.'''

n = 5
i=0

num=[5]

for i in range(i,n):
    num.append(int(input('Insira um número: ')))

print(num)

xi = 0
xn = len(num)

for numX in num:
    xi +=numX
print ('A média aritmética é: ', xi/xn)