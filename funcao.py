'''
Sintaxe de uma função:

def nome(PARÂMETROS):
    OPERAÇÕES/INSTRUÇÕES
    return RETORNO

obs1.: O retorno é opcional
obs2.: OS parâmetros também são opcionais
'''

'''
Exemplo 01: Função para imprimir um texto
'''
from calendar import c


def imprimir():
    print('IFRN')


imprimir()

'''
Exempolo 02: Criar uma função que retornará o nome da instituição
'''
def instituicao():
    return 'IFRN2'

# Possibilidade 01: Imprimir
print(instituicao())

# Possibilidade 02: Salvar em variável
texto = instituicao()
print('Chamada 02', texto)

'''
Exemplo 03: Criar uma função que recebe como parâmetro o nome de uma instituição e imprime
'''
def  nome_instituicao(nome):
    print(nome)

nome_instituicao('IFRN3')

'''
Exemplo 04: Crie uma função que recebe o nome de uma função e retorna o seguinte texto: 
"Instituição: NOME"
'''
def nome_formatado(nome):
    return 'Instituição: '+nome

print(nome_formatado('IFRN4'))

'''
Exemplo 05: Crie uma função que recebe dois números 
inteiros e retorna o resultado da soma entre eles
'''
def soma(num1, num2):
    return num1+num2

print(soma(10,5))

'''
Parâmetros DEFAULT
Se você não definir um valor para o parâmetro, ele receberá um valor padrão/default
'''
'''
Exemplo: criar uam função que terá 3 parâmetros: nome, usuario e senha. Se não definir 
o valor de usuario, ele será "root". Se não definir o valos de senha, ele será "123"
'''
def autenticacao(nome, usuario='root', senha='123'):
    print(nome, '-', usuario,'-',senha)
    # print(usuario)
    # print(senha)

autenticacao('Administrador', 'admin', '12345')
autenticacao('Administrador')
autenticacao('Administrador', 'admin')

'''
PARÂMETROS posisionais: é possivel alterar a ordem em que os 
argumentos são passados aos parâmetros da função
'''
def cadastro(nome, cpf, idade, telefone):
    print(nome,'-', cpf,'-', idade,'-', telefone)

cadastro('Fabiana', '123', '25','84 999')
cadastro('Fabiana', '123',telefone='84 999',idade='25')
cadastro('Fabiana',telefone='84 999',idade='25',cpf='123')
cadastro(telefone='84 999',idade='25',cpf='123', nome='Fabiana')
#cadastro('123',telefone='84 999',idade='25', nome='Fabiana')
