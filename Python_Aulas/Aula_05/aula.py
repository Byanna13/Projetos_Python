# 'r' comando de leitura
arquivo = open('arquivo.txt', 'r',encoding="utf-8")
print(arquivo.read())
arquivo.seek(0)
print(arquivo.read())
print(arquivo.tell())
arquivo.close()

arquivo = open('arquivo.txt', 'w')
arquivo.write('Novo textto')
arquivo.close()