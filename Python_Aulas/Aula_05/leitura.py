#Importa dar permissão apenas de leitura
arquivo = open('pokemon.csv', 'r')
texto = arquivo.read()
linhas = texto.split('\n')

#print(linhas)

colunas = linhas[0].split(',')
print(colunas[1])