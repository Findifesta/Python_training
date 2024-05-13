# Escreva uma função que o parâmetro seja um número inteiro.
# Se o número for ímpar, retorne a mensagem " número ímpar"
# Se o numero for par, retorne a mensagem "número par"
# Se for qualquer outro tipo, retorne a mensagem "parâmetro com o tipo errado" e exiba um erro do tipo TypeError
# Ops, exiba um erro do tipo type erro com a mensagem "parâmetro do tipo errado"


try:
    numero = int(input('Digite o número que deseja testar:'))
except ValueError as error:
    raise ValueError(
        'Não é possível converter a string em número inteiro.') from error


def checa_par():
    """Função que checa se é par ou"""
    if type(numero) != int:
        print('Parâmetro do tipo errado')
    elif numero % 2 == 0:
        print(numero, 'é par')
    else:
        print(numero, 'é impar')


checa_par()
