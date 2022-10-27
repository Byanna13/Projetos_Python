print('Programa divisão por zero')
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
# espaço com tab é: 'identação'

try:
    d = x/y
except ZeroDivisionError as e:
    print('Divisão por Zero não é permitida')
finally:
    print('Finally vai ser execultada independente do Try.')