peso = float(input('Digite outro número: '))
altura = float(input('Digite outro número: '))

resultado = peso/altura
    
if resultado < 18.7:
    print("Seu IMC é: Abaixo do peso")
elif resultado >= 18.5 and resultado < 24.9:
    print("Seu IMC é: Normal")
elif resultado >=25 and resultado < 29.9:
    print("Seu IMC é: Sobrepeso")
else:
    print("Seu IMC é: Obesidade")