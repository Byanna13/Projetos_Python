import math

print('## RAIZES REAIS DE UMA EQUACAO ##')
print('Equação no formato ax2 + bx + c = 0')

strA = input('Digite o valor de a: ')
strB = input('Digite o valor de b: ')
strC = input('Digite o valor de c: ')

vlA = int(strA)
vlB = int(strB)
vlC = int(strC)

delta = (vlB * vlB) - (4 * vlA * vlC)

x1 = (-vlB + math.sqrt(delta)) / (2 * vlA)
x2 = (-vlB - math.sqrt(delta)) / (2 * vlA)

print('x1: ' + str(x1))
print('x2: ' + str(x2))

# print('A: ' + str(vlA))
# print('B: ' + str(vlB))
# print('C: ' + str(vlC))

# print(delta)