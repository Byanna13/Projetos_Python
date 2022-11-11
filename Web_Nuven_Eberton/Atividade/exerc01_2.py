'''Construir um programa Python de nome exerc01_2.py para calcular e exibir a
média ponderada de 4 números dados pelo usuário e cuja ponderação é: 2, 3, 4, 5.'''

n = 4
i=0

num=[4]

for i in range(i,n):
    num.append(int(input('Insira um número: ')))

print(num)

xi = 0
xn = len(num)
p1 = 2
p2 = 3
p3 = 4
p4 = 5

for numX in num:
    xi +=numX
print ('A média é: ', ((xi+p1)+(xi+p2)+(xi+p3)+(xi+p4)/xn))