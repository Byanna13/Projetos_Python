#Índice referente ao número da amostra.
n=int(input("Insira o número total de amostras"))
#Índice i que vai percorrer todas as amostras
i=0
#Lista vazia para conter as amostras
Amostras=[]
#For para percorrer todo o contador das médias
for i in range(i,n):        
    #Adiciona o valor da amostra dentro da lista de amostras
    Amostras.append(int(input("Insira o valor das amostras")))
#Escreve a lista de amostras na tela para o usuário
print(Amostras)

#Soma das amostras
Xi = 0
#Total 
N = len(Amostras)
for amostrai in Amostras:
    Xi +=amostrai
print ("Esse é o valor da soma das amostras", Xi)
print ("Este é a quantidade de amostras que você possui", N)

print ("Esta é a média", Xi/N)

# Média Ponderada

#Lista com os pesos de cada variável
pi = []
#Lista com os valores de cada variável
xi = []

#Lista com os produtos do peso e da variável associada ao índice i
amostraponderadai = []

for i in range (i,n):
    pi.append(int(input("Insira o peso associado a variável: ",i)))
    xi.append(int(input("Insira a variável associado ao índice:", i)))
    amostraponderadai.append(pi(i)*xi(i))

#Soma das amostras
PiXi = 0
Nponderadai = len(amostraponderadai)

#Total do produto da amostra pelo peso
for pixi in amostraponderadai:
    PiXi += pixi
print ("Este é o valor da soma dos produtos entre as amostras e seus respectivos pesos", PiXi)
print ("Este é a quantidade de amostras para a análise da média ponderada", Nponderadai)           
print ("Esta é a média ponderada do conjunto de dados", PiXi/Nponderadai)